"""Build the single-file HTML report from the pipeline outputs.

Inputs  outputs/ideas.json, outputs/stats.json, outputs/map.json, outputs/verify.json (optional),
        outputs/findings.json (narrative written after reading the results), data/voids*.json, score logs
Output  outputs/report.html
"""
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
DATA = ROOT / "data"

ARMS = [  # key, label, sub, filter
    ("calibration", "Rewritten Steam games", "same idea, new words", lambda r: r["method"] == "calibration"),
    ("control", "Brainstorm, no map", "AI asked for original ideas", lambda r: r["method"] == "control"),
    ("v1-frontier", "v1 · frontier voids", "empty points beyond the edge (64-d)", lambda r: r["method"] == "v1-void" and r["family"] == "frontier"),
    ("v1-hole", "v1 · hole voids", "gaps between games (64-d)", lambda r: r["method"] == "v1-void" and r["family"] == "hole"),
    ("v2-blend", "v2 · blend voids", "emptiest mix of 2-3 games (full space)", lambda r: r["method"] == "v2-blend"),
    ("v3-search", "v3 · novelty search", "AI writes, the space scores each draft", lambda r: r["method"] == "v3-search"),
]


def idea_key(r):
    return f"{r['method']}:{r.get('void_id') or r['title']}"


def slim(r, voids):
    s = r["score"]
    out = {k: r.get(k) for k in ("rank", "title", "method", "family", "void_id", "tags", "short_description",
                                 "description", "pitch", "drafts_scored", "void_emptiness_percentile",
                                 "void_parents", "would_rank")}
    out["key"] = idea_key(r)
    if r.get("void_id"):
        out["void_tags"] = [t for t, _ in voids[r["void_id"]]["decoded_tags"][:6]]
    out["score"] = {k: s.get(k) for k in ("novelty_z", "z_bge", "z_minilm", "novelty_bge_percentile",
                                          "novelty_minilm_percentile", "novelty_sem_percentile", "target_sim")}
    out["score"]["nearest"] = [{"name": n["name"], "appid": n["appid"], "sim": n["sim"]} for n in s["nearest"][:3]]
    return out


def logged_drafts_per_void():
    """Scored drafts per void from the server logs (agents' self-reports undercount scripted probes)."""
    c = {}
    for f in ("score_log.jsonl", "score_log_8767.jsonl"):
        p = DATA / f
        if p.exists():
            for line in open(p):
                v = json.loads(line)["req"].get("void_id")
                if v:
                    c[v] = c.get(v, 0) + 1
    return c


def count_drafts():
    n = 0
    for f in ("score_log.jsonl", "score_log_8767.jsonl"):
        p = DATA / f
        if p.exists():
            n += sum(1 for _ in open(p))
    return n


def main():
    ideas = json.loads((OUT / "ideas.json").read_text())
    stats = json.loads((OUT / "stats.json").read_text())
    mp = json.loads((OUT / "map.json").read_text())
    verify = json.loads((OUT / "verify.json").read_text()) if (OUT / "verify.json").exists() else {}
    text = json.loads((OUT / "findings.json").read_text())
    voids = {v["void_id"]: v for v in json.loads((DATA / "voids.json").read_text())}
    voids.update({v["void_id"]: v for v in json.loads((DATA / "voids_full.json").read_text())})
    meta_raw = json.loads((DATA / "raw" / "s2_meta.json").read_text())
    scraped = datetime.fromtimestamp(meta_raw["scraped_at_unix"], tz=timezone.utc).strftime("%-d %b %Y")

    everyone = ideas["ideas"] + ideas["controls"] + ideas["calibration"]
    arms = []
    for key, label, sub, f in ARMS:
        grp = [r for r in everyone if f(r)]
        if not grp:
            continue
        a = stats["arms"]
        name = {"calibration": "calibration", "control": "control", "v1-frontier": "v1-void (frontier)",
                "v1-hole": "v1-void (hole)", "v2-blend": "v2-blend", "v3-search": "v3-search"}[key]
        st = a[name]
        arms.append({"key": key, "label": label, "sub": sub, "z": [r["score"]["novelty_z"] for r in grp],
                     "titles": [r["title"] for r in grp], "median": st["novelty_z_median"],
                     "bge": st["bge_percentile_median"], "minilm": st["minilm_percentile_median_heldout"],
                     "top5": st["share_top5pct_both_models"], "landing": st.get("target_sim_median")})

    n_decoded_voids = len({r["void_id"] for r in ideas["ideas"] if r.get("void_id")})
    logged = logged_drafts_per_void()
    for r in ideas["ideas"]:
        if r.get("void_id"):
            r["drafts_scored"] = logged.get(r["void_id"], r.get("drafts_scored"))
    payload = {
        "meta": {"scraped": scraped, "n_games": len(pd.read_parquet(DATA / "games.parquet", columns=["appid"])),
                 "n_voids": n_decoded_voids,
                 "n_drafts": count_drafts()},
        "stats": stats,
        "arms": arms,
        "ideas": [slim(r, voids) for r in ideas["ideas"]],
        "controls": [slim(r, voids) for r in ideas["controls"]],
        "verify": verify,
        "map": mp,
        **text,
    }
    html = (ROOT / "report" / "template.html").read_text()
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = html.replace("/*__DATA__*/null", blob)
    (OUT / "report.html").write_text(html)
    print(f"wrote outputs/report.html ({len(html) / 1e6:.2f} MB)")
    write_markdown(payload)


VERDICT = {"none_found": "no prior game found", "close": "a close game exists", "exists": "already exists"}
LABEL = {"v1-void/frontier": "v1 frontier void", "v1-void/hole": "v1 hole void", "v2-blend/blend": "v2 blend void",
         "v3-search/search": "v3 novelty search", "control": "brainstorm (no map)"}


def write_markdown(p):
    lines = ["# Ranked game ideas", "",
             "Every idea the pipeline wrote, ranked by isolation from all 195,015 Steam games: σ = standard "
             "deviations more isolated than a typical game, averaged over bge-small and MiniLM (MiniLM was never "
             "shown to the writing agents). Percentiles = share of Steam games that are less isolated. "
             "Prior-art verdicts come from adversarial web searches; *thin* means the search budget ran out after 1-2 searches.",
             "", "Full interactive report: `outputs/report.html`.", ""]

    def block(r, head):
        s, v = r["score"], p["verify"].get(r["key"])
        mk = "control" if r["method"] == "control" else f"{r['method']}/{r['family']}"
        out = [f"## {head} {r['title']}", "",
               f"**{s['novelty_z']:+.2f}σ** · bge {s['novelty_bge_percentile']:.2f}% · MiniLM {s['novelty_minilm_percentile']:.2f}% · "
               f"{LABEL.get(mk, mk)} · closest Steam game: {s['nearest'][0]['name']} ({s['nearest'][0]['sim']:.2f})", ""]
        if v:
            thin = " (thin check)" if v["searches_run"] <= 2 else ""
            out += [f"Prior art: **{VERDICT[v['prior_art']]}**{thin}. {v['explanation']}"
                    + (f" [{v['closest_match']}]({v['closest_url']})" if v.get("closest_url") else ""),
                    f"Coherence {v['coherence']}/5: {v['coherence_note']}", ""]
        out += [f"*Tags:* {', '.join(r['tags'])}", "", f"> {r['short_description']}", "", r["description"], "",
                f"*Pitch:* {r['pitch']}", ""]
        return out

    for r in p["ideas"]:
        lines += block(r, f"{r['rank']}.")
    lines += ["---", "", "# Baseline: the same AI with no map", ""]
    for r in p["controls"]:
        lines += block(r, f"(would rank ~{r['would_rank']})")
    (OUT / "IDEAS.md").write_text("\n".join(lines))
    print("wrote outputs/IDEAS.md")


if __name__ == "__main__":
    main()
