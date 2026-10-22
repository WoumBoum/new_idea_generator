"""Re-score every generated text with the scoring server (both models) and rank the ideas.

Nothing the agents *reported* about their own scores is trusted: every final text is re-embedded here.

Novelty unit: for each model, z = (novelty - mean novelty of real games) / std of real games,
i.e. "how many standard deviations more isolated than a typical Steam game". The ranking key is the
average z over the two independently trained embedding models (bge-small, MiniLM). The agents only
ever saw bge scores, so MiniLM doubles as a held-out check that an idea is not just exploiting bge.

Arms
  v1-void       voids found in the top-64 principal components (05_voids.py): frontier + hole families
  v2-blend      voids found in the full space as the emptiest mix of 2-3 established games (05b)
  v3-search     no target point: the LLM iterates drafts against the bge novelty score
  control       the same LLM asked for original ideas, no vector space at all
  calibration   24 real Steam games rewritten from scratch (same idea, new words)

Inputs  outputs/raw/{decoded,decoded_v2,novelty_search,control,calibration}.json
Outputs outputs/ideas.json, outputs/stats.json
"""
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from scipy.stats import mannwhitneyu

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
RAW = OUT / "raw"
SERVER = f"http://127.0.0.1:{os.environ.get('PORT', 8766)}"

space = pd.read_parquet(ROOT / "data" / "space.parquet")
real = space[space.embeddable]
REF = {k: (float(real[f"novelty_{k}"].mean()), float(real[f"novelty_{k}"].std())) for k in ("bge", "minilm")}


def rescore(item, void_id=None):
    r = requests.post(f"{SERVER}/score", json={"void_id": void_id, "tags": item["tags"],
                                               "short_description": item["short_description"],
                                               "description": item["description"]}, timeout=120).json()
    assert r.get("novelty_minilm") is not None, "ranking server must run both models"
    r.pop("doc_embedded", None)
    r["z_bge"] = (r["novelty_bge"] - REF["bge"][0]) / REF["bge"][1]
    r["z_minilm"] = (r["novelty_minilm"] - REF["minilm"][0]) / REF["minilm"][1]
    r["novelty_z"] = (r["z_bge"] + r["z_minilm"]) / 2
    return r


def load(name):
    p = RAW / f"{name}.json"
    return json.loads(p.read_text()) if p.exists() else []


def main():
    voids = {v["void_id"]: v for v in json.loads((ROOT / "data" / "voids.json").read_text())}
    if (ROOT / "data" / "voids_full.json").exists():
        voids.update({v["void_id"]: v for v in json.loads((ROOT / "data" / "voids_full.json").read_text())})

    ideas = []
    for arm, rows in (("v1-void", load("decoded")), ("v2-blend", load("decoded_v2"))):
        for it in rows:
            v = voids[it["void_id"]]
            ideas.append({**it, "method": arm, "family": v["family"], "void_emptiness": v["emptiness"],
                          "void_emptiness_percentile": v["emptiness_percentile_vs_games"],
                          "void_parents": [p["name"] for p in v["parent_games"][:3]],
                          "score": rescore(it, it["void_id"])})
    for it in load("novelty_search"):
        ideas.append({**it, "method": "v3-search", "family": "search", "void_id": None, "score": rescore(it)})
    controls = [{**it, "method": "control", "score": rescore(it)} for it in load("control")]

    calib = []
    for it in load("calibration"):
        s = rescore(it)
        ids = [n["appid"] for n in s["nearest"]]
        it["original_rank_in_nearest"] = ids.index(it["original_appid"]) + 1 if it["original_appid"] in ids else None
        o = real.loc[real.appid == it["original_appid"]].iloc[0]
        it["original_novelty_z"] = float(((o.novelty_bge - REF["bge"][0]) / REF["bge"][1] +
                                          (o.novelty_minilm - REF["minilm"][0]) / REF["minilm"][1]) / 2)
        calib.append({**it, "method": "calibration", "score": s})

    ideas.sort(key=lambda r: -r["score"]["novelty_z"])
    for k, r in enumerate(ideas, 1):
        r["rank"] = k
    zs = [r["score"]["novelty_z"] for r in ideas]
    for c in controls:  # where each control idea would have ranked among the pipeline ideas
        c["would_rank"] = 1 + sum(z > c["score"]["novelty_z"] for z in zs)
    (OUT / "ideas.json").write_text(json.dumps({"ideas": ideas, "controls": controls, "calibration": calib},
                                               indent=1, ensure_ascii=False))

    def summary(grp):
        z = np.array([r["score"]["novelty_z"] for r in grp])
        out = {"n": len(grp), "novelty_z_median": float(np.median(z)), "novelty_z_mean": float(z.mean()),
               "novelty_z_max": float(z.max()),
               "bge_percentile_median": float(np.median([r["score"]["novelty_bge_percentile"] for r in grp])),
               "minilm_percentile_median_heldout": float(np.median([r["score"]["novelty_minilm_percentile"] for r in grp])),
               "semantic_percentile_median": float(np.median([r["score"]["novelty_sem_percentile"] for r in grp])),
               "share_top5pct_both_models": float(np.mean([r["score"]["novelty_bge_percentile"] >= 95 and
                                                           r["score"]["novelty_minilm_percentile"] >= 95 for r in grp]))}
        ts = [r["score"]["target_sim"] for r in grp if r["score"].get("target_sim") is not None]
        if ts:
            out["target_sim_median"] = float(np.median(ts))
        return out

    stats = {"reference": {k: {"mean": m, "std": s} for k, (m, s) in REF.items()}, "n_games": int(len(real)),
             "arms": {}}
    groups = {
        "v1-void (frontier)": [r for r in ideas if r["method"] == "v1-void" and r["family"] == "frontier"],
        "v1-void (hole)": [r for r in ideas if r["method"] == "v1-void" and r["family"] == "hole"],
        "v2-blend": [r for r in ideas if r["method"] == "v2-blend"],
        "v3-search": [r for r in ideas if r["method"] == "v3-search"],
        "control": controls,
        "calibration": calib,
    }
    cz = [r["score"]["novelty_z"] for r in controls]
    for name, grp in groups.items():
        if not grp:
            continue
        stats["arms"][name] = summary(grp)
        if controls and name != "control":
            z = [r["score"]["novelty_z"] for r in grp]
            stats["arms"][name]["p_more_novel_than_control"] = float(mannwhitneyu(z, cz, alternative="greater").pvalue)
            stats["arms"][name]["p_less_novel_than_control"] = float(mannwhitneyu(z, cz, alternative="less").pvalue)
    allg = ideas + controls
    stats["heldout_corr_bge_vs_minilm_z"] = float(np.corrcoef([r["score"]["z_bge"] for r in allg],
                                                              [r["score"]["z_minilm"] for r in allg])[0, 1])
    if calib:
        stats["calibration_original_found_in_top8"] = float(np.mean([c["original_rank_in_nearest"] is not None for c in calib]))
        stats["calibration_original_is_nearest"] = float(np.mean([c["original_rank_in_nearest"] == 1 for c in calib]))
    realz = ((real.novelty_bge - REF["bge"][0]) / REF["bge"][1] +
             (real.novelty_minilm - REF["minilm"][0]) / REF["minilm"][1]) / 2
    stats["real_games_z_quantiles"] = {str(q): float(np.quantile(realz, q / 100)) for q in (50, 90, 99, 99.9)}
    stats["real_games_z_max"] = float(realz.max())
    (OUT / "stats.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps(stats, indent=1))
    for r in ideas[:20]:
        s = r["score"]
        print(f"#{r['rank']:2d} z={s['novelty_z']:.2f} bge%={s['novelty_bge_percentile']:.2f} "
              f"minilm%={s['novelty_minilm_percentile']:.2f} [{r['method']}/{r['family']}] {r['title']}")


if __name__ == "__main__":
    main()
