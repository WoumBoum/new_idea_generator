export const meta = {
  name: 'idea-controls',
  description: 'Control experiments: unguided LLM brainstorm of original game ideas + rewrite-calibration of 24 real Steam games',
  phases: [{ title: 'Controls', detail: 'brainstorm baseline and rewrite calibration in parallel' }],
}

const ROOT = '/home/user/new_idea_generator'

const FORMAT_RULES = `Store-page format for every game (this exact format is what gets embedded and compared against 195,015 Steam games):
- title: an original name.
- tags: 8 to 14 tags chosen ONLY from the Steam tag vocabulary in ${ROOT}/outputs/raw/tag_vocab.txt (one tag per line; copy spelling exactly), ordered from most to least important. Every tag must be true of the game.
- player_modes: from ["Single-player","Multi-player","Co-op","Online Co-op","PvP","Online PvP","Shared/Split Screen","Shared/Split Screen Co-op","Shared/Split Screen PvP","LAN Co-op","LAN PvP","MMO","Cross-Platform Multiplayer"] (pick what applies).
- short_description: 1-2 sentences, at most 300 characters, like the blurb under a Steam capsule.
- description: 120-200 words of plain store-page prose: setting, what the player does moment to moment (core loop), the goal, and what makes it different. No bullet-point keyword lists, no invented words, no existing franchise names.`

const IDEA_PROPS = {
  title: { type: 'string' },
  tags: { type: 'array', items: { type: 'string' } },
  player_modes: { type: 'array', items: { type: 'string' } },
  short_description: { type: 'string' },
  description: { type: 'string' },
  pitch: { type: 'string', description: 'one sentence: what is new about it' },
}

const CONTROL_SCHEMA = {
  type: 'object',
  properties: {
    ideas: {
      type: 'array', minItems: 16, maxItems: 16,
      items: { type: 'object', properties: IDEA_PROPS, required: Object.keys(IDEA_PROPS) },
    },
  },
  required: ['ideas'],
}

const CAL_PROPS = {
  original_appid: { type: 'integer' },
  title: { type: 'string' },
  tags: { type: 'array', items: { type: 'string' } },
  short_description: { type: 'string' },
  description: { type: 'string' },
}
const CAL_SCHEMA = {
  type: 'object',
  properties: {
    rewrites: {
      type: 'array', minItems: 24, maxItems: 24,
      items: { type: 'object', properties: CAL_PROPS, required: Object.keys(CAL_PROPS) },
    },
  },
  required: ['rewrites'],
}

phase('Controls')
const [control, calibration] = await parallel([
  () => agent(`You are the baseline arm of an experiment about whether AI can come up with brand-new video game ideas.

Task: invent 16 video game concepts that are as ORIGINAL as you can make them: ideas you believe are unlike any game that exists on Steam (195,000+ games). Aim for genuinely new concepts, not "X meets Y" mash-ups of famous games, but each one must still be a coherent, buildable, fun-sounding game with a clear core loop. Make the 16 ideas different from each other.

Rely only on your own creativity: do not search the web, and do not read or run anything in the repository except reading the tag vocabulary file named below.

${FORMAT_RULES}

Return all 16 ideas.`, { label: 'control:brainstorm', phase: 'Controls', schema: CONTROL_SCHEMA }),

  () => agent(`You are the calibration arm of an experiment that measures how "new" a game idea is by embedding its Steam store page and measuring the distance to all 195,015 Steam games. We need to know how far a page moves when the IDEA stays the same but the WORDING is completely new.

Use the Read tool (not shell commands; do not run Bash at all) to read ${ROOT}/outputs/raw/calibration_games.json and the tag vocabulary file. The JSON holds 24 real Steam games (original_appid, original_name, tags, short_description, description_excerpt).

For each game, act as a different copywriter writing that same game's store page from scratch:
- keep the game concept identical (same setting, same mechanics, same goal, same genre),
- rewrite every sentence in your own words (do not copy any phrase of more than 4 words from the original),
- invent a new title (do not reuse the original name or any franchise / character names),
- choose tags from the vocabulary file that are accurate for the game, in your own order of importance (you may reuse the original tags where they are accurate).

${FORMAT_RULES}

Return 24 rewrites, each with the original_appid copied exactly.`, { label: 'control:calibration', phase: 'Controls', schema: CAL_SCHEMA }),
])

return { control: control ? control.ideas : null, calibration: calibration ? calibration.rewrites : null }
