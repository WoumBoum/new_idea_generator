"""2-D map of Steam's idea-space for the report.

UMAP of every game's semantic coordinates (same 64-d space the voids were found in), then the voids
and the generated ideas are placed on it with umap.transform.
Caveat shown in the report: a 2-D picture cannot preserve 64-d emptiness. A void can look crowded on
the map because UMAP puts every point next to its nearest neighbours; the distances in the idea
cards (computed in the full space) are the real measurement.

Output: outputs/map.json (quantised coordinates + genre per game, names for well-known games,
        positions of voids and ideas)
"""
import base64
import json
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import umap
from sentence_transformers import SentenceTransformer

sys.path.insert(0, str(Path(__file__).parent))
from common import compose_doc, concept_tags_of  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
F = torch.nn.functional

# first match wins; order = most specific first
GENRES = [
    ("Visual Novel", {"Visual Novel", "Dating Sim", "Interactive Fiction", "Otome"}),
    ("Horror", {"Horror", "Psychological Horror", "Survival Horror"}),
    ("Shooter", {"FPS", "Shooter", "Shoot 'Em Up", "Bullet Hell", "Twin Stick Shooter", "Top-Down Shooter"}),
    ("Racing & Sports", {"Racing", "Sports", "Driving", "Football (Soccer)", "Golf", "Automobile Sim"}),
    ("Puzzle", {"Puzzle", "Logic", "Hidden Object", "Match 3", "Puzzle Platformer"}),
    ("Platformer", {"Platformer", "2D Platformer", "3D Platformer", "Precision Platformer", "Metroidvania"}),
    ("Strategy", {"Strategy", "RTS", "Turn-Based Strategy", "Tower Defense", "Grand Strategy", "4X", "Card Game",
                  "Deckbuilding", "Board Game", "Tactical"}),
    ("RPG", {"RPG", "Action RPG", "JRPG", "CRPG", "Roguelike", "Roguelite", "Dungeon Crawler"}),
    ("Simulation", {"Simulation", "Management", "City Builder", "Farming Sim", "Life Sim", "Building", "Sandbox",
                    "Survival", "Crafting"}),
    ("Adventure", {"Adventure", "Point & Click", "Walking Simulator", "Exploration", "Story Rich", "Mystery"}),
    ("Action", {"Action", "Fighting", "Hack and Slash", "Beat 'em up", "Arcade"}),
    ("Casual", {"Casual", "Clicker", "Idle", "Relaxing", "Cute", "Family Friendly"}),
]


def genre_of(tags):
    for t in tags:
        for gname, gset in GENRES:
            if t in gset:
                return gname
    return "Other"


def main():
    games = pd.read_parquet(DATA / "games.parquet")
    keep = games.embeddable.values
    g = games[keep].reset_index(drop=True)
    E = torch.from_numpy(np.load(DATA / "emb_bge.npy")[keep].astype(np.float32))
    pca = np.load(DATA / "pca_bge.npz")
    D = int(pca["d_sem"])
    mu = torch.from_numpy(pca["mean"])
    V = torch.from_numpy(pca["components"][:D])

    def sem(e):
        return F.normalize((e - mu) @ V.T, dim=1).numpy()

    cache = DATA / "umap.pkl"
    if cache.exists():  # the fit takes a while; reuse it when only the ideas changed
        reducer, XY = pickle.loads(cache.read_bytes())
    else:
        Zn = sem(E)
        print("fitting UMAP on", Zn.shape, flush=True)
        reducer = umap.UMAP(n_neighbors=15, min_dist=0.08, metric="euclidean", random_state=0, low_memory=True,
                            verbose=True)
        XY = reducer.fit_transform(Zn)
        cache.write_bytes(pickle.dumps((reducer, XY)))
    if len(sys.argv) > 1 and sys.argv[1] == "--fit-only":
        return

    voids = json.loads((DATA / "voids.json").read_text())
    vdirs = np.load(DATA / "void_dirs.npy")
    ideas = json.loads((OUT / "ideas.json").read_text())
    model = SentenceTransformer("BAAI/bge-small-en-v1.5", device="cpu")
    model.max_seq_length = 256

    def place(items):
        if not items:
            return []
        docs = [compose_doc(concept_tags_of(it["tags"]), it["short_description"], it["description"]) for it in items]
        e = torch.from_numpy(np.asarray(model.encode(docs, normalize_embeddings=True), dtype=np.float32))
        return reducer.transform(sem(e)).tolist()

    xy_void = reducer.transform(vdirs).tolist()
    # v2 voids live in the full space; project the decoded ones into the same semantic coordinates
    if (DATA / "voids_full.json").exists():
        decoded = {it["void_id"] for it in ideas["ideas"] if it.get("void_id")}
        vfull = json.loads((DATA / "voids_full.json").read_text())
        vecs = torch.from_numpy(np.load(DATA / "void_full_vecs.npy"))
        keep_v = [k for k, v in enumerate(vfull) if v["void_id"] in decoded]
        if keep_v:
            xy_void += reducer.transform(sem(vecs[keep_v])).tolist()
            voids = voids + [vfull[k] for k in keep_v]
    xy_idea = place(ideas["ideas"])
    xy_ctrl = place(ideas["controls"])

    lo, hi = XY.min(0), XY.max(0)

    def q(p):
        return [int(round((p[0] - lo[0]) / (hi[0] - lo[0]) * 4095)), int(round((p[1] - lo[1]) / (hi[1] - lo[1]) * 4095))]

    genre_names = [gn for gn, _ in GENRES] + ["Other"]
    gidx = {gn: k for k, gn in enumerate(genre_names)}
    famous = g.review_count.values >= 500
    xy16 = np.array([q(p) for p in XY], dtype=np.uint16).reshape(-1)
    genre8 = np.array([gidx[genre_of(t)] for t in g.concept_tags], dtype=np.uint8)
    out = {
        "n": int(len(g)),
        "genres": genre_names,
        "xy_b64": base64.b64encode(xy16.tobytes()).decode(),        # uint16 x,y pairs on a 0..4095 grid
        "genre_b64": base64.b64encode(genre8.tobytes()).decode(),   # uint8 index into genres
        "labels": [[int(k), g.name.iloc[k]] for k in np.where(famous)[0]],  # games with >= 500 reviews
        "voids": [{"void_id": v["void_id"], "family": v["family"], "xy": q(p)} for v, p in zip(voids, xy_void)],
        "ideas": [{"rank": it["rank"], "title": it["title"], "void_id": it["void_id"], "xy": q(p)}
                  for it, p in zip(ideas["ideas"], xy_idea)],
        "controls": [{"title": it["title"], "xy": q(p)} for it, p in zip(ideas["controls"], xy_ctrl)],
    }
    (OUT / "map.json").write_text(json.dumps(out, separators=(",", ":"), ensure_ascii=False))
    print("wrote outputs/map.json", len(out["labels"]), "labelled games", flush=True)


if __name__ == "__main__":
    main()
