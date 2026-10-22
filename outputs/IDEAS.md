# Ranked game ideas

Every idea the pipeline wrote, ranked by isolation from all 195,015 Steam games: σ = standard deviations more isolated than a typical game, averaged over bge-small and MiniLM (MiniLM was never shown to the writing agents). Percentiles = share of Steam games that are less isolated. Prior-art verdicts come from adversarial web searches; *thin* means the search budget ran out after 1-2 searches.

Full interactive report: `outputs/report.html`.

## 1. The Ringers of Saxby Green

**+4.64σ** · bge 100.00% · MiniLM 100.00% · v3 novelty search · closest Steam game: Bell Ringer (0.65)

Prior art: **a close game exists**. Change ringing as a playable loop already exists. Show Me The Ropes is a rhythm game for learning and ringing methods, and the Abel/Mobel and Ringing Room simulators have you ring one bell in time while the computer or remote players ring the others. Abel also lets you call touches. None of them has a captain who calls swaps live, AI villagers who drift out of time, or the recruiting and village-politics management layer, so the core is taken but the framing is not. [Show Me The Ropes (itch.io, browser rhythm/educational bell-ringing game); also the Abel/Mabel/Mobel and Ringing Room change-ringing simulators](https://bladeofbilboa.itch.io/show-me-the-ropes)
Coherence 4/5: The loop is clear and buildable: keep time, call swaps, spot the ringer who drifts. But it mixes call-changes with non-repeating method peals, and calling a 5,000-change, three-hour peal by hand would need heavy abstraction.

*Tags:* Rhythm, Historical, Puzzle, Management, Atmospheric, Relaxing, Singleplayer, Indie, Logic

> In 1820 the church bells are the village's voice. Captain eight ringers on eight ropes, call the changes for weddings, funerals and fairs, and ring a three-hour peal without a slip.

In a Suffolk parish in 1820, the church bells announce every christening, wedding, funeral, harvest home and piece of news from London, and the ringers who pull them are the proudest folk in the village. You are their new captain, and the rival band from the market town across the river has never let you forget it. Eight bells hang in the tower, each heavy as a cart horse and swung full circle on a rope. They sound one after another in rounds, and you call out which neighbouring pair should swap places next, so the order wanders through thousands of rows without repeating. Moment to moment you pull your own rope in steady time, call the changes, and listen for the ringer who has drifted late or lost their place. Between practices you recruit the blacksmith, the schoolmistress, the poacher and the miller's daughter, teach them to handle a rope without being hauled off their feet, settle quarrels over the beer money, and keep the peace with a curate who thinks it all far too loud. The goal is a full peal, five thousand changes without a fault, for the squire's wedding.

*Pitch:* English change ringing becomes the game: you lead a village band of bell ringers, calling the swaps in a pattern that must never repeat while keeping eight amateur villagers in time.

## 2. Dawn Caller

**+4.31σ** · bge 100.00% · MiniLM 99.99% · v3 novelty search · closest Steam game: 深夜1時の交換手 (0.68)

Prior art: **a close game exists** (thin check). The central twist already exists as a released game. In Suhoor Hero you play a Ramadan drummer walking the streets to wake people for suhoor, and you play drum sequences correctly, though only to calm street dogs. The RamadanCraft Minecraft mod also has a drummer NPC that wakes the village. Neither has Dawn Caller's loop: planning a route through 30 nights so every named household is woken before dawn, plus personalised calls at each door and relationships with the quarter. Note: the shared web-search budget ran out partway through, so only 2 searches ran and Turkish 'Ramazan davulcusu' mobile games were not checked. More prior art is likely there. [Suhoor Hero by odilektasli (itch.io / Google Play)](https://odilektasli.itch.io/suhoor-hero)
Coherence 4/5: A clear, warm premise: route planning under a dawn deadline plus rhythm calls at each door. The two halves need careful blending, and remembering names could become busywork.

*Tags:* Historical, Rhythm, Puzzle, Time Management, Atmospheric, Wholesome, Singleplayer, Indie

> Cairo, 1935. Through the thirty nights of Ramadan, walk the old city's alleys with a small drum before dawn and call every family by name, so no one sleeps through the last meal before the fast.

In the old quarter of Cairo in 1935, the nights of Ramadan belong to the dawn caller: the person who walks the alleys in the dark hours with a small drum and a lantern, stopping at each door to call the family by name and wake them for the meal before the day's fast begins. Your father did it for forty years; this year it is your turn. Each evening you plan your route through a maze of lanes, courtyards and stairways, because every household must be woken in time to cook and eat before the call to prayer. Moment to moment you walk, beat a steady rhythm, and sing short rhymed greetings for each door, using the right names and a kind word for the sick widow or the new baby. Children follow you, shopkeepers offer tea, and grumpy neighbours shout from balconies. Forget a family and they will not forgive you. At the end of the month, the people you woke repay you with sweets, coins and cloth for the feast. The goal is to earn the trust of the whole quarter.

*Pitch:* A route-planning and drumming game about the Ramadan dawn caller: across thirty nights you wake every household in an old Cairo quarter by name, in time, before the fast begins.

## 3. Forty Thousand Words

**+4.19σ** · bge 100.00% · MiniLM 99.99% · v3 novelty search · closest Steam game: Mini Words - minimalist puzzle (0.71)

Prior art: **no prior game found**. I found no game about compiling a historical dictionary: harvesting quotations, splitting words into senses, picking the illustrative quote, all under a money and deadline squeeze. The only definition-writing games are party bluffing games (Dictionarium, Fictionary) and a nonsense-dictionary sandbox on itch.io (The Impossible Dictionary). They share the act of defining words and nothing else. [Dictionarium (Jackbox Party Pack 6), a party game where players write definitions for made-up words](https://www.jackboxgames.com/dictionarium/)
Coherence 3/5: The theme is strong, but the moment-to-moment verb is vague: how do you score a player-written definition? And 40,000 words forces abstraction into a few hand-made entries plus bulk management, which the pitch leaves unresolved.

*Tags:* Historical, Puzzle, Management, Investigation, Education, Relaxing, Singleplayer, Indie

> London, 1747. A group of booksellers has paid you to write the first great English dictionary in three years. Hire copyists, mark up every book you own and define forty thousand words before the money runs out.

In 1747 a group of London booksellers pays you a large advance to do what no one has done: write a complete dictionary of English, with a quotation from a great writer for every meaning of every word, in three years. You rent a garret off Fleet Street, hire six copyists, some of them drunk, and fill the room with borrowed books. Moment to moment you read through poets, sermons, law books and gardening manuals, mark the sentences that show a word's meaning, and pass them to your copyists to cut into slips. Then, word by word, you sort the slips, decide how many meanings each word has, write a definition for each and choose the best quotation. Some definitions are a joy; others take a week. Lenders want their books back with your pencil marks rubbed out, creditors knock at the door, and a lord who once ignored you suddenly wants credit. The booksellers want pages, not perfection. The goal is to finish before the advance is gone and the rival French academy can laugh.

*Pitch:* You write an 18th-century dictionary against a deadline: gather quotations, split each word into its meanings and pick the best example, while managing copyists, creditors and the money left.

## 4. Saturday Night Noisemaker

**+4.18σ** · bge 100.00% · MiniLM 99.99% · v3 novelty search · closest Steam game: Grave Benders (0.67)

Prior art: **no prior game found** (thin check). Searches for a live-foley or silent-film sound-effects game found only real-world foley history and classroom exercises (for example the ds106 'Charlie Chaplin's Foley Artist' assignment), not a game. Pick-the-right-prop-and-hit-the-moment is a rhythm-game pattern (Rhythm Heaven-style cue reading), but no game with the silent-cinema foley twist turned up. Caveat: the shared search budget ran out after 2 searches, so itch.io jam games tagged 'foley' were not checked, and a jam entry could plausibly exist.
Coherence 4/5: The core loop is strong and readable: watch a mirrored, blurry film and trigger the right noisemaker on cue. The mining shifts, prop crafting and strike management feel bolted on.

*Tags:* Rhythm, Historical, Comedy, Funny, Hand-drawn, Casual, Singleplayer, Indie, Music

> In 1925 the pictures are silent, but the miners in the hall still hear every gunshot, train whistle and custard pie. Stand behind the screen with your box of noisemakers and play the film live.

In 1925 films have no soundtrack, so the miners' hall in a Welsh valley town hires someone to stand behind the screen on Saturday nights and make the noises live. That someone is you, a pit boy with quick hands. Your kit is a bass drum, a bicycle bell, a train whistle, coconut shells, a crank wind machine, a cap pistol, a sheet of tin and a bucket of coal, and the chapel organist at the piano will not wait for you. Moment to moment you watch the film flicker through the back of the screen, mirrored and blurry, and hit each noise as it happens: a door slam, a car horn, a cowboy's six-gun, a custard pie in the face. Miss the moment and the whole hall laughs at you instead of the picture; get the slapstick timing right and the benches shake. Between shows you work your shift underground, build new noisemakers, and argue with the projectionist about which reels to rent. The goal is to keep the hall full through a long strike.

*Pitch:* A prop-based timing game in which you perform the sound effects for silent films live from behind the screen, picking the right noisemaker and hitting each on-screen moment for a mining-town crowd.

## 5. The Prompter's Trapdoor

**+4.09σ** · bge 100.00% · MiniLM 99.98% · v3 novelty search · closest Steam game: Play - An Interactive Piece (0.68)

Prior art: **no prior game found** (thin check). I found no game where you are a hidden prompter judging the timing and volume of whispered lines while actors forget, skip scenes or switch languages. Not For Broadcast shares the idea of rescuing a live show with well-timed actions, but its verbs are camera cuts, censoring and ads, not prompting. Only one search finished before the shared web-search budget ran out, so this verdict is less thoroughly checked than the others. [Not For Broadcast (Steam), a real-time game where you save a live TV show from a control room](https://store.steampowered.com/app/1147550/Not_For_Broadcast/)
Coherence 4/5: A clear real-time attention and timing loop (follow the script, read faces, choose when and how loud to whisper) with a good recovery challenge when actors improvise. The touring and feud layer is light but works.

*Tags:* Comedy, Historical, Narrative, Real-Time, Funny, Story Rich, Singleplayer, Indie, Hand-drawn

> Bombay, 1890. Hide beneath the stage of a touring theatre company and whisper forgotten lines to its stars, through songs, sword fights and painted thunderstorms.

In 1890 a theatre company from Bombay tours the railway towns of India, performing grand dramas full of songs, magic, sword fights and painted thunderstorms, in three languages on three different nights. The stars are famous, the plays are long, and nobody knows every line. That is why the company keeps you, the prompter, crouched beneath a trapdoor at the front of the stage with the only complete script and an oil lamp. Moment to moment you follow the play line by line, watch the actors' faces for the frozen look of a forgotten speech or verse, and whisper the next words at the right moment and volume. Too early and you insult the proud leading man; too loud and the front rows laugh; too late and the demon king stands silent while the princess waits to be rescued. Actors skip scenes, add songs the crowd demands and switch languages mid-act, and you must find your place again fast. Between shows the company travels by train, and you learn each actor's habits and settle backstage feuds. The goal is to bring the company home from its longest tour.

*Pitch:* You play the hidden prompter of a touring theatre company, saving live shows by whispering the right line at the right moment and volume while the actors improvise, skip scenes and switch languages.

## 6. Three Miles in the Dark

**+3.87σ** · bge 99.99% · MiniLM 99.97% · v3 novelty search · closest Steam game: Secret of the Abbey (0.68)

Prior art: **no prior game found** (thin check). Searching for legging through canal tunnels found only historical sources (Wikipedia, canal museums, Dudley Tunnel Trust), with no game built on it. The general mechanic of two players alternating inputs to push a boat in sync exists as party and sports minigames (tandem canoe or rowing types), but that is only a shared genre mechanic. Caveat: the shared search budget ran out after 1 search, so this verdict rests on thin evidence.
Coherence 3/5: Clear and buildable: a co-op stamina rhythm game in the dark. But one long tunnel of steady alternating steps risks monotony, and the meta layer (bargaining, inn, training partners) is generic.

*Tags:* Historical, Rhythm, Simulation, Atmospheric, Local Co-Op, Difficult, Singleplayer, Indie

> Yorkshire, 1830. The canal tunnel is three miles long, pitch dark and has no towpath, so you lie on a plank across the boat and walk it through with your boots on the dripping walls.

In 1830 the canal crosses the Pennine hills through a tunnel three miles long, too narrow for a towpath, so the horses are led over the moor while the boats are pushed through by men lying on their backs. You are one of those men, a legger, paid a shilling a trip from a hut at the tunnel mouth. You and your partner lie on planks laid across the boat's bow, and by the light of a single candle you walk the boat along by pressing your boots against the wet walls, step by step, in steady rhythm. Moment to moment you keep time with your partner, shorten your stride where the tunnel narrows, call out at passing places, and save your strength for the long stretch where water pours from the roof and the air turns foul. Push out of step and the boat scrapes and stalls; go too fast and your legs give out halfway. Between trips you bargain with boat families, drink at the tunnel inn, nurse your knees and train new partners. Play alone or with a friend on the second plank, and become the fastest pair on the canal before the railway arrives.

*Pitch:* A two-person rhythm and stamina game about 'legging', where you lie on your back and walk a canal boat through a dark three-mile tunnel by pushing your feet against the walls in step with a partner.

## 7. The Drum That Speaks

**+3.82σ** · bge 99.99% · MiniLM 99.98% · v3 novelty search · closest Steam game: Fingerdrums (0.69)

Prior art: **no prior game found** (thin check). Path of Ayan shares the instrument, the setting and a drum-at-events-for-reputation meta loop. It has no tonal-language decoding, no context-based resolution of homophones and no relaying messages between towns, which is this idea's central twist. I found no game that decodes tonal drum messages. [Path of Ayan (itch.io student prototype), a rhythm survival game where you play the Yoruba talking drum at events for money and reputation](https://topzone.itch.io/the-path-of-ayan)
Coherence 4/5: A strong deduction loop in the vein of Chants of Sennaar (tone patterns map to several words, and context picks the right one), paired with a performance step to relay the message. Clear and buildable, though it depends on careful, authentic Yoruba linguistic content.

*Tags:* Puzzle, Historical, Language Learning, Atmospheric, Narrative, Rhythm, Singleplayer, Indie

> West Africa, 1850. The language here rises and falls in pitch, and so does your drum. Listen to the next town's drummer across the forest, work out the words, and beat the message on toward the palace.

In the Yoruba towns of 1850, speech is musical: every word rises and falls in pitch, and a skilled drummer can make a talking drum say almost anything by squeezing its cords to bend the note. You are the new royal drummer of a small town on the road between the coast and a king's palace, and you are still learning the drum's language. Moment to moment you listen to the next town's drumming drift across the forest, write down its high, middle and low beats, and work out which words and proverbs they could stand for, since many words share the same melody and only context tells them apart. Then you drum the message onward, squeezing and striking in the right pattern so the town beyond can understand it. Messages announce births, deaths, markets, visiting traders and approaching danger, and one wrong word turns a wedding into a funeral. At court you drum praise names for chiefs and guests, where a clever proverb wins favour. Between messages you carve drums, train apprentices and learn the history of every family. The goal is to become the drummer whose word the king trusts.

*Pitch:* A decoding and relay puzzle built on the Yoruba talking drum: you work out tonal drum messages from the next town by context and pass them on accurately, where one wrong word changes the news.

## 8. Bellfast Tower

**+3.65σ** · bge 99.99% · MiniLM 99.93% · v3 novelty search · closest Steam game: Bell Ringer (0.70)

Prior art: **a close game exists**. The core co-op loop already exists: in Ringing Room each online participant controls one bell rope and the band rings methods together in real time. Abel/Mabel/Mobel let a single player ring one bell against computer ringers, and Show Me The Ropes on itch.io turns method ringing into a Guitar Hero-style rhythm game. These are training tools or simple rhythm trainers, though, not games with physical bell handling, a campaign of teaching beginners, tower restoration and a post-WWI story. So the narrative and progression wrapper is new, but the mechanic is not. [Ringing Room (online change-ringing platform); also Abel/Mabel/Mobel simulators and 'Show Me The Ropes' (itch.io rhythm game)](https://cccbr.org.uk/2020/06/07/ringing-room-a-users-guide/)
Coherence 4/5: Well defined: one rope per player, keep time, swap places in methods without clashing. Change ringing is niche and steep to learn, but the beginner-band story is a natural tutorial.

*Tags:* Rhythm, Faith, Music, Physics, Online Co-Op, Co-op, Team-Based, Historical, Wholesome, Narrative

> 1919. The bells of St Anne's fell silent when the village ringers went to war and never came home. Rehang the bells, recruit a band of complete beginners, and teach them to ring before the new year.

Bellfast Tower begins in an English village church a year after the Great War. The old band of ringers marched away in 1914 and none of them returned, and the bells have hung silent ever since. The ropes are rotten, a bell is cracked and nobody remembers how it was done. With the vicar's blessing and a handful of volunteers, you set out to bring them back. Ringing is hard physical work: each bell weighs as much as a small car and swings a full circle with every pull, and the band must keep perfect time as the bells swap places in long patterns called methods. Teach a farmer, a schoolgirl, a shy postman and a wounded soldier to handle a rope safely, then to ring rounds, then to ring changes. Mend the frame, raise money at the fete and keep the band together through grief and harvests. Play alone with computer ringers or with friends online, each holding one rope, and ring the village into the new year.

*Pitch:* A co-op rhythm game built on English church change-ringing, where each player handles one physically swinging bell and the band must ring permutation patterns together without a clash.

## 9. Seating Europe

**+3.63σ** · bge 99.99% · MiniLM 99.92% · v3 novelty search · closest Steam game: Etiquette Elegance (0.70)

Prior art: **a close game exists**. The core loop, a logic puzzle where you seat guests so their likes, dislikes and pet peeves are satisfied (wedding receptions included), is exactly what Is This Seat Taken? does, and it is a hit on Steam. Several itch.io jam games also do guest seating. What sets this idea apart is the layer on top: who can overhear whom, consequences that play out over the evening (treaties or duels), the 1905 diplomatic setting and the bribed police informant. The central puzzle exists; the overhearing/diplomacy twist was not found. [Is This Seat Taken? (Poti Poti Studio / Wholesome Games, Steam/Switch/mobile, 2025); also itch.io jam games HomeTable, Wedding Planner (LD54), Antisocial Bubbles: Wedding Edition (GGJ25)](https://store.steampowered.com/app/3035120/)
Coherence 4/5: A clear constraint puzzle with readable stakes. Overhearing radius and consequences that run between evenings give it depth beyond plain seating puzzles; the informant choice is a nice moral layer.

*Tags:* Puzzle, Logic, Historical, Comedy, Diplomacy, Funny, Choices Matter, Singleplayer, Indie

> Vienna, 1905. As head waiter of Europe's grandest hotel dining room, seat diplomats, bankers and countesses so that the right people meet, the wrong ones never do, and every dinner ends in toasts.

In 1905 the dining room of a grand Vienna hotel is where the fate of Europe is quietly arranged between the soup and the coffee, and you are its head waiter. Every evening ambassadors, archdukes, bankers, composers, cavalry officers and countesses reserve tables, and you decide where each one sits, who faces whom and who can overhear which conversation. Each guest has a rank, a temper, a secret and a list of people they cannot stand. Moment to moment you place name cards on a floor plan of tables, read notes from the doorman and the cloakroom girl, and redraw the plan when a late telegram arrives or a duchess appears without a booking. Then the evening unfolds: a quiet table by the palms may let a treaty be agreed, while an insult across the room ends in pistols at dawn. Meanwhile a polite gentleman from the police pays you to seat certain guests where he can listen, and you must decide whose side you are on. The goal is to keep the peace of Europe for one more season.

*Pitch:* A seating-chart logic puzzle used as quiet diplomacy: where you seat each guest, and who can overhear whom, decides treaties, duels and police informing in a 1905 hotel dining room.

## 10. Landfall Captions

**+3.13σ** · bge 99.95% · MiniLM 99.85% · v3 novelty search · closest Steam game: Chick-Chat (0.72)

Prior art: **no prior game found**. I found no game where you play a live broadcast captioner. Steno Hero has the closest mechanic: a Guitar Hero-style game where you type song lyrics as you hear them. It has no story, broadcast or choices. Not For Broadcast is about live-TV decisions, but you switch cameras and do not type. Only 3 searches ran before the shared web-search budget ran out, so the check is incomplete. [Steno Hero / Steno Arcade (PC, Open Steno Project)](https://crowdsupply.com/for-all-to-play/steno-hero)
Coherence 4/5: Clear core loop: type what you hear, under time pressure, with real stakes. Letting the player choose what to keep when speech outruns typing fixes the problem that nobody can transcribe at broadcast speed.

*Tags:* Typing, Narrative, Emotional, Choices Matter, Modern, Real-Time, Dialogue Heavy, Multiple Endings, Realistic, Time Management

> Work the overnight shift as the live captioner at a small-town TV station. Type every word spoken on air in real time while a hurricane cuts the town off, and your captions become its lifeline.

Landfall Captions puts you in a cramped booth at a local television station on the night a hurricane makes landfall. You are the live captioner: everything said on air must appear as text within seconds, so viewers who cannot hear the broadcast know where to go and when to leave. Anchors improvise, reporters shout over the wind, and the emergency office reads out road closures and shelter addresses that must be typed exactly right. A wrong street name can send people the wrong way. When the power goes and the station switches to radio, your captions on the website become the only place deaf viewers can follow the news. Between broadcasts the phone rings with questions, the station manager pushes for ratings, and the building leaks. You decide what to keep when the anchor speaks faster than anyone can type, and whether to post a warning nobody approved. Six real-time hours of rising water, and every word counts.

*Pitch:* A real-time typing game where you are a TV station's live captioner during a hurricane, and your speed, accuracy and choices about what to keep decide which deaf viewers reach safety.

## 11. Coconuts and Thunder

**+3.03σ** · bge 99.98% · MiniLM 98.91% · v3 novelty search · closest Steam game: A Western Drama (0.69)

Prior art: **no prior game found** (thin check). One web search for a live radio-drama foley game found only real-world foley and radio-play articles, no game. The per-turn search budget ran out after that, so the check is thin. Small jam games about foley artists likely exist on itch.io but could not be confirmed. No released game was found that combines live script-cue foley with prop crafting and couch co-op.
Coherence 4/5: A rhythm/cue-hitting loop where the 'notes' are physical props, with prop invention between shows and split-table co-op. It is buildable and naturally a party game; the improvisation and 'impossible sound' parts need tight rules.

*Tags:* Rhythm, Comedy, Physics, Crafting, Historical, Co-op, Local Co-Op, Narrative, Party Game, Simulation

> It is 1938 and the radio play goes out live in ten minutes. You make every sound the listeners hear, from horses and storms to gunshots and slammed doors, with nothing but a table full of junk.

Coconuts and Thunder puts you at the sound effects table of a radio drama studio in the golden age of broadcasting. Actors read the script into the microphone and you make the world around them, live, with no second take. Coconut shells become galloping horses, crumpled cellophane becomes a crackling fire, a box of gravel becomes footsteps, and a sheet of tin becomes thunder. Follow the script, watch the director's hand signals, and hit every cue at exactly the right moment. A late door slam ruins a murder scene. A wrong sound turns a love story into a comedy. Between shows you build new props from whatever you can find, invent sounds for scripts that ask for impossible things like a rocket landing on the moon, and keep up with a cast that loves to improvise. Play alone or with friends on the same couch, each running part of the table, and keep the nation listening every week.

*Pitch:* You are the live sound-effects artist on a 1930s radio drama, hitting script cues with household props in real time and building new props between broadcasts.

## 12. Heave and Sing

**+3.02σ** · bge 99.98% · MiniLM 99.18% · v3 novelty search · closest Steam game: Laylines (0.70)

Prior art: **already exists** (thin check). Ragnarock is a released VR rhythm game. You drum to set the beat for your Viking crew's rowing, and you race rival longships online, in local split-screen or against ghost ships. That matches this pitch almost word for word, with Vikings in place of a tea clipper. The itch.io game Shanties in Strange Waters is a rhythm game about keeping up with the crew's halyard shanty, which is this idea's exact shanty-hauling twist. Rhythm Heaven's Pirate Crew is another crew-rows-on-the-beat example. What is new here is only the layer around the music: choosing songs for each task, crew tiring when the tempo is too fast, and a long narrative voyage. [Ragnarock (Steam / Quest / PSVR2, WanadevStudio)](https://store.steampowered.com/app/1345820/Ragnarock/)
Coherence 4/5: The rhythm-to-speed race is proven to work. The challenge is spreading it over a 99-day voyage and giving co-op players, each on their own line, enough to do.

*Tags:* Rhythm, Music, Sailing, Historical, Racing, Co-op, Online Co-Op, Team-Based, Narrative, Atmospheric

> Lead the work songs on a tea clipper racing from China to London in 1866. Every rope is hauled by hand, and the crew pull only as fast and as long as you can keep them singing.

Heave and Sing puts you aboard a sleek tea clipper in the great race to bring the season's first tea from China to London, ninety-nine days across three oceans. You are the shantyman, the sailor whose job is to sing. Raising the anchor, setting sail and pumping the hold are all done by hand, and a crew only pulls together when someone keeps the rhythm. Choose the right song for each job, call the verses, and hold the beat so thirty sailors haul at the same moment. Sing too fast and they tire. Sing too slow and the sail is not set before the squall hits, and the rival ships pull ahead. Between watches you learn songs from sailors of a dozen countries, make up verses about the cook, and lift the spirits of a crew that shares no single language. Play alone or with friends online, each hauling a line, and bring your ship into London first.

*Pitch:* A rhythm game turned into an ocean race: as the ship's shantyman you set the tempo of the crew's work, and your ship's speed against rival clippers depends on how well you keep the beat.

## 13. Saddlebag Nurse

**+2.97σ** · bge 99.97% · MiniLM 99.32% · v3 novelty search · closest Steam game: Dr. Cares - Family Practice (0.71)

Prior art: **no prior game found** (thin check). The one search on the Frontier Nursing Service and horseback nurse-midwife games returned only history and documentaries (Angels on Horseback, KET), no game. The search budget ran out after that. Rural-doctor and delivery-route games exist in general, but none found pairs horseback route planning across a roadless district with hands-on births at the bedside.
Coherence 4/5: Two clear layers: plan rounds and travel on the map, then short bedside procedures. Horse care, trust and record-keeping risk system bloat, but the core loop holds together.

*Tags:* Horses, Medical Sim, Historical, Female Protagonist, Narrative, Exploration, Nature, Choices Matter, Emotional, Management

> Kentucky mountains, 1925. You are a nurse-midwife on horseback, the only care for hundreds of families spread across hollows with no roads. Ride out in any weather and bring mothers and babies through.

Saddlebag Nurse follows a young nurse-midwife on her first posting to a remote mountain district where the nearest hospital is two days away. Her clinic is a log cabin, her ambulance is a horse called Pepper, and her patients live up creeks and ridges that no car can reach. Each day you plan rounds across the district map, fording rivers, climbing trails and checking on expecting mothers, sick children and old folks living alone. Then a rider arrives at night, and you set out to a birth in the rain. At the bedside you work with what is in your saddlebags: listen, feel the baby's position, time the labour and watch for the warning signs that mean you must act. Families are proud, suspicious of outsiders and full of their own remedies, and trust is earned one visit at a time. Care for your horse, keep careful records, and get the whole district through a year of floods, fevers and snow.

*Pitch:* A medical game played on horseback: you plan rounds across a roadless 1920s mountain district as a nurse-midwife, then handle births at the bedside with only what fits in your saddlebags.

## 14. Doorstep 1917

**+2.89σ** · bge 99.91% · MiniLM 99.67% · v3 novelty search · closest Steam game: Legacy 1917 (0.72)

Prior art: **a close game exists** (thin check). Lake has the same core loop: deliver mail around a small town, get to know the residents through dialogue choices, and let relationships and choices shape a branching story. It lacks this idea's main twist: deciding how to break wartime death notices, plus cycling against the clock to deliver urgent telegrams. I found no game about a WWI telegram messenger, but only 1 search ran before the budget ran out. Small itch.io or jam games on this topic may exist and were not checked. [Lake (PC/Xbox/PS, Gamious, 2021)](https://store.steampowered.com/app/1118240/Lake/)
Coherence 4/5: Strong emotional hook. The fast cycling routes and the slow scenes on doorsteps may pull against each other in pacing, but the two halves connect well.

*Tags:* Cycling, Historical, World War I, Female Protagonist, Narrative, Emotional, Choices Matter, Story Rich, Life Sim, Time Management

> It is 1917 and the boys have gone to war, so the post office hires you. Ride your bicycle through town with telegrams of births, business and death, and learn to read a face before you hand one over.

Doorstep 1917 is a story about the young people who carried news through a small industrial town during the First World War. Every morning you collect envelopes at the post office counter and ride out through cobbled streets, steep hills and factory yards. Some telegrams are good news: a wedding, a birth, an order for the mill. Some are the ones every family dreads, from the War Office, and people learn to fear the sight of your cap. Plan your route, beat the clock for urgent messages, and decide how to deliver the hardest ones: wait with a mother until a neighbour comes, find the father at the factory first, or hand it over and ride on. Your bicycle needs repairs, your wages help feed your family, and the older messengers think a girl will not last a month. Over a year you come to know every street and every family. Finish the year with your job, your conscience and your friends.

*Pitch:* A bicycle delivery game where the hard part comes after you arrive: as a wartime telegram messenger you decide how to break good and terrible news to the same families all year.

## 15. Sky Post of Paris

**+2.78σ** · bge 99.84% · MiniLM 99.69% · v3 novelty search · closest Steam game: Wonderfall (0.72)

Prior art: **no prior game found** (thin check). The one search on the 1870 siege balloon post and pigeon microfilm turned up only history articles (Smithsonian, Stanley Gibbons, NASM), no game. The search budget ran out after that. Steering a balloon only by changing altitude to catch winds is a known mechanic in balloon sims. No game was found built on the two-way pairing of unsteerable outbound balloons and inbound pigeon microfilm.
Coherence 4/5: Clear logistics and launch-decision loop: build balloons, read the wind, steer by altitude, get pigeon replies back. Copying messages by hand at the end is thin, and success depends on how much control the flight phase gives the player.

*Tags:* Historical, Flight, Birds, Management, Physics, Strategy, Atmospheric, Choices Matter, Resource Management, Crafting

> Paris, 1870. The city is under siege and the only way out is up. Launch mail balloons by night, and bring replies home on pigeons carrying thousands of letters shrunk onto a film no bigger than a thumbnail.

Sky Post of Paris is set during the four-month siege of Paris. Enemy armies surround the city and every road is cut. You run the post that keeps it talking to the world. Turn empty railway stations into workshops where seamstresses stitch and varnish cotton balloons, fill them from the city gas mains, and train navy sailors to fly them. Each night you read the wind and decide whether to launch. Once aloft, a balloon cannot be steered, so you guide it only by dropping sand to climb or venting gas to sink into a better wind, and a bad choice carries it into enemy hands. Outgoing balloons carry letters and baskets of homing pigeons. The replies come back on those pigeons, thousands of messages photographed onto tiny films tucked into a feather quill. When a bird lands in your loft, project the film onto a wall and have clerks copy every message by hand. Manage cloth, gas, crews and hope until the siege ends.

*Pitch:* A two-way logistics game set in the 1870 siege of Paris: balloons you cannot steer carry the mail out, and homing pigeons carrying microfilm letters bring the replies back.

## 16. The Airlock Kitchen

**+2.28σ** · bge 99.80% · MiniLM 96.71% · v3 novelty search · closest Steam game: Abyssal Starfeast (0.75)

Prior art: **no prior game found** (thin check). Dave the Diver combines diving and cooking: you dive by day and run a sushi restaurant by night. But you are the diver, not a cook feeding a sealed saturation-diving crew whose work suffers when they eat badly. Project Into the Void (coming soon on Steam) is a saturation-diving simulator but has no cooking. I found nothing that matches the airlock-feeding twist, but only 1 search ran before the budget ran out. [DAVE THE DIVER (Steam/Switch, Mintrocket)](https://store.steampowered.com/app/1868140/DAVE_THE_DIVER/)
Coherence 3/5: Original setting, but the feedback is indirect: you cook, then passively watch how the divers perform. Cooking for 40 sailors as well risks turning it into a generic cooking sim unless food visibly changes outcomes on the seabed.

*Tags:* Cooking, Modern, Underwater, Realistic, Management, Narrative, Emotional, Time Management, Resource Management, Atmospheric

> Six divers will live inside a sealed pressure chamber for twenty-eight days while they repair a pipeline on the seabed. You are the ship's cook, and every one of their meals goes in through a tiny airlock.

The Airlock Kitchen is set on a diving support ship working in the North Sea. Six saturation divers live sealed inside a steel chamber on deck, kept at the pressure of the seabed, and each day a bell lowers them to repair a broken pipeline a hundred metres below. They cannot come out for a month. You are the ship's cook. You feed forty sailors in the mess and pass the divers' meals through a small airlock in the chamber wall. Under pressure, bread collapses, flavours fade and the helium in the air makes the divers cold and hungry all the time. Plan menus that keep them warm and strong, time meals around dives and rest, and follow their work on the seabed through the helmet cameras in the dive control room, where a tired, hungry diver starts making mistakes. Storms toss the galley and the supply boat runs late. Keep the whole ship fed and bring every diver home.

*Pitch:* A cooking and management game where you feed saturation divers sealed in a pressure chamber for a month, and how well you feed them shows up in their work on the seabed.

## 17. Unauthorised Carols

**+2.19σ** · bge 98.80% · MiniLM 99.08% · v2 blend void · closest Steam game: Christmas Rhythm (0.79)

Prior art: **a close game exists**. Electric Bard already combines rhythm guitar lanes with choosing, mid-song, which lyric line to sing. One option 'lifts the crowd', one 'twists them' and one 'fades into safety and silence', which is close to the idea's approved-vs-forbidden choice. Clipped (a rockstar turned radio censor deciding what songs the public hears), Unbeatable and Rhythms of Revolution (musicians against a regime) cover the censorship side. No single game found combines editing lyrics past a censor before the gig with a live safe-or-real lyric choice under secret-police scrutiny. [Electric Bard (itch.io, HTML5 jam game, Mini Jam 203)](https://scalphamission.itch.io/electric-bard)
Coherence 4/5: Clear two-phase loop (censor-editing desk, then a rhythm gig with lyric choices feeding opinion/police heat); the rhythm layer may stay shallow but the design is buildable and the comedy premise is strong.

*Tags:* Simulation, Dystopian, Choices Matter, Casual, Music, Rhythm, Text-Based, Story Rich, Comedy, Interactive Fiction, Christmas, Dark Humor

> A censorship simulator with a guitar. Christmas has been banned in a post-war country, but your rock band is touring anyway. Edit your lyrics past the censors, play each gig in rhythm and shape the people's opinion one carol at a time.

In a grey post-war country governed by the recently elected Loyalist Party, carols are now classified as unauthorised gatherings. As the songwriter of the Sleigh Bells, the last independent rock band in the country, your job is to get the music through.

Before every concert the setlist goes to the local censor's office. Read the new regulations, remove and edit words, swap whole verses and decide which songs to hide inside harmless folk tunes. Every edit changes the people's opinion, the band's reputation and the interest of the secret police.

Then the curtain rises. Play rock versions of famous Christmas songs in a simple rhythm game, and choose in the moment whether to sing the approved lyric or the real one. The crowd reacts to every choice, and so do the officers in the back row.

Between towns, read letters from fans, smugglers and tired bureaucrats. Bring the holiday back to a frightened country, or play it safe and keep the band together until Christmas Eve.

*Pitch:* A censorship sim where the text you edit is your own band's Christmas rock lyrics, and the rhythm game is where you decide in real time whether to sing the approved line or the forbidden one.

## 18. Seating Plan: 1943

**+2.05σ** · bge 98.58% · MiniLM 98.38% · v2 blend void · closest Steam game: Bunker 1945 - Capture the Gray Wolf (0.77)

Prior art: **already exists**. Is This Seat Taken? is a released cozy logic puzzler built on the same loop: you seat 'hilariously particular' characters whose pet peeves decide who can sit next to whom, across venues including banquets, a wedding reception, buses and taxis. The idea uses nearly the same wording. The only difference is a WWII 1943 summit reskin with historical notes, which is setting, not mechanics. I found no WWII-themed seating puzzle. [Is This Seat Taken? (Poti Poti Studio / Wholesome Games, Steam, Aug 2025)](https://store.steampowered.com/app/3035120/)
Coherence 4/5: A proven, clearly buildable constraint-puzzle loop. The WWII summit theme suits the comedy of protocol, though it adds little to the gameplay.

*Tags:* Puzzle, Casual, Logic, Strategy, Comedy, World War II, Historical, War, Family Friendly, 2D, Top-Down, Colorful

> A cozy strategy-flavoured logic puzzle set during the 1943 North Africa campaign of World War II. As protocol officer of a secret Allied summit, find the perfect seat for hilariously particular generals, diplomats and staff, each with pet peeves, without starting a second war at dinner.

North Africa, January 1943. While tank columns fight across the desert, the Allied leaders gather at a seaside hotel to plan the next stage of World War II, and somebody has to decide where everyone sits. That somebody is you.

Every level is a seating puzzle drawn from the summit's busy days: the opening banquet, a cramped briefing room, the motorcade to the airfield, a press photograph on the hotel steps. Each guest has a portrait card listing what they need and what they cannot stand. The admiral must face the sea, the general refuses to sit below the air marshal, two interpreters must stay beside their delegations and the war correspondent cannot be within earshot of anything secret.

Drag guests into place, watch their moods change and rearrange until the whole table is satisfied. New rules arrive as the summit goes on, from blackout curtains to surprise guests. Between puzzles, short historical notes explain the real conference behind the comedy. It is a light, top-down logic game about the small human details behind the big decisions of the war.

*Pitch:* A cozy seating-arrangement logic puzzle set at a 1943 North African Allied summit, where the strategy of the war comes down to who refuses to sit next to whom.

## 19. Contraband Beard

**+2.04σ** · bge 97.36% · MiniLM 99.10% · v1 frontier void · closest Steam game: DragonLineage (0.77)

Prior art: **a close game exists**. BeardMan already has a sentient beard as the hero's tool: growing it extends attack and grapple range, and the villain is a Barber who wants to shave every creature. Who Stole My Beard? (Steam) builds stealth and authority-dodging around beard laws, but in reverse, since there being beardless is illegal. Not found anywhere: the beard as hidden contraband that grows while you sleep, open-world stealth from patrolling barbers, and PvP barber hunters. [BeardMan (itch.io, Windows/macOS platformer)](https://cwru-ecse390.itch.io/beardman)
Coherence 3/5: Memorable hook and a sound tension (a longer beard is more useful but harder to hide), but the explore/hide/sleep loop is thin and the PvP barber mode and 'beard remembers places' feel bolted on.

*Tags:* Exploration, 3D, Simulation, Adventure, Atmospheric, Third Person, Story Rich, Stealth, PvP, Medieval, Open World, Birds

> Your beard grows while you sleep. Birds nest in it. It remembers everything. And in this kingdom, beards are illegal.

Grow the longest beard in the land, in a kingdom where beards are against the law. Royal barbers patrol every road, and a bare chin is the only safe chin. You are an old man whose beard has a mind of its own. Every night you sleep it grows a little longer, and it seems to be alive: sparrows nest in it, it stirs when danger is near, and it remembers the places it has brushed against. By day you wander villages, forests and castle towns, ducking into haystacks whenever a barber passes; by night you find somewhere safe to sleep. You explore, you hide, you sleep, and the beard grows. A longer beard is harder to hide, but it can lift, catch and remember things a shaven chin never could. Online, players can take the role of royal barbers and hunt each other's beards across the same countryside. Play it alone as a gentle, strange story about growing old in a kingdom that has forgotten its grandfathers, or online as a game of hide and seek.

*Pitch:* A third-person stealth and exploration sim where your growing, living beard is your progression, your tool and the contraband you must hide, with an optional online mode where players act as royal barbers hunting it.

## 20. Seeds of Freedom

**+1.93σ** · bge 99.60% · MiniLM 91.73% · v1 hole void · closest Steam game: Our Land (0.74)

Prior art: **no prior game found**. I found no game set on the eve of Ghana's 1957 independence, and none that combines village football with Oware matches against elders that unlock oral history. Sankofa shares the educational Ghana-history village setting, but a girl gathers folk tales in a much earlier era, with no sport or board-game gating. Mancala Adventures has character duels but no history or story unlocks. [Sankofa (UC Irvine educational game, 18th/19th-century Asante/Ghana)](https://news.uci.edu/2018/05/21/uci-created-computer-game-that-immerses-players-in-18th-century-ghana-wins-award)
Coherence 3/5: Workable but loose: an educational walking adventure that gates its story behind two unrelated minigames (an arcade kickabout and Oware), with no strong core loop tying them together.

*Tags:* Board Game, Football (Soccer), Action-Adventure, Historical, Turn-Based, Third Person, Casual, Action, Strategy, Adventure, Education, Sports

> A third-person adventure about football, board games and history in a West African village.

It is early 1957 and Kofi has come home from the city to his grandfather's village on the Gold Coast, weeks before the country becomes Ghana. The village football club has been invited to play an exhibition match on Independence Day, and Kofi wants a place on the team. In this relaxed third-person 3D adventure you wander the market, the cocoa farms, the mission school and the chief's courtyard, talking to neighbours, running errands and training on the red dirt pitch by the river. Football matches are quick, arcade-style kickabouts that anyone can play. In the evenings the elders gather to play Oware, and beating them at the ancient board game is the only way to earn their stories about the cocoa boom, the colonial schools and the long road to freedom. A short, gentle and educational adventure about a real moment in history, told through sport, games and the people who played them.

*Pitch:* An educational third-person village adventure set on the eve of Ghana's independence, where you earn your place through street football and Oware matches, and winning at the board game unlocks oral history.

## 21. The Ashcombe Idol

**+1.88σ** · bge 99.03% · MiniLM 95.02% · v2 blend void · closest Steam game: Love n Dream 3 (0.76)

Prior art: **already exists**. A story mystery that moves forward through match-3 puzzles is a long-established casual genre. That includes Lovecraftian versions (Jewel Link Mysteries: Mountains of Madness, Cthulhu Awakens) and cursed-artifact detective versions (Big Fish's Detective Barnett: The Cursed Artifact). Rotating 3D-cube match-3 also exists (Cube Match, Temple PuzzleBox). Only the film-set framing and the 3D lattice skin are new. [Jewel Link Mysteries: Mountains of Madness (Nintendo DS, Avanquest)](https://www.cubed3.com/games/reviews/nintendo-ds/jewel-link-mysteries-mountains-of-madness)
Coherence 3/5: Workable, but it is a standard match-3 adventure with a muddled third-person/action layer, and a self-sealing rotating 3D lattice risks poor readability.

*Tags:* Puzzle, Adventure, Story Rich, Match 3, Casual, 3D, Strategy, Lovecraftian, Mystery, Historical, Logic, Action

> Hired as consultant on a maverick director's new film about an ancient cult, a history professor finds the prop idol on set is real. Unlock its secrets in 3D match-3 action puzzles and find out whether you are filming a story or starring in one.

Professor Tom Avery was hired to make a maverick director's period film look historically accurate. Then the crew moves into the real Ashcombe University, the director unveils an idol borrowed from the college museum, and the actors start forgetting their lines in favour of words none of them should know.

Explore the campus and the half-built film sets in third person, reading old expedition journals, script rewrites and letters from the museum's founders. When the idol stirs, the game becomes an action puzzle: a rotating 3D lattice of carved stones where you swap neighbours to line up three or more matching symbols, setting off chain reactions before the lattice seals itself again.

Each solved lattice unlocks new rooms, new footage and new truths. The faster you clear it, the more the director films, and the more the idol seems to be watching back.

Has Tom become the unwitting star of the film, or has he stumbled into something far older than history?

*Pitch:* A story-driven mystery on a film set where every sealed secret is a rotating 3D match-3 lattice, so the investigation moves forward through puzzle chains instead of dialogue trees.

## 22. Black Door Holdings

**+1.73σ** · bge 95.81% · MiniLM 97.44% · v2 blend void · closest Steam game: The Black Pyramid (0.78)

Prior art: **a close game exists**. The central twist, a business you inherited whose economic loop pulls you toward Lovecraftian horror while you uncover the previous owner's secrets, already exists. Sunken Engine has an inherited shop, sanity and the father's secrets. DREDGE ties profit to deeper, more eldritch waters, and in Drill Deep you mine deeper for an empire and approach something ancient. None of them is a Victorian oil-tycoon empire paired with point-and-click investigation of a missing patient. [Sunken Engine (Two Nomads/PlayWay, Steam, Oct 2025); also DREDGE (2023) and Drill Deep (Steam, announced)](https://rawg.io/games/sunken-engine)
Coherence 4/5: The bridge between the halves is clear (the richest wells go deepest toward the horror), though a day tycoon / night point-and-click split risks two half-games.

*Tags:* Management, Adventure, Economy, Story Rich, Point & Click, Lovecraftian, Simulation, Choices Matter, Pixel Graphics, Psychological Horror, Resource Management, Multiple Endings

> When his wealthiest patient vanishes, a Victorian psychiatrist is left in charge of the man's oil enterprise. Grow the business of black gold from a few wells into a global empire, while the search drags you deeper into a conspiracy of darkness and madness.

England, 1891. Dr. Edmund Hale's most troubled patient, the oil baron Silas Crane, disappears the night after describing a black door at the bottom of his deepest well. His will names Hale as the trustee of everything he owns.

By day you run the oil enterprise: buy new fields, hire crews and engineers, sign contracts with railway barons, invest in refineries and ride the rise and fall of crude prices to keep the shareholders loyal. By night you search for your patient in pixel-art point-and-click scenes, questioning frightened workers, reading his session notes and examining strange core samples brought up from below.

Profit and dread are bound together. The richest wells reach the deepest places, and every barrel sold buys a little more knowledge and a little less sanity. Choose which fields to open and which to seal, whom to pay and whom to silence.

Rise from reluctant trustee to oil magnate, or follow Crane into the madness waiting beneath his empire. Several endings await.

*Pitch:* An oil-tycoon management sim and a Lovecraftian point-and-click mystery are one loop: the psychiatrist hunting his missing patient has to run the patient's oil empire, and every profitable well drills closer to the horror.

## 23. Bitter Remedies

**+1.71σ** · bge 97.88% · MiniLM 94.59% · v2 blend void · closest Steam game: Clue: Murder By Death (0.77)

Prior art: **a close game exists**. In Strange Horticulture you run an odd little shop, and which plant you give each customer drives an occult murder mystery that you also investigate by exploring the town on a map. That is the same shop-plus-investigation core loop. Not covered: the 1888 Whitechapel chemist setting, nightly chemistry tests, and the twist that your own bottles are evidence that may convict you. Ripper investigations (Sherlock Holmes vs Jack the Ripper) and period apothecary sims (Dear Apothecary) exist separately. [Strange Horticulture (Bad Viking, Steam, 2022)](https://store.steampowered.com/app/1574580/Strange_Horticulture/)
Coherence 4/5: Clear day-shop/night-investigation loop where sales choices feed the evidence; buildable and on-tone, though the 'tip one flask into another' brewing is thin.

*Tags:* Casual, Simulation, Adventure, Detective, Puzzle, Investigation, Management, Mystery, Choices Matter, Story Rich, Crime, Point & Click

> Become a self-taught back-alley chemist in 1888 London and discover the darker side of chemistry. Mix dubious concoctions for strange customers, then help hunt the killer stalking the fog before your own bottles convict you.

Whitechapel, autumn 1888. Your little back-alley shop sells hair tonics, miracle lotions and the occasional black-market mixture that is better not asked about. Business is fine until a bottle with your label is found beside a victim of the most feared killer in England, and a sharp-eyed detective starts dropping by every evening with polite questions.

Days are spent behind the counter. Brewing is simple, just tip one flask into another and see what happens, but every customer wants something different and you decide what you are willing to make and who you will sell it to. Watch your stock, money and reputation, because every bottle may come back as evidence.

Nights belong to the investigation. Run real Victorian chemistry tests on the samples the detective leaves with you, match handwriting in your order book and point and click through foggy streets to question regulars and suspects. Each clue can clear your name or tighten the noose, depending on what you choose to reveal. Darkly funny, gently paced and full of moral choices, it is a detective story told from the wrong side of the counter.

*Pitch:* A Victorian murder mystery told from behind the counter of a shady chemist's shop: the bottles you sell by day are the evidence you must analyse by night, and they may convict you.

## 24. Good Dog, Old Games

**+1.60σ** · bge 97.77% · MiniLM 92.00% · v2 blend void · closest Steam game: Ian's Eyes (0.77)

Prior art: **a close game exists**. In Ian's Eyes you play North, a seeing-eye dog guiding Ian, a blind boy, on his first day at a new school. That is the same escort-as-guide-dog twist, and even the school framing matches. Several itch.io jam games do the same (Guiding Paws, Life of a Guide Dog, Stan). What I did not find is the setting of a video game history museum where playable retro exhibits act as the door locks. [Ian's Eyes (Florida Replay, Steam, 2016)](https://store.steampowered.com/app/452340/Ians_Eyes/)
Coherence 3/5: Clear escort loop, but there is a thematic and mechanical tension: it is unclear who plays the screen-based retro exhibits, the dog or the blind boy, and how they open doors.

*Tags:* Adventure, Retro, 1990's, Old School, Casual, 2D, Historical, 1980s, Puzzle, Family Friendly, Side Scroller, Dogs

> School trips are tough for an eight-year-old who is blind, and tougher when the class leaves him locked inside a video game museum after dark. You play as his lifelong canine companion: guide him through fifty years of playable history and help him escape.

First days at school are tough enough. Ollie's first class trip is to the national museum of video games, and he cannot see a single screen. He has Juno, his guide dog, and a head full of old games his dad taught him to play by sound. When the class leaves without them and the lights go out, the two of them are on their own.

You play as Juno. Every gallery is a different decade, and every exhibit still runs: dozens of playable classics, from 1970s paddle games to 1980s arcade cabinets and 1990s home consoles. Ollie holds your harness while you lead him through side-scrolling rooms, sniff out safe paths, push switches, bark warnings and work out which old machines open which doors.

Along the way, recorded interviews with designers, original sketches and design documents in each gallery tell the story of how games were made, and hide the clues you need to get out. A gentle, old-school adventure about trust, history and seeing the world differently.

*Pitch:* An escort-puzzle adventure where a guide dog leads a blind boy through a museum of video game history after dark, and the playable retro exhibits are the locks on every door.

## 25. Wallcode 1920

**+1.56σ** · bge 94.14% · MiniLM 96.09% · v1 frontier void · closest Steam game: Revolution: Young Mao (0.80)

Prior art: **a close game exists**. War In The Dark has you command your forces only through coded messages (tapped Morse code) and intercept and decipher enemy orders. That is the same 'orders as code, crack the enemy's code' core loop, but as a 2D turn-based wiretapping game rather than first-person painted walls. Decrypto (board game) shares encoding for your team while the other team intercepts, and Graffiti Wars/CS sprays share painting over walls. No game was found where painted wall symbols are the squad's command channel. [War In The Dark (Sprout Studio, Steam, announced for Q1 2027)](https://store.steampowered.com/app/4949240)
Coherence 2/5: Tag soup: 'realistic FPS' plus paint-commanded squads plus notebook cipher-breaking plus visual novel plus roguelite classes, with no clear account of how real-time first-person action fits slow cipher work.

*Tags:* Visual Novel, First-Person, Strategy, Realistic, Action, Adventure, Historical, Class-Based, Roguelite, 3D, Puzzle, Choices Matter

> In a frontier town in 1920, orders are written on walls. Paint codes for your squad, break the enemy's, and reach every checkpoint first.

Wallcode 1920 is a realistic first-person war game where two teams paint the walls, break each other's codes and race to the checkpoints. Neither army trusts the radio, so orders are left in paint and chalk.

Every street is an arena. You carry a paint pot, a stick of chalk and a cipher notebook. Paint a symbol and your squad obeys it: wait, cross, breach. Enemy scouts paint their own, so you copy their marks, break the cipher in your notebook and paint over them to send their runners into a dead end. Hold every checkpoint before they do and the district is yours.

Between missions the story plays out as an illustrated visual novel in the signals office, where officers, couriers and a suspected traitor test your loyalty. Every run builds a new town with fresh ciphers; fall, and you begin again with what you learned and a new class unlocked: the runner, the codebreaker or the forger who can copy enemy handwriting.

*Pitch:* A first-person war fought only through painted wall-codes: you guide your squad with symbols, crack and over-paint the enemy's chalk ciphers, and race their runners through the streets, with the story told as a visual novel between roguelite runs.

## 26. Prime Time Planet

**+1.56σ** · bge 98.80% · MiniLM 85.41% · v1 frontier void · closest Steam game: Terra Trials (0.76)

Prior art: **a close game exists**. Showgunners is a linear, story-driven game about a contestant on a cruel TV show. Fame from fans turns into sponsorships with rewards, the host adds hazards, and between fights you avoid traps, solve puzzles and talk to other contestants. Rogue Labyrinth (2025, where 'ratings matter more than survival') and DeathRun TV (likes unlock powers) cover the ratings-as-progression angle. What differs is that the idea spends ratings in a control room to sabotage rivals and pick hazards, and its rounds are short skill challenges rather than tactics battles. [Showgunners (Artificer / Good Shepherd, PC, May 2023)](https://en.wikipedia.org/wiki/Showgunners)
Coherence 3/5: Muddled: three modes (skill rounds, strategy screen, point-and-click) plus contradictory tags (difficult/casual, linear/incremental/survival). Workable, but the core loop is unclear.

*Tags:* Adventure, Difficult, Strategy, Female Protagonist, Retro, Linear, Incremental, Story Rich, Survival, Pixel Graphics, Casual, 2D

> A pixel-art game show adventure about one stubborn mechanic trying to win back her family's farm on live television.

Welcome to Prime Time Planet, the most watched game show on television. Rook, a stubborn mechanic from a mining colony, signs up to win back her family's farm, and you guide her through every episode. On stage, every challenge is a small test of timing and nerve: cross collapsing bridges, dodge spotlights and answer the host's riddles before the buzzer. Between rounds you switch to the control room, a casual strategy screen where ratings become currency: buy sponsor gear, bribe the set designers, choose which hazards to face next and which rival contestants to sabotage. Backstage, you point and click through dressing rooms, prop stores and the editing suite to find tools, allies and secrets. The show is difficult and the hosts are cruel, yet the season follows a linear story with a beginning, a twist and a finale. Every episode Rook survives adds a little more to her kit and her fan club, so a run that starts fragile ends with a contestant the whole planet roots for. Can she survive twelve episodes, win the audience, save the farm and expose the network behind the cameras?

*Pitch:* A linear, story-driven pixel adventure in which you are both the contestant on a cruel TV game show and her backstage schemer, spending ratings on sponsors and sabotage between short skill rounds.

## 27. Nora Off the Page

**+1.55σ** · bge 97.27% · MiniLM 91.61% · v1 hole void · closest Steam game: Undercover with Nora (0.77)

Prior art: **a close game exists**. In The Book Keeper the characters of a narrated enchanted storybook escape and you chase them down and catch them (as a 3D platformer, not a runner). Sierra's Mixed-Up Fairy Tales has you put displaced characters back into their stories. StoryToys pop-up storybook apps (e.g. Puss in Boots) already put chase and obstacle-jumping minigames inside read-along chapters. No exact read-along chapter that turns into an arcade runner was found. [The Book Keeper (Futuregames students, itch.io)](https://futuregames.itch.io/the-book-keeper)
Coherence 4/5: Simple, clear and buildable family loop (read a chapter, then a jump/slide chase that rebuilds the story); low novelty but coherent.

*Tags:* Casual, Cute, Visual Novel, Female Protagonist, Adventure, Story Rich, Colorful, 3D, Action, Comedy, Cartoony, Linear

> Run through the pages of a talking pop-up book. Each chapter is read aloud and fully animated, then turns into a fast, cute runner as Nora races to catch the little aliens escaping from her bedtime story.

Nora Off the Page is a colorful story adventure for families. Nora's favorite pop-up book is about a crew of tiny aliens, and tonight they have decided to leave it. With every alien that escapes, the story falls apart. Each chapter starts like a voiced storybook, with animated 3D pages, words that light up as they are read and simple choices about what Nora says and where she looks next. Then the chase begins and the game becomes a bright arcade runner. Sprint across paper meadows, cardboard rooftops and the inside of a birthday cake, jump over puddles of spilled ink, slide under fences and collect stars while the runaway aliens zip ahead in their tiny saucers. Catch them and they return to the page, adding new scenes, songs and jokes to the story. Chapters are short and linear, controls are just jump and slide, and a gentle mode keeps younger players going. Funny, warm and quick, it is a story you can read and run.

*Pitch:* A voiced, read-along pop-up storybook where each chapter turns into a cute arcade runner, chasing the runaway aliens back onto the page to rebuild the story.

## 28. Billy-Jo and the Martian Gallery

**+1.46σ** · bge 97.01% · MiniLM 89.05% · v2 blend void · closest Steam game: Ruff Night At The Gallery (0.78)

Prior art: **already exists** (thin check). The core concept already exists in Ruff Night at the Gallery. You spend a night in a closed art gallery whose dog paintings are haunted, ghost dogs jump off their canvases to lick you ('Don't get licked!'), and you collect keys to get through each exhibit. It is light, cute horror tagged Horror/Cute/Puzzle/Dogs. What differs is only framing and presentation: the Mars and rocket-kid premise, 2D 90s pixel point-and-click instead of first-person 3D, and puzzles built into the artworks (which Ib also does). Only 1 search was run because the shared web-search budget ran out, but the match is direct. [Ruff Night At The Gallery (Steam / itch.io, CaseyDonnellanGames)](https://store.steampowered.com/app/1463470/Ruff_Night_At_The_Gallery/)
Coherence 4/5: Clear and small in scope: sneak, solve art puzzles, find keys. Cute horror with non-lethal ghosts is a proven tone. The Mars and rocket wrapper adds little to the loop.

*Tags:* Retro, 1990's, 2D, Old School, Sci-fi, Family Friendly, Horror, Cute, Puzzle, Point & Click, Space, Dogs

> A kid genius, a homemade rocket and an alien art gallery haunted by ghost dogs: a cute little 1990s-style horror adventure. Explore the dark halls, find the keys, admire the artwork and get back to Earth before bedtime without getting licked.

Billy-Jo is eight, a certified backyard genius, and slightly lost. His homemade rocket ship has run out of fuel on Mars, and the only building for miles is a grand gallery of Martian art, closed for the night and full of ghosts. Friendly ones. Mostly. They are dogs, and they want to lick you.

Point, click and sneak through the gallery's echoing wings in chunky 1990s pixel art. Each room hides a puzzle built from its paintings and sculptures: line up a cosmic portrait, rotate a statue, decode the brushstrokes to find the keys that unlock the next hall and the fuel cells for your rocket. Ghost pups drift between the exhibits, sniffing for you; hide behind plinths, toss a squeaky toy to distract them or zap them with your trusty toy ray gun to buy a few seconds.

Spooky but never cruel, short and replayable, it is a love letter to the shareware adventures of the early nineties, with a gallery full of dogs that just want a friend.

*Pitch:* An early-90s shareware-style sci-fi adventure in which a backyard rocket kid gets stranded in a Martian art gallery haunted by affectionate ghost dogs, and the artworks themselves are the puzzles.

## 29. The Last Löyly

**+1.36σ** · bge 94.56% · MiniLM 90.45% · v1 hole void · closest Steam game: Saunageddon (0.82)

Prior art: **a close game exists**. Shaun Sauna is a wave shooter where you defend a sauna, and it has sauna health pickups. Sauna of the DEAD uses hot löyly air as a weapon, Sauna2000 pairs a sauna-restoring sim with psychedelic Finnish horror, and FimbulWinter is a Scandinavian winter FPS where you defend your base at night. None of them adds the idea's own piece: a heat-management sim (logs, water, stones) whose steam heals you and pushes back frost enemies in an endless winter, or the VR play. [Shaun Sauna And The Steamy Robots (itch.io); also Sauna of the DEAD (Steam), Sauna2000 (Steam), FimbulWinter](https://eikon.itch.io/shaun-sauna-and-the-steamy-robots)
Coherence 4/5: Clear loop: tend the stove between waves, then shoot the frost. The heat resource ties the halves together, but the 'realistic' and 'psychedelic' tags pull in different directions.

*Tags:* First-Person, Action, Shooter, Simulation, 3D, Atmospheric, Surreal, Psychedelic, VR, Realistic, Physics, Adventure

> A surreal first-person shooter in a sauna at the end of the world. Keep the stove burning, throw steam at the cold, and shoot back the frost that crawls out of the endless night.

The Last Löyly is a surreal, psychedelic first-person VR shooter set in a Finnish sauna at the end of the world. One morning the sun did not rise. The lake froze to the bottom, the forest turned to glass, and the sauna on the shore became the only warm place left.

Between attacks you run the sauna as a realistic physics simulation. Split logs, feed the stove, carry water from the ice hole and keep the stones hot. Every ladle of water on the stones releases a wave of steam that heals you and pushes the cold back.

Then the frost comes to life. Ice figures, frozen elk and whispering shapes crawl over the snow toward the light. Hold them off with an old hunting shotgun, a flare pistol and buckets of boiling water, aiming by hand in VR or with a mouse on a flat screen.

Stay in the heat too long and the steam brings psychedelic visions of the summer that is gone. Survive the long night and find out why the sun went out.

*Pitch:* A first-person survival shooter where the base you defend is a working sauna sim: heat the stones, throw steam to heal and push back the cold, and shoot living frost at the end of the world, with psychedelic steam visions.

## 30. Spellbook Mixtape

**+1.30σ** · bge 93.56% · MiniLM 89.66% · v2 blend void · closest Steam game: Wizard101 (0.78)

Prior art: **a close game exists** (thin check). Kord is a deckbuilder in which each card is a musical phrase. Placing cards (with suit locks across linked slots, similar to 'cards that share a key') composes a multitrack song unique to each run, which is the idea's central twist. Jam Jam! (itch.io jam game) is also a deckbuilder where melody, harmony and rhythm cards build a song. Neither has the wizard-school exploration, turn-based duels or 90s music-video worlds, so this is close rather than exists. Only 1 search was run because the search budget ran out, so other music deckbuilders may also exist. [Kord (itch.io, browser prototype, Octave Games Studio, 2026)](https://octavegamesstudio.itch.io/kord)
Coherence 3/5: The deckbuilding loop with key-matching combos that layer music works. The theme stacks wizard school, 90s music videos, a mystery, crafting and dorm decorating, so it reads muddled.

*Tags:* 2D, Pixel Graphics, Adventure, 1990's, Deckbuilding, Card Game, Retro, Mystery, Magic, Music, Casual, Colorful

> A nostalgic 2D deckbuilding adventure set in a wizard academy whose worlds look like strange 1990s music videos. Build a spellbook of cards, duel odd creatures and unravel why the music professor vanished.

The music professor of a floating wizard academy has gone rogue, and the songs that hold its worlds together are falling silent. As a first-year student with a battered spellbook, you set out through twenty strange worlds that look like forgotten 1990s music videos: neon highways full of space cars, chrome deserts guarded by grinning demons, and cities of giant talking heads.

Explore each world in colourful 2D pixel art, chat with its odd residents and collect clues about the professor's disappearance. When trouble starts, combat switches to turn-based card duels. Your spells are cards drawn from a deck you build yourself: fire, frost, thunder, bloom and dream schools, each with its own sound. Play cards that share a key and they layer into a song that grows more powerful each turn.

Between worlds you return to the academy to craft new spell cards, swap tracks with classmates and decorate your dorm. Light puzzles, a gentle difficulty curve and a mystery told across every world make it a cozy, nostalgic deckbuilding adventure for anyone who grew up with wizard school stories.

*Pitch:* A wizard-school deckbuilder where every spell is a musical phrase and every world is a surreal retro-futuristic 1990s music video, so building your deck also means composing the soundtrack.

## 31. Starfall Over Taihoku

**+1.26σ** · bge 90.65% · MiniLM 91.32% · v1 hole void · closest Steam game: Raid on Taihoku (0.79)

Prior art: **a close game exists**. Raid on Taihoku already does the whole ground half: a girl surviving the 1945 American air raids on Taipei, exploring safe zones and sneaking through danger zones. Nothing found has the idea's real twist, an alien rocket found in a bomb crater that turns the game into a side-scrolling space shooter with RPG upgrades. [Raid on Taihoku (PC/Switch, 2023, Mizo Games/Softstar)](https://rawg.io/games/raid-on-taihoku)
Coherence 3/5: Two separate games bolted together (home-front stealth survival and a space shmup). The jump from a real wartime tragedy to a rescue-the-alien story could jar.

*Tags:* Action, Adventure, Anime, Sci-fi, Space, RPG, 2D, Shooter, Story Rich, Action-Adventure, World War II, Historical

> During the air raids of 1945 Taipei, a schoolgirl finds a crashed rocket that is not from this world. An anime sci-fi action RPG that begins in wartime and ends in space.

In the last summer of the war, sirens sound over Taipei almost every day. Lin Mei-hua is fourteen, and she has learned to run when the sirens start. One morning, in a crater by the river, she finds a sleek silver rocket that no army built, and a small voice inside it asking for help. Starfall Over Taihoku is a 2D anime action-adventure in two halves. On the ground, you sneak through bombed streets and shelters, gathering parts and keeping the rocket secret while helping neighbors survive the raids. Then the rocket wakes, and the story leaves the earth: pilot it in fast side-scrolling shooter stages through orbit, asteroid belts and the derelict stations of the travelers who lost it. Salvage you bring back levels up the rocket's weapons and shields, while the friends Mei-hua makes along the way unlock new skills and story paths. Every chapter is told through hand-drawn scenes and quiet conversations about family, loss and courage. The goal is to send the stranger home before the war ends, and to decide what Mei-hua will carry back down to earth.

*Pitch:* An anime story-driven action RPG that joins a historical home-front survival story (1945 Taipei under air raids) to a space shooter, as a schoolgirl repairs and flies home an alien rocket she found in a bomb crater.

## 32. Bearer of the Lamp

**+1.22σ** · bge 91.40% · MiniLM 89.25% · v2 blend void · closest Steam game: Nefertari: Journey to Eternity (0.83)

Prior art: **a close game exists** (thin check). The VR player's loop already exists as a released product. Nefertari: Journey to Eternity is a VR reconstruction of Nefertari's tomb where you explore 'its art, history, construction, and mythology through interactive elements', almost the same wording as the idea. Asymmetric VR-versus-desktop hunts are also an established form (Nemesis Perspective, Epochalyptic, VRoom). No search found the two combined, with the tomb as a hunting arena and a lamp that changes hands, so this is close rather than exists. Only 1 search was run, plus page fetches, because the search budget ran out. [Nefertari: Journey to Eternity (Steam VR, Experius VR/CuriosityStream, 2018)](https://store.steampowered.com/app/861400/)
Coherence 3/5: The lamp-steal role swap and the light-versus-dark asymmetry are neat. But reading murals slowly to open doors fights with being hunted, so the educational half and the thriller half pull against each other.

*Tags:* Simulation, VR, Education, Historical, Action, Thriller, Asymmetric VR, Exploration, 3D, First-Person, Atmospheric, Mythology

> Step inside a faithful VR reconstruction of Queen Nefertari's tomb in this asymmetric multiplayer thriller. The lamp bearer reads the painted walls to reach the burial chamber; the agile ba-bird flock hunts the bearer through the dark to seize the light and take their place.

The tomb of Nefertari, great royal wife of Ramesses II, has been rebuilt in virtual reality, chamber by chamber, with its painted gods and spells restored to their original colours. Every match takes place inside it.

The Bearer plays in VR with the only lamp. Step inside at true scale, raise the light to reveal murals and hieroglyphs, and handle interactive reconstructions that explain the history, building methods and mythology behind each scene. Every scene understood opens a sealed door. When the flock attacks, focus the lamp into a beam to fend off the monsters and survive.

The Flock plays on desktop as ba-birds, the human-headed souls of ancient Egyptian belief. Agile and fast in the dark, they swoop through shafts and side passages, but the light burns them. Hunt down the Bearer from the shadows, and whoever lands the final blow takes the lamp and becomes the new Bearer.

Play solo against an AI flock, or online with friends. Between matches, an in-game museum gathers everything you have discovered.

*Pitch:* An educational VR tomb reconstruction turned into the arena of an asymmetric hunt: the VR player has to study the real paintings to progress while desktop players, as ba-bird souls, try to steal the lamp.

## 33. The Last Updraft

**+1.20σ** · bge 90.16% · MiniLM 89.59% · v1 frontier void · closest Steam game: The Bridge to Yesterday (0.80)

Prior art: **a close game exists**. Two Swords already makes a two-rival life story into PvP. Two players take one childhood-friends-turned-rivals character each and fight three duels at different ages, and who wins each fight decides which of 8 endings you get. Lose It! (itch.io) also ties the story outcome to the result of a split-screen race. Nothing found has the glider racing, the exploration and puzzles on foot between races, the single-player rival who adapts, or the sisters setup. [Two Swords (itch.io, 2-player narrative fighting game)](https://milessupshur.itch.io/two-swords)
Coherence 4/5: The core works: race chapters with an ending decided by the versus result. Scope spreads across racing, on-foot exploration, puzzles and both single-player and versus modes.

*Tags:* Action, Adventure, PvP, Racing, Puzzle, Sports, Exploration, Emotional, Post-apocalyptic, Flight, 3D, Third Person, Female Protagonist, Split Screen

> Two estranged sisters, one last glider race across the ruined valley they grew up in. Play the story alone against your rival sibling, or split the screen with a friend and fight over every shortcut, memory and finish line in versus mode.

Years after the war emptied the valley, the old glider race returns for one final season. Ada and June used to fly it together. Now they barely speak, and both of them have entered.

Every chapter is a head-to-head race between the sisters, part sport, part argument. You launch from broken towers, ride the wind through collapsed bridges and overgrown factories, and fight for the faster line. Between races, each sister explores the valley on foot, finds old letters and photographs, and solves small puzzles that open new routes: a shortcut their father built, a thermal above the dam where they once crashed.

In single-player you choose a sister and race the other, whose flying changes with what you learn about her. In versus mode, two players take a sister each in split-screen or online, and the story's ending depends on who wins the final course. A competitive sports game about family, rivalry and finally saying sorry.

*Pitch:* A story-driven PvP sports game: the whole narrative is a head-to-head glider rivalry between two sisters, and when two players take a sister each, whoever wins the versus final decides how the story ends.

## 34. Spike of Peace

**+0.96σ** · bge 87.05% · MiniLM 81.93% · v1 frontier void · closest Steam game: The Spike Cross (0.79)

*Tags:* Action, Volleyball, Sports, 3D, Third Person, Physics, Difficult, Colorful, Cute, Emotional, Action Roguelike, Dwarves, Elves, Local Multiplayer

> No more battles. The elves and dwarves will settle their war with volleyball. Dive, spike and survive spell-filled rallies as a young elf who never wanted to fight.

Spike of Peace is a colourful third-person physics volleyball game, cute on the surface, difficult in the hands and emotional at heart. For a hundred years elves and dwarves fought over the valley; now every border is decided by a match on the sand.

You play as Lirra, a young elf who lost her brother in the last battle and now captains a village team nobody believes in. The campaign is an action roguelike road trip: each run brings random rivals, courts and blessings that change how the ball flies. Lose a match and the road starts again, but your friends grow closer every time.

Rallies are physics-driven and difficult. You control every jump, dive and spike, and dwarf teams hurl enchanted serves that burst into storms of bouncing orbs, so each point becomes a small bullet hell you survive with timing and nerve.

Between matches, quiet story scenes deal with friendship, old grudges and what peace really costs. Play solo, or bring a friend for split-screen two-on-two.

*Pitch:* A fantasy war replaced by a volleyball tournament: hard, physics-driven 3D rallies where enemy spells turn each point into a small bullet hell, built as an emotional action-roguelike road trip with split-screen 2v2.

## 35. Bert's Big Week

**+0.95σ** · bge 91.73% · MiniLM 73.76% · v1 hole void · closest Steam game: ZomB (0.78)

*Tags:* Pixel Graphics, 2D, Point & Click, Adventure, Strategy, Casual, Cute, Cartoony, Comedy, Zombies, Top-Down, Tower Defense

> The new mayor of a tiny mountain village has one week before the zombies arrive. Solve silly point-and-click puzzles by day, then click your way through the night defending the town you just about held together.

Bert's Big Week is a comedic pixel art adventure with a tower defense twist. Bert won the election in a village of forty people because nobody else ran, and on his first day the radio announces a zombie outbreak heading up the valley. Days play like a classic point-and-click adventure: explore the village, talk to its odd residents, collect strange items and combine them to solve puzzles, from convincing the baker to make cement bread to teaching the goat to guard the gate. Every solved problem becomes something useful for the night: a pie catapult, a scarecrow trap, a volunteer with a frying pan. When the sun sets, the view switches to a top-down map of the village. Place your defenses along the lanes, click on shuffling zombies to bonk them, and spend the coins they drop on quick upgrades while the waves grow sillier and bigger. Survive the week, keep everyone in one piece and uncover where the zombies came from.

*Pitch:* A classic comedy point-and-click adventure where every puzzle you solve by day becomes a defence for that night's clicker tower-defence siege by goofy zombies.

## 36. Home Field '98

**+0.93σ** · bge 90.75% · MiniLM 74.32% · v2 blend void · closest Steam game: Backyard Football '99 (0.79)

*Tags:* 1990's, Psychological Horror, 2D, Retro, Sports, Pixel Graphics, Horror, Casual, Football (American), Point & Click, Old School, Atmospheric

> Summer, 1998. June's backyard is the only field on the block, so every kid in the neighbourhood plays football at her house. They don't know it is haunted. Win cute retro football games by day, and face a point-and-click psychological horror by night.

Home Field looks like the 1990s sports games you played as a kid: chunky top-down pixel art, cheerful music and simple controls that let anyone pick up and play football. Choose your team from the kids on your street, each with a nickname, a favourite play and a secret, and score touchdowns between the swing set and the garden shed. A friend can take the rival team in local versus play.

But June lives in the house beside the field, and it is not empty. As the summer goes on, the matches change. Players vanish from the roster, the crowd stops cheering and the windows watch every down.

When the others go home, explore the house in point-and-click scenes. Talk to parents who will not answer, search the attic and basement, and help June balance a normal childhood with the horrors waiting upstairs.

Winning and losing both move the story forward. A perfect season opens some doors; a bad loss opens others. Play through a summer of friendship, rivalry and dread, and decide which memories are worth keeping.

*Pitch:* A cute 1990s kids' football game where the field is the backyard of the heroine's haunted house: the matches and the point-and-click horror affect each other, and wins and losses both move the story forward.

## 37. Mallet Marshal

**+0.87σ** · bge 75.83% · MiniLM 86.66% · v1 hole void · closest Steam game: Toy Tactics (0.82)

*Tags:* Casual, Strategy, VR, Physics, Simulation, Real Time Tactics, Comedy, Minimalist, Tactical, Intentionally Awkward Controls, Score Attack, Action, 3D

> Command a tiny army with nothing but a mallet. Tap to march, knock twice to charge, and whack the moles and goblins that pop out of the battlefield, one clumsy swing at a time.

Mallet Marshal is a casual VR physics strategy game. A tiny army lives in a field full of holes, and you are the giant with the mallet.

Your soldiers are brave but not very bright. Tap one and it marches where it faces, knock it twice and it charges, knock the ground and the whole squad digs in. Enemy troops march in from the far side, while moles, beetles and burrowing goblins pop up from the holes in between, and every one of them can be whacked too.

The trick is choosing what to hit. Each swing either commands a unit or fights an enemy, never both, so every second is a quick tactical decision. Physics does the rest: soldiers tumble, shields bounce, and a wild swing can send your own captain flying.

Minimalist toy-box visuals, short rounds, a score attack ladder and a two-handed hard mode keep the mallet busy.

*Pitch:* A real-time tactics game in VR where your only input is a clumsy mallet: every swing either gives an order to your tiny soldiers or whacks an enemy popping out of the holes, never both.

## 38. Ashgrove After Dark

**+0.86σ** · bge 71.49% · MiniLM 88.82% · v1 frontier void · closest Steam game: Apoc Wilds (0.81)

*Tags:* Simulation, Exploration, Adventure, Casual, 3D, Strategy, PvP, Turn-Based Combat, Creature Collector, Psychological Horror, First-Person, Turn-Based Tactics, Puzzle, Atmospheric

> Run a small shelter for strange creatures at the edge of an empty town that rearranges itself every night. Explore its streets in first person, take in what you find, and send your creatures into turn-based battles against the things that follow you back.

The shelter on Ashgrove Lane was cheap for a reason. The town beyond the gate has been empty for years, and every night its streets, shops and apartments quietly swap places. The creatures that wander out of it are not in any book.

By day you run the shelter: cook feed, build pens, clean, heal and befriend residents like the lantern-cat, the paper fox and the slow, enormous moss-hound. By dusk you walk into town with a flashlight, mapping streets that will be gone tomorrow, solving small puzzles to open locked buildings, and searching for new creatures. Other keepers can join your town online to explore with you, or face your creatures in turn-based PvP duels.

Some things in the town do not want to be found. When they catch up with you, your creatures fight in turn-based battles where trust, mood and the light you carry matter as much as strength. A cozy management sim slowly turning into something stranger.

*Pitch:* A cozy creature-shelter management sim joined to first-person exploration of a town that rebuilds itself every night, where the creatures you care for fight in turn-based battles that depend on their trust and mood, against the town's horrors or against other keepers online.

## 39. Night Choir

**+0.84σ** · bge 89.94% · MiniLM 69.60% · v1 frontier void · closest Steam game: Motorcycle Night Ride (0.79)

*Tags:* Adventure, Action, Racing, 3D, Story Rich, Atmospheric, Exploration, Third Person, Action-Adventure, Music, Surreal, VR

> Ride a motorbike through the dreams of a sleeping town. Race along roads built by music, fight off the riders of its nightmares, and piece together the story of the night everyone stopped waking up.

Night Choir is a third-person racing adventure set inside dreams. One night every resident of a small coastal town fell asleep and never woke. You arrive on an old motorbike and discover you can ride into their dreams, where roads are built from the music each sleeper remembers. Race along winding melodies over oceans, through ruined cathedrals and across endless rooftops, keeping your speed in time with the song to stop the road from collapsing. In the darker dreams, shadow riders hunt you down, and you fight back at full speed, shoving them off the road and breaking their chains before they reach the dreamer. Off the bike, explore each dream on foot, talk to the dreamers and find the memories that explain why they cannot wake. Each rescued sleeper adds a new instrument to your bike's radio and opens new roads. The whole journey can be played on a flat screen or in VR, and a split-screen mode lets two friends race the finished dream roads head to head. Atmospheric, musical and story-rich, it is a racing game you play for the journey.

*Pitch:* A story-driven racing adventure where the tracks are built from music inside sleepers' dreams. You keep in time with the song so the road holds, fight nightmare riders at speed, and explore on foot to wake the town.

## 40. Wren and Clover

**+0.84σ** · bge 73.24% · MiniLM 86.86% · v1 frontier void · closest Steam game: BRASSWIND BRIGADE (0.82)

*Tags:* Casual, Cute, Relaxing, Adventure, RPG, 3D, Fantasy, Female Protagonist, Tanks, Military, VR, Exploration

> A young noble girl and her little tank must prepare their tiny country for war. Recruit knights, archers and cooks, and get everyone ready in time.

Her name is Wren. Her tank is called Clover. Clover has never fired a shot; her grandfather swapped the cannon for a watering can. Roll across flower meadows, snowy passes and sandy beaches. Repair bridges, clear roads and rebuild windmills. Visit castles, farms and fishing villages, recruit knights, archers and cooks, and practise archery and horse riding with the old general. Every friend you make joins the cause with a skill of their own, and every upgrade makes Clover faster, stronger and a little bit cuter. Explore a big open countryside at your own speed and enjoy the beautiful scenery. No stress, no timers, just fun. Supports VR headsets and gamepads, and can also be played on a flat screen with a mouse and keyboard. When summer ends, all your preparation, and all the friends you made on both sides of the border, decide whether the war happens at all.

*Pitch:* A cozy, no-combat 3D adventure RPG, playable in VR, where a noble girl and her repurposed tank get a tiny kingdom ready for a war through exploring, repairing and making friends, and may stop it from happening at all.

## 41. Nightrotor

**+0.83σ** · bge 95.28% · MiniLM 54.39% · v2 blend void · closest Steam game: The Darkest Island (0.78)

*Tags:* Action, Adventure, Horror, 1990's, Action-Adventure, Atmospheric, Retro, Flight, Shooter, Dark, Survival Horror, 3D

> A retro 1990s action-adventure: pilot a deadly helicopter gunship into the darkness over a haunted island, battle the evil that waits below and complete dangerous night missions, where getting in is easy and getting out is hell.

Inspired by the gunship flight games and survival horror classics of the 1990s, this new adventure puts our hero in the pilot's seat. Winter, 1996: command has lost contact with its island radar station. The island is pitch dark, the radio hisses with voices that should not be there, and the old mansion on its cliffs has every light burning.

Take off from a lonely carrier, fly low along cliffs and coves, and battle possessed soldiers, crawling things and flying shapes with your cannon, rockets and searchlight. Rescue survivors, escort supply boats and destroy the stone totems that keep the darkness alive.

Some objectives cannot be reached from the cockpit. Set down in a courtyard or on a rooftop and the game shifts to tense on-foot exploration of the mansion, where each room you clear reveals a new landing zone or a new piece of the mystery. Fuel, ammunition and armour are always scarce, so every sortie is a gamble. Chunky polygon graphics, arcade-friendly flight handling and a droning synth score complete the retro action horror experience.

*Pitch:* A 1990s-style gunship action game whose mission map is a haunted-house survival horror: the island is fought from the air, the mansion is cleared on foot, and each one opens the way into the other.

## 42. Lena and the Endless Line

**+0.83σ** · bge 74.10% · MiniLM 85.98% · v2 blend void · closest Steam game: Cursed Shorts (0.81)

*Tags:* Casual, 2D, Adventure, Minigames, Surreal, Female Protagonist, Trains, Arcade, Colorful, Simulation, Anime, Exploration

> A collection of dozens of subway-flavoured microgames! Lena fell asleep on the U7 and now the ride never ends. Travel famous lines from Berlin to New York in a dream where every station is a quick, strange challenge and every passenger is one of the oddest characters you will ever meet.

Every evening Lena takes the U7 home through Berlin. Tonight she dozed off between stations, and when the doors opened the platform was made of jelly, the conductor was a heron and the network map had grown lines to cities all over the world.

Ride one famous route after another, from Berlin and Paris to New York and Tokyo, each recreated in bright anime-style 2D with its real station names and its own dream twist. At every stop the doors open onto a microgame lasting a few seconds: hold the handrail through a sudden curve, stamp a ticket for a ghost, help a tourist find the exit or catch a train before it melts.

Clear enough stops to reach the end of the line and unlock the next city. Between rides, explore the dream carriages, chat with the strange regulars and collect souvenirs from every station. Some of them know the way back to the waking world.

A cheerful, surreal journey for anyone who has ever fallen asleep on the train.

*Pitch:* A cheerful microgame collection built on real, famous subway lines: every station stop is a surreal few-second microgame in a commuter's never-ending dream, not another subway-anomaly horror game.

## 43. The Hill Remembers

**+0.81σ** · bge 86.00% · MiniLM 73.75% · v1 hole void · closest Steam game: Next Player (0.79)

*Tags:* Platformer, Action, 3D, Atmospheric, Physics, Casual, Horror, Psychological Horror, Post-apocalyptic, 3D Platformer, Stylized, Linear

> A psychological horror platformer about a child's red ball rolling down the endless hill of a town emptied by a catastrophe. Bounce and steer through ash-grey streets, and find out who keeps carrying you back to the top.

The Hill Remembers is an atmospheric 3D physics platformer about a red rubber ball that cannot stop rolling. The town on the hill was emptied in a single night when the sky turned grey, and every street leads down. Steer through yards, staircases, playgrounds and flooded basements, bounce off cars and fences, and use slopes and ramps to clear gaps and reach hidden paths. It begins almost cozy, the sun low and the streets quiet, but each time you reach the bottom, something carries you back to the top, and the town has changed. Doors are open that were closed. Toys have moved. A shape stands in the window of the house at the end of the road. The horror is psychological and slow, built from repetition, silence and small wrong details in a stylized, soft world. Runs are short and linear, controls are just steering and a bounce, and the story is told entirely through what you roll past.

*Pitch:* A cozy roll-down-the-hill physics toy that turns into a looping psychological horror story: each time you roll down, the post-apocalyptic town at the bottom has changed in small, wrong ways.

## 44. Keeper of the Snowbound Keep

**+0.81σ** · bge 71.07% · MiniLM 86.85% · v1 frontier void · closest Steam game: Medieval Thieves Academy (0.81)

*Tags:* Casual, Simulation, 3D, First-Person, Realistic, Co-op, Strategy, Medieval, Hidden Object, Online Co-Op, Co-op Campaign, Family Friendly

> The siege is over and the snow is still falling. Clean up the aftermath, gather scattered arrows and lost belongings, patch the walls and get the castle ready for the next attack, alone or with friends.

High in the mountains stands a realistic medieval castle, cut off by snow. All winter it held out against a siege, and now the enemy has gone, leaving broken carts, scattered arrows and frozen mud behind. Your grandfather was the castle's caretaker before you. Now the job is yours.

Work in first person through the realistic, snowbound keep. Shovel snow off the battlements, pull arrows from the gates, rebuild the walls stone by stone, and rescue the frightened horses, goats and chickens still hiding in the barn. Search the drifts for the belongings the villagers lost while sheltering inside, and sort the potions and spellbooks the old wizard left scattered across his study.

Then plan your season. Decide which repairs come first, where to store firewood and how to stock the cellar before the spring thaw opens the pass again, and whoever is waiting on the other side.

Play alone at a calm pace or bring up to three friends in online co-op to split the work. No combat and no blood, just the quiet satisfaction of turning a battered castle back into a home.

*Pitch:* A nonviolent, realistic first-person co-op game set after a medieval siege: you don't fight the war, you clean up after it, searching for lost belongings, rescuing animals and rebuilding a snowbound castle.

## 45. A Long Bounce Home

**+0.74σ** · bge 75.77% · MiniLM 79.80% · v1 frontier void · closest Steam game: One More Slime (0.82)

*Tags:* Archery, Action Roguelike, Casual, Action, Underground, Colorful, Third Person, Aliens, Cartoony, Physics, Cute, 3D

> Play as a squishy alien slime with a tiny bow, stranded in a colorful forest after a meteorite crash. Bounce, stretch and shoot glowing arrows through bright glades and dark underground caves to collect the fragments you need to fly home.

A meteorite has crashed into a strange, colorful forest on Earth. Riding inside was Blip, a small alien slime with a tiny bow, and its little ship is now a hundred glowing fragments scattered across glades, rivers and deep caves.

Play in third person as a squishy alien slime with a tiny bow. Bounce off mushrooms, stretch across gaps, roll down hills and stick to walls with physics-driven movement that feels great to master. Forest critters do not appreciate visitors, so fire glowing arrows to pop beetles, scare off owls and light up the dark underground caves where the biggest fragments landed.

Every trip underground is different. Tunnels shift, new creatures appear and power-ups like split arrows, double bounce or a sticky shell change how each run plays. Bring fragments back to the crash site to rebuild your ship piece by piece and unlock new hats, colors and abilities for your slime.

Short, colorful arcade runs, gentle atmosphere and a cute hero make it easy to pick up, while hidden paths and tricky bosses reward players who want to explore every corner.

*Pitch:* A casual 3D action roguelike starring a stretchy physics slime that fights with a bow: bouncy movement and glowing arrows that light up procedurally shifting caves, in place of the usual top-down twin-stick shooting.

## 46. Dumplings After Dark

**+0.71σ** · bge 77.09% · MiniLM 76.83% · v1 frontier void · closest Steam game: Deadlivery Night (0.80)

*Tags:* 2D, Story Rich, Anime, Casual, Management, Cooking, Crime, Zombies, Top-Down, Crafting, Co-op, Female Protagonist

> The city fell to the dead, and the gangs now run what is left. Keep your dumpling bar open, pay for protection, and feed the survivors.

Mio inherited the dumpling bar from her grandfather the week the city fell. Now the dead wander the streets, the Kurose gang controls the harbour and the night market, and rival gangs fight over the blocks around her shop. Every week the gang comes to collect, and every week you find a way to pay. By night you sneak through the ruined city in top-down 2D, scavenging flour, cabbage and gas canisters, and fighting off the infected with kitchen knives, frying pans and anything else you can find. By day you open the doors, cook for the survivors and trade dumplings for bullets, medicine and information. Regulars come back day after day, each with a story to tell and a skill to offer. Unlock new recipes, upgrade your kitchen and expand the bar. A second player can join in local co-op as the bar's bodyguard. Several endings depend on which gang you side with, and on whether you can keep the last restaurant in the city open.

*Pitch:* A top-down 2D anime restaurant-management and survival game in which you run the last dumpling bar in a zombie-overrun city held by rival gangs: scavenge by night, cook and trade by day, and pay protection to survive.

## 47. Pip and the Wandering Wonder Circus

**+0.71σ** · bge 71.26% · MiniLM 81.54% · v1 hole void · closest Steam game: Puzzles Magic (0.81)

*Tags:* 2D, RPG, Casual, Puzzle, Adventure, Colorful, JRPG, Fantasy, Story Rich, Action, Anime, Atmospheric

> A colorful 2D puzzle RPG about a traveling circus of misfit mages. Roll a magic ball through puzzle rooms to gather colored stars, battle monsters in quick action fights, and put on shows to bring wonder back to a gloomy, haunted kingdom.

Ever since the Grey Duke banned laughter, the towns of Pelloria have gone quiet, colorless and a little bit eerie. Then a creaky wagon rolls into the capital: the Wandering Wonder Circus, a small troupe of misfit mages led by Pip, a young juggler whose enchanted ball can grow, shrink and glow. Behind the painted smiles, every member of the troupe is hiding a sad secret.

Travel from town to town, explore candlelit forests, flooded mines and a gloomy gothic castle, and help the locals with their problems. Every area is full of puzzle rooms: roll the ball through mazes so it pulls in matching colored stars and leaves the cursed ones behind, bounce it off mirrors and bumpers, and use each performer's magic to reach new places. Monsters lurking along the road are fought in short, snappy action battles where you swap between party members on the fly.

In every town, put on a show. Pick acts, arrange the stage and time your spells to bring color back to the streets and recruit new friends to the troupe.

A warm, funny story about friendship, with bright anime-style art and plenty of secrets to find.

*Pitch:* A story-rich 2D JRPG where the party is a traveling circus. Exploration is ball-physics puzzles built around the juggler's enchanted ball, and each town's arc ends in a staged magic show that wins it back.

## 48. The Silent Score

**+0.70σ** · bge 81.30% · MiniLM 71.93% · v1 hole void · closest Steam game: Codename Incubus (0.80)

*Tags:* Action-Adventure, 2D, Exploration, Atmospheric, Emotional, Bullet Hell, Story Rich, Colorful, Top-Down, Music, Soundtrack, Psychedelic

> A musician who has lost his hearing returns to the island where he wrote his first song. Explore its silent shores, recover the melodies scattered across it, and face the bosses that guard each one in bullet-hell duels set to music.

Teo wrote the songs everyone hummed, until the day he could no longer hear them. He returns to the island where he grew up and finds it silent. Explore the colourful island in top-down 2D, from tide pools and lighthouse cliffs to the overgrown concert hall at its heart. Each region hides a fragment of a lost song, and each fragment is guarded by a creature born of Teo's memories: an old teacher, a rival, a love he left behind. Dodge, dash and strike back in time with the music. Learn to dodge by seeing the beat before you can hear it. Recover a song and colour floods back into that part of the island in bright, psychedelic waves. The soundtrack grows richer with every melody you recover. A short, emotional action-adventure about grief, art and learning to listen again.

*Pitch:* An emotional top-down exploration game with bullet-hell boss duels whose patterns follow music the deaf hero cannot hear, so the player learns to read rhythm visually while each recovered song brings colour and sound back to the island.

## 49. Kit of Cornertown

**+0.70σ** · bge 71.01% · MiniLM 81.35% · v1 hole void · closest Steam game: Yellow Terminal (0.82)

*Tags:* Action, Simulation, Life Sim, Adventure, Multiple Endings, Idler, Casual, Shooter, Third-Person Shooter, Desktop Companion, Management, Wholesome

> A desktop companion who lives on your screen and runs missions in her own tiny shooter city while you work. Click to send her out, buy her new cars, and talk to her: she remembers what you said.

Kit lives in a tiny city in the corner of your screen, and she is the only hero it has. She talks to you between missions, remembers what you said last week, and writes you a letter when you are away. When the clockwork gangs raid the town, she heads out on missions, and you can watch her run and shoot through the streets in tiny firefights full of bullets and gold. When you want a break, click to take control and play a mission yourself. Every mission pays out in coins for new cars, weapons, clothes and furniture, and the town slowly comes back to life as shops reopen and neighbors return. Off duty she sleeps, cooks and tinkers with her car while you work, study or browse. How you treat her, and which jobs you send her on, decide which of several endings her story reaches, from settling down as the town mechanic to setting off to find where the clockwork gangs come from. Built to run lightly in the background, it is a companion first and a shooter whenever you want one.

*Pitch:* A desktop companion who has her own little third-person shooter world: she idles through missions in a tiny city while you work, remembers your conversations, and you can take over any mission yourself, with several life-sim endings.

## 50. Colony Call

**+0.67σ** · bge 72.70% · MiniLM 78.00% · v1 frontier void · closest Steam game: Bat Flapper (0.82)

*Tags:* Action, Family Friendly, Atmospheric, Top-Down, 3D, Exploration, Arcade, Minimalist, Stylized, Colorful, Casual, Local Co-Op

> Bats see with sound. In this family arcade adventure, every chirp lights up the dark caves for a moment, and every lost bat you rescue adds its echo to yours.

A rockfall has scattered the colony through the caves below the old forest. Two young bats, one for each player, are sent to bring everyone home. The caves are pitch black until you chirp, and each call outlines walls and creatures in glowing echoes before the darkness returns. Swoop through twisting tunnels, snap up moths for energy, and dart past spiders and owls that hunt by listening. Every call helps you see, but the hunters hear it too, so choose when to chirp and when to fly blind. Each cavern is a quick action run with lost bats to find; free them and they follow your flight path, adding their own echoes to light the way, so the bigger your colony grows the more of the cave you can see. Playing solo, your sibling bat follows your lead and echoes your calls; with a friend on the same screen, the two of you can split up, and two overlapping calls reveal far more than one. Simple top-down controls and gentle checkpoints make it a family game, while perfect runs reward score chasers. Gather every bat and lead the colony out at dusk.

*Pitch:* A family couch co-op arcade game played almost blind: you see the caves only through echolocation, and every rescued bat adds its own echo, so the colony you rescue is also how you see.

## 51. Masha's Icy Way Home

**+0.63σ** · bge 75.79% · MiniLM 72.83% · v1 hole void · closest Steam game: Adelaide: A Tiny Adventure (0.81)

*Tags:* Cute, Casual, Pixel Graphics, 2D, Psychological Horror, Arcade, Atmospheric, Action, Adventure, Retro, Colorful, Platformer

> Walk a little girl home from school across a small Siberian town in the winter of 2003. Slip, slide and score your way down frozen sidewalks in a cute pixel arcade game, and notice how the town changes a little more every evening.

Every evening Masha walks home from school along the same frozen street: past the bakery, the bus stop, the playground and the long grey apartment blocks. The sidewalk is pure ice, and getting home in one piece is a game.

Each walk is a short arcade run. Shuffle, slide and balance across the ice, hop over puddles and snowbanks, grab coins for sweets at the kiosk and chain near-misses for a higher score. The pixel art is bright and cozy, the music is cheerful, and the cats on the stairwell are very cute. Some evenings she gets home safe and warm; some evenings she takes a tumble and has to get up again.

But the walk home is never quite the same. A streetlight that was not there yesterday. A neighbour who waves from a window of an empty building. A song on the radio that knows her name. As the days pass, the town quietly rearranges itself, and the shortest way home starts leading somewhere else. A cozy retro arcade game with a slow, creeping psychological horror story hidden in the snow.

*Pitch:* A cute score-attack arcade game about slipping across icy sidewalks, played as a child's daily walk home in a 2003 Siberian town, where the route itself slowly becomes a psychological horror story.

## 52. Beep Battle

**+0.61σ** · bge 77.94% · MiniLM 68.85% · v1 frontier void · closest Steam game: Metal Detector Simulator (0.84)

*Tags:* 3D, Casual, Simulation, Strategy, Top-Down, First-Person, Roguelike, Colorful, Cute, PvP, Party Game, Relaxing

> A competitive metal detecting simulation for one to four players. Plan routes on a top-down tide map, then sweep a 3D beach in first person and dig for the best finds while drafting sneaky tools between rounds.

Beep Battle is a casual treasure-hunting simulation where friends and rivals compete on the same stretch of sand. Each round generates a fresh 3D beach hiding coins, lost rings, shipwreck relics, junk and the odd crab. Study the top-down tide map to plan your route, then drop into first person: sweep the coil, read the signal strength, and dig before someone else gets there. The water rises during the round, so anything you leave behind gets buried again. Between rounds, spend your haul in a roguelike shop and draft upgrades and tricks: wider coils, a pinpointer, decoy signals, sandcastles that block a rival's path, a seagull that steals someone's last find. After five rounds, the most valuable collection wins the beach. Play solo against cheeky computer rivals for a relaxed run, or invite friends online for loud, silly matches. Short sessions, bright visuals and simple controls make it an easy pick-up game for families and groups.

*Pitch:* Metal detecting as a competitive roguelike party game: a top-down planning phase leads into a first-person dig on a shared beach, with tools drafted between rounds to outdig or sabotage your rivals.

## 53. Recall 1916

**+0.58σ** · bge 79.06% · MiniLM 65.62% · v1 hole void · closest Steam game: Wargame Construction Set (0.80)

*Tags:* Casual, Simulation, Strategy, Minimalist, 2D, Pixel Graphics, War, Abstract, VR, Relaxing, Education, Wargame, World War I

> Train your memory and your eyes like a WWI scout: short pattern drills, spot-the-difference maps and memory duels against other players online.

This calm, abstract game about war, memory and attention is inspired by real training methods used in the First World War. The battlefield is shown for three seconds, then hidden. Memorize a pattern of trenches, wire and craters on a small pixel-art grid, then rebuild it from memory. Each level is a small battle map drawn in coloured squares. Read a sequence of lamp flashes and repeat it back. Remember where every soldier stood. In VR, the battle map lies on a wooden field table in front of you. Climb the ranks from private to general as your memory improves, and learn about history while training your brain. Challenge other players online in quick memory duels. Simple pixel graphics and a calm soundtrack. No violence, no gore, just focus, patience and a steady eye.

*Pitch:* A non-violent, minimalist memory and attention trainer built on WWI scouting drills: rebuild hidden pixel battle maps, repeat lamp signals and duel other players online, on a flat screen or on a VR field table.

## 54. Camp Larkhollow

**+0.57σ** · bge 90.33% · MiniLM 46.76% · v1 frontier void · closest Steam game: Fantasy Camp Builder (0.79)

*Tags:* Casual, Simulation, Strategy, 3D, Top-Down, RPG, Adventure, Point & Click, Top-Down Shooter, Shoot 'Em Up, Incremental, Fantasy

> A casual point-and-click camp simulation by day, a top-down shoot 'em up by night. Run a fantasy summer camp for young wizards, grow it with incremental upgrades, level up your counselors, and grab a wand after dark to blast mischief spirits away.

Every summer, families from across the kingdom send their children to Camp Larkhollow to learn a little magic and a lot about each other. This year, you are the new camp director.

Days are for planning. From a top-down view of the camp, point and click to schedule lessons, assign counselors, stock the kitchen and decide who goes canoeing. A good plan keeps campers happy; a bad one ends with a frog outbreak in the dining hall.

Evenings are for stories. Sit by the campfire, talk with campers and staff, and help a shy kid find her spell or settle a rivalry between cabins.

Nights are for defense. Mischief spirits drift out of the forest, and the game becomes a light top-down shoot 'em up: grab your wand, sweep the paths and blast glowing swarms back into the trees before they reach the cabins.

Every calm night earns camp points that feed a gentle incremental climb: new activities, bigger cabins, better wands and level-ups for your counselors. By summer's end, Larkhollow should be the happiest camp in the realm.

*Pitch:* A camp-management sim where each day has three parts: point-and-click scheduling, campfire stories and a top-down wand shoot 'em up at night, all feeding one incremental upgrade loop.

## 55. Cartridge Cartel '91

**+0.56σ** · bge 68.80% · MiniLM 74.03% · v1 hole void · closest Steam game: Mall Rivals (0.82)

*Tags:* Simulation, Action, PvP, Strategy, Co-op, Online Co-Op, VR, Retro, Comedy, Arcade, PvE, 1990's, Satire

> Run a game company in the 1990s console wars. Design cartridges, rig the arcades, steal rivals' mascots and squeeze players for every coin, in a satirical PvP business sim for up to four friends, in VR or on screen, or team up in co-op to survive the crash.

It is 1991, home consoles are exploding and four tiny studios want to rule the shelves. Each player runs one of them, on a monitor or from a cramped virtual office in VR. Hire developers, pick genres from fighting games to flight sims, gamble on the coming virtual reality craze, build cartridges in a simple drag-and-drop design screen, and then actually play your own games in short arcade tests to see if they are any good.

The real competition is dirty. Bribe magazine reviewers, sabotage a rival's launch party, copy their hit with a cheaper knockoff, and invent ever more outrageous ways to make players pay: secret codes sold by phone, collectible cartridges, exclusive colour variants. At every trade show, rival bosses settle scores in head-to-head arcade duels using each other's games. Each season the market reacts, and greedy decisions can backfire spectacularly.

Play competitive PvP matches online or on the same screen, or join forces in co-op campaigns against ruthless AI publishers. Loud, funny and painfully familiar, it is a business simulation about how video games learned to sell themselves.

*Pitch:* A satirical multiplayer business sim of the 1990s console wars in which you actually play the arcade games your studio ships, settle rivalries in head-to-head duels, and can run your studio from a VR office.

## 56. The Long Patrol

**+0.55σ** · bge 67.11% · MiniLM 74.91% · v1 hole void · closest Steam game: Joey's Nightmare II (0.82)

*Tags:* Card Battler, Horror, Turn-Based Tactics, Psychological Horror, 1980s, 2D, Turn-Based Strategy, Military, Surreal, Turn-Based, Deckbuilding, Pixel Graphics, Roguelite

> A 1988 Vietnam veteran relives the war in his nightmares, one card at a time. A retro pixel-art horror deckbuilder.

Ohio, 1988. Every night, Frank Doyle is back in Vietnam, and the jungle has changed: radio static that speaks his name, a patrol that never ends, shapes in the elephant grass that are not quite soldiers. In this retro pixel-art roguelite deckbuilder you fight through Frank's nightmares one night at a time. Command your old squad as a hand of cards: point man, radio operator, medic and machine gunner, each with their own deck. Battles play like a tiny tactical wargame: position your squad, call in support and hold the line until dawn. Fear is a resource: let it climb too high and your squad starts to break. By day, the waking world is a small life of its own: the veterans' hall, a phone call to your daughter, a late movie on cable, and each choice reshapes the deck you will take back into the dark. Survive thirty nights, piece together what really happened on that last patrol, and decide what Frank needs to let go of.

*Pitch:* A retro roguelite card battler set inside a Vietnam veteran's recurring nightmares in 1988, where your old squad is your hand of cards and each night plays out as a small tactical wargame.

## 57. Wallnut Winter

**+0.55σ** · bge 64.26% · MiniLM 77.12% · v1 frontier void · closest Steam game: Jery Mice vs Cats: Home Invasion (0.82)

*Tags:* Action, Puzzle, Family Friendly, Atmospheric, Adventure, First-Person, Surreal, Abstract, Co-op, Online Co-Op, Local Co-Op, Animals

> A surreal first-person action puzzle game about rodents racing through a snowed-in house that turns abstract after dark. Play as a mouse, a squirrel, a beaver or a hamster, alone, in co-op or head to head.

Snow has buried the old house on the hill, and the four rodents sheltering in its walls, from the house mouse to a beaver who wandered in from the frozen pond, are cut off from their winter stores. After dark the house turns surreal: rooms float apart, stairs fold over and the snow falls upward. Each rodent has its own talent. The mouse squeezes through tiny gaps, the squirrel climbs and leaps, the beaver gnaws and builds bridges, and the hamster rolls in its ball to power old machines. Puzzles mix all four: chew a beam into a ramp, roll the hamster across it, then send the mouse through the gap it reveals. Every room is also a race against the dawn, because the house snaps back to normal at sunrise and anything left behind is lost. Play the story alone and switch between the four at any time, or invite up to three friends to each take a rodent in online or local co-op. Once a room is solved, unlock it in race mode and see who can reach the exit first. Gather the stores and find out what keeps the house dreaming.

*Pitch:* A first-person, rodent's-eye co-op puzzle game where four species with different abilities solve a snowbound house that becomes abstract each night, and every solved room turns into a head-to-head race.

## 58. Bean to Cup

**+0.46σ** · bge 80.21% · MiniLM 53.99% · v1 frontier void · closest Steam game: Coffee Beans (0.80)

*Tags:* Casual, Action, 3D, Colorful, Third Person, Relaxing, Fantasy, Adventure, Physics, Stylized, Education, Open World

> Roll, bounce and race as a single coffee bean across an open fantasy storybook world, from mountain farm to steaming cup. A colorful third-person physics adventure that quietly teaches how real coffee is grown and brewed.

Every cup of coffee starts as a cherry on a mountainside. This one starts with you: a small, stubborn bean named Arabel who wants to see the world.

Roll through a bright, open 3D fantasy world in third person. Bounce down terraced hills, ride drying racks like slides, tumble through a spinning roaster and slip past grinders that would love to make you powder. The physics are soft and playful, so every fall is a chance to try a new route, and quick reflexes help you dodge hungry birds and rolling barrels.

Each connected region is a step in coffee's real journey: picking, washing, sun-drying, sorting, shipping, roasting and brewing. Friendly farm spirits and a sleepy café cat explain what is happening and why, so you learn more about your morning cup than most baristas ever do.

Wander freely, collect flavor notes hidden off the beaten path, and unlock new bean skins. When you want a challenge, race other players' beans online through bouncy obstacle courses.

Relaxing, colorful and full of little discoveries, it is a big adventure for a very small bean.

*Pitch:* An open-world physics adventure in third person where you play the coffee bean itself, and each region you roll through is a real step from farm to cup, which makes it an educational game without any quiz screens.

## 59. Pell's Long Winter

**+0.43σ** · bge 55.54% · MiniLM 76.50% · v1 frontier void · closest Steam game: Rat Hunt (0.83)

*Tags:* Atmospheric, Choices Matter, 2D, Casual, Action, Top-Down, Family Friendly, Colorful, Arcade, Stylized, Animals, Multiple Endings

> Play as a rat in an atmospheric 2D adventure where your choices matter and every night is a race against time. Bring food home before dawn and decide who you can trust.

Under the floorboards of a sleepy town, a rat family is counting the nights until spring. Each night you slip out as Pell, the eldest pup, with one job: bring food home before the sun comes up. Every outing is a tense little dash through the dark. Scurry between shadows, climb drainpipes and dart away from cats, owls and brooms. And every night asks something of you: share your find with the hungry mice next door, or keep it for your siblings? Take the safe road past the church, or risk the busy market for a bigger prize? Trust the sly crow who offers a shortcut, or the old sewer rat who never smiles? Each decision opens or closes paths through town, turns strangers into friends or rivals, and changes which of your family's stories plays out by the end of winter. Seasons turn the town around you: snow hides the trails, thaw floods the drains, and the people upstairs start setting traps. Gentle controls, soft hand-painted colors and no harsh failure make it welcoming for younger players, while many endings reward anyone who wants to see every path.

*Pitch:* A family-friendly, choices-matter story told through short timed foraging runs: each night is an arcade dash against the dawn, and what you do with the food decides your rat family's winter and its ending.

## 60. Supper at the River of Night

**+0.43σ** · bge 58.08% · MiniLM 73.93% · v1 hole void · closest Steam game: Dungeon Cooking (0.82)

*Tags:* Strategy, Casual, 2D, RPG, Story Rich, Dark Fantasy, Atmospheric, Card Game, Visual Novel, Dark Humor, Cooking, Time Management

> Cook the last meal for every soul crossing into the afterlife. Draw ingredient cards, listen to the stories of the newly dead, meet the underworld's quotas, and serve the dish that decides where they go next.

At the edge of the River of Night stands a small, crooked inn, and every soul must eat there before crossing. You are its new cook, bound to the stove by a contract you do not remember signing, and the underworld's management expects results.

Each night a handful of guests arrive: a greedy merchant, a knight who died of embarrassment, a witch who insists she is only visiting. Talk with them in short visual novel scenes, learn what they regret and what they loved, then draw ingredient cards from a pantry stocked with memories, spices and strange things from the river.

Service is short and tense. Combine cards into dishes before the candles burn down and the ferryman's bell rings. A meal that matches a soul's story sends them gently onward; a careless one sends them somewhere much worse. Between nights, plan the week turn by turn, balancing a shrinking pantry, the inn's debts and the quarterly soul quotas set by a very polite demon accountant.

Unlock darker recipes, upgrade the kitchen and uncover how you ended up here. Grim, funny and quietly moving, every ending is cooked by your hand.

*Pitch:* A card-based cooking game where each dish is a judgment: you learn a dead soul's story in visual-novel scenes and then build the final meal that decides where they go, while an underworld bureaucracy sets quotas you have to meet.

## 61. Sprue Arena

**+0.40σ** · bge 78.70% · MiniLM 50.94% · v1 frontier void · closest Steam game: Plamo Kits (0.80)

*Tags:* Action, Casual, 3D, Top-Down, Arcade, PvE, Simulation, Strategy, Mechs, Shooter, Relaxing, Hobby Sim, Dinosaurs, Online Co-Op

> Snap together a dinosaur model kit, paint it, then drop it onto the table and blast waves of wind-up invaders in casual top-down co-op.

Sprue Arena is a casual 3D action game in two halves: a relaxing hobby workbench and a fast top-down battle table.

At the bench you snap parts from plastic runners and plan your build like a strategy puzzle with a limited budget of parts. Mix a raptor frame with a triceratops shield head and a rocket tail, paint your mechanical dinosaur, and test it on the cutting mat.

Then you drop it onto the table. Desks, shelves and living room floors become PvE battlefields where waves of wind-up invaders pour out of toy boxes. Stomp, dodge and shoot in arcade top-down combat, grab spare parts to repair mid-fight, and clear the wave to unlock new kits.

Play solo or bring up to three friends in online co-op, each with their own build. Combine roles, revive teammates and chase high scores on daily tables. Short rounds, deep customisation and no pressure between battles make it easy to pick up for one more build.

*Pitch:* A relaxing model-kit hobby sim and an arcade top-down co-op shooter in one: the mechanical dinosaur you snap off the sprue and paint at the bench is the unit you then fight with against waves of wind-up toys.

## 62. Iron Lullaby

**+0.22σ** · bge 35.91% · MiniLM 77.58% · v1 hole void · closest Steam game: Haxrail (0.83)

*Tags:* 2D, Choices Matter, Roguelite, Choose Your Own Adventure, Story Rich, Visual Novel, Action, Multiple Endings, Twin Stick Shooter, Robots, War, Emotional, Bullet Hell

> A battered war robot finds an orphaned girl in the ruins of a city it helped destroy. Shoot your way through roguelite twin-stick runs against robot legions each night, and raise her through branching days where every choice changes who she becomes.

The war machines won, then forgot why they were fighting. Unit K-7 is one of them, damaged and alone, until it finds Ilse, eight years old, hiding in the cellar of a bombed school. K-7 decides to keep her alive. It has no idea how.

Nights are roguelite runs. Leave the shelter and blast through procedurally arranged streets in fast twin-stick bullet hell combat against the robot legions that still patrol the city. Collect food, medicine and parts, upgrade your weapons and frame between runs, and get home before dawn. Fail and Ilse goes hungry.

Days play out as a branching visual novel about raising a child. Ration what you scavenged to meet her needs, answer her questions about her parents, decide what to tell her about what you are, and help her cope with nightmares, loneliness and the other survivors who hate machines. Every choice shapes who she becomes and how she sees you, and the story has many endings, not all of them with K-7 in them.

*Pitch:* A war-time parenting drama played from the side of the enemy machine: roguelite twin-stick runs at night pay for the branching choices of the day, and the child grows up shaped by both.

## 63. The Lantern Cats

**+0.21σ** · bge 76.49% · MiniLM 37.84% · v1 frontier void · closest Steam game: Glowtide Isle (0.82)

*Tags:* Casual, 2D, Choices Matter, Simulation, Relaxing, Cute, Atmospheric, Colorful, Strategy, Stylized, Physics, Fantasy, Cats, Multiple Endings

> Keep a little lantern burning for a family of sleepy cats. Nudge floating islands into orbit around its light, decide which islands stay warm and which drift into the dark, and watch the tiny lives on them change with every choice.

At the bottom of an endless night hangs one small lantern, and you are its keeper. Floating islands drift in from the dark, and with a gentle push you can pull them into orbit around the light, where meadows, villages and strange gardens begin to grow.

Everything moves with soft, real physics, so every island you add tugs on all the others. Sessions are short and calm, with a little action: flick away falling embers, catch drifting rocks before they collide, spin a little moon, string bridges of light between neighbours. Then the cats ask for something. Bring one island closer to the flame and another freezes in shadow. Let two peoples meet, or keep them apart. Feed the lantern, or let it dim.

Your choices ripple through the whole sky, and no two finished worlds look the same. Cute, colourful and quietly melancholy: a relaxing simulation about caring for something much larger than you.

*Pitch:* A relaxing 2D orbital-physics caretaking sim where every island you place pulls on the others, and the choices about who gets the lantern's limited light branch the story toward many endings.

## 64. Thirteen Doors

**+0.21σ** · bge 74.67% · MiniLM 39.59% · v1 hole void · closest Steam game: 1X1 (0.80)

*Tags:* Action, Adventure, Point & Click, Boss Rush, 2D, Action-Adventure, Action RPG, Hack and Slash, Escape Room, Fantasy, Bullet Hell, Comedy, Arcade

> A point-and-click boss rush in a cursed castle. Click to slash, click to dodge, and solve each locked room before the candle burns out, with nothing but a sword and a mouse.

Thirteen Doors is a 2D point-and-click action adventure set in a hand-painted castle that rebuilds itself every night. You are a squire locked inside at sunset, and the only way out is through thirteen doors, each guarded by a boss.

Every room works twice. First it is an escape room: search the painted walls, combine objects and crack the lock. Then the guardian wakes and the room becomes an arena. Click where you want to strike, drag to block, flick to dodge, and weave through bullet-hell patterns of fire, arrows and cursed coins.

A candle burns on the castle clock. Time spent puzzling is time the bosses grow stronger, so you decide when to explore and when to rush. Between rooms you upgrade your sword, armour and charms in a simple RPG screen.

Short runs, hand-drawn bosses who grumble, gloat and sulk when they lose, and the old-school feel of a browser classic, rebuilt for today.

*Pitch:* Each room of a cursed castle is first an escape-room puzzle and then a mouse-only, bullet-hell boss fight, with a burning candle forcing you to trade puzzle time against how strong the next boss gets.

## 65. Floppy Fault

**+0.20σ** · bge 31.80% · MiniLM 79.60% · v1 hole void · closest Steam game: Swing of the Valkyries (0.84)

*Tags:* Puzzle, 2D, Retro, Casual, Puzzle Platformer, Shooter, Action Roguelike, Bullet Hell, Platformer, Difficult, Roguelite, Minimalist

> A difficult, minimalist retro puzzle platformer with a gun and roguelike runs. Solve one-screen logic puzzles inside a forgotten 1980s home computer, and when you get it wrong, shoot your way through the bullets.

Remember the action puzzle classics of the eighties and early nineties? Simple rules, colored pieces, one screen, and a timer ticking down. You are a tiny hero inside one of those old computers, trying to fix a corrupted floppy disk.

Each screen is a small logic puzzle: push blocks, light switches, connect wires or sort colored pixels into the right slots. Solve it cleanly and the next screen loads. Make a mistake and the glitches fight back, spawning bugs that fill the screen with bullets. Jump between platforms, dodge, shoot back with your little blaster and finish the puzzle under fire.

The disk is different every time you load it, so every run is new. Collect upgrades between screens: an undo charge, a slow-motion shield, a shot that freezes bugs into stepping stones. Lose all your lives and reboot from the start.

Clean minimalist pixel art, chiptune music and short runs. Easy to learn, hard to master, and much harder when you rush.

*Pitch:* A puzzle platformer where mistakes are punished with bullet-hell waves instead of a reset, built into roguelite runs through a corrupted retro floppy disk.

## 66. Rewind at Gallows Gulch

**+0.18σ** · bge 57.52% · MiniLM 55.01% · v1 hole void · closest Steam game: Rush Roulette (0.82)

*Tags:* Adventure, Puzzle, 2D, Casual, 2D Platformer, Comedy, Puzzle Platformer, Strategy, Cartoony, Horror, Co-op, Grid-Based Movement, Western, Time Manipulation

> A cowardly sheriff and his overconfident deputy chase monsters through a cursed western town, rewinding time to undo their mistakes. A grid-based comedy horror puzzle platformer for one or two players.

Tonight the saloon is full of ghouls, the bank vault is haunted, and the only lawmen left are a sheriff who is afraid of the dark and a deputy who is afraid of nothing and should be. Each level is a cartoony 2D puzzle platformer stage packed with traps, monsters and very bad ideas. Every step on the grid counts, because the monsters only move when you do. Plan your moves, think before you jump and work together: one lawman lures a creature while the other sneaks past. When it all goes wrong, and it will, pull out the sheriff's cursed pocket watch and rewind time a few moves to try again. Solve puzzles, capture each monster alive and lock it up in the town jail, where the prisoners start offering unhelpful advice. Play alone by switching between the two, or team up with a friend in online co-op for twice the chaos. Swing on chandeliers, ride runaway mine carts and push coffins onto pressure plates across haunted saloons, flooded mines and a graveyard that will not stay quiet.

*Pitch:* A turn-based, grid-based 2D puzzle platformer and comedy horror western for two lawmen: monsters move only when you move, and a cursed pocket watch rewinds bad plans, playable solo or in online co-op.

## 67. Flyswatter Night Watch

**+0.18σ** · bge 48.87% · MiniLM 63.06% · v1 hole void · closest Steam game: Teddy Won't Help (0.83)

*Tags:* Casual, 3D, Cute, Horror, Action, Adventure, Idler, Relaxing, First-Person, Atmospheric, Stylized, Minimalist

> A small, strange 3D game about a sleepy night watchman in a tiny house full of cute little monsters. Swat them with a flyswatter, collect coins, then nap while the house keeps working.

You are the night watchman of a very small, very odd house. Every night, cute little monsters crawl out of the walls: round ghosts, fuzzy spiders, giant mosquitoes, sock goblins. They are not really dangerous, just annoying.

Walk the dim 3D rooms in first person, swat monsters with your trusty flyswatter, and collect the coins they drop. Spend coins on silly upgrades like a bigger swatter, a louder alarm clock, or a cat that hunts while you sleep.

When you get tired, go to bed. The house keeps working without you, and when you wake up there are new coins, new rooms, and sometimes a new monster waiting at the foot of the bed.

Simple controls, short sessions, a little action, soft low-poly visuals with a slightly creepy touch. Relaxing, cute and a little spooky. Suitable for all ages. Play for five minutes or leave it running all day.

*Pitch:* A first-person cute-horror idle game: you actively swat harmless little monsters around a tiny house, then go to sleep and let the house, your traps and your cat keep earning for you.

## 68. Rooftop Rations

**+0.14σ** · bge 40.38% · MiniLM 68.19% · v1 hole void · closest Steam game: GTL Schedule (0.84)

*Tags:* Simulation, Shooter, Action, Strategy, RPG, Roguelike, FPS, Pixel Graphics, Choices Matter, Shoot 'Em Up, Immersive Sim, Management

> A roguelike FPS where you defend your town from invaders and decide how to feed its people, in a world where food is contraband. Fight in first person, then choose who eats and what to build.

The Ministry owns every seed and every loaf, and growing your own food is a crime. Yet in a flooded quarter of the old city, a small free town has planted gardens on the rooftops, and you are the one who keeps it alive. Each run you head out in first person to defend the town from Ministry raids and bring home whatever food you can carry. Streets, patrols, weapons and convoys are randomized every time, and the pixel-art firefights are fast and unforgiving. Fall, and the haul is lost. Back home, the shooting stops and the town sim begins. Share out the food, plant the rooftops, build workshops and decide how far to trust the smugglers who want a cut. Feed the gunsmith and your weapons improve, starve the radio crew and you miss the next convoy, turn away refugees and the town remembers. Every choice shapes who follows you and how the Ministry answers. Keep the gardens growing until the city is ready to rise.

*Pitch:* A roguelike first-person shooter tied to a food-rationing town sim: each run's haul from raids decides who in a hidden rooftop-garden town gets fed, and those choices feed back into your weapons, allies and the regime's response.

## 69. Rocky Road Rampage

**+0.10σ** · bge 64.10% · MiniLM 41.27% · v1 frontier void · closest Steam game: Midnight Scoop (0.81)

*Tags:* Action, Simulation, Casual, 3D, Driving, Zombies, Vehicular Combat, Action RPG, Stylized, Action-Adventure, Cartoony, RPG

> A small seaside town is overrun by zombies in the middle of summer. Drive your ice cream truck through the outbreak, ram zombies, serve survivors and upgrade your van while your little robot sidekick shoots from the roof.

Sunny Shores was the perfect summer beach town until the zombies arrived. Now everyone is hiding indoors, and the only vehicle still on the road is yours: a cute, battered ice cream truck driven by a retired soldier who just wanted a quiet life.

Drive through a bright, cartoony 3D town in a casual action simulation. Follow the jingle to hungry survivors, park, and serve cones and popsicles before the music draws a crowd. Then floor it. Ram zombies with your truck, swerve through alleys and let your little robot sidekick, riding on the roof, blast anything that gets too close.

Every sale earns cash and experience. Spend it on armor, bigger freezers, monster-truck tires and silly weapons like the sprinkle cannon, and level up your driver and robot. Clear each neighborhood's boss to open new roads along the coast.

No gore, just goofy zombies, sticky fingers and the satisfying chaos of running a business at the end of the world.

*Pitch:* A vending simulation and a vehicular action RPG in one loop: every sale of ice cream rings the jingle that draws the horde, so running the business and surviving the outbreak are the same activity.

## 70. Multiverse Cup

**+0.07σ** · bge 62.50% · MiniLM 40.42% · v1 frontier void · closest Steam game: Racing the Gods (0.82)

*Tags:* Roguelike, Racing, Perma Death, Online Co-Op, Third Person, Shooter, Casual, Adventure, First-Person, Roguelite, PvP, Arcade

> Race through a different universe every lap, shooting rivals and adapting to new physics. One life per cup, no second chances.

Welcome to the Multiverse Cup, the only race where the track changes reality under you. Each lap jumps the whole field into a different universe: low gravity, flipped upside down, made of candy, on fire, or drowned under a purple ocean. Your blaster matters as much as your engine: shoot rivals, clear debris and open shortcuts between worlds. The single-player campaign is a roguelike adventure: your racer has one life per cup, damage carries over between laps, and every universe you survive offers a new part, weapon or perk to bolt onto your hovercraft. Lose your racer and the next one starts from scratch. Switch between a third-person chase camera and a first-person cockpit at any time. In online PvP up to eight pilots race head to head, or team up with a friend in online co-op to run the campaign together. Learn the rules of each world, find the shortcuts between dimensions and become the champion of every reality.

*Pitch:* A permadeath roguelike combat racer where every lap shifts the whole field into a different universe with its own physics, so you have to adapt, shoot and keep one fragile hovercraft alive.

## 71. Lunar Pest Roll

**+0.06σ** · bge 35.09% · MiniLM 66.65% · v1 hole void · closest Steam game: Null Ascent: Stellar (0.84)

*Tags:* Casual, Arcade, Strategy, Incremental, Action, Shooter, 3D, First-Person, Idler, Score Attack, Dice, PvP

> A casual arcade shooter meets an incremental dice game. Roll for your loadout, blast mutant pests across an abandoned moon base for high scores, and bank every lucky streak into upgrades that keep stacking while you are away.

Moon Base Delta was evacuated after the lab's experimental cabbages learned to walk. Somebody has to clean it up, and the contract went to the lowest bidder: you.

Before every run you roll the supply dice. The numbers decide your blaster, your oxygen and the odd perk you get to carry: a six might give you a plasma mop, snake eyes a water pistol and a prayer. Then you jump into a short, fast first-person arcade run through the base's corridors, shooting glowing slugs, sprinting carrots and flying spore pods for combos and credits.

Back at the shuttle, the game becomes an incremental strategy layer. Add faces to your dice, weight the odds, hire robot sweepers and build turrets in cleared sectors. Your automated crew keeps working while you are offline, so every return trip starts with a bigger bank and a deeper base.

Prestige the operation for permanent bonuses, chase records on global score leaderboards, and challenge rivals in quick online PvP races to clear the same wing first.

Goofy, quick and very hard to put down.

*Pitch:* An arcade FPS cleanup job wrapped in an idle/incremental dice economy: dice rolls set your loadout for each run, and each run's earnings let you weight the dice and automate the base, with online PvP races on top.

## 72. Out the Door

**+0.04σ** · bge 57.79% · MiniLM 42.53% · v1 frontier void · closest Steam game: Oniyama Academy: 14 Days of Rough Love (0.82)

*Tags:* Life Sim, Bullet Hell, Cute, Exploration, Third Person, Psychological, Relaxing, Action-Adventure, Wholesome, Simulation, Casual, Colorful

> Fight the fluffy anxiety monsters that stop a shy girl from leaving her apartment, one cute, colorful action roguelike run at a time.

Juniper has not left her tiny apartment in weeks. Every time she reaches for the door, her worries come out to play as round, fluffy monsters. In this cute 3D action game you help her push back. Every outing is a short run through her neighborhood, and every day the worries take new shapes. Dodge soft, colorful bullet patterns, bonk monsters with a pillow, a houseplant or a trusty umbrella, and collect small courage charms that change how you fight. When a run ends, nothing is lost. Back home, a relaxing life sim lets you water plants, cook a simple meal, text a friend or tidy up, and each calm moment unlocks new abilities for tomorrow. Grow braver every day until the front door is just a door again.

*Pitch:* A cute, gentle 3D bullet-hell roguelike about social anxiety: each run takes a shy girl a little farther from her front door, and calm life-sim time at home powers up the next outing.

## 73. Lantern Isles

**+0.01σ** · bge 61.39% · MiniLM 36.84% · v1 frontier void · closest Steam game: Lightkeeper (0.82)

*Tags:* Casual, Strategy, 2D, Adventure, Point & Click, Shooter, Hidden Object, Simulation, Puzzle, RTS, Cute, RPG

> Explore a chain of cute islands, find what the last settlers hid, and grow tiny villages that defend themselves at night. A casual mix of point-and-click searching, small real-time battles and bullet hell shooting from the lighthouse.

Lantern Isles is a casual 2D strategy adventure across a handful of small islands. You arrive by boat with a few villagers and a lantern. On each island, point and click through illustrated scenes to search for hidden tools, seeds and old maps left behind by the settlers who came before. Every item you find unlocks something: a sawmill, a watchtower, a new villager with a special skill. Assign villagers to gather, build and farm in real time, and expand your settlement across the island. At night, mischievous sea spirits come ashore in glowing swarms. Command your villagers to hold the walls, then take the lighthouse cannon yourself and weave its beam through bullet hell patterns to shoot down the brightest spirits. Each island has a small puzzle at its heart and a keeper who levels up your crew with new abilities. Sessions are short, the art is soft and colorful, and the challenge grows gently as you sail from one island to the next.

*Pitch:* Hidden-object searching powers a cute 2D real-time village builder, and each night ends in a bullet hell defence that you fly yourself from the lighthouse.

## 74. Hollowfrost

**-0.03σ** · bge 61.59% · MiniLM 33.70% · v1 frontier void · closest Steam game: Frozen Below: Arctic Expedition (0.82)

*Tags:* Adventure, Action, 2D, Casual, Puzzle, Shooter, Exploration, RPG, 2D Platformer, VR, FPS, Survival, Fantasy

> Stranded on a frozen island with only a bow, a lantern and a talking owl, you explore a hand-drawn 2D map of glacier caves, solve ice-light puzzles and take aim yourself when the frost spirits wake each night.

Your ship breaks apart in the pack ice and you wash up on Hollowfrost, an island that the maps refuse to show. All you carry is a hunting bow, a lantern and an owl who seems to know far more than she says.

By day you explore a hand-drawn 2D island as a side-scrolling platformer, cave by cave. Climb frozen waterfalls, leap between ice floes, and solve simple light puzzles hidden in old carvings: reflect your lantern off ice mirrors, melt the right pillar, line up the constellations on a stone door.

By night the frost spirits come, and the view drops into first person. Plant your feet, nock an arrow and aim for real, with a mouse or standing in VR. Fire arrows thaw bridges, rope arrows open shortcuts, and every spirit you calm drops a shard of warmth.

Spend those shards on new skills and gear, and use them to rebuild the old lighthouse at the island's peak. Light it, and a ship might finally see you.

*Pitch:* A survival adventure that switches viewpoint every day: by day a hand-drawn 2D platformer for exploring and solving puzzles, by night a first-person archery shooter you can play standing up in VR.

## 75. Tick of the Gun

**-0.20σ** · bge 49.99% · MiniLM 30.90% · v1 hole void · closest Steam game: P.A.G. Post Apocalypse Guns (0.83)

*Tags:* Puzzle, Strategy, Turn-Based Strategy, Roguelike, 3D, Isometric, Difficult, Arcade, Procedural Generation, Post-apocalyptic, Perma Death, Western, Bullet Hell, Grid-Based Movement

> A post-apocalyptic western puzzle roguelike: every gunman shoots when you do. Arrange the chaos so you are the last one standing.

Two hundred years after the bombs, the West is wild again, and every meeting ends with guns drawn. Each encounter in this roguelike puzzle game is a frozen standoff on a small isometric grid: raiders, scavengers and rogue robots, each aiming at someone, each with a rule for how they react. Every action you take, a step, a shot, a dive behind a wreck or a kicked fuel barrel, moves the world forward one tick, and every bullet in the air moves with it. Read the lines of fire, predict who will shoot whom, and turn the standoff into a readable bullet hell that ends with you still breathing. Each standoff is a logic puzzle with a clean solution, but the wasteland is procedurally generated and death is permanent. Between encounters, recruit drifters with strange guns and stranger rules, patch up your ride and push further down the highway. Short runs, arcade-quick retries and brutally difficult late fights. Count every bullet and walk away.

*Pitch:* A permadeath wasteland roguelike where every fight is a frozen multi-gunman standoff and bullets advance one tick per action, so a bullet hell becomes a readable logic puzzle you solve to be the last one standing.

## 76. Loaded Die

**-0.44σ** · bge 16.12% · MiniLM 50.10% · v1 hole void · closest Steam game: Run, Run from the Blast! (0.87)

*Tags:* 2D, Action, Platformer, 2D Platformer, Side Scroller, Pixel Graphics, Arcade, Difficult, Puzzle, Roguelite, Puzzle Platformer, Action Roguelike

> You are a die. Every time you tumble, the face that lands on top changes how you jump, dash and fight. Roll through brutal pixel-art platforming runs, solo or in couch co-op, where the right number at the right moment is everything.

Somewhere in a forgotten arcade cabinet, a single six-sided die has escaped the board. Now it has to roll, bounce and flip its way through a crumbling world of tiles and traps to get home.

You do not just move, you tumble. Each roll turns the die a quarter turn, and the face that lands on top decides your power: one lets you float, two gives a double jump, three a wall cling, four a ground pound, five a dash, and six a burst of fire. Every screen is a small puzzle: count your rolls so the right face is up before you reach the gap, the spikes or the enemy.

Runs are built from random side-scrolling rooms with bouncy, physics-driven movement, crumbling platforms, conveyor belts, card-soldier enemies and loaded dice that cheat. Between floors you carve new pips onto your faces, swap abilities and gamble on risky upgrades that reshape your whole build.

It is a difficult, arcade-fast platformer with a roguelite heart, plus a casual mode with extra checkpoints. Bring a friend in local co-op as a second die and roll together.

*Pitch:* A precision platformer where how you move is itself the puzzle: whichever face of the die lands on top sets your current ability, so you plan every roll ahead, and a roguelite layer lets you rewrite the faces between floors.

---

# Baseline: the same AI with no map

## (would rank ~34) Secondhand Truth

**+1.16σ** · bge 92.41% · MiniLM 85.19% · brainstorm (no map) · closest Steam game: PARLEY (0.78)

Prior art: **a close game exists**. Loop Me In is a gossip-routing puzzle: you place character types (Yeller, Super Spreader) to get gossip from the Smack Talker to the Insider. Where the Water Tastes Like Wine has stories you seed come back changed and exaggerated as they spread. Defenestration of Mary Margaret and Heretic are other rumor-spreading games. No game found combines routing with personality-driven, predictable changes to the sentence's content, which is the idea's twist, so close rather than exists. [Loop Me In (itch.io jam puzzle) / Where the Water Tastes Like Wine (Steam, Dim Bulb)](https://lewlew-mcdewdew.itch.io/loop-me-in)
Coherence 4/5: The puzzle is clear and authored: pick an entry point and predict how each personality transforms the sentence. Writing deterministic sentence mutations is the hard part, but it can be built with templated statements.

*Tags:* Strategy, Puzzle, Simulation, Medieval, Comedy, Stealth, Real-Time with Pause, Choices Matter, Multiple Endings, Replay Value, Singleplayer, Indie

> Plant one whispered sentence in a medieval market town and watch it change as it passes from mouth to mouth. Steer the gossip through boasters, mishearers and zealots so the right version reaches the right ear by nightfall.

A small medieval market town runs on routine: the baker opens at dawn, the washerwomen meet at the river, the guards drink at the tavern after the evening bell. You are a stranger with one tool, a whispered sentence. Each chapter sets a goal, such as freeing a wrongly jailed tanner or stopping a forced marriage, and a version of the truth that must reach a particular ear before nightfall. Choose who hears your words first, then watch the day unfold in pausable real time as the sentence travels. Every listener retells it in their own way. The boaster doubles every number, the half-deaf blacksmith swaps similar-sounding words, the priest adds a moral, and the skeptic strips out the juicy part. Changes stack, so a harmless remark about a missing goat can reach the magistrate as an accusation of witchcraft. Study schedules and temperaments, intercept the story with a second whisper to correct its course, and never speak to the same person twice, or suspicion will trace the tale back to you. Each chapter has several solutions, and the outcomes carry into the next.

*Pitch:* The unit you control is gossip itself: a sentence that mutates predictably through each townsperson's personality, turning a social network into a routing puzzle.

## (would rank ~24) The Lip Reader

**+1.63σ** · bge 97.84% · MiniLM 92.65% · brainstorm (no map) · closest Steam game: Purpose of Visit (0.77)

Prior art: **no prior game found**. No video game was found where lip-reading is the deduction mechanic, with sounds that look alike on the lips creating real ambiguity. The lip-reading results were only party games (Read My Lips, Hearing Things, Mega Mouth) and training tools. Orwell shares the loop of filing surveillance reports that superiors act on, and Unheard is a detective game built on hearing past events, but neither uses visual speech decoding. [Orwell: Keeping an Eye on You (Steam), nearest only in surveillance reports whose contents have consequences](https://store.steampowered.com/app/491950/Orwell/)
Coherence 4/5: Clear loop: film, scrub frames, match mouth shapes, assemble the transcript, live with the consequences. The risk is that the viseme ambiguity feels like guessing unless the context clues are designed tightly.

*Tags:* Investigation, Espionage, Puzzle, Cold War, Detective, Mystery, Story Rich, Choices Matter, Atmospheric, Historical, Singleplayer, Indie

> From a rented attic above a divided city, spy on conversations you can never hear. Decode lip movements frame by frame, rebuild what was said, and decide whose secrets end up in your report.

It is the winter of a long cold war, and your agency has given you a telephoto camera, a pair of binoculars and an attic window above a busy square full of cafes, tram stops and embassy doors. You cannot hear a single word below, but you can read lips. Each case begins with surveillance: track targets, catch them mid-conversation, and record short reels of film. Back at your desk you scrub through the footage frame by frame and match mouth shapes to sounds. Many sounds look identical on the lips, so 'bomb', 'mop' and 'pop' share a shape, and only context, gestures and what you already know can tell them apart. Assemble the fragments into a transcript, flag the uncertain words, and file your report. Your superiors act on what you write, so a single misread can burn an innocent courier or let a defector slip away. As the cases connect, you start to notice that someone in the square is choosing their words very carefully, as if they know exactly where you are watching from.

*Pitch:* Lip-reading becomes the core deduction mechanic, where visually identical mouth shapes create real ambiguity that the player resolves through context and evidence.

## (would rank ~29) The Quiet Meter

**+1.43σ** · bge 93.72% · MiniLM 93.66% · brainstorm (no map) · closest Steam game: Murder In Complex (0.80)

Prior art: **no prior game found**. No game found uses minute-by-minute household utility readings as the evidence for a crime. The same idea exists only as academic research and patents (inferring household activity from appliance power signatures, also known as NILM). Timeline-deduction games (Crimson Rain, The Midnight Guest) and, from memory without a search to confirm, Unheard (reconstructing events from audio) share the 'rebuild the night from one indirect channel' structure but not the data source.
Coherence 4/5: A clear deduction loop: tag the signatures, place them on a timeline, explain every anomaly. It fits Obra Dinn-style verification well, though reading charts may feel dry without strong presentation.

*Tags:* Detective, Investigation, Puzzle, Logic, Mystery, Crime, Modern, Minimalist, Narrative, Mouse Only, Singleplayer, Indie

> Solve crimes in a twelve-storey apartment block using nothing but minute-by-minute electricity, water and gas readings. Learn every appliance's signature, rebuild each resident's night, and find the reading that should not exist.

A building is a diary that nobody meant to write. As a forensic analyst for the city's utility company, you are called in when the police have run out of witnesses. Each case hands you a block of flats and a night's worth of meter data: electricity, water and gas, sampled every minute for every unit. At first it is just lines on a chart. Then you learn to read them. A sharp three-minute spike is a kettle. Hot water paired with a gas burner is a shower. A slow rhythmic wave is a washing machine on its spin cycle. Tag these signatures, place them on a shared timeline, and the residents come alive: who woke at three, who pretended to be away, which empty flat suddenly drew power for exactly forty minutes. Cross-reference units to catch people moving between them, test theories against the data, and submit a reconstruction that must account for every anomaly. Later buildings add solar panels, faulty wiring, shared boilers and suspects who know how to disguise their footprint.

*Pitch:* Detective work done entirely from household utility consumption curves, turning appliance signatures into the evidence and the timeline into the solution.

## (would rank ~27) The Interpreter's Chair

**+1.55σ** · bge 95.50% · MiniLM 94.68% · brainstorm (no map) · closest Steam game: This Is the Peace (0.78)

Prior art: **a close game exists**. Intergalactic Interpreter makes you the go-between in peace talks between two leaders who speak different languages (one in alien gibberish). You make timed dialogue choices, war must be avoided, and there are multiple peace or doom endings. Diplomatic Dictation casts you as a translator who bends politicians' words to make them sound good. Both are small jam games, and neither page confirms the idea's specific system of partly bilingual aides who can catch your edits, or the corridor favour-trading between sessions. [Intergalactic Interpreter (itch.io, GMTK Game Jam 2021); also Diplomatic Dictation (itch.io)](https://sebastianscaini.itch.io/intergalactic-interpreter)
Coherence 5/5: Very clear and buildable loop: hear the true meaning, choose how to render it, the table reacts, and the risk of detection grows. The stakes are strong and it replays well.

*Tags:* Choices Matter, Diplomacy, Political Sim, Narrative, Dialogue Heavy, Multiple Endings, Story Rich, Thriller, Psychological, Replay Value, Singleplayer, Indie

> Two nations are negotiating a ceasefire, and you are the only person in the room who understands both sides. Translate faithfully, or quietly bend every sentence toward the peace you believe in, without getting caught.

A ceasefire summit has been arranged in a remote mountain hotel, and you are the sole interpreter between two delegations who share no common language. Every word passes through you. As each speaker talks, you hear the full meaning, including the threat hidden in a polite phrase and the concession a general did not mean to offer. Then you choose how to deliver it. Render it faithfully, soften an insult, sharpen a vague promise, drop a dangerous aside, or slip in a phrase of your own. The table reacts in real time: tempers rise and cool, trust grows or collapses, and positions on the map shift. Your manipulation is not invisible. Each side has aides who understand fragments of the other language, and a careless change can be noticed, recorded and used against you. Between sessions, corridors, dinners and late phone calls let both sides press you for private favours. Five days of talks lead to many endings, from lasting peace to renewed war to your own quiet disappearance.

*Pitch:* The player is the communication channel itself, editing every sentence of a negotiation while partially bilingual witnesses threaten to expose the edits.

## (would rank ~28) Sold to the Back Row

**+1.48σ** · bge 94.22% · MiniLM 94.25% · brainstorm (no map) · closest Steam game: Auction Simulator (0.79)

Prior art: **no prior game found**. Existing auctioneer games cover only the crowd-scanning half. In Cherrypick's mobile Auctioneer you spot the highest paddle in a crowd under a timer. In Papeer Auktioneer you click target items in a moving crowd. Neither has a rhythm chant. Auction-chant music appears only as a DDR song ('Auctioneer Beats'). No game found that combines keeping a chant on the beat with reading bidder signals, budgets and the timing of the hammer. [Auctioneer (mobile, Cherrypick Games); Papeer Auktioneer (itch.io jam)](https://papeer-auktioneer.itch.io/gamejam)
Coherence 4/5: A strong dual-task hook in the vein of Rhythm Heaven, with clear success and failure states and a natural difficulty ramp. Keeping the beat while scanning for subtle bids needs careful readability tuning.

*Tags:* Rhythm, Job Simulator, Simulation, Music, Fast-Paced, Score Attack, Comedy, Casual, Colorful, Local Multiplayer, Singleplayer, Indie

> Become a fast-talking auctioneer. Keep your bid chant locked to the beat while scanning a packed room for nods, winks and twitching paddles, and squeeze every last coin from the crowd before the hammer falls.

Auctioneering is music with money attached, and you are about to learn the rhythm. Each lot opens with a starting price and a room full of bidders. Your chant is a rhythm track: hit the beats to keep the filler words rolling and the crowd hypnotised, and if you stumble the room loses interest. While your mouth runs, your eyes work. Bidders signal in tiny ways: a raised catalogue, a tap of the nose, a glance to a partner, a paddle lifted half an inch. Spot a bid, point at it on the beat, and the price climbs a step. Every bidder has a hidden budget and a temperament, so read their hesitation, coax them with a smaller increment, or bluff a bid from the back wall if you dare. Drop the hammer too early and you leave money on the table; wait too long and the lot goes unsold. Work your way from livestock barns and storage lockers to estate sales and glittering city galleries, then face rival auctioneers in a split-screen chant-off.

*Pitch:* A rhythm game fused with crowd-reading, where keeping the auction chant on beat and spotting subtle bids must happen at the same time.

## (would rank ~31) Card Section

**+1.29σ** · bge 84.18% · MiniLM 95.68% · brainstorm (no map) · closest Steam game: Eishockey Manager Legacy (0.81)

Prior art: **no prior game found**. I found no video or tabletop game where you design a stadium card-stunt mosaic for the seat grid and then conduct an unreliable crowd live. Searches only turned up real card stunts and tifos, plus phone and LED 'crowd as pixels' tech for live events. None of these is a game.
Coherence 4/5: Clear plan-then-execute loop like Overcooked crossed with Picross, and live crowd failures give real-time tension. Simulating thousands of bodies is a scope risk, but it can be built.

*Tags:* Puzzle, Management, Time Management, Sports, Level Editor, Real-Time, Colorful, Casual, Funny, Co-op, Online Co-Op, Singleplayer, Indie

> Plan the giant pictures that thousands of fans make by holding up coloured cards, then conduct them live on match day. Late arrivals, swapped seats and distracted children will ruin your masterpiece unless you react fast.

Halftime is in ninety seconds and twelve thousand people are about to become your pixels. In the planning phase you design card stunts for a stadium's seating: draw a mosaic on the seat grid, break it into frames for animated sequences, and print an instruction slip for every seat. You choose how complicated each slip should be, because a clever ten-step animation means nothing if fans cannot follow it. On match day the plan meets the public. Spectators arrive late, sit in the wrong row, drop their cards, hold them upside down, or wander off for snacks just before the big reveal. You conduct from the press box in real time: call each flip over the loudspeaker, spot gaps forming in your image, send volunteers running with spare cards, and improvise simpler fallbacks when a section falls apart. Images are scored for accuracy and crowd excitement, unlocking larger venues and trickier stands. Friends can join online, each conducting their own block of seats, and a design editor lets you share stunts with the community.

*Pitch:* An entire stadium crowd becomes an unreliable pixel display that you design for in advance and then conduct live as people fail to follow instructions.

## (would rank ~20) Rounds and Changes

**+2.04σ** · bge 98.95% · MiniLM 97.69% · brainstorm (no map) · closest Steam game: Click on bells together (0.76)

Prior art: **a close game exists**. Ringing Room already does the core loop online: each person takes one bell in a shared virtual tower and rings methods in time, computer ringers (Wheatley) fill the empty bells, and players call bobs and singles with hotkeys. Abel and Mobel offer the same thing solo with 20,000 methods. What it lacks is the pitched centrepiece, physically controlling a swinging bell's balance with pull and check, along with any game wrapper such as a campaign or progression. It is a practice tool rather than a game, so this is close, bordering on exists. [Ringing Room (browser virtual belltower, 2020) with its Wheatley computer ringer; also Abel/Mabel/Beltower change-ringing simulators (PC/Mac/iOS)](https://ringingroom.co.uk/help)
Coherence 4/5: A clear, authentic co-op rhythm loop. Learning methods on top of swing physics makes the curve very steep, and network latency is a known problem for online ringing.

*Tags:* Rhythm, Online Co-Op, Co-op, Music, Puzzle, Simulation, Physics, Logic, Cozy, Multiplayer, Singleplayer, Indie

> Ring tower bells the old way with friends: each player pulls one heavy swinging bell, swapping places in shifting mathematical patterns while keeping every stroke perfectly in time.

High in a village church tower, eight ropes hang in a circle. Each one is attached to a bell weighing as much as a small car, and each is yours to control. This kind of ringing is not about melodies. The bells sound one after another in rows, and with every row the order changes according to a pattern called a method. Your job is to know where your bell belongs in each row and get it there. Pull harder to hold the bell up longer and strike later; check your pull to come in sooner. Overdo it and the bell swings past its balance point and the whole band falls apart. Ring alone with patient computer ringers, or join up to seven friends online, each on a rope, while one of you conducts, calling out changes that rearrange the pattern mid-flow. The campaign follows a neglected tower brought back to life: recruit locals, learn new methods, ring for weddings and festivals, and train for a marathon touch of thousands of unbroken changes.

*Pitch:* A co-op rhythm game built on the real tradition of change ringing, where the challenge is timing a heavy swinging bell while tracking your place in a moving permutation.

## (would rank ~34) Unseen Stage

**+1.19σ** · bge 83.14% · MiniLM 94.09% · brainstorm (no map) · closest Steam game: ACT OUT (0.81)

Prior art: **a close game exists**. Mime games where pantomimed walls and objects actually work already exist (Other Inside has imaginary walls and a pantomime lasso; Magic Mime and Blind Exit use invisible walls). Platformers where things exist only while seen also exist (Out of the World, Object Impermanence), and It's Mime Time! has a mime performing for spectators in an invisible maze. I found nothing that makes mimed objects solid only while an NPC audience is watching, so that crowd-attention resource is the new part. [Other Inside (IndieDB mime puzzle game); also Blind Exit (itch.io, LD54) and Out of the World (2.5D platformer where objects you see materialize)](https://www.indiedb.com/games/other-inside)
Coherence 4/5: An elegant, readable rule: attention is the resource and audience types are the puzzle variables. Steering the crowd could get fiddly, but the core is strong.

*Tags:* Puzzle Platformer, Puzzle, Platformer, 2D, Side Scroller, Silent Protagonist, Hand-drawn, Comedy, Cute, Wholesome, Family Friendly, Singleplayer, Indie

> A street mime whose imaginary walls, ladders and ropes become solid, but only while someone is watching. Gather an audience, hold their attention, and perform your way across a city that has forgotten how to pretend.

In a grey city where nobody has time for street performers, a silent mime discovers that a convincing act becomes real. Trace a wall with your palms and it blocks the way. Climb an imaginary rope hand over hand and you rise. Lean on a counter that is not there and it holds your weight. There is one condition: the object exists only while an audience member is watching and believing. Every level is a puzzle about attention. Gather onlookers, keep them entertained, and lead them to places where their gaze covers the gaps you need to cross. Children believe almost anything, office workers glance away to check the time, and a stern critic needs a flawless performance before your ladder turns solid. Lose the crowd mid-climb and you fall. Perform gestures with precise inputs, chain them into routines, and use your invisible creations to trap guards, lift friends and cross rooftops. The wordless story, told in hand-drawn panels, follows the mime as the city slowly learns to play again.

*Pitch:* Pantomimed objects are solid only inside an audience's line of sight, so crowd attention becomes the platforming resource the player must earn and steer.

## (would rank ~34) Root Exchange

**+1.17σ** · bge 88.72% · MiniLM 89.85% · brainstorm (no map) · closest Steam game: Mutualist (0.85)

Prior art: **already exists**. In Mutualist you play the mycelial network itself ('A forest is not a collection of trees. It is a market'). You draw connections tree by tree and route carbon, phosphorus and water between species, facing beetles, frost and an underground parasite, then sporulate to reset into new forests. That matches this idea's premise, trade loop, threats and spore-to-new-forest progression almost point for point. Smaller relatives are Mycelium Empire (itch.io, fungus trades with plant roots), Mycenial (itch.io) and the board game Undergrove, which covers the same trade from the trees' side. [Mutualist (EvilWays/Securen, Steam, Early Access announced for Nov 2, 2026)](https://store.steampowered.com/app/5367990/Mutualist/)
Coherence 4/5: A clean economic-management loop with a clear ecological metaphor. Setting exchange rates and taking a cut maps naturally onto the sim.

*Tags:* Economy, Resource Management, Strategy, Simulation, Nature, Trading, Management, Underground, Real-Time with Pause, Science, Atmospheric, Singleplayer, Indie

> Become the fungus beneath an old forest and run its hidden marketplace. Thread through the soil, link tree roots, broker sugar for minerals, and take your cut while keeping the whole forest alive through drought and rivals.

Beneath every old forest lies a network of fungal threads linking the roots of trees, and you are that network. Trees make sugar in the sunlight but struggle to pull minerals and water from the soil; you mine minerals but cannot make sugar. Every connection you grow is a trading route. Extend threads through layers of earth, wrap the roots of oaks, pines and birches, and set exchange rates with each tree. Ferry surplus sugar from sunlit giants to shaded saplings, move water toward the thirsty in a dry spell, and skim a share from every transaction to fund further growth. The forest responds to your choices. Starve the young trees and the canopy thins within a decade; overcharge the old ones and they cut you off and court a rival fungus spreading from the next valley. Seasons shift demand, beetles and drought test your reserves, and loggers can sever whole districts overnight. When your network is strong, raise mushrooms above ground to send spores toward new forests with harsher conditions.

*Pitch:* The player is the underground fungal network that brokers nutrients between trees, an ecological trading economy seen entirely from the soil.

## (would rank ~48) Long Water

**+0.70σ** · bge 73.51% · MiniLM 79.61% · brainstorm (no map) · closest Steam game: Clan & Flood (0.82)

Prior art: **a close game exists**. In JefferyXue's River you play the river's source, and humans automatically settle, farm and die by your drought or flood, which is the same 'you are the river that civilizations depend on' premise. The solo TTRPG You Are A River maps a river's course and narrates the history of the world along it. Neither has turn-based meander carving and silt over millennia, or towns building dams and embankments to pin you in place. [River by JefferyXue (itch.io); also You Are A River (solo TTRPG, Big Lizard Games)](https://jefferyxue.itch.io/river/devlog/298032/development-documentation-of-river)
Coherence 3/5: Evocative, but a river's agency and goals are abstract: the 'strength of current' economy and the win and fail conditions ('if you endure') are vague, so it risks being a toy rather than a game.

*Tags:* God Game, Turn-Based Strategy, Strategy, Simulation, Nature, Procedural Generation, Atmospheric, Relaxing, Sandbox, Beautiful, Singleplayer, Indie

> You are a river flowing across ten thousand years. Carve valleys, choose where silt settles, flood and retreat, and shape the towns that rise on your banks while they build dams and walls to bend you to their will.

Begin as meltwater at the edge of a retreating glacier and end, if you endure, as a broad delta spilling into the sea. Each turn spans a decade. Spend the strength of your current to cut into an outer bank, drop silt on an inner bend, abandon a loop to leave an oxbow lake, or gather spring rain into a flood that spreads fertile mud across the plain. Life answers your choices. Reeds, fish and herons follow clean shallows, and people follow the fish. Villages appear where your soil is richest, and they love you while you feed them. As they grow, they begin to argue with you: mills narrow your channel, embankments pin you in place, bridges ask you to stay still, and eventually a dam threatens to stop you altogether. You can bend around them, nourish them, or break them with a hundred-year flood. Every valley is procedurally shaped, and every playthrough leaves a different map of towns, wetlands and ruins along the path you chose.

*Pitch:* The player is a river across millennia, shaping its own course while the civilizations it feeds work to pin it in place.

## (would rank ~23) Fair or Foul

**+1.72σ** · bge 97.22% · MiniLM 96.02% · brainstorm (no map) · closest Steam game: Weather Dragger (0.78)

Prior art: **a close game exists**. The daily loop of 'read instruments and signs, issue a forecast, live with the consequences' exists in several small games. In J. Weatherman Jr. you forecast by interpreting instrument data, Silent Sky has you gather pressure, wind and temperature and warn authorities or lose your job, Dracula's Meteorologist (1895) predicts weather from clues, and Rituals of Raindrops and Rays ties daily weather prediction to villager satisfaction. None found has a physically simulated sky, a 19th-century harbour storm signal, or forecaster trust that changes how the fleet behaves. The search budget ran out before lighthouse- and storm-signal-specific queries could run. [J. Weatherman Jr. (itch.io), with Silent Sky (itch.io) and Rituals of Raindrops and Rays (itch.io)](https://defaulttidus.itch.io/weatherman)
Coherence 4/5: A strong daily decide-then-see-outcome loop with meaningful stakes. A fully physical sky sim is expensive, and the forecasting has to stay readable rather than become guesswork.

*Tags:* Simulation, Science, Life Sim, Education, Atmospheric, Historical, Nature, Puzzle, Narrative, Choices Matter, Singleplayer, Indie

> Become the weather watcher of a stormy nineteenth-century fishing village. Read clouds, pressure and seabirds each dawn, raise your forecast on the harbour mast, and live with what happens when the boats come home, or don't.

The fishing boats will not leave the harbour until they see your flag. As the new weather watcher of a small village on a wild northern coast in the nineteenth century, your forecast decides whether families eat this week and whether some of them come back at all. Each dawn you climb to the station and observe. The sky is fully simulated, with fronts, pressure systems and cloud formations that behave as they do in reality, so a thickening veil of high cloud, a falling barometer and a wind backing to the south all mean something. Combine your instruments with the village's own signs: gulls staying ashore, an old sailor's aching knee, a halo around the moon. Then raise a fair, caution or storm signal on the harbour mast and watch the fleet decide. Your accuracy builds trust, and trust changes behaviour, since a doubted forecaster is ignored on the day it matters most. Over the seasons, upgrade instruments, keep a logbook of patterns, trade readings with distant stations by telegraph, and get to know the people whose lives ride on your judgement.

*Pitch:* A forecasting game where the player reads a physically simulated sky to make daily predictions whose credibility decides a village's fortunes.

## (would rank ~70) Valley Fold

**+0.07σ** · bge 28.16% · MiniLM 74.22% · brainstorm (no map) · closest Steam game: By My Command (0.85)

Prior art: **no prior game found** (thin check). I found no game where you design units by placing mountain and valley folds on a crease grid, with the folded geometry setting tactical stats. Folded Wishes only lets players fold cosmetic pieces for a tile game. Only 1 search could be run because the shared web-search budget ran out, so this verdict is weakly supported. A follow-up check for origami or paper-army tactics games is recommended. [Folded Wishes (board game, 2020, comes with origami paper for players to fold their own pieces)](https://www.tlamagames.com/en/board-games/folded-wishes/)
Coherence 3/5: A distinctive hook, but real crease-pattern collapsing is hard to make intuitive, and mapping arbitrary folds to balanced stats is a serious design problem. It needs heavy abstraction.

*Tags:* Turn-Based Tactics, Crafting, Strategy, Puzzle, Tactical, Roguelite, Grid-Based Movement, Turn-Based Combat, Stylized, Replay Value, Singleplayer, Indie

> Fold your own army. Every crease you make on a square of paper decides how your units move, strike and survive, then they march into turn-based battles across a cluttered scholar's desk.

On a scholar's desk at night, paper armies wage war across open books, ink pools and the ridges of a fallen ruler. You do not recruit soldiers; you fold them. Each unit starts as a blank square on a crease grid. Place mountain and valley folds, collapse the sheet, and the shape you create becomes the unit. Long sharp points give reach, extra flaps become legs and speed, stacked layers turn into armour, and broad wings let a piece glide from the rim of a teacup. Simple folds are reliable; ambitious ones are powerful but tricky to collapse correctly. Then take the fight to the grid in turn-based battles where terrain matters: ink soaks and weakens paper, a desk fan scatters light units, and a candle is as deadly as it sounds. Damaged units come back creased and torn, and you can refold them between fights, but every refold weakens the sheet. Collect new papers, from thin tissue to stiff card and metal foil, as you push through a roguelite campaign across a sprawling study.

*Pitch:* Unit design is literal paper folding: the geometry of the crease pattern you fold becomes the unit's stats in tactical combat.

## (would rank ~17) The Last Tuning

**+2.27σ** · bge 96.09% · MiniLM 99.83% · brainstorm (no map) · closest Steam game: Who am I: Remedy (0.77)

Prior art: **a close game exists** (thin check). I NEED TO PRACTICE is a horror game where you tune four strings by turning pegs and then play. Off-key playing makes the haunting close in (lights flicker, shadows creep), which shares this idea's twist that sour notes summon danger. It differs a lot, though: it is a short bowed-string piece about playing, not by-ear piano tuning through acoustic beats across a house of instruments. Only one web search ran for this idea because the shared search budget ran out, so a direct match could have been missed. [I NEED TO PRACTICE (itch.io, free horror sim)](https://randomgamer13.itch.io/i-need-to-practice)
Coherence 4/5: A distinctive, well-tied mechanic: the beat-rate tuning is both puzzle and threat. Accessibility for players with weak pitch perception is a real design risk.

*Tags:* Psychological Horror, Music, Puzzle, Horror, First-Person, Atmospheric, Mystery, Exploration, Story Rich, Dark, Singleplayer, Indie

> A piano tuner is hired to restore every instrument in a shuttered mansion. Tune by ear, string by string, as each sour note you correct quiets something in the house, and each one you leave wavering draws it closer.

In the autumn of 1926 you are hired to tune every piano in a shuttered country house: the grand in the ballroom, the upright in the servants' hall, the toy piano in the nursery and dozens more. The family will not say why, and they will not stay the night. Tuning works the way it does in real life. Open the instrument, set your lever on a pin, and listen. Two strings slightly apart produce a wavering beat; turn the pin until the beat slows and vanishes, or until it pulses at the exact rate a tempered interval needs. Play with headphones and the house becomes an instrument too. Every piano you set right calms part of the presence that lives here and reveals a fragment of the composer who once did. Every wavering, sour note attracts it. You cannot fight it and you cannot run far, so you must decide how much noise to make, which rooms to finish first, and when to stop and simply listen. Letters, scores and old recordings slowly reveal what was left unfinished.

*Pitch:* A horror game whose central skill is authentic by-ear piano tuning, with acoustic beating serving as both the puzzle and the thing that summons danger.

## (would rank ~36) Morning Control

**+0.94σ** · bge 92.86% · MiniLM 70.26% · brainstorm (no map) · closest Steam game: Snow Resort Simulator (0.80)

Prior art: **no prior game found** (thin check). Ski Patrol is an open-world skiing game that lists 'mitigating avalanche hazards' among its objectives. Its core is skiing and errands, and its store pages show no snow-pit reading, blast-or-close decisions or season-long snowpack memory. Only 1 search could be run because the shared web-search budget ran out, so a deeper check for avalanche or snow-science sims is recommended. [Ski Patrol (Pita, Steam Early Access, 2024)](https://rawg.io/games/ski-patrol)
Coherence 4/5: A tight daily loop (investigate, decide, live with it) with good built-in pressure from the manager and guests. The persistent buried snowpack is a strong systemic hook, though the topic is niche.

*Tags:* Simulation, Snow, Job Simulator, Management, Skiing, Strategy, Science, Realistic, Atmospheric, Choices Matter, Singleplayer, Indie

> Lead the avalanche crew at a mountain resort. Dig snow pits before dawn, read the buried layers, choose which slopes to blast or close, and open the mountain safely before the first chairlift turns.

Every morning the mountain asks a question, and you have until the lifts open to answer it. As head of the avalanche team at a busy ski resort, you start in darkness with overnight reports: snowfall, wind direction and temperature swings that may have buried a weak layer under a fresh slab. Choose which slopes to investigate, ski out with your crew, and dig. Each snow pit is a cross-section of the season, and reading it is a puzzle of crystal shapes, hardness and test results that tell you whether a slope will hold. Then decide: throw hand charges, fire the avalanche cannon, ski-cut a slope yourself, or keep it roped off for the day. The resort manager wants the famous runs open by nine, the guests want fresh powder, and the mountain does not care about either. Through the day, sun and wind keep changing the picture, so you reopen, close and respond to rescues. Seasons build on one another, since every storm and every decision is buried in the snowpack you will dig through next month.

*Pitch:* Snow science as the core loop: reading a layered snowpack and triggering controlled slides, with the whole season's weather persisting as buried history.

## (would rank ~34) Altitude Only

**+1.00σ** · bge 92.84% · MiniLM 74.63% · brainstorm (no map) · closest Steam game: Squall Riders (0.79)

Prior art: **already exists**. Kaze no NOTAM is a balloon game where you control only up and down (burner and vent). A panel shows the wind direction at each altitude, and you steer to targets by picking a layer, with winds shifting by weather and time of day. Balmy Balloonists is a competitive balloon race where your altitude choice decides your wind and costs ballast or gas. Many smaller games use the same twist (The Balloonist and Patterns of the Wind on Playdate, Blazing Balloons, a 2018 Gordon Bennett gas-balloon game from HEIA-FR). Only the real-time online shared-sky race is new. [Kaze no NOTAM / NOTAM of Wind (Artdink, PlayStation, 1997); also the board game Balmy Balloonists](https://obscuritory.com/sim/kaze-no-notam/)
Coherence 4/5: An elegant one-input design with real depth. Long races and the risk of copying the leader need careful pacing.

*Tags:* Racing, Flight, Simulation, Strategy, Resource Management, Competitive, PvP, Physics, Multiplayer, Atmospheric, Relaxing, Singleplayer, Indie

> A long-distance balloon race where your only control is up or down. Read invisible rivers of wind stacked in the sky, spend your ballast wisely, and drift hundreds of miles to the target ahead of your rivals.

Gas balloons have no engine, no rudder and no steering wheel. You can rise by dropping sand and sink by venting gas, and that is all. Yet the sky is layered, with each altitude carrying its own wind, and a good pilot steers by choosing which layer to ride. Before each race, study forecasts and launch small pilot balloons to see how winds turn with height. In the air, watch cloud drift, chimney smoke and other racers for clues, then commit: climb into a fast westerly, drop into a slow southerly to curve around a mountain range, or hold steady and wait for the evening shift. Every climb costs ballast and every descent costs gas, and both run out. Races cover hundreds of miles and play out over hours compressed into tense, quiet sessions, ending in a precise landing near a target. Online, everyone shares the same simulated sky, so watching another balloon swing away reveals a wind you cannot see, while simply copying a rival means you can never beat them.

*Pitch:* A racing game with a single vertical control, where steering means reading and choosing between invisible stacked layers of wind.

## (would rank ~24) The Night Compositor

**+1.64σ** · bge 97.92% · MiniLM 92.77% · brainstorm (no map) · closest Steam game: The Newspapers of the day (0.78)

Prior art: **a close game exists**. Letterpress Simulator is a released first-person drag-and-drop print-shop sim built around the tasks of printing an edition and reading type upside down and backwards. COMPOSITOR is a puzzle about getting loose sorts standing in the composing stick, and Fit to Print is a real-time puzzle about laying out a newspaper front page against a deadline. I found no game that combines hand-setting mirrored type, justification, newspaper layout and a nightly deadline with censorship and type shortages. [Letterpress Simulator (Befuddly, itch.io); also COMPOSITOR (CSAF, Game Boy) and Fit to Print (Flatout Games board game, 2023)](https://befuddly.itch.io/letterpress-simulator)
Coherence 4/5: A clear Papers, Please-style job loop with a strong deadline. Letter-by-letter picking could get tedious, so pacing and abstraction of the typing step matter.

*Tags:* Typing, Time Management, Puzzle, Historical, Job Simulator, Simulation, Word Game, Spelling, Management, Narrative, Singleplayer, Indie

> Work the night shift at a nineteenth-century newspaper, setting every word by hand in backwards metal type. Justify lines, fit columns around adverts, and lock the front page before the presses roll at dawn.

It is midnight in a city newsroom in the 1890s, and tomorrow's paper does not exist yet. Stories arrive in scrawled handwriting, and you must turn them into metal. Pick letters from the type case, where every letter has its own compartment, and drop them into your composing stick, upside down and mirrored. Fill each line exactly, using thin and wide spaces to justify it, because a loose line will fall out on the press. Then lay the finished columns into the page frame, a fitting puzzle of headlines, advertisements and illustrations that must lock together without gaps. The clock never stops. Breaking news forces you to tear up a finished column, the editor wants a bigger headline, the censor sends a list of words to cut, and the type case runs short of capital letters halfway through an election story, so you have to rephrase on the fly. Each morning the printed paper shows your mistakes in public. Between shifts, hire apprentices, buy new typefaces, and follow the stories that slowly reveal what is happening in the city.

*Pitch:* Hand-setting mirrored metal type under a deadline, combining typing, word-fitting and spatial page layout into a single job loop.
