"""Embed every game's concept document.

usage: python pipeline/03_embed.py <model-key>     (keys: bge, minilm)

Runs on CPU with bf16 autocast (uses AMX/AVX-512 where present; ~2.5x faster than fp32,
cosine agreement with fp32 > 0.9999). Checkpoints every chunk so a restart resumes.
Output: data/emb_<key>.npy (float16, L2-normalised, row i = games.parquet row i)
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parents[1]
MODELS = {
    "bge": "BAAI/bge-small-en-v1.5",
    "minilm": "sentence-transformers/all-MiniLM-L6-v2",
}
CHUNK = 8192


def load_model(key):
    m = SentenceTransformer(MODELS[key], device="cpu")
    m.max_seq_length = 256
    return m


def encode(model, texts, batch_size=64):
    with torch.autocast("cpu", dtype=torch.bfloat16):
        e = model.encode(texts, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=False)
    e = np.asarray(e, dtype=np.float32)
    return e / np.linalg.norm(e, axis=1, keepdims=True)


def main():
    key = sys.argv[1]
    torch.set_num_threads(4)
    docs = pd.read_parquet(ROOT / "data" / "games.parquet", columns=["doc"]).doc.fillna("").tolist()
    model = load_model(key)
    dim = model.get_sentence_embedding_dimension()
    ck_dir = ROOT / "data" / f"emb_{key}_chunks"
    ck_dir.mkdir(exist_ok=True)
    t0 = time.time()
    for ci, start in enumerate(range(0, len(docs), CHUNK)):
        f = ck_dir / f"{ci:04d}.npy"
        if f.exists():
            continue
        np.save(f, encode(model, docs[start:start + CHUNK]).astype(np.float16))
        done = min(start + CHUNK, len(docs))
        rate = done / (time.time() - t0)
        print(f"[{key}] {done}/{len(docs)}  {rate:.0f} docs/s  eta {(len(docs) - done) / max(rate, 1e-9) / 60:.0f} min",
              flush=True)
    emb = np.concatenate([np.load(ck_dir / f"{i:04d}.npy") for i in range((len(docs) + CHUNK - 1) // CHUNK)])
    assert emb.shape == (len(docs), dim), emb.shape
    np.save(ROOT / "data" / f"emb_{key}.npy", emb)
    print(f"[{key}] saved {emb.shape}", flush=True)


if __name__ == "__main__":
    main()
