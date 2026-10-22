# new_idea_generator

> "One thing AI can't do is create a brand new idea."
>
> "Of course it can. Take all 100,000+ games on Steam, scrape their descriptions and metadata, semantically plot
> them in vector space using embeddings, mathematically choose a location in vector space far away from
> neighbors, convert that back to a description and metadata, boom, brand new ideas ranked by how unlike any
> other ideas they are."

This repo does all of that, then tests whether it actually works better than just asking an AI for original ideas.

**Short answer:** yes, with one change to the recipe. Used as a live judge of distance while the AI writes, the
embedding space produced 16 game concepts more isolated than 99.9% of Steam, and the web search found no prior
game for most of them. The literal "pick an empty point, then decode it" recipe only worked once it searched the
full embedding space, and even then it merely tied a plain AI brainstorm.

Everything is in [`outputs/IDEAS.md`](outputs/IDEAS.md) (all 76 ideas, ranked) and `outputs/report.html`
(interactive map and charts, self-contained).

## What was done

| Step | What | Code |
|---|---|---|
| Scrape | Every game on the Steam store, **195,015** (61,995 announced but unreleased), via Steam's keyless `IStoreQueryService` API paged by app ID: descriptions, user tags, player modes, release and review data. | `pipeline/01_scrape.py` |
| Concept docs | Per game: top 12 descriptive tags + short description + first 120 words of the store page. No titles, developers or prices. | `pipeline/02_clean.py`, `pipeline/common.py` |
| Embed | Two independent models: `BAAI/bge-small-en-v1.5` (primary) and `all-MiniLM-L6-v2` (held out: never shown to any agent). CPU, bf16. | `pipeline/03_embed.py` |
| Isolation | novelty = 1 − mean cosine similarity to the 10 nearest games, exact kNN over all games; expressed as σ above a typical game. | `pipeline/04_space.py` |
| Vector → metadata | Linear decoder from the space to 363 tags + 13 player modes (precision@5 = 0.79 on 19,495 held-out games vs 0.47 for always guessing the most common tags). | `pipeline/04_space.py` |
| Find empty points | **v1**: gradient ascent on emptiness in the top 64 principal components, constrained to the populated region; 24 "frontier" + 24 "hole" voids. **v2**: the emptiest weighted mix of 2–3 established games, in the full space; 24 found, 12 decoded. | `pipeline/05_voids.py`, `pipeline/05b_voids_full.py` |
| Vector → text | An AI agent writes a Steam store page for each void; a local server embeds every draft exactly like a real game and reports how close it landed and what it collided with; the agent revises. ~7,500 drafts embedded in total. | `pipeline/06_server.py`, `workflows/decode_voids_*.js` |
| **v3** novelty search | No target point: the agent writes ideas and the server scores each draft's distance to all 195k games (bge only). | `workflows/novelty_search_v3.js` |
| Controls | (a) the same AI asked for 16 original ideas with no data; (b) 24 real Steam games rewritten from scratch (same idea, new words). | `workflows/controls.js` |
| Rank | Every final text re-embedded under both models; ranked by the mean σ. | `pipeline/07_rank.py` |
| Prior art | Adversarial agents web-searched every idea above +1σ (49 ideas) for existing games on any platform. | `workflows/verify_prior_art.js` |
| Report | UMAP map of all games + ideas, comparison chart, ranked cards. | `pipeline/08_map.py`, `pipeline/09_report.py` |

## Results

Isolation in σ above a typical Steam game (mean of bge and MiniLM). For reference, Steam's own 99th percentile is
+2.0σ and its single most isolated entry is +4.58σ.

| Group | n | median σ | bge pct | MiniLM pct (held out) | top 5% on both | prior art: none found / close / exists |
|---|---|---|---|---|---|---|
| Real games rewritten (calibration) | 24 | −0.50 | 18 | 31 | 0% | – |
| AI brainstorm, no map (control) | 16 | +1.36 | 93.3 | 93.2 | 19% | 6 / 8 / 2 |
| v1 frontier voids (64-d) | 24 | +0.64 | 76 | 77 | 4% | 1 / 7 / 0 (top 8 of v1 checked) |
| v1 hole voids (64-d) | 24 | +0.57 | 71 | 74 | 0% | ″ |
| v2 blend voids (full space) | 12 | +1.53 | 96.4 | 90.8 | 33% | 0 / 6 / 3 (9 checked) |
| **v3 novelty search** | 16 | **+3.64** | **99.99** | **99.92** | **100%** | 10 / 5 / 1 |

* **The metric measures ideas, not wording.** A real game rewritten from scratch scores −0.5σ and its original is
  still among the 8 nearest games 71% of the time. The held-out model agrees with the primary one (r = 0.89).
* **v1 underperformed** because its search space (the top principal components) mostly encodes broad traits like
  genre, art style and mood. Its voids were unusual mixes of those traits; once written as concrete games they
  landed in crowded territory of the full space (frontier ideas: 97th percentile in the space they were
  searched in, 76th in the full space used for ranking).
* **v2 fixed the mismatch** by searching where it ranks, and tied the brainstorm (p = 0.24). Blends of existing
  games kept resembling existing games: every checked v2 idea had a close or exact match.
* **v3 won clearly** (p < 10⁻⁶ vs the brainstorm). It found one rich vein, pre-industrial niche trades played
  straight (bell-ringing captain, theatre prompter, talking-drum relay, live foley artist, canal "legger"), and mined it.
* **Isolated ≠ unprecedented.** "Heave and Sing" (v3, +3.0σ) turned out to match *Ragnarock*; "Seating Plan: 1943"
  (v2) is a reskin of *Is This Seat Taken?*. The web-search budget ran out mid-check, so 11 of the 16 v3 verdicts
  rest on 1–2 searches and are provisional.

### Top 10

| # | Idea | σ | Prior art |
|---|---|---|---|
| 1 | **The Ringers of Saxby Green**: captain a village band of 1820 church bell ringers, calling the changes live | +4.64 | close (bell-ringing simulators exist) |
| 2 | **Dawn Caller**: route-plan and drum through 30 Ramadan nights to wake every household before dawn | +4.31 | close (*Suhoor Hero*), thin check |
| 3 | **Forty Thousand Words**: write the first English dictionary in 1747 before the money runs out | +4.19 | none found |
| 4 | **Saturday Night Noisemaker**: perform a silent film's sound effects live from behind the screen | +4.18 | none found, thin check |
| 5 | **The Prompter's Trapdoor**: hidden prompter whispering forgotten lines to a touring 1890 theatre company | +4.09 | none found, thin check |
| 6 | **Three Miles in the Dark**: two-player rhythm/stamina game "legging" a canal boat through a tunnel | +3.87 | none found, thin check |
| 7 | **The Drum That Speaks**: decode and relay tonal Yoruba talking-drum messages between towns | +3.82 | none found, thin check |
| 8 | **Bellfast Tower**: co-op change ringing, one physically swinging bell per player | +3.65 | close |
| 9 | **Seating Europe**: seat diplomats in a 1905 Vienna dining room so treaties happen and duels don't | +3.63 | close (*Is This Seat Taken?*) |
| 10 | **Landfall Captions**: live TV captioner typing through a hurricane broadcast | +3.13 | none found |

## Reproduce

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/cpu && pip install -r requirements.txt
python pipeline/01_scrape.py          # ~2 min, 197 requests
python pipeline/02_clean.py           # ~5 min
python pipeline/03_embed.py bge       # ~45 min on 4 CPU cores
python pipeline/03_embed.py minilm    # ~25 min
python pipeline/04_space.py bge && python pipeline/04_space.py minilm
python pipeline/05_voids.py && python pipeline/05b_voids_full.py
PORT=8765 SCORE_MODELS=bge python pipeline/06_server.py &   # what the writing agents talk to
PORT=8766 python pipeline/06_server.py &                    # both models, for ranking
# run workflows/*.js with Claude Code's Workflow tool (they write outputs/raw/*.json)
PORT=8766 python pipeline/07_rank.py
python pipeline/08_map.py && python pipeline/09_report.py
```

`data/` (raw scrape, embeddings, indexes) is git-ignored; `outputs/steam_games.parquet` holds every game's
concept tags, short description and isolation scores.

## Caveats

* Isolation is measured against Steam only; other platforms are covered by the web search, not the embedding.
* Embedding distance measures how differently an idea is *described*. That tracks how differently it plays,
  but it is not the same thing.
* One AI model wrote every text. The voids and scores steered it; the wording and coherence are the model's.
* Regions dominated by adult content were excluded from the void search. About 2% of games have only
  non-English descriptions, which an English embedding model places less reliably.
