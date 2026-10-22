"""Find empty regions ("voids") of Steam's idea-space and read their metadata back out.

Space: semantic coordinates z = top-64 centred principal components of the bge embeddings.
Similarity = cosine of z, so a location is a *direction* d (unit vector in z-space).
emptiness(d) = 1 - mean cosine similarity to the 10 nearest of the ~195k real games.

Two families of voids, both found by gradient ascent on emptiness:

  FRONTIER  start from random directions drawn from the data's own spread (and from blends of
            random games); move freely. Plausibility constraint, enforced by projection after every
            step: the Mahalanobis radius r(d) = m*||d/sigma|| must stay <= R = 75th percentile of r
            over real games. Without it "far from everything" means "pointing along a low-variance
            axis no real description ever moves along". These are the most literal "far from all
            neighbours" points: feature combinations no game has.

  HOLE      start next to a random real game or blend; the void may only move inside the cone of its
            24 nearest real games (d = normalised non-negative mix of them). The optimum is the point
            in that neighbourhood farthest from *every* game: a gap between existing ideas rather
            than a point off the edge of the map. The mix weights are its "parent games".

Then for both: drop voids whose neighbourhood is mostly adult-only or non-English games (the first
we don't want to generate; the second are artefacts of an English model reading other languages);
greedy diverse selection (emptiest first; each new void must have cosine < SEP to every chosen void
and share at most 2 of its 10 nearest games); metadata read-out with the linear decoder
(04_space.py): P(tag), P(player mode).

Output: data/voids.json, data/void_dirs.npy (unit z-directions), data/void_candidates.parquet
"""
import json
import sys
from importlib import import_module
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.optimize import nnls

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
sys.path.insert(0, str(Path(__file__).parent))
torch.set_num_threads(4)
torch.manual_seed(0)

N_SEEDS = 60000           # per family
N_REFINE = 2000           # per family
STEPS = 120
N_PER_FAMILY = 24
SEP = 0.5
K = 10
N_ANCHORS = 24
ADULT = {3, 4}            # Steam content descriptors: adult-only sexual content, frequent nudity/sexual content
ADULT_TAGS = {"Sexual Content", "Nudity", "Hentai", "NSFW"}
MAX_ADULT_P = 0.15        # max decoded P(Sexual Content) / P(Nudity) at a void
F = torch.nn.functional


def topk_sims(X, Zn, k=K, block=8192):
    out_v, out_i = [], []
    for s in range(0, X.shape[0], block):
        v, i = torch.topk(X[s:s + block] @ Zn.T, k, dim=1)
        out_v.append(v)
        out_i.append(i)
    return torch.cat(out_v), torch.cat(out_i)


def project_to_cap(d, sigma, m, R, iters=40):
    """Unit direction with radius <= R, by shrinking low-variance coordinates: d / (1 + lam*A)."""
    A = (m / sigma) ** 2
    over = m * (d / sigma).norm(dim=1) > R
    if not over.any():
        return d
    dd = d[over]
    lo = torch.zeros(len(dd))
    hi = torch.ones(len(dd))

    def too_big(lam):
        return m * (F.normalize(dd / (1 + lam[:, None] * A), dim=1) / sigma).norm(dim=1) > R

    for _ in range(60):
        f = too_big(hi)
        if not f.any():
            break
        hi[f] *= 4
    for _ in range(iters):
        mid = (lo + hi) / 2
        f = too_big(mid)
        lo = torch.where(f, mid, lo)
        hi = torch.where(f, hi, mid)
    out = d.clone()
    out[over] = F.normalize(dd / (1 + hi[:, None] * A), dim=1)
    return out


def ascend(param_to_d, P, Zn, steps=STEPS, lr=0.01, post=None, label=""):
    """Gradient ascent on emptiness. param_to_d maps parameters P -> unit directions."""
    P = P.clone().requires_grad_(True)
    opt = torch.optim.Adam([P], lr=lr)
    pool = None
    for step in range(steps):
        d = param_to_d(P)
        if step % 10 == 0:
            with torch.no_grad():
                _, pool = topk_sims(d, Zn, k=256)
        top = torch.topk((d.unsqueeze(1) * Zn[pool]).sum(2), K, dim=1).values.mean(1)
        opt.zero_grad()
        top.sum().backward()
        opt.step()
        if post is not None:
            with torch.no_grad():
                P.copy_(post(P))
        if step % 30 == 0 or step == steps - 1:
            print(f"  [{label}] step {step}: mean emptiness {1 - top.mean().item():.4f}", flush=True)
    return P.detach()


def main():
    games = pd.read_parquet(DATA / "games.parquet")
    keep = games.embeddable.values
    g = games[keep].reset_index(drop=True)
    E = torch.from_numpy(np.load(DATA / "emb_bge.npy")[keep].astype(np.float32))
    pca = np.load(DATA / "pca_bge.npz")
    D = int(pca["d_sem"])
    mu = torch.from_numpy(pca["mean"])
    V = torch.from_numpy(pca["components"][:D])
    Z = (E - mu) @ V.T
    Zn = F.normalize(Z, dim=1)
    sigma = Z.std(0)
    m = float(Z.norm(dim=1).median())
    n = len(Zn)

    def radius(d):
        return m * (d / sigma).norm(dim=-1)

    R = float(torch.quantile(radius(Zn), 0.75))
    print(f"{n} games, D={D}, typical |z|={m:.3f}, radius cap R={R:.2f}", flush=True)

    def blends(N):
        picks = torch.randint(0, n, (N, 3))
        w = torch.distributions.Dirichlet(torch.ones(3)).sample((N,))
        w[torch.rand(N) < 0.5, 2] = 0
        return F.normalize((Z[picks] * (w / w.sum(1, keepdim=True)).unsqueeze(2)).sum(1), dim=1)

    def best(d, k):
        v, _ = topk_sims(d, Zn)
        return torch.argsort(1 - v.mean(1), descending=True)[:k]

    # ---------------- FRONTIER ----------------
    seeds = torch.cat([F.normalize(torch.randn(N_SEEDS // 2, D) * sigma, dim=1), blends(N_SEEDS // 2)])
    seeds = project_to_cap(seeds, sigma, m, R)
    seeds = seeds[best(seeds, N_REFINE)]
    d_front = ascend(lambda P: F.normalize(P, dim=1), seeds, Zn,
                     post=lambda P: project_to_cap(F.normalize(P, dim=1), sigma, m, R), label="frontier")
    d_front = F.normalize(d_front, dim=1)

    # ---------------- HOLE ----------------
    seeds_h = torch.cat([Zn[torch.randint(0, n, (N_SEEDS // 2,))], blends(N_SEEDS // 2)])
    _, anchors = topk_sims(seeds_h, Zn, k=N_ANCHORS)
    # a hole seed is the centroid of its anchors; keep the emptiest centroids for refinement
    cent = F.normalize(Zn[anchors].mean(1), dim=1)
    keep_h = best(cent, N_REFINE)
    anchors = anchors[keep_h]
    A = Zn[anchors]                                  # (N_REFINE, 24, D)

    def mix(P):
        return F.normalize((F.softplus(P).unsqueeze(2) * A).sum(1), dim=1)

    P_h = ascend(mix, torch.zeros(len(anchors), N_ANCHORS), Zn, lr=0.05, label="hole")
    d_hole = mix(P_h)
    w_hole = F.softplus(P_h)

    # ---------------- score, filter, select ----------------
    adult = torch.tensor([bool(ADULT & set(c)) or bool(ADULT_TAGS & set(t))
                          for c, t in zip(g.content_descriptors, g.tags)])
    nonen = torch.tensor((g.lang != "en").values)
    space = pd.read_parquet(DATA / "space.parquet")
    real_sem = np.sort(space.loc[space.embeddable, "novelty_sem"].values)

    dec = torch.load(DATA / "decoder_bge.pt")
    model = import_module("04_space").Decoder(D, len(dec["labels"]))
    model.load_state_dict(dec["state_dict"])
    labels = dec["labels"]

    all_rows, voids, dirs = [], [], []
    for family, d in (("frontier", d_front), ("hole", d_hole)):
        v, i = topk_sims(d, Zn, k=20)
        emp = 1 - v[:, :K].mean(1)
        rad = radius(d)
        fa, fn = adult[i].float().mean(1), nonen[i].float().mean(1)
        with torch.no_grad():
            Pall = torch.sigmoid(model(m * d))
        adult_cols = [labels.index(f"tag:{t}") for t in ADULT_TAGS if f"tag:{t}" in labels]
        p_adult = Pall[:, adult_cols].max(1).values
        ok = (fa <= 0.25) & (fn <= 0.25) & (rad <= R * 1.01) & (p_adult <= MAX_ADULT_P)
        pct = np.searchsorted(real_sem, emp.numpy()) / len(real_sem) * 100
        # parents: non-negative reconstruction from 16 nearest games (frontier) / anchor weights (hole)
        _, i16 = topk_sims(d, Zn, k=16)
        rows = pd.DataFrame({"family": family, "emptiness": emp.numpy(), "percentile_vs_games": pct,
                             "nn1_sim": v[:, 0].numpy(), "radius": rad.numpy(), "frac_adult": fa.numpy(),
                             "frac_nonen": fn.numpy(), "ok": ok.numpy()})
        all_rows.append(rows)
        print(f"[{family}] emptiness median {emp.median():.4f} max {emp.max():.4f}; "
              f"percentile vs games median {np.median(pct):.2f}; pass filters {int(ok.sum())}", flush=True)

        chosen = []
        for j in [j for j in torch.argsort(emp, descending=True).tolist() if ok[j]]:
            nb = set(i[j, :K].tolist())
            if all(float(d[j] @ d[c]) < SEP and len(nb & set(i[c, :K].tolist())) <= 2 for c in chosen) and \
                    all(float(d[j] @ pd_) < SEP for pd_ in dirs):
                chosen.append(j)
            if len(chosen) == N_PER_FAMILY:
                break
        with torch.no_grad():
            Pr = torch.sigmoid(model(m * d[chosen])).numpy()
        for r_, j in enumerate(chosen):
            p = Pr[r_]
            lo = np.argsort(-p)
            if family == "hole":
                ww = w_hole[j].numpy()
                idx = anchors[j].numpy()
                fit = 1.0
            else:
                idx = i16[j].numpy()
                B = Zn[idx].numpy().T
                ww, _ = nnls(B, d[j].numpy())
                rec = B @ ww
                fit = float(rec @ d[j].numpy() / (np.linalg.norm(rec) + 1e-12))
            order = np.argsort(-ww)[:6]
            parents = [{"appid": int(g.appid.iloc[int(idx[q])]), "name": g.name.iloc[int(idx[q])],
                        "weight": round(float(ww[q] / ww.sum()), 3)} for q in order if ww[q] > 1e-6]
            nbrs = [{"appid": int(g.appid.iloc[int(i[j, t])]), "name": g.name.iloc[int(i[j, t])],
                     "sim": round(float(v[j, t]), 4), "tags": list(g.concept_tags.iloc[int(i[j, t])][:8]),
                     "short_description": g.short_description.iloc[int(i[j, t])][:300]} for t in range(15)]
            voids.append({
                "void_id": f"V{len(voids) + 1:02d}",
                "family": family,
                "emptiness": round(float(emp[j]), 4),
                "emptiness_percentile_vs_games": round(float(pct[j]), 3),
                "nearest_game_sim": round(float(v[j, 0]), 4),
                "radius": round(float(rad[j]), 3),
                "parent_fit_cos": round(fit, 3),
                "parent_games": parents,
                "decoded_tags": [(labels[c][4:], round(float(p[c]), 3)) for c in lo if labels[c].startswith("tag:")][:15],
                "decoded_player_modes": [(labels[c][5:], round(float(p[c]), 3)) for c in lo
                                         if labels[c].startswith("mode:")],
                "neighbors": nbrs,
            })
            dirs.append(d[j])
    pd.concat(all_rows).to_parquet(DATA / "void_candidates.parquet", index=False)
    np.save(DATA / "void_dirs.npy", torch.stack(dirs).numpy())
    (DATA / "voids.json").write_text(json.dumps(voids, indent=1, ensure_ascii=False))
    for vd in voids:
        print(vd["void_id"], vd["family"], vd["emptiness"], f"pct={vd['emptiness_percentile_vs_games']}",
              "|", ", ".join(t for t, _ in vd["decoded_tags"][:7]), "| parents:",
              "; ".join(p["name"] for p in vd["parent_games"][:3]))


if __name__ == "__main__":
    main()
