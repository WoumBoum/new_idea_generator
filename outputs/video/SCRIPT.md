# Explainer video script

Narration for `outputs/video/uncharted_steam_explainer.mp4` (2:19, fits X's 2:20 limit). Timings are where each line starts in the video.
The voice is Kokoro (open-weights text-to-speech, voice `af_heart`). To re-record in your own voice, read these lines at the same pace;
`video/make_audio.py` rebuilds the timings from `video/script.json`, and `video/render.mjs` re-renders the picture.

## hook
- `0:00.4` Someone said A.I. can't come up with a brand new idea.
- `0:03.6` Someone replied: sure it can. Put every Steam game on a map, find the empty spots, and turn them back into ideas.
- `0:10.3` So I tested it. It worked, just not the way they said.

## download
- `0:13.5` First, I downloaded every game's page from Steam, the biggest P.C. game store. All one hundred and ninety-five thousand.

## embedding
- `0:21.3` Then an A.I. turned each game's description into a point on a map, so similar games land close together.
- `0:27.7` That's called an embedding.
- `0:29.1` Two zombie shooters? Neighbors. A farming game? Far away.

## map
- `0:32.7` Here's the map. Every dot is a real Steam game, and genres form neighborhoods.

## score
- `0:37.5` To score an idea, I put it on the map and look at its ten closest games.
- `0:41.4` The farther away they are, the more unusual the idea.

## sanity
- `0:44.6` Can new wording fake a high score?
- `0:46.3` No. When the A.I. rewrote real games in totally new words, most landed near the originals.

## voids
- `0:52.4` Then I found empty spots on the map, far from every game.
- `0:55.6` For each one, an A.I. wrote a game idea and kept rewriting it to land there.

## baseline
- `1:00.5` For comparison, I also just asked the same A.I.: give me game ideas nobody has made.

## results
- `1:06.2` Surprise: the empty spots lost.
- `1:08.3` For a typical idea from just asking, about sixteen thousand Steam games were more unusual. For the empty spots, fifty-three thousand. Fewer is better.
- `1:17.5` Why? I'd searched a simplified map that mostly knows genre and style.
- `1:21.5` On the full map, empty spots only tied with just asking.

## compass
- `1:25.0` What won? Using the map as a compass.
- `1:27.2` The A.I. writes an idea, the map says which games it's too close to, and it moves away.
- `1:32.2` Now only about eighty Steam games were more unusual.
- `1:35.0` And a second map it never saw agreed.

## ideas
- `1:37.4` Here's what came out.
- `1:38.5` Captain a village's church bell ringers in eighteen twenty.
- `1:41.4` Be the hidden prompter, whispering lines to actors who forgot them.
- `1:44.9` Perform a silent film's sound effects live.
- `1:47.5` Write the first great English dictionary before the money runs out.

## check
- `1:51.3` But unusual isn't never made, so another A.I. searched the web for all sixteen ideas.
- `1:56.9` Ten turned up nothing similar, though most checks were quick.
- `1:59.7` Five had something close.
- `2:01.2` And one already existed: a Viking rowing rhythm game called Ragnarock.

## outro
- `2:05.8` So, can A.I. come up with a new idea?
- `2:08.1` With the map as its compass, its typical idea was more unusual than ninety-nine point nine percent of Steam.
- `2:14.4` The map didn't invent them. It just kept saying: that's been done.
