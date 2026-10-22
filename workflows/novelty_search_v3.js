export const meta = {
  name: 'novelty-search-v3',
  description: 'v3: LLM writes game ideas while the embedding space scores distance to all 195k Steam games each draft (novelty search, MiniLM held out)',
  phases: [{ title: 'Search', detail: 'two agents, 8 ideas each, iterate drafts against the novelty score' }],
}

const SCRATCH = (args && args.scratch) || '/tmp/new_idea_generator'   // where agents write draft files

const ROOT = '/home/user/new_idea_generator'

const IDEA_PROPS = {
  title: { type: 'string' },
  tags: { type: 'array', items: { type: 'string' } },
  player_modes: { type: 'array', items: { type: 'string' } },
  short_description: { type: 'string' },
  description: { type: 'string' },
  pitch: { type: 'string', description: 'one sentence: what is new about this game' },
  drafts_scored: { type: 'integer' },
  first_novelty_bge_percentile: { type: 'number' },
  final_novelty_bge_percentile: { type: 'number' },
}
const SCHEMA = {
  type: 'object',
  properties: { ideas: { type: 'array', minItems: 8, maxItems: 8,
    items: { type: 'object', properties: IDEA_PROPS, required: Object.keys(IDEA_PROPS) } } },
  required: ['ideas'],
}

const prompt = (k) => `You are running a novelty search for video game ideas.

Background: all 195,015 games on Steam were scraped and each game's concept (tags + store description) was embedded with a sentence-embedding model. A local scoring server embeds any draft store page the same way and tells you how far it sits from every existing game. Your job: produce 8 game ideas that are as far from all existing Steam games as you can get them, while each one remains a coherent, buildable, fun game.

Scoring server (curl from Bash; already running):
- Score a draft: write a JSON file, then
    curl -s -X POST http://127.0.0.1:8767/score -H 'Content-Type: application/json' --data @draft.json
  with draft.json = {"tags": [...], "short_description": "...", "description": "..."}
  Returns novelty_bge (1 - mean cosine similarity to the 10 nearest Steam games) and novelty_bge_percentile (share of real Steam games that are LESS isolated than your draft; this is the score you maximise), nearest (the closest real games: what you collide with), decoded_tags, warnings.
- Put draft files under ${SCRATCH}/novelty_${k}/ (create it), not in the repository.
- Tag vocabulary: ${ROOT}/outputs/raw/tag_vocab.txt (or curl -s http://127.0.0.1:8767/tags).

Procedure, for each of your 8 ideas:
1. Start from a fresh seed concept, different from your other ideas. Score it.
2. Revise and re-score at least 7 more times (at least 8 scored drafts per idea). Read the nearest list: it tells you which existing games your idea resembles. Move the idea away from them by changing the premise, the core loop or the setting, not by changing words. When an idea stalls, try a substantially different premise.
3. Final = the coherent draft with the highest novelty_bge_percentile. Report its numbers exactly as returned.

Writing rules (the score must come from the IDEA, not from the wording):
- title: an original name, not an existing game.
- tags: 8-14 tags from the vocabulary, most important first, every one true of the game.
- player_modes: e.g. Single-player, Online Co-op, PvP.
- short_description: 1-2 sentences, at most 300 characters, like the blurb under a Steam capsule.
- description: 120-200 words of plain store-page prose a Steam player would understand: setting, what the player does moment to moment (core loop), the goal, what makes it different.
- Forbidden: obscure jargon or rare words used to push the score, keyword lists, invented words, mentions of embeddings/novelty/scores, existing franchise or game names, sexual content.
- Coherence beats score: never keep a change that makes the game less playable or less clear just because the score went up.

Return all 8 ideas with drafts_scored and the novelty_bge_percentile of the first and the final draft.`

phase('Search')
const res = await parallel([1, 2].map(k => () => agent(prompt(k), { label: `novelty-search:${k}`, phase: 'Search', schema: SCHEMA })))
return { ideas: res.filter(Boolean).flatMap(r => r.ideas) }
