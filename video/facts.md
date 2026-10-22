# Facts sheet for the explainer video (all numbers from outputs/stats.json, outputs/ideas.json, outputs/verify.json)

- Scraped every game on the Steam store: 195,015 (incl. 61,995 announced but unreleased).
- Concept text per game = tags + short description + first 120 words of the store page; embedded with two models
  (bge-small = main; MiniLM = second, never shown to the writing AI).
- Novelty = 1 - average similarity to the 10 nearest Steam games. Compared to all games.
- Calibration: 24 real games rewritten by the AI in new words. A typical rewrite: ~138,000 Steam games are more unusual
  (29th percentile). The original game was among the 8 nearest neighbours for 71% (17/24) of rewrites; nearest for 38%.
- "How many Steam games are MORE unusual than a typical (median) idea", averaged across both models:
    rewritten real games 137,820 | v1 empty spots (searched in a simplified 64-dimension version of the map) 52,927 |
    just asking the AI (16 ideas, no map) 15,969 | v2 empty spots in the full map (12 ideas) 11,772 |
    v3 compass / novelty search (16 ideas) 84.
- v1 = 48 empty spots (searched in top-64 principal components, which mostly capture genre/art style/mood).
- v2 vs just asking: statistically a tie (p = 0.24). v3 vs just asking: p < 0.000001.
- v3: all 16 ideas in the top 5% under both models; median percentile 99.96% (rounds to "more unusual than 99.9% of Steam").
- Top idea (bell ringers, 1820): only 1 Steam game more unusual under the main model, 8 under the second.
- ~7,500 drafts were written and measured in total.
- Prior-art web check on the 16 v3 ideas: 10 nothing similar found, 5 something close, 1 already exists (Ragnarock,
  a VR Viking rowing/drumming rhythm game). 11 of the 16 checks got only 1-2 web searches (search budget ran out).
- Example v3 ideas: The Ringers of Saxby Green (captain an 1820 village band of church bell ringers, calling changes);
  The Prompter's Trapdoor (hidden prompter whispering lines to an 1890 touring theatre company);
  Saturday Night Noisemaker (perform silent-film sound effects live behind the screen);
  Forty Thousand Words (write the first English dictionary in 1747 before the money runs out).
  Note: bell ringers got a "close" verdict (bell-ringing simulators exist); dictionary got "none found" (3 searches);
  prompter and noisemaker got "none found" on thin checks.
- The 2-D map in the video is a flattened projection (UMAP) of the real space.
