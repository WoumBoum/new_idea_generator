# Explainer video script

Narration for `outputs/video/uncharted_steam_explainer.mp4` (16:9) and `uncharted_steam_explainer_vertical.mp4` (9:16, for phones). Both run 2:17, inside X's 2:20 limit. Timings are where each line starts.
The voice is Kokoro (open-weights text-to-speech, voice `af_heart`). Acronyms are written AI and PC with no periods, so they are spoken in one breath ("ay-EYE", "pee-SEE") instead of as two separate letters.
To re-record in your own voice, read these lines at the same pace; `video/make_audio.py` rebuilds the timings from `video/script.json`, and `video/render.mjs` (add `--portrait` for the vertical cut) re-renders the picture.

## hook
- `0:00.4` Someone said AI can't come up with a brand new idea.
- `0:03.4` Someone replied: sure it can. Put every Steam game on a map, find the empty spots, and turn them back into ideas.
- `0:10.1` So I tested it. It worked, just not the way they said.

## download
- `0:13.3` First, I downloaded every game's page from Steam, the biggest PC game store. All one hundred and ninety-five thousand.

## embedding
- `0:21.0` Then an AI turned each game's description into a point on a map, so similar games land close together.
- `0:27.0` That's called an embedding.
- `0:28.4` Two zombie shooters? Neighbors. A farming game? Far away.

## map
- `0:32.0` Here's the map. Every dot is a real Steam game, and genres form neighborhoods.

## score
- `0:36.8` To score an idea, I put it on the map and look at its ten closest games.
- `0:40.8` The farther away they are, the more unusual the idea.

## sanity
- `0:43.9` Can new wording fake a high score?
- `0:45.6` No. When the AI rewrote real games in totally new words, most landed near the originals.

## voids
- `0:51.4` Then I found empty spots on the map, far from every game.
- `0:54.7` For each one, an AI wrote a game idea and kept rewriting it to land there.

## baseline
- `0:59.5` For comparison, I also just asked the same AI: give me game ideas nobody has made.

## results
- `1:05.0` Surprise: the empty spots lost.
- `1:07.1` For a typical idea from just asking, about sixteen thousand Steam games were more unusual. For the empty spots, fifty-three thousand. Fewer is better.
- `1:16.3` Why? I'd searched a simplified map that mostly knows genre and style.
- `1:20.3` On the full map, empty spots only tied with just asking.

## compass
- `1:23.8` What won? Using the map as a compass.
- `1:26.0` The AI writes an idea, the map says which games it's too close to, and it moves away.
- `1:30.8` Now only about eighty Steam games were more unusual.
- `1:33.6` And a second map it never saw agreed.

## ideas
- `1:36.0` Here's what came out.
- `1:37.1` Captain a village's church bell ringers in eighteen twenty.
- `1:40.0` Be the hidden prompter, whispering lines to actors who forgot them.
- `1:43.5` Perform a silent film's sound effects live.
- `1:46.1` Write the first great English dictionary before the money runs out.

## check
- `1:49.9` But unusual isn't never made, so another AI searched the web for all sixteen ideas.
- `1:55.1` Ten turned up nothing similar, though most checks were quick.
- `1:58.0` Five had something close.
- `1:59.5` And one already existed: a Viking rowing rhythm game called Ragnarock.

## outro
- `2:04.0` So, can AI come up with a new idea?
- `2:06.2` With the map as its compass, its typical idea was more unusual than ninety-nine point nine percent of Steam.
- `2:12.4` The map didn't invent them. It just kept saying: that's been done.
