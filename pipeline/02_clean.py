"""Turn raw Steam store pages into one clean table of games.

Each game gets:
  - plain-text short + full description (BBCode, images, links stripped)
  - tag names in Steam's vote-weight order, player-mode + feature category names
  - release / review / price metadata
  - `doc`: the text that gets embedded. It describes the game *concept* only:
        "<tags>. <short description> <first ~120 words of the long description>"
    Titles, developer names, prices and marketing boilerplate are left out so that
    distance in embedding space means "a different idea", not "a different brand".
Output: data/games.parquet
"""
import gzip
import html
import json
import re
from glob import glob
from pathlib import Path

import langid
import pandas as pd

from common import compose_doc, concept_tags_of

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

TAGS = {t["tagid"]: t["name"] for t in json.loads((RAW / "tags.json").read_text())}
CATS = {c["categoryid"]: c["display_name"] for c in json.loads((RAW / "categories.json").read_text())}

BOILERPLATE = re.compile(
    r"(wishlist|add to your wishlist|join (our|the) discord|follow us|twitter|facebook|instagram|youtube|"
    r"tiktok|press kit|patreon|kickstarter|newsletter|steam deck verified|copyright|all rights reserved|"
    r"©|minimum requirements|system requirements)",
    re.I,
)


def bbcode_to_text(s: str) -> str:
    if not s:
        return ""
    s = html.unescape(s)
    s = re.sub(r"\[img[^\]]*\].*?\[/img\]", " ", s, flags=re.I | re.S)
    s = re.sub(r"\[(video|previewyoutube|dynamiclink)[^\]]*\].*?\[/\1\]", " ", s, flags=re.I | re.S)
    s = re.sub(r"\[(img|video|previewyoutube|dynamiclink)[^\]]*\]", " ", s, flags=re.I)
    s = re.sub(r"\[url=[^\]]*\](.*?)\[/url\]", r"\1", s, flags=re.I | re.S)
    s = re.sub(r"\[\*\]", "\n- ", s)
    s = re.sub(r"\[/?(p|h\d|list|olist|b|i|u|strike|spoiler|noparse|hr|table|tr|td|th|quote|code|url|\*)[^\]]*\]",
               "\n", s, flags=re.I)
    s = re.sub(r"\[[^\]]{0,40}\]", " ", s)  # any leftover short tag
    s = re.sub(r"<[^>]+>", " ", s)  # stray html
    s = re.sub(r"https?://\S+|www\.\S+", " ", s)
    s = s.replace("\r", "\n")
    lines = [re.sub(r"[ \t ]+", " ", ln).strip(" -•*") for ln in s.split("\n")]
    lines = [ln for ln in lines if ln and not BOILERPLATE.search(ln)]
    return "\n".join(lines).strip()


def lang_of(text: str) -> str:
    t = text[:600]
    if not t.strip():
        return "unk"
    return langid.classify(t)[0]


def row(it: dict) -> dict:
    bi = it.get("basic_info") or {}
    short = bbcode_to_text(bi.get("short_description", "")).replace("\n", " ")
    full = bbcode_to_text(it.get("full_description_bbcode", ""))
    tag_list = [TAGS.get(t["tagid"], str(t["tagid"])) for t in sorted(it.get("tags", []), key=lambda t: -t["weight"])]
    if not tag_list:
        tag_list = [TAGS.get(t, str(t)) for t in it.get("tagids", [])]
    concept_tags = concept_tags_of(tag_list)
    cats = it.get("categories") or {}
    rev = (it.get("reviews") or {}).get("summary_filtered") or {}
    bpo = it.get("best_purchase_option") or {}

    doc = compose_doc(concept_tags, short, full)

    return {
        "appid": it["appid"],
        "name": it.get("name", ""),
        "short_description": short,
        "description": full[:4000],
        "tags": tag_list,
        "concept_tags": concept_tags,
        "player_modes": [CATS.get(c, str(c)) for c in cats.get("supported_player_categoryids", [])],
        "features": [CATS.get(c, str(c)) for c in cats.get("feature_categoryids", [])],
        "content_descriptors": it.get("content_descriptorids", []),
        "release_unix": (it.get("release") or {}).get("steam_release_date"),
        "coming_soon": bool(it.get("is_coming_soon")),
        "early_access": bool(it.get("is_early_access")),
        "is_free": bool(it.get("is_free")),
        "price_cents": int(bpo.get("final_price_in_cents") or 0) if not it.get("is_free") else 0,
        "review_count": rev.get("review_count", 0),
        "percent_positive": rev.get("percent_positive"),
        "developers": [d.get("name") for d in bi.get("developers", [])],
        "publishers": [p.get("name") for p in bi.get("publishers", [])],
        "doc": doc,
    }


def main():
    rows = {}
    for f in sorted(glob(str(RAW / "pages" / "s2_*.json.gz"))):
        for it in json.load(gzip.open(f))["store_items"]:
            if it.get("success") == 1 and it.get("appid"):
                rows[it["appid"]] = row(it)
    df = pd.DataFrame(list(rows.values())).sort_values("appid").reset_index(drop=True)
    df["lang"] = [lang_of(f"{a} {b}") for a, b in zip(df.short_description, df.description)]
    df["doc_words"] = df.doc.str.split().str.len()
    # "Embeddable" = enough concept text to place the game in idea-space.
    df["embeddable"] = (df.short_description.str.len() + df.description.str.len() >= 40) | (df.concept_tags.str.len() >= 3)
    out = ROOT / "data" / "games.parquet"
    df.to_parquet(out, index=False)
    print(f"{len(df)} games -> {out}")
    print("embeddable:", int(df.embeddable.sum()))
    print("coming soon:", int(df.coming_soon.sum()), " released:", int((~df.coming_soon).sum()))
    print("top languages:", df.lang.value_counts().head(12).to_dict())
    print("doc words: median", df.doc_words.median(), "p90", df.doc_words.quantile(0.9))


if __name__ == "__main__":
    main()
