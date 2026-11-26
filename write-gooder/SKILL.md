---
name: write-gooder
description: WriteGooder. Write prose that sounds like a person said it. The text is written once, from notes, as one person talking to one other person, then read by a fresh listener and repaired a sentence at a time. Use this whenever you write or rewrite anything a person will publish or send under their own name, such as an article, blog post, Reddit or forum reply, email, newsletter, social post, product page, listing, bio, cover letter or white paper, even if they don't ask for a "human" voice. Also use it whenever someone says a text sounds like AI, sounds generated, robotic, generic, salesy or "not like me", or asks to humanize it, make it natural, or make it sound like a person wrote it. Not for code, reference documentation, legal text or everyday answers in chat.
---

# WriteGooder

Version 2.0, 25 November 2026.

## Why a model sounds like a model

Two things cause it, and this method is built against both.

**It picks the favourite every time.** At each word a model takes the wording most writers would take. A sentence with five parts gets the favourite for each of the five. No person does that five times running, because somewhere in the sentence they say the one thing that is only true of their situation. A sentence made only of favourites is correct and belongs to nobody. A model also can't go back, so it likes sentence shapes that are safe to start before it knows the ending, and it was trained toward a helpful, balanced, polished voice that sums everything up.

**It has no point of view.** A person's message comes from somewhere. There is an owner, the thing they are looking at, the one person they are telling, and what they want that person to do. By default a model has none of these. It writes as nobody, about what has been written about the thing, to everyone at once, and its only intention is to hand back a complete and pleasing answer. So it covers everything evenly and leaves nothing out, and a reader hears that inside two lines.

Asking a model to rewrite its text doesn't help, because the rewrite is made the same way. The second cause feeds the first: when the owner, the thing and the listener are real and specific, the likely next word changes. So most of the work here happens before any sentence is written.

`references/why.md` has the longer account. The first time you use this skill in a conversation, read it and `references/worked_example.md` before stage 1, then put both away. They are not open while you write.

## When rules pull against each other

They sometimes do. This is the order that wins:

1. Invent nothing.
2. The listener can follow it (known before new, nothing left hanging).
3. The intention: what the listener is to do.
4. Every paragraph has something of the owner's in it.
5. Advice about order, such as where the doubt goes.

A flag from a script is a place to look. Never change a sentence only to make a flag go away, at any stage.

## The five rules that hold on every road

1. **Write it once, from notes.** After the notes nothing is ever freely rewritten. Later stages only mark, cut, reorder, or redo one sentence from the note it came from.
2. **Invent nothing.** Facts come from what you were given. What the owner thinks, expected, saw or wants comes only from the owner. A missing one is a question or a visible gap, never a guess dressed as theirs.
3. **Write it down before you use it.** You only know what you have written. Each stage writes its output before the next begins.
4. **Keep the habit list shut until repair.** Reading bad phrases before writing makes you more likely to write them. `references/habits.md` is opened in stage 4 and not before.
5. **One round, then stop.** More rounds make a text stiffer and more even. The person whose name goes on it is the judge.

## Which road

- **You can start a separate agent and run code:** use everything below. This is the full road.
- **You are in a plain chat with no tools:** the same stages, with you rereading as the listener in stage 3. Say at hand-over that the check was weaker. `WriteGooder_For_ChatGPT.txt` beside this skill is the pasteable version.
- **You are a small local model, or a program is driving you one step at a time:** read `references/small_models.md`. It gives each stage as a short form.
- **The person already said or wrote it roughly themselves** (a voice note, a rough paragraph): that is the best material there is. Go to "Their own words" in `references/voice.md`. You will cut and order and write nothing new.

## Stage 1: setup and notes

Write this block. Tag every line `told`, `told in part` or `guessed`.

```
OWNER:       who is saying this, what they have to do with it, and whether they say "I" or "we"
THING:       what exactly they are looking at
LISTENER:    one person in one place, what they already know, what they doubt or suspect
STARTS WITH: what the listener has in their head when they begin reading
             (what they asked, the title, the thread, what they know about the owner)
WHERE:       where it will be read, and how long things usually are there
INTENTION:   what the owner wants the listener to do or decide afterwards
ANGLE:       the main thing the owner wants this listener to take away
VOICE:       level 1, 2 or 3 (see references/voice.md; this line needs no tag)
SENT:        the date it goes out (leave the line out if the piece names no day or deadline)
```

Read `references/voice.md` now to choose the VOICE level.

- The listener is one person, never "a general audience". When it goes to several people, pick the one most of them are like, and afterwards check that no sentence is false for the others ("the empty app you got" is false for a tester who never hit the bug).
- The intention is something the listener does or decides. "To inform" and "to raise awareness" don't count. For a reply to someone's question, the default intention is that they can now make the decision they asked about.
- A guess about what the owner thinks or wants is a question for the person.

Then write the NOTES as a numbered list of fragments. Never write finished sentences here, because a finished sentence gets copied into the text. There are five kinds:

- `F` **facts.** Tag each `given` or `worked out`. Arithmetic on given facts is worked out. A conclusion or a judgement is not a fact, even if it sounds like one.
- `T` **takes.** What the owner makes of a fact: what they expected, what surprised them, what they changed because of it, what they would tell someone else, what they can't explain.
- `W` **witness.** Something only a person who was there could report: what they saw happen, what went wrong while they watched, what annoyed them. A single event the owner watched and timed ("one edit took 11 minutes 46 seconds") is a witness note even when it arrives in a list of facts. One of these does more for a piece than any amount of polish.
- `Q` **their words.** A view, a feeling, an apology or a wish the owner put in their own wording, including in the brief ("I'm sorry it happened", "It was bigger"). A plain statement of fact in a brief is an `F` note even when it says "we". When a `Q` note is used, it goes in exactly as they said it, at any voice level; you may change who it is said to ("them" to "you") and nothing else. It is still weighed like any other note, and a C is left out.
- `R` **reasoning.** What follows from the facts, worked out by you: the answer to the question the listener asked, a recommendation, a likely cause. Write which facts it rests on and how sure it is. This is allowed and wanted, because a piece that only reports facts reads like a school report. It has two limits. It is said as reasoning ("on our tests", "as far as we can tell", "that would mean") and never as certainty the facts don't give. And it is never about what the owner expected, felt, saw or wants, which only they can say.

`T`, `W` and `Q` come only from the owner, who may be a person or a company speaking as "we". Where one is missing and would matter, write `T?` or `W?` with the question you would ask.

Start each note line with its kind, number and weight, like `F3 A two cards, 24 GB each [given]`. The check script reads that form. One note may stand behind more than one sentence.

**Asking.** If the person is there, ask at most three questions, once, and choose the three that would add the most. A good default set: what did you expect and what surprised you, what did you see happen, and what do you want the reader to do. If nobody is there to ask, carry on, keep the tags, and list the open questions at hand-over.

**Weigh the notes.** Mark each note against the intention:

- `A`: the listener must have this for the intention to work.
- `B`: it supports an A.
- `C`: true, and this listener doesn't need it.

## Stage 2: write it as the owner

Read `references/writing.md` now, every time. This is the stage where the text is made, so it has the most detailed instructions. In short:

1. **Choose.** Use the A notes, hang the B notes off them, and leave the C notes out or give them a few words. List what you left out.
2. **Open.** The first sentence has two halves: something the listener already has, then the most important new thing about it.
3. **Talk.** The listener asks, the owner answers out loud, two sentences at most per answer. Every sentence carries the notes it came from in brackets, like `[F3, T1]`.
4. **Join.** Remove the questions. Add only short joining words. Reorder whole answers if a reference would otherwise be left hanging.
5. **Title.** If the piece has one: a plain label, written last, with no tags.

Have only the setup block, the notes and `references/writing.md` in front of you while you write.

Keep the stages as separate files or sections so each can be checked: the setup and notes together, then the choice and the talk, then the tagged text, then the clean text.

When the tagged text is done, run the check if you can run code. The scripts are in this skill's `scripts` folder: `python <skill folder>/scripts/check_draft.py <tagged file> --notes <notes file>` (on Windows set `PYTHONIOENCODING=utf-8` first). It names sentences with no note behind them, paragraphs with nothing of the owner's in them, cause words to check, a short name used before its full name, and even sentence lengths, and it prints the first sentence of each paragraph so you can check they give the piece in small. It contains no bad phrases, so it is safe to run before repair.

Look at each thing it names and decide by the rules in `references/writing.md`. Some flags are right to leave: a cause word is fine when a given fact states the cause, an ask paragraph has no take in it, and nothing is left out when the material was already chosen for you.

## Stage 3: the listener reads

`references/reader.md` is the brief for a fresh reader. Hand it to a separate agent with the text (tags removed) and the LISTENER, STARTS WITH and WHERE lines, and nothing else. A reader that didn't write the text is a better judge than you are.

The reader changes nothing. It says who is talking, what they want, where it got lost, what nobody would say aloud, what it didn't need, what it still needs, and whether there is anything in the piece that only someone who was there could have told it.

If the reader's account of who is talking and what they want doesn't match OWNER and INTENTION, the choice of notes or the angle was wrong. Go back to "Choose" once.

## Stage 4: repair

Now open `references/habits.md`, and run `python <skill folder>/scripts/flag_habits.py <clean file>` if you can run code. Mark every sentence that shows a habit. Add the reader's marks. Then read each sentence once more against two things the reader can't know: is it false for any of the other people it goes to, and is every day or date right for the SENT date.

For each marked sentence, do one of these and nothing else:

- **Cut it,** or cut the half of it the listener didn't need. Two cut-down halves may be joined with a short joining word.
- **Redo it from its notes.** Cover the old sentence. Look only at its notes and the listener's question it answered, and answer again. Don't rephrase the old wording, because that keeps its skeleton. If the new answer comes out close to the old one, the old one was fine. Leave it.
- **Move it.** A whole sentence or paragraph may be moved so that a reference sits next to what it points at.

Rules for this stage:

- Anything added must come from the notes. Notes you left out in "Choose" may be used here if the reader asked for them.
- If the reader needs something that is in no note, don't write it. Leave the sentence as it is and put the question in the hand-over. A need that belongs to no sentence ("will my projects come back?") goes straight to the hand-over.
- When a sentence would be wrong or unusable without an answer only the person has (a deadline that can be read as two days, a link that isn't there), put a visible gap in the text, in square brackets, like `[which Wednesday?]`. A gap the person can see is better than a sentence that looks finished and isn't.
- A title or subject line is redone from the notes the same way, as a label.
- The reader marks spoken, blunt or loose sentences only when they can be misread. Don't tidy a sentence because it sounds like talk, and don't remove something that is part of the voice.
- Don't change a sentence only to clear a flag from the script.
- Marks about the whole text (every sentence the same length, a template order, no witness moment) can't be fixed sentence by sentence. Try the weight rule once: fold a C fact into its neighbour, or give the most important point a second sentence from a `W` or `T` note. If there is no such note, say so at hand-over. It needs the person, not another round.

One round. Check the changed sentences once more against the habit list (run the script again if you can) and stop.

## Hand over

Give the text with the tags removed (`check_draft.py --clean` does this). After it, in a few lines:

- first, whether it is ready to go out, and if not, the one or two things that stop it (a gap in brackets, a placeholder link)
- what you guessed (every `guessed` line in the setup), and anything that is yours and not theirs, such as a subject line, a greeting or a sign-off
- the open questions, in the order a reader would ask them, with the one or two that would improve the piece most at the top
- sentences you still doubt
- which voice level you used, and whether a fresh reader checked it

Don't describe the stages or list what you changed unless asked.

## Files

- `references/writing.md`: stage 2 in full. Choosing and weighing, the opening, the talk, the rules for a sentence, joining, titles, tables, and what changes by kind of piece. Read at stage 2, every time.
- `references/voice.md`: the three voice levels, the voice card, and the road for text the person already said themselves. Read at stage 1 when choosing the level.
- `references/reader.md`: the fresh reader's brief, and what to do with its answers. Read at stage 3.
- `references/habits.md`: the faux pas list with bad and better pairs. Stage 4 only.
- `references/worked_example.md`: one piece taken through every stage. Read it the first time you use this skill in a conversation.
- `references/why.md`: why models sound like models, the research, and why the method is built this way. Read once.
- `references/research.md`: the studies and public lists on how people spot generated text.
- `references/small_models.md`: each stage as a short form, for a small local model or a program that drives the stages.
- `scripts/check_draft.py`: checks on the tagged text. Stage 2.
- `scripts/flag_habits.py`: the mechanical habits. Stage 4.

WriteGooder is free, from the people who make Concierge LLM. Its home is https://conciergellm.com/writegooder/
