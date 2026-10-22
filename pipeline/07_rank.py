"""Re-score every generated text with the scoring server and rank the ideas.

Nothing the decoder agents *reported* about their own scores is trusted: every final idea, control
idea and calibration rewrite is re-embedded here.

Novelty unit: for each model, z = (novelty - mean novelty of real games) / std of real games,
i.e. "how many standard deviations more isolated than a typical Steam game". The ranking key is the
average z over the two independently trained embedding models (bge-small, MiniLM).

Inputs  outputs/raw/decoded.json, outputs/raw/control.json, outputs/raw/calibration.json
Outputs outputs/ideas.json, outputs/stats.json
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from scipy.stats import mannwhitneyu

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
RAW = OUT / "raw"
SERVER = "http://127.0.0.1:8765"

space = pd.read_parquet(ROOT / "data" / "space.parquet")
real = space[space.embeddable]
REF = {k: (real[f"novelty_{k}"].mean(), real[f"novelty_{k}"].std()) for k in ("bge", "minilm")}


def rescore(item, void_id=None):
    r = requests.post(f"{SERVER}/score", json={"void_id": void_id, "tags": item["tags"],
                                               "short_description": item["short_description"],
                                               "description": item["description"]}, timeout=120).json()
    r["z_bge"] = (r["novelty_bge"] - REF["bge"][0]) / REF["bge"][1]
    r["z_minilm"] = (r["novelty_minilm"] - REF["minilm"][0]) / REF["minilm"][1]
    r["novelty_z"] = (r["z_bge"] + r["z_minilm"]) / 2
    return r


def main():
    voids = {v["void_id"]: v for v in json.loads((ROOT / "data" / "voids.json").read_text())}
    decoded = json.loads((RAW / "decoded.json").read_text())
    rows = []
    for it in decoded:
        s = rescore(it, it["void_id"])
        v = voids[it["void_id"]]
        rows.append({**it, "group": "void-decoded", "family": v["family"], "void_emptiness": v["emptiness"],
                     "void_emptiness_percentile": v["emptiness_percentile_vs_games"], "score": s})
    controls, calib = [], []
    if (RAW / "control.json").exists():
        for it in json.loads((RAW / "control.json").read_text()):
            controls.append({**it, "group": "control-brainstorm", "score": rescore(it)})
    if (RAW / "calibration.json").exists():
        for it in json.loads((RAW / "calibration.json").read_text()):
            s = rescore(it)
            names = [n["appid"] for n in s["nearest"]]
            it["original_rank_in_nearest"] = names.index(it["original_appid"]) + 1 if it["original_appid"] in names else None
            orig = space.loc[space.appid == it["original_appid"]].iloc[0]
            it["original_novelty_z"] = float(((orig.novelty_bge - REF["bge"][0]) / REF["bge"][1] +
                                              (orig.novelty_minilm - REF["minilm"][0]) / REF["minilm"][1]) / 2)
            calib.append({**it, "group": "calibration-rewrite", "score": s})

    rows.sort(key=lambda r: -r["score"]["novelty_z"])
    for k, r in enumerate(rows, 1):
        r["rank"] = k
    (OUT / "ideas.json").write_text(json.dumps({"ideas": rows, "controls": controls, "calibration": calib},
                                               indent=1, ensure_ascii=False))

    def zs(group):
        return np.array([r["score"]["novelty_z"] for r in group])

    stats = {"reference": {k: {"mean": float(m), "std": float(s)} for k, (m, s) in REF.items()},
             "n_games": int(len(real))}
    for name, grp in (("void_decoded", rows), ("control_brainstorm", controls), ("calibration_rewrite", calib)):
        if grp:
            z = zs(grp)
            stats[name] = {"n": len(grp), "novelty_z_median": float(np.median(z)), "novelty_z_mean": float(z.mean()),
                           "novelty_z_max": float(z.max()),
                           "bge_percentile_median": float(np.median([r["score"]["novelty_bge_percentile"] for r in grp])),
                           "minilm_percentile_median": float(np.median([r["score"]["novelty_minilm_percentile"] for r in grp]))}
    for fam in ("frontier", "hole"):
        grp = [r for r in rows if r["family"] == fam]
        if grp:
            stats[f"void_decoded_{fam}"] = {"n": len(grp), "novelty_z_median": float(np.median(zs(grp))),
                                            "target_sim_median": float(np.median([r["score"]["target_sim"] for r in grp]))}
    if controls:
        u = mannwhitneyu(zs(rows), zs(controls), alternative="greater")
        stats["void_vs_control_mannwhitney_p"] = float(u.pvalue)
    if calib:
        stats["calibration_original_found_in_top8"] = float(np.mean([c["original_rank_in_nearest"] is not None for c in calib]))
        stats["calibration_original_is_nearest"] = float(np.mean([c["original_rank_in_nearest"] == 1 for c in calib]))
        stats["calibration_original_novelty_z_median"] = float(np.median([c["original_novelty_z"] for c in calib]))
    (OUT / "stats.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps(stats, indent=1))
    for r in rows[:15]:
        s = r["score"]
        print(f"#{r['rank']:2d} z={s['novelty_z']:.2f} bge%={s['novelty_bge_percentile']:.2f} "
              f"minilm%={s['novelty_minilm_percentile']:.2f} target={s.get('target_sim')} [{r['family']}] {r['title']}")


if __name__ == "__main__":
    main()
