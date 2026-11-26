# What is known about how people spot generated text

Read 23 Nov 2026. Sources are at the bottom. Where a claim comes from a blog list and not a study, it says so.

## Where the style comes from

It is tempting to say a model writes this way because it picks the most likely next word. That is part of it, but one study points at something more specific. Reinhart and others (PNAS, 2025) compared human text with text from base models and from the same models after instruction tuning. The base models wrote close to the way people do. The tuned ones, the kind everyone actually uses, did not. So the style is mostly a trained house style, laid on top of the likeliest-word effect.

That house style is dense and noun-heavy. Against human writing, GPT-4o used:

- "-ing" clauses hanging off a sentence about 5 times as often ("Bryan, leaning on his agility, dances around the ring, evading Show's heavy blows.")
- "that" clauses as the subject about 2.6 times as often
- nouns made from verbs (words in "-tion", "-ment") about 2 times as often
- pairs of words joined by "and" about 1.9 times as often
- passives with no doer about half as often

It also overused single words at enormous rates (camaraderie, tapestry, intricate, palpable, amidst at around 100 times the human rate), and bigger models were no closer to human than smaller ones.

A second study (Shaib and others, 2024) looked at sentence skeletons, meaning the order of the parts of speech with the words taken out. Generated text repeats the same skeletons much more than human text does.

## What readers actually notice

Russell, Karpinska and Iyyer (2025) had people label 300 articles as human or generated and explain why. People who use these models a lot for their own writing were very good at it: a majority vote of five of them got 299 of 300 right, better than most detection software. People who rarely use the models were poor at it and too sure of themselves.

What the good readers said they went by, as a share of their explanations:

- vocabulary, 53% (the known words, but also odd word choices)
- sentence structure, 36% ("not only this but that", lists of exactly three, sentences all alike)
- grammar and punctuation, 25% (too perfect; people make small slips and mix their punctuation)
- originality, 24% (safe, no surprise, no humour)
- quotes, 22% (every quoted person talks the same way)
- clarity, 20% (over-explains, tells where it could show)
- then formatting, tidy conclusions, formality, stock names, tone

What they said read as human: unusual word choices and good analogies, sentence lengths that vary a lot, specific details that could be checked, a visible point of view, and an ending that stops without a summary.

Two findings matter most for this skill.

First, text that had been "humanized" with a guide written from these readers' own clues still got caught by the majority vote every time. The vocabulary clue dropped but the others held. Removing the list of tells does not make text pass with people who read a lot of it.

Second, the one reader who was fooled treated informality as proof of a human. Slang, "just" and "actually" were enough for them. That is a reason not to fake chattiness: it fools the weakest readers and reads as a costume to the rest.

## The public lists

Wikipedia's editors keep the most careful one ("Signs of AI writing"). Its main groups:

- Inflated importance: "stands as", "serves as", "is a testament to", "plays a pivotal role", "underscores its importance", "reflects a broader", "evolving landscape".
- The "-ing" tail used as shallow analysis: "highlighting", "underscoring", "emphasizing", "ensuring", "reflecting", "fostering".
- Negative parallelism in three forms: "not just X but also Y", "it's not X, it's Y", and "Y rather than X". The page notes "rather than" has become especially common in recent output, which is the neighbour effect: train out one form and the next one grows.
- The rule of three.
- Avoiding plain "is" and "has": "serves as", "boasts", "features", "offers".
- Vague attribution: "experts argue", "observers have noted", "industry reports".
- Formula endings: "Despite these challenges", "Future outlook", "In summary".
- Talking to the user: "I hope this helps", "Certainly!", "let me know", "Would you like".
- Formatting: title case headings, heavy bold, bold lead-in lists, emoji bullets, curly quotes.
- Word lists by model era. For models from mid-2026 on it lists: matters, quietly, steady, practical, dependable, prioritize, leverage, foster, multifaceted, clearer. It also says recent models write shorter sentences of about 8 to 20 words with more full stops and commas, and it now files the em dash as a historical sign.

The page is firm that no single sign proves anything, that people write these things too, and that fixing the signs is not the goal.

Community lists (blogs and GitHub, so weaker evidence) add: "Here's the thing", "Here's the kicker", "Honestly?", "Let that sink in", "That's not a bug, it's a feature", "The best part?", "No fluff", and for Claude in particular "genuinely", "honest", "load-bearing", "surface", "unpack", "lean into".

"That's what actually matters" is not on any list by name, but it belongs to a family these lists do describe: a short line that tells the reader how much the last sentence weighed. This skill calls it the verdict line.

## Detection software

The older tools measure two things: how predictable each word is to a language model, and how much sentence length and build vary ("burstiness"). Generated text is more predictable and more even. Newer tools are trained classifiers and their makers say little about what they look at. All of them make mistakes, are unreliable on short texts, and flag careful human writing fairly often. This skill is not aimed at them. A piece that reads well to a person who knows the subject is the target, and platform labels that ask whether AI was used still get answered truthfully.

## What follows for the method

1. A list of banned phrases is necessary and not enough. It handles the 53% clue and little else, and the humanized-text result shows what happens when that is all you do.
2. Each fix grows a neighbour. "Not X but Y" became "rather than". The em dash went and the short even sentence came. So the list in `habits.md` names the neighbour for every habit, and the lists of favourite words have to be refreshed.
3. The grammar findings give concrete rewrites: verbs in place of nouns, a person as the subject, plain "is" and "has", "says" for "says", and ending the sentence when the fact ends.
4. What reads as human is mostly content: a specific detail, something that went wrong, a point of view, a word chosen because it fits and not because it is likely. That has to come from the person. The skill should ask for it and never invent it.
5. Evenness is the tell that survives everything else, in sentence length, sentence build and paragraph size. The retelling step in the listener pass is the best tool found so far for breaking it, because speech is uneven by nature.
6. A reader who has not seen the draft catches more than the writer rereading. That is true of people and it is why the skill uses a separate cold reader where it can.

## Honest limit

Nothing here makes generated text undetectable to people who read a lot of it. In the study above, five such readers together were almost never wrong, even against text built to fool them. What this method can do is remove the sentences that make a reader stop trusting the piece, and make it read like something a person would stand behind.

## Sources

- Wikipedia: Signs of AI writing. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Reinhart and others, "Do LLMs write like humans? Variation in grammatical and rhetorical styles", PNAS 2025. https://arxiv.org/abs/2410.16107
- Russell, Karpinska, Iyyer, "People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text", ACL 2025. https://arxiv.org/abs/2501.15654
- Shaib and others, "Detection and Measurement of Syntactic Templates in Generated Text", EMNLP 2024. https://arxiv.org/abs/2407.00211
- Kobak and others, "Delving into ChatGPT usage in academic writing through excess vocabulary". https://arxiv.org/abs/2406.07016
- GPTZero on perplexity and burstiness. https://gptzero.me/news/perplexity-and-burstiness-what-is-it/
- Community lists: https://github.com/archiewood/claudeisms and https://github.com/anthropics/claude-code/issues/53454
