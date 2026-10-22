"""Void search v2: search in the same space the ideas are ranked in.

Why v2 exists: v1 (05_voids.py) searched the top-64 principal components. Those axes mostly encode
generic attributes (genre, art style, mood), so its voids were unusual *combinations of generic tags*.
Written out as store pages, those ideas landed in crowded parts of the full embedding space, where
the specific premise dominates similarity. v2 searches the full 384-d bge space with exactly the
novelty metric used for the final ranking:

    emptiness(x) = 1 - mean cosine similarity to the 10 nearest of ~195k real games   (== novelty_bge)

Every v2 void is a non-negative mix of real game embeddings, so it stays reachable by real text:

  BLEND  2-3 established games (>= 100 reviews, English, not adult) picked at random; the mix weights
         are optimised for emptiness, with every parent keeping >= 20% weight so it stays a real blend.
  HOLE   the cone of a random game's 24 nearest neighbours; weights optimised for emptiness. The
         optimum is the gap in the middle of a crowded neighbourhood.

A mix of unit vectors has shorter length before normalisation, which inflates its similarity to
everything; so a void's emptiness here is, if anything, an underestimate.
Filters and diversity as in v1 (adult/non-English neighbourhoods; centred cosine < SEP; <= 2 shared
nearest games). Metadata read-out with the v1 decoder on the void's semantic coordinates.

Output: data/voids_full.json, data/void_full_vecs.npy (unit vectors in the full bge space)
"""
import json
import sys
from importlib import import_module
from pathlib import Path

import numpy as np
import pandas as pd
import torch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
sys.path.insert(0, str(Path(__file__).parent))
torch.set_num_threads(4)
torch.manual_seed(1)
F = torch.nn.functional

N_SEEDS = 40000
N_REFINE = 2000
STEPS = 100
N_PER_FAMILY = 24
K = 10
N_ANCHORS = 24
MIN_PARENT_W = 0.2
SEP = 0.5
ADULT = {3, 4}
ADULT_TAGS = {"Sexual Content", "Nudity", "Hentai", "NSFW"}
MAX_ADULT_P = 0.15


def topk_sims(X, E, k=K, block=4096):
    vs, ix = [], []
    for s in range(0, len(X), block):
        v, i = torch.topk(X[s:s + block] @ E.T, k, dim=1)
        vs.append(v)
        ix.append(i)
    return torch.cat(vs), torch.cat(ix)


def ascend(mix, P, E, lr, label, project=None):
    P = P.clone().requires_grad_(True)
    opt = torch.optim.Adam([P], lr=lr)
    pool = None
    for step in range(STEPS):
        x = mix(P)
        if step % 10 == 0:
            with torch.no_grad():
                _, pool = topk_sims(x, E, k=256)
        top = torch.topk((x.unsqueeze(1) * E[pool]).sum(2), K, dim=1).values.mean(1)
        opt.zero_grad()
        top.sum().backward()
        opt.step()
        if project is not None:
            with torch.no_grad():
                P.copy_(project(P))
        if step % 25 == 0 or step == STEPS - 1:
            print(f"  [{label}] step {step}: mean emptiness {1 - top.mean().item():.4f}", flush=True)
    return P.detach()


def main():
    games = pd.read_parquet(DATA / "games.parquet")
    keep = games.embeddable.values
    g = games[keep].reset_index(drop=True)
    E = torch.from_numpy(np.load(DATA / "emb_bge.npy")[keep].astype(np.float32))
    E = F.normalize(E, dim=1)
    n = len(E)
    space = pd.read_parquet(DATA / "space.parquet")
    real_nov = np.sort(space.loc[space.embeddable, "novelty_bge"].values)
    pca = np.load(DATA / "pca_bge.npz")
    D = int(pca["d_sem"])
    mu = torch.from_numpy(pca["mean"])
    V = torch.from_numpy(pca["components"][:D])
    m_typ = float(((E - mu) @ V.T).norm(dim=1).median())

    adult = torch.tensor([bool(ADULT & set(c)) or bool(ADULT_TAGS & set(t))
                          for c, t in zip(g.content_descriptors, g.tags)])
    nonen = torch.tensor((g.lang != "en").values)
    established = np.where((g.review_count.values >= 100) & (g.lang.values == "en") & ~adult.numpy()
                           & ~g.coming_soon.values)[0]
    print(f"{n} games; {len(established)} established parents for blends", flush=True)

    # ---------------- BLEND ----------------
    k3 = 3
    picks = torch.from_numpy(established[np.random.default_rng(1).integers(0, len(established), (N_SEEDS, k3))])
    two = torch.rand(N_SEEDS) < 0.5  # half the blends use 2 parents
    mask3 = torch.ones(N_SEEDS, k3)
    mask3[two, 2] = 0

    def blend_x(P, idx, msk):
        w = torch.softmax(P.masked_fill(msk == 0, -1e9), dim=1)
        return F.normalize((w.unsqueeze(2) * E[idx]).sum(1), dim=1)

    x0 = blend_x(torch.zeros(N_SEEDS, k3), picks, mask3)
    v0, _ = topk_sims(x0, E)
    best = torch.argsort(1 - v0.mean(1), descending=True)[:N_REFINE]
    bi, bm = picks[best], mask3[best]

    def proj_blend(P):  # keep every active parent at >= MIN_PARENT_W
        w = torch.softmax(P.masked_fill(bm == 0, -1e9), dim=1)
        k_act = bm.sum(1, keepdim=True)
        w = torch.where(bm > 0, MIN_PARENT_W + (1 - MIN_PARENT_W * k_act) * w, torch.zeros_like(w))
        return torch.log(w.clamp_min(1e-9))

    Pb = ascend(lambda P: blend_x(P, bi, bm), torch.zeros(N_REFINE, k3), E, 0.05, "blend", project=proj_blend)
    xb = blend_x(Pb, bi, bm)
    wb = torch.softmax(Pb.masked_fill(bm == 0, -1e9), dim=1)

    # ---------------- HOLE ----------------
    seeds = torch.randint(0, n, (N_SEEDS,))
    _, anchors = topk_sims(E[seeds], E, k=N_ANCHORS + 1)
    anchors = anchors[:, 1:]  # drop the seed itself; the hole sits among its neighbours
    cent = F.normalize(E[anchors].mean(1), dim=1)
    vc, _ = topk_sims(cent, E)
    keep_h = torch.argsort(1 - vc.mean(1), descending=True)[:N_REFINE]
    anchors = anchors[keep_h]
    A = E[anchors]

    def hole_x(P):
        return F.normalize((F.softplus(P).unsqueeze(2) * A).sum(1), dim=1)

    Ph = ascend(hole_x, torch.zeros(len(anchors), N_ANCHORS), E, 0.05, "hole")
    xh = hole_x(Ph)
    wh = F.softplus(Ph)

    dec = torch.load(DATA / "decoder_bge.pt")
    model = import_module("04_space").Decoder(D, len(dec["labels"]))
    model.load_state_dict(dec["state_dict"])
    labels = dec["labels"]
    adult_cols = [labels.index(f"tag:{t}") for t in ADULT_TAGS if f"tag:{t}" in labels]

    voids, vecs, cent_dirs = [], [], []
    for family, X, idx, W, prefix in (("blend", xb, bi, wb, "B"), ("hole", xh, anchors, wh, "H")):
        v, i = topk_sims(X, E, k=20)
        emp = 1 - v[:, :K].mean(1)
        pct = np.searchsorted(real_nov, emp.numpy()) / len(real_nov) * 100
        z = (X - mu) @ V.T
        with torch.no_grad():
            P = torch.sigmoid(model(m_typ * F.normalize(z, dim=1)))
        ok = (adult[i].float().mean(1) <= 0.25) & (nonen[i].float().mean(1) <= 0.25) & \
             (P[:, adult_cols].max(1).values <= MAX_ADULT_P)
        print(f"[{family}] emptiness median {emp.median():.4f} max {emp.max():.4f}; percentile vs games median "
              f"{np.median(pct):.2f} p90 {np.quantile(pct, .9):.2f}; pass filters {int(ok.sum())}", flush=True)
        cdir = F.normalize(X - mu, dim=1)
        chosen = []
        for j in [j for j in torch.argsort(emp, descending=True).tolist() if ok[j]]:
            nb = set(i[j, :K].tolist())
            if all(float(cdir[j] @ cdir[c]) < SEP and len(nb & set(i[c, :K].tolist())) <= 2 for c in chosen) and \
                    all(float(cdir[j] @ cd) < SEP for cd in cent_dirs):
                chosen.append(j)
            if len(chosen) == N_PER_FAMILY:
                break
        for r_, j in enumerate(chosen):
            p = P[j].numpy()
            lo = np.argsort(-p)
            ww = W[j].numpy()
            order = np.argsort(-ww)[:6]
            parents = [{"appid": int(g.appid.iloc[int(idx[j, q])]), "name": g.name.iloc[int(idx[j, q])],
                        "weight": round(float(ww[q] / ww.sum()), 3),
                        "tags": list(g.concept_tags.iloc[int(idx[j, q])][:8]),
                        "short_description": g.short_description.iloc[int(idx[j, q])][:300]}
                       for q in order if ww[q] > 1e-6]
            nbrs = [{"appid": int(g.appid.iloc[int(i[j, t])]), "name": g.name.iloc[int(i[j, t])],
                     "sim": round(float(v[j, t]), 4), "tags": list(g.concept_tags.iloc[int(i[j, t])][:8]),
                     "short_description": g.short_description.iloc[int(i[j, t])][:300]} for t in range(15)]
            voids.append({
                "void_id": f"{prefix}{r_ + 1:02d}",
                "family": family,
                "space": "full",
                "emptiness": round(float(emp[j]), 4),
                "emptiness_percentile_vs_games": round(float(pct[j]), 3),
                "nearest_game_sim": round(float(v[j, 0]), 4),
                "parent_games": parents,
                "decoded_tags": [(labels[c][4:], round(float(p[c]), 3)) for c in lo if labels[c].startswith("tag:")][:15],
                "decoded_player_modes": [(labels[c][5:], round(float(p[c]), 3)) for c in lo
                                         if labels[c].startswith("mode:")],
                "neighbors": nbrs,
            })
            vecs.append(X[j])
            cent_dirs.append(cdir[j])
    np.save(DATA / "void_full_vecs.npy", torch.stack(vecs).numpy())
    (DATA / "voids_full.json").write_text(json.dumps(voids, indent=1, ensure_ascii=False))
    for vd in voids:
        print(vd["void_id"], vd["emptiness"], f"pct={vd['emptiness_percentile_vs_games']}", "|",
              " + ".join(f"{p['name']} ({p['weight']:.0%})" for p in vd["parent_games"][:3]), "|",
              ", ".join(t for t, _ in vd["decoded_tags"][:5]))


if __name__ == "__main__":
    main()
