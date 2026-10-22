"""Scoring server: embeds a draft game idea exactly like a real Steam game and reports where it lands.

Runs on http://127.0.0.1:8765 . Decoder agents call it in a loop: write -> score -> revise.

GET  /void/<id>        the void's target info: decoded tags, player modes, the 15 nearest real games
GET  /tags             Steam's tag vocabulary (only these tags are accepted)
POST /score            {"void_id": "V07" | null, "tags": [...], "short_description": "...", "description": "..."}
                       -> target_sim     cosine between the draft and the void point (how well it landed)
                          novelty_bge    1 - mean cosine to the 10 nearest of 195k Steam games (primary model)
                          novelty_minilm same, under a second, independently trained embedding model
                          *_percentile   share of real Steam games that are LESS isolated than this draft
                          nearest        the closest real games, so the writer can see what it collides with
                          decoded_tags   what the metadata decoder reads back from the draft's vector
POST /nearest          {"text": "..."}  -> nearest real games to free text (a "does this exist?" probe)
Every /score call is appended to data/score_log.jsonl (the audit trail of each idea's iterations).
"""
import json
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer

sys.path.insert(0, str(Path(__file__).parent))
from common import compose_doc, concept_tags_of  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PORT = 8765
torch.set_num_threads(4)

games = pd.read_parquet(DATA / "games.parquet")
keep = games.embeddable.values
g = games[keep].reset_index(drop=True)
space = pd.read_parquet(DATA / "space.parquet")
REAL_NOV = {k: np.sort(space.loc[space.embeddable, f"novelty_{k}"].values) for k in ("bge", "minilm")}
EMB = {k: torch.from_numpy(np.load(DATA / f"emb_{k}.npy")[keep].astype(np.float32)) for k in ("bge", "minilm")}
MODELS = {"bge": SentenceTransformer("BAAI/bge-small-en-v1.5", device="cpu"),
          "minilm": SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")}
for m in MODELS.values():
    m.max_seq_length = 256
dec = torch.load(DATA / "decoder_bge.pt")
LIN = torch.nn.Linear(384, len(dec["labels"]))
LIN.load_state_dict(dec["state_dict"])
LABELS = dec["labels"]
VOIDS = {v["void_id"]: v for v in json.loads((DATA / "voids.json").read_text())} if (DATA / "voids.json").exists() else {}
VOID_VEC = torch.from_numpy(np.load(DATA / "void_vectors.npy")) if (DATA / "void_vectors.npy").exists() else None
VOCAB = sorted({t for ts in games.tags for t in ts})
VOCAB_LOWER = {t.lower(): t for t in VOCAB}
LOCK = threading.Lock()
LOG = open(DATA / "score_log.jsonl", "a")


def embed(key, text):
    with LOCK, torch.no_grad(), torch.autocast("cpu", dtype=torch.bfloat16):
        e = MODELS[key].encode([text], normalize_embeddings=True, show_progress_bar=False)
    e = torch.from_numpy(np.asarray(e, dtype=np.float32))
    return torch.nn.functional.normalize(e, dim=1)[0]


def novelty(key, e, k=10):
    v, i = torch.topk(EMB[key] @ e, 15)
    nov = 1 - float(v[:k].mean())
    pct = float(np.searchsorted(REAL_NOV[key], nov) / len(REAL_NOV[key]) * 100)
    return nov, pct, v, i


def score(req):
    raw_tags = req.get("tags") or []
    tags, unknown = [], []
    for t in raw_tags:
        canon = VOCAB_LOWER.get(str(t).strip().lower())
        (tags.append(canon) if canon else unknown.append(t))
    short = (req.get("short_description") or "").strip()
    desc = (req.get("description") or "").strip()
    ctags = concept_tags_of(tags)
    doc = compose_doc(ctags, short, desc)
    e_bge = embed("bge", doc)
    e_min = embed("minilm", doc)
    nb, pb, v, i = novelty("bge", e_bge)
    nm, pm, _, _ = novelty("minilm", e_min)
    out = {
        "novelty_bge": round(nb, 4), "novelty_bge_percentile": round(pb, 3),
        "novelty_minilm": round(nm, 4), "novelty_minilm_percentile": round(pm, 3),
        "nearest": [{"name": g.name.iloc[int(j)], "appid": int(g.appid.iloc[int(j)]), "sim": round(float(s), 4),
                     "tags": list(g.concept_tags.iloc[int(j)][:6])} for s, j in zip(v[:8], i[:8])],
        "unknown_tags_dropped": unknown,
        "doc_embedded": doc,
        "warnings": [],
    }
    with torch.no_grad():
        p = torch.sigmoid(LIN(e_bge)).numpy()
    out["decoded_tags"] = [(LABELS[c][4:], round(float(p[c]), 2)) for c in np.argsort(-p)
                           if LABELS[c].startswith("tag:")][:10]
    vid = req.get("void_id")
    if vid:
        if vid not in VOIDS:
            out["warnings"].append(f"unknown void_id {vid}")
        else:
            idx = list(VOIDS).index(vid)
            out["void_id"] = vid
            out["target_sim"] = round(float(VOID_VEC[idx] @ e_bge), 4)
            out["void_nearest_game_sim"] = VOIDS[vid]["nearest_game_sim"]
    if len(short) > 320:
        out["warnings"].append("short_description over 320 chars (Steam caps ~300)")
    if len(desc.split()) < 60:
        out["warnings"].append("description under 60 words; write ~120-200 words like a store page")
    LOG.write(json.dumps({"t": time.time(), "req": req, "res": {k: out[k] for k in out if k != "doc_embedded"}}) + "\n")
    LOG.flush()
    return out


def nearest(req):
    e = embed("bge", req.get("text", ""))
    _, _, v, i = novelty("bge", e)
    return {"nearest": [{"name": g.name.iloc[int(j)], "appid": int(g.appid.iloc[int(j)]), "sim": round(float(s), 4),
                         "tags": list(g.concept_tags.iloc[int(j)][:6]),
                         "short_description": g.short_description.iloc[int(j)][:200]} for s, j in zip(v[:10], i[:10])]}


class H(BaseHTTPRequestHandler):
    def _send(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path.startswith("/void/"):
            vid = self.path.split("/")[-1]
            return self._send(VOIDS[vid]) if vid in VOIDS else self._send({"error": "unknown void"}, 404)
        if self.path == "/tags":
            return self._send(VOCAB)
        if self.path == "/health":
            return self._send({"ok": True, "voids": len(VOIDS), "games": len(g)})
        self._send({"error": "not found"}, 404)

    def do_POST(self):
        try:
            req = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            if self.path == "/score":
                return self._send(score(req))
            if self.path == "/nearest":
                return self._send(nearest(req))
            self._send({"error": "not found"}, 404)
        except Exception as ex:  # report, don't crash the server
            self._send({"error": repr(ex)}, 400)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print(f"serving {len(g)} games, {len(VOIDS)} voids on :{PORT}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
