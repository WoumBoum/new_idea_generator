"""Measure the shape of Steam's idea-space.

For each embedding model:
  1. exact k-nearest-neighbours of every game (cosine, k=30, self excluded)
  2. isolation of every game:  novelty = 1 - mean cosine similarity to its 10 nearest games
     (this distribution is the yardstick every generated idea is compared against)
For the primary model (bge) only:
  3. PCA of the space. The top-D centred components are the "semantic coordinates" z used by the
     void search: a game and a synthetic point are compared by cosine of their z, so neither side
     is advantaged by the idiosyncratic leftover dimensions every real text carries.
     Isolation of every game is also measured in these coordinates (the void-search yardstick).
  4. a linear decoder  z -> P(tag), P(player mode)   (the "vector -> metadata" inverse),
     trained on 90% of games, validated on 10%.

Outputs: data/knn_<key>.npz, data/space.parquet, data/pca_bge.npz, data/decoder_bge.pt, data/decoder_metrics.json
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
K = 30
K_NOVELTY = 10
D_SEM = 64  # semantic coordinates = top-64 centred principal components
torch.set_num_threads(4)


def load_emb(key):
    return torch.from_numpy(np.load(DATA / f"emb_{key}.npy").astype(np.float32))


def knn_all(E, mask, k=K, block=2048):
    """Exact top-k cosine neighbours of every row among rows where mask is True (self excluded)."""
    ref_idx = torch.nonzero(mask).squeeze(1)
    R = E[ref_idx]
    n = E.shape[0]
    idx = np.zeros((n, k), dtype=np.int32)
    sim = np.zeros((n, k), dtype=np.float32)
    for s in range(0, n, block):
        S = E[s:s + block] @ R.T  # (b, n_ref)
        rows = torch.arange(s, min(s + block, n))
        # exclude self: position of row i inside ref_idx
        self_pos = torch.searchsorted(ref_idx, rows)
        hit = (self_pos < len(ref_idx)) & (ref_idx[self_pos.clamp(max=len(ref_idx) - 1)] == rows)
        S[torch.arange(len(rows))[hit], self_pos[hit]] = -2.0
        v, j = torch.topk(S, k, dim=1)
        idx[s:s + block] = ref_idx[j].numpy()
        sim[s:s + block] = v.numpy()
        if (s // block) % 20 == 0:
            print(f"  knn {s}/{n}", flush=True)
    return idx, sim


class Decoder(torch.nn.Module):
    """Linear probe on standardised semantic coordinates."""

    def __init__(self, d_in, n_out):
        super().__init__()
        self.register_buffer("mu", torch.zeros(d_in))
        self.register_buffer("sd", torch.ones(d_in))
        self.lin = torch.nn.Linear(d_in, n_out)

    def forward(self, z):
        return self.lin((z - self.mu) / self.sd)


def train_decoder(Z, Y, label_names, epochs=15):
    """Multi-label linear probe: semantic coords -> label logits. Returns model + validation metrics."""
    n = Z.shape[0]
    g = torch.Generator().manual_seed(0)
    perm = torch.randperm(n, generator=g)
    n_val = n // 10
    va, tr = perm[:n_val], perm[n_val:]
    Yt = torch.from_numpy(Y.astype(np.float32))
    model = Decoder(Z.shape[1], Y.shape[1])
    model.mu.copy_(Z[tr].mean(0))
    model.sd.copy_(Z[tr].std(0))
    opt = torch.optim.Adam(model.parameters(), lr=3e-3)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, epochs)
    lossf = torch.nn.BCEWithLogitsLoss()
    for ep in range(epochs):
        p = tr[torch.randperm(len(tr), generator=g)]
        for b in range(0, len(p), 512):
            bi = p[b:b + 512]
            opt.zero_grad()
            loss = lossf(model(Z[bi]), Yt[bi])
            loss.backward()
            opt.step()
        sched.step()
        with torch.no_grad():
            vl = lossf(model(Z[va]), Yt[va]).item()
        print(f"  decoder epoch {ep} val_loss {vl:.4f}", flush=True)
    with torch.no_grad():
        P = torch.sigmoid(model(Z[va])).numpy()
    Yv = Y[va.numpy()]
    from sklearn.metrics import average_precision_score, roc_auc_score
    common = np.argsort(-Y.sum(0))[:60]
    ap = {label_names[c]: float(average_precision_score(Yv[:, c], P[:, c])) for c in common if Yv[:, c].sum() > 5}
    auc = float(np.mean([roc_auc_score(Yv[:, c], P[:, c]) for c in common if 0 < Yv[:, c].sum() < len(Yv)]))
    topk = np.argsort(-P, axis=1)[:, :5]
    prec5 = float(np.mean([Yv[i, topk[i]].mean() for i in range(len(Yv))]))
    base5 = float(np.mean([Yv[i, common[:5]].mean() for i in range(len(Yv))]))
    return model, {"val_games": int(n_val), "mean_auc_top60_labels": auc, "precision_at_5": prec5,
                   "precision_at_5_if_always_guessing_5_most_common": base5,
                   "avg_precision_top60": float(np.mean(list(ap.values()))), "per_label_ap": ap}


def main():
    keys = sys.argv[1:] or ["bge", "minilm"]
    games = pd.read_parquet(DATA / "games.parquet")
    mask = torch.from_numpy(games.embeddable.values.copy())
    space = pd.DataFrame({"appid": games.appid})

    for key in keys:
        print(f"[{key}] kNN", flush=True)
        E = load_emb(key)
        idx, sim = knn_all(E, mask)
        np.savez_compressed(DATA / f"knn_{key}.npz", idx=idx, sim=sim.astype(np.float16))
        space[f"novelty_{key}"] = 1 - sim[:, :K_NOVELTY].mean(1)
        space[f"nn1_sim_{key}"] = sim[:, 0]
        space[f"nn1_{key}"] = games.appid.values[idx[:, 0]]
        nov = space.loc[games.embeddable.values, f"novelty_{key}"]
        print(f"[{key}] novelty quantiles:", nov.quantile([.5, .9, .99, .999]).round(4).to_dict(), flush=True)
    space["embeddable"] = games.embeddable.values
    space.to_parquet(DATA / "space.parquet", index=False)

    if "bge" in keys:
        E = load_emb("bge")[mask]
        mu = E.mean(0)
        U, S, Vt = torch.linalg.svd(E - mu, full_matrices=False)
        var = (S ** 2) / (S ** 2).sum()
        np.savez(DATA / "pca_bge.npz", mean=mu.numpy(), components=Vt.numpy(), sing=S.numpy(),
                 explained=var.numpy(), d_sem=D_SEM)
        print(f"PCA explained variance, first {D_SEM} comps: {float(var[:D_SEM].sum()):.3f}", flush=True)

        # isolation in semantic coordinates (centred top-D PCA, cosine)
        Z = (E - mu) @ Vt[:D_SEM].T
        Zn = torch.nn.functional.normalize(Z, dim=1)
        _, sim_sem = knn_all(Zn, torch.ones(len(Zn), dtype=torch.bool), k=K_NOVELTY)
        sem = np.full(len(games), np.nan, dtype=np.float32)
        sem[games.embeddable.values] = 1 - sim_sem.mean(1)
        space["novelty_sem"] = sem
        space.to_parquet(DATA / "space.parquet", index=False)
        print("semantic-space novelty quantiles:",
              pd.Series(sem).dropna().quantile([.5, .9, .99, .999]).round(4).to_dict(), flush=True)

        g = games[games.embeddable].reset_index(drop=True)
        tag_counts = pd.Series([t for ts in g.concept_tags for t in ts]).value_counts()
        tag_names = tag_counts[tag_counts >= 150].index.tolist()
        modes_present = pd.Series([m for ms in g.player_modes for m in ms]).value_counts()
        mode_names = [m for m in modes_present.index if modes_present[m] >= 150]
        labels = [f"tag:{t}" for t in tag_names] + [f"mode:{m}" for m in mode_names]
        Y = np.zeros((len(g), len(labels)), dtype=np.uint8)
        col = {l: i for i, l in enumerate(labels)}
        for r, (ts, ms) in enumerate(zip(g.concept_tags, g.player_modes)):
            for t in ts:
                if f"tag:{t}" in col:
                    Y[r, col[f"tag:{t}"]] = 1
            for m in ms:
                if f"mode:{m}" in col:
                    Y[r, col[f"mode:{m}"]] = 1
        print(f"decoder: {len(tag_names)} tags + {len(mode_names)} player modes", flush=True)
        model, metrics = train_decoder(Z, Y, labels)
        torch.save({"state_dict": model.state_dict(), "labels": labels, "d_in": D_SEM}, DATA / "decoder_bge.pt")
        (DATA / "decoder_metrics.json").write_text(json.dumps(metrics, indent=1))
        print("decoder metrics:", {k: v for k, v in metrics.items() if not isinstance(v, dict)}, flush=True)


if __name__ == "__main__":
    main()
