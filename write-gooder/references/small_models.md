# Small models and programs that drive the stages

A small local model can't hold a long guide in its head, loses the start of a long conversation, and skips a long road. A program around it can hold what it can't. So for a small model the method is the same, and it is delivered differently: one stage per call, each as a short form, with the program keeping the outputs and running the checks.

This applies to assistants like Concierge that run on a local model, and to anyone wiring WriteGooder into their own tool.

Not yet proven: as of 25 November 2026 none of this has been run on a local model. Treat the forms as a first version and judge them by output.

## Principles

- **Code holds, prompts don't.** Anything that can be checked by a program is checked by the program, and the model is only told the result.
- **One call, one job.** Each call sees only what that job needs. The habit list is never in a call that writes.
- **Forms, not essays.** The model fills in fields. A field left empty is a question for the person.
- **Short flags.** A check answers in at most eight plain lines, each with a reason.
- **The program keeps the notes.** The model is handed the notes it needs by number.

## The calls

**Call 1, setup.** Give the request and whatever the person supplied. Ask for exactly this:

```
OWNER:
I OR WE:
THING:
LISTENER (one person):
THEY DOUBT:
STARTS WITH:
WHERE AND LENGTH:
INTENTION (what they do afterwards):
ANGLE:
```
After each line, `told` or `guessed`. Program: any `guessed` on OWNER, INTENTION or ANGLE becomes a question to the person, three at most.

**Call 2, notes.** Give the material. Ask for a numbered list, one fragment per line, each starting with `F`, `T`, `W`, `Q` or `R`, and `A`, `B` or `C`. Rules in the prompt: fragments only; `T`, `W`, `Q` only if the person said it; otherwise `T?` with the question; an `R` line names the facts it rests on. Program: reject lines that end in a full stop and run over about 14 words (they are sentences), and reject a `T` or `W` whose words don't appear in the person's material.

**Call 3, opening.** Give STARTS WITH, ANGLE and the A notes. Ask for one sentence: first half something the listener already has, second half the angle, with note tags. Program: `check_draft.py` on it.

**Call 4, talk.** One question per call. Give the setup block, the question, the notes not yet used, and the sentences so far. Ask for an answer of one or two sentences with note tags, built on a take where there is one. The program chooses the next question from the fixed set, puts THEY DOUBT second, and stops when the A notes are used or the length is reached.

**Call 5, join.** Give the answers in order. Ask only for: the order to put them in, where paragraphs break, and a joining word between any two (from the allowed list, or none). The program applies it. The model writes no new sentence here.

**Check.** The program runs `check_draft.py` and sends back any sentence it names with one instruction each: "no note behind this, cut it or give its note", "this uses 'the 27B' before the full name", "this paragraph has no take".

**Call 6, reader.** A fresh call with no history: the brief from `reader.md` and the clean text. On one machine with one model this is the same model with an empty context, which is weaker than a different reader but much better than none.

**Call 7, repair.** One marked sentence per call. Give the sentence's notes and the question it answered, and not the old sentence. Ask for the answer again. The program runs `flag_habits.py` on the result. One round.

**Hand over.** The program assembles it: clean text, guessed lines, open questions.

## Level 1 for a small model

When the person dictated it, the calls are simpler and safer: setup, then one call that returns only a list of line numbers to keep and their order, then the reader. The model never writes a sentence.

## What to expect

A small model will do the forms well and the taste parts badly. That is why the taste parts are forms. Expect plainer text than a large model gives, with fewer faults than the same small model writing freely. Whether it sounds like a person is still for the person to say.
