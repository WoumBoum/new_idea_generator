"""Scrape every game on the Steam store.

Uses Steam's public (keyless) store APIs:
  - IStoreQueryService/Query      -> pages through every item of type "game" (1000 per call),
                                     with descriptions, tags, release date and review summary inline
  - IStoreService/GetTagList      -> tag id -> tag name
  - IStoreBrowseService/GetStoreCategories -> category id -> name (player modes, features)

Output: data/raw/pages/page_XXXXXX.json.gz (one per request), data/raw/tags.json, data/raw/categories.json
Re-running skips pages already on disk, so an interrupted scrape resumes.
"""
import gzip
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PAGES = RAW / "pages"
PAGE_SIZE = 1000
API = "https://api.steampowered.com"
CTX = {"language": "english", "country_code": "US"}
DATA_REQUEST = {
    "include_basic_info": True,
    "include_tag_count": 20,
    "include_release": True,
    "include_full_description": True,
    "include_reviews": True,
    "include_ratings": True,
}

session = requests.Session()
session.headers["User-Agent"] = "new-idea-generator research scraper (one pass, polite)"


def get(url, params, tries=6):
    for attempt in range(tries):
        try:
            r = session.get(url, params=params, timeout=90)
            if r.status_code == 200:
                return r.json()
            print(f"  HTTP {r.status_code} on {url} (attempt {attempt + 1})", flush=True)
        except Exception as e:  # network hiccup
            print(f"  error {e!r} (attempt {attempt + 1})", flush=True)
        time.sleep(2 ** (attempt + 1))
    raise RuntimeError(f"giving up on {url} {params}")


def query_page(start, sort=None):
    q = {"start": start, "count": PAGE_SIZE, "filters": {"type_filters": {"include_games": True}}}
    if sort is not None:
        q["sort"] = sort
    body = {"query": q, "context": CTX, "data_request": DATA_REQUEST}
    return get(f"{API}/IStoreQueryService/Query/v1/", {"input_json": json.dumps(body)})["response"]


# sort=2 orders by appid ascending, which keeps deep pagination stable.
# (The default relevance sort drifts between calls and repeats ~35% of games.)
SORT_BY_APPID = 2


def fetch_and_save(start, pass_name):
    out = PAGES / f"{pass_name}_{start:07d}.json.gz"
    if out.exists():
        return start, None
    resp = query_page(start, sort=SORT_BY_APPID)
    items = resp.get("store_items", [])
    with gzip.open(out, "wt", encoding="utf-8") as f:
        json.dump({"start": start, "metadata": resp.get("metadata"), "store_items": items}, f)
    return start, len(items)


def main():
    PAGES.mkdir(parents=True, exist_ok=True)
    pass_name = sys.argv[1] if len(sys.argv) > 1 else "s2"

    tags = get(f"{API}/IStoreService/GetTagList/v1/", {"language": "english"})["response"]["tags"]
    (RAW / "tags.json").write_text(json.dumps(tags))
    cats = get(f"{API}/IStoreBrowseService/GetStoreCategories/v1/",
               {"input_json": json.dumps({"language": "english"})})["response"]["categories"]
    (RAW / "categories.json").write_text(json.dumps(cats))
    print(f"{len(tags)} tags, {len(cats)} categories", flush=True)

    total = query_page(0, sort=SORT_BY_APPID)["metadata"]["total_matching_records"]
    starts = list(range(0, total + PAGE_SIZE, PAGE_SIZE))
    print(f"total_matching_records={total}; {len(starts)} pages", flush=True)
    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=3) as ex:
        futs = [ex.submit(fetch_and_save, s, pass_name) for s in starts]
        for fut in as_completed(futs):
            s, n = fut.result()
            done += 1
            if done % 10 == 0 or done == len(starts):
                print(f"[{done}/{len(starts)}] start={s} items={n} elapsed={time.time() - t0:.0f}s", flush=True)
    (RAW / f"{pass_name}_meta.json").write_text(json.dumps({"total_matching_records": total, "pages": len(starts),
                                                            "scraped_at_unix": int(time.time())}))
    print("done", flush=True)


if __name__ == "__main__":
    main()
