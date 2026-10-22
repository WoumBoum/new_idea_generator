export const meta = {
  name: 'verify-prior-art',
  description: 'Adversarial prior-art search: try to refute each generated game idea\'s novelty with web search, and rate coherence',
  phases: [{ title: 'Refute', detail: 'each agent hunts for existing games matching a batch of ideas' }],
}

const FILE = args.file      // JSON list of {rank (an id), title, tags, short_description, description, pitch}
const IDS = args.ids        // the ids this run checks
const N_AGENTS = args.agents || 8

const VERDICT = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          rank: { type: 'integer' },
          title: { type: 'string' },
          prior_art: { type: 'string', enum: ['exists', 'close', 'none_found'],
            description: 'exists = a released or announced game with substantially the same core concept; close = shares the central twist or core loop but differs in a major way; none_found = nothing comparable found after a real search' },
          closest_match: { type: 'string', description: 'name + platform of the closest existing game/product, or "none"' },
          closest_url: { type: 'string', description: 'URL of the evidence, or ""' },
          explanation: { type: 'string', description: '1-3 sentences: what overlaps and what does not' },
          searches_run: { type: 'integer' },
          coherence: { type: 'integer', minimum: 1, maximum: 5,
            description: '5 = clear, buildable, fun-sounding core loop; 3 = workable but muddled; 1 = self-contradictory or not a game' },
          coherence_note: { type: 'string' },
        },
        required: ['rank', 'title', 'prior_art', 'closest_match', 'closest_url', 'explanation', 'searches_run', 'coherence', 'coherence_note'],
      },
    },
  },
  required: ['verdicts'],
}

function prompt(batch) {
  return `You are an adversarial reviewer. A pipeline claims the game ideas below are brand new: it embedded all 195,015 Steam games and generated ideas in the empty regions of that space. Your job is to REFUTE that claim for each idea by finding existing games (on Steam, itch.io, consoles, mobile, browser, game jams, or announced/in development) or tabletop games with substantially the same core concept.

For each idea:
1. Identify its core concept: the central twist and the core loop (ignore the title and flavour text).
2. Run at least 4 different web searches (WebSearch) phrased the way a player would describe it ("game where you ...", genre + twist, itch.io + twist, the mechanic name). Open promising results (WebFetch) when a snippet is not enough to judge.
3. Verdict: exists / close / none_found (definitions in the schema). Be strict: shared genre or shared setting alone is NOT "close"; the central twist or core loop must match. But do not go easy either: if the core twist exists anywhere, say so.
4. Rate coherence 1-5 as a game designer would, with a one-line note.

Ideas: read the JSON file ${FILE} with the Read tool and take ONLY the entries whose "rank" field is one of: ${batch.join(', ')}. (The "rank" field is just an id.)

Return one verdict per idea (${batch.length}), copying the id into rank and the title exactly.`
}

phase('Refute')
const batches = Array.from({ length: N_AGENTS }, () => [])
IDS.forEach((id, k) => batches[k % N_AGENTS].push(id))
const res = await parallel(batches.filter(b => b.length).map(b => () =>
  agent(prompt(b), { label: `refute:${b.join(',')}`, phase: 'Refute', schema: VERDICT })))
const verdicts = res.filter(Boolean).flatMap(r => r.verdicts)
const missing = IDS.filter(id => !verdicts.some(v => v.rank === id))
if (missing.length) log(`no verdict for ids: ${missing.join(', ')}`)
return { verdicts, missing }
