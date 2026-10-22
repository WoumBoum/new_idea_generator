export const meta = {
  name: 'decode-voids-v2',
  description: 'v2: decode full-space blend voids (emptiest mixes of 2-3 established Steam games) into store pages',
  phases: [{ title: 'Decode', detail: 'each agent decodes a batch of voids via the local scoring server' }],
}

const SCRATCH = (args && args.scratch) || '/tmp/new_idea_generator'   // where agents write draft files

const ROOT = '/home/user/new_idea_generator'
const VOIDS = args.voids || args.batches.flat()   // [{void_id, family}]
const N_AGENTS = args.agents || 8

const IDEA_PROPS = {
  void_id: { type: 'string' },
  title: { type: 'string' },
  tags: { type: 'array', items: { type: 'string' } },
  player_modes: { type: 'array', items: { type: 'string' } },
  short_description: { type: 'string' },
  description: { type: 'string' },
  pitch: { type: 'string', description: 'one sentence: what is new about this game' },
  interpretation: { type: 'string', description: '1-2 sentences: how you read the void (decoded tags, parents, neighbours)' },
  drafts_scored: { type: 'integer' },
  first_target_sim: { type: 'number' },
  final_target_sim: { type: 'number' },
  final_novelty_bge_percentile: { type: 'number' },
}
const SCHEMA = {
  type: 'object',
  properties: {
    ideas: { type: 'array', items: { type: 'object', properties: IDEA_PROPS, required: Object.keys(IDEA_PROPS) } },
  },
  required: ['ideas'],
}

function prompt(batch) {
  return `You are decoding points of a vector space back into video game ideas.

Background: all 195,015 games on Steam were scraped. Each game's concept (its tags + store description) was embedded with a sentence-embedding model, and we mathematically located "voids": points in that space that are far away from every existing game. Your job: for each void assigned to you, write the Steam store page of the game that would live exactly at that point. A local scoring server embeds your draft the same way the real games were embedded and tells you how close to the void you landed.

Your voids: ${batch.map(v => `${v.void_id} (${v.family})`).join(', ')}
(blend = the emptiest weighted mix of 2-3 established Steam games, its parent_games; the game that lives there genuinely fuses what those parents are about into ONE concept, it is not one parent with the other bolted on as a mode)

Scoring server (use curl from Bash; it is already running):
- curl -s http://127.0.0.1:8767/void/V07
    decoded_tags: P(tag) read out of the void's coordinates by a decoder trained on every Steam game. This IS the void's metadata, and the strongest signal of what lives there.
    decoded_player_modes: same for player modes.
    parent_games: the real games whose weighted mix IS the void's position (its ingredients), with tags and descriptions.
    neighbors: the 15 nearest real games. The void is the place FARTHEST from them, so your game must not be any of them.
- curl -s http://127.0.0.1:8767/tags   (the allowed tag vocabulary; it is also in ${ROOT}/outputs/raw/tag_vocab.txt)
- Score a draft: write a JSON file, then
    curl -s -X POST http://127.0.0.1:8767/score -H 'Content-Type: application/json' --data @draft.json
  with draft.json = {"void_id": "V07", "tags": [...], "short_description": "...", "description": "..."}
  Returns target_sim (cosine between your draft and the void in the full embedding space; THIS is what you maximise), novelty_bge / novelty_minilm with *_percentile (share of real Steam games that are less isolated than your draft), nearest (closest real games), decoded_tags (what the decoder reads from your draft), warnings.
  Put draft files under ${SCRATCH}/drafts/ (create it), not in the repository.

Procedure, for each void:
1. Read the void. Ideas that merely feel original often already exist (a test draft about a haunted 1990s solitaire game landed right next to an existing Steam game called Forbidden Solitaire), so always read the nearest list the server returns. Form a hypothesis: ONE coherent game that the decoded tags and parent games point to, and that is unlike every neighbour.
2. Write draft 1 and score it.
3. Revise and re-score at least 7 more times (at least 8 scored drafts per void; keep going while target_sim is still climbing, up to ~14). In the first few drafts try genuinely different interpretations of the void (different settings, core loops, tag sets), not word tweaks; then refine the best one. Use the feedback: compare your draft's decoded_tags with the void's; if a nearest game is very similar, change what makes you resemble it. Tags are embedded first and weigh heavily, so test tag choice and order deliberately.
4. Final = the coherent draft with the highest target_sim. Report its numbers exactly as the server returned them.

Writing rules (the result must be a real, pitchable game, not an embedding hack):
- title: an original name, not an existing game.
- tags: 8-14 tags from the vocabulary, most important first, every one true of the game you describe.
- player_modes: from the names in decoded_player_modes (e.g. Single-player, Online Co-op).
- short_description: 1-2 sentences, at most 300 characters, like the blurb under a Steam capsule.
- description: 120-200 words of plain store-page prose: setting, what the player does moment to moment (core loop), the goal, and what makes it different.
- Keep it suitable for a general audience: no sexual content, even if a neighbour or parent game has it.
- Forbidden: keyword lists stuffed into prose, invented words, mentions of voids/vectors/embeddings, existing franchise or game names, contradictory tags.
- Coherence beats score: never keep a change that makes the game self-contradictory or unplayable just because target_sim went up.

Return one idea per assigned void (${batch.length} total), with drafts_scored, the target_sim of your first draft and of your final draft, and the final draft's novelty_bge_percentile.`
}

phase('Decode')
let batches
if (args.batches) {
  batches = args.batches
} else {
  batches = Array.from({ length: N_AGENTS }, () => [])
  VOIDS.forEach((v, k) => batches[k % N_AGENTS].push(v))
}
const results = await parallel(batches.filter(b => b.length).map((b, k) => () =>
  agent(prompt(b), { label: `decode:${b.map(v => v.void_id).join(',')}`, phase: 'Decode', schema: SCHEMA })))
const ideas = results.filter(Boolean).flatMap(r => r.ideas)
const missing = VOIDS.map(v => v.void_id).filter(id => !ideas.some(i => i.void_id === id))
if (missing.length) log(`missing decodes for: ${missing.join(', ')}`)
return { ideas, missing }
