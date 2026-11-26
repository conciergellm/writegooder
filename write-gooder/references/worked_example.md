# One piece through every stage

A forum post, taken from the first real test of this method. It shows the build of each stage. Don't borrow its wording or its facts for another piece.

The request: a post for a forum about running language models at home, from the maker of a paid app, reporting a test of three models. Nobody was available to answer questions.

## Stage 1: setup and notes

```
OWNER:       owner of a paid agent app that runs on local models; a video editor and
             motion designer. "I" for what he thought, "we" for the company's work.   [told]
THING:       three models on his own PC with two graphics cards: eight one-step
             questions and six longer jobs, with scores and times                       [told]
LISTENER:    one regular of that forum with one or two 24 GB cards who wants a model
             for tool calling. Knows the jargon. Doubts any post from an app maker,
             and doubts that six jobs prove much.                                       [guessed]
STARTS WITH: the forum's subject and the title; has never heard of the owner            [guessed]
WHERE:       a text post there; usually a few short paragraphs and a table             [told in part]
INTENTION:   reply with their own numbers on other hardware                            [told]
ANGLE:       the model that fits on one card did the same jobs in about half the time
             of the one that needs both                                                 [guessed]
VOICE:       level 3, no samples
```

Notes (a few of 32):

```
F4  A  one PC; two 24 GB cards; Windows 11                          [given]
F7  A  test a: 8 simple questions, one tool call each               [given]
F8  A  test b: 6 longer jobs: plan, several tools, check own result [given]
F10 A  model one: fits one card; longer jobs 6 of 6, about 2 min    [given]
F12 A  model two: needs both cards; 6 of 6, about 4 min             [given]
F15 C  cache setting on the two big models                          [given]
F17 A  thinking allowance: model two 4,096 a turn, model one 1,024; not rerun matched [given]
F25 B  model one about half model two's time                        [worked out]
T1  A  expected model two to be the better agent
Q1  A  "It was bigger."
T2  A  moved the app to model one; second card left free for his editing apps
R1  A  the time gap can't be put down to the models alone: thinking allowance differed 4 to 1 (rests on F17; sure)
T?  what did you make of the tie?
W?  what did you see on screen while the jobs ran?
```

Three takes and one piece of reasoning against 29 facts. By the rule in `writing.md`, that is a short piece with the settings in a table.

## Stage 2: write it as the owner

**Choose.** Left out: the cache setting, the prompt reading speeds, and a story about a job that lost its memory twice. The story was the hardest cut. It is the most useful thing in the material for someone with the same card, and it doesn't serve the intention of this post, so it is named at hand-over as a piece of its own.

**Open.** Old half, from STARTS WITH: models of this family tested as agents on these cards. New half, the angle.

**Talk** (tags shown, wording shortened here):

```
What happened?
  We tested three models as agents on a PC with two 24 GB cards, and the one that
  fits on a single card finished the same jobs in about half the time of the one
  that needs both. [F4, F10, F12, F25]

Is that the model or your settings?        <- the listener's strongest doubt, asked second
  I can't pin that on the models alone. The two-card model was allowed four times
  the thinking per turn, and we haven't rerun them matched. [R1, F17]

What did you expect?
  I'd expected the two-card one to be the better agent, because it was bigger. [T1, Q1]

Why should I believe a post from someone selling something?
  I make a paid agent app that runs on local models, and we ran this to choose
  the model for it. [F1, F3]

What did you test?   ...   Show me the numbers.   (table)   ...
What did you do about it?
  We moved the app to the one-card model, which leaves the second card free for
  my editing apps. [T2]

What don't you know?   ...
What do you want from me?
  If you run either model on a 4090, a 5090 or a 16 GB card, I'd like to see your
  time for a job with several tool calls. [F22]
```

Things to notice:

- The doubt came second, before the listener had time to harden it. A template would have put it in a "limitations" paragraph at the end.
- "because it was bigger" is his own wording, so it stays.
- The seller's line arrives fourth, in the answer to the question that needs it. Nothing made it go first.
- The ask names what to send. An earlier version said "I'd like to see your numbers", and the reader couldn't tell which numbers.
- No sentence says the cache setting. It sits in the table.

**Join.** Questions removed. "So" before "we moved the app" was checked: T2 says he moved because of the result, so the cause word has a note behind it.

**Title.** A label: speed and agent results for three models on these cards.

## Stage 3: what a fresh reader said about the first version

That version had opened with "I thought the bigger model would be the better agent because it was bigger". The reader's marks, shortened:

- It believed the speaker was a real person, because of two things: "a paid agent app" said plainly, and the second card being left free for his editing apps. "Nobody invents that."
- It didn't know what was being talked about until the second paragraph. The owner of this method said the same in his own words: the sentence sounded human, and the paragraph started from the wrong place.
- A "that" pointed at a number five paragraphs back.
- One paragraph only read a table row back.
- It didn't believe the ask.
- "Every sentence is about the same length ... nothing got him excited or annoyed ... there is not one thing he saw happen on screen."

## Stage 4: repair

- Cut: the paragraph that read the table back, a sentence that repeated the title, and two half-sentences the reader didn't need.
- Redone from notes: the opening, the sentence about the thinking allowance.
- Moved: the thinking allowance, up next to the times it explains.
- Left alone and reported: the definition of the longer jobs. The reader wanted one job spelled out, and no note had one.

## Hand over

After the text:

- Guessed: the listener, the usual length, and that he would lead with the time difference.
- Open questions, most useful first: What did you see on screen while the jobs ran? What was one of the six jobs, spelled out? Is "about 2 minutes" per job or for all six?
- Still in doubt: the last sentence, until the second question is answered.
- Voice level 3. A fresh reader checked it.
- The job that lost its memory twice is a good short post of its own.

## What the example shows

The stages didn't make this piece sound like its owner. They made it honest, ordered for its reader, and free of filler, and they ended by pointing at the two questions only he can answer. That is the method working. The last step is always the person's.
