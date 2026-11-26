# Why the method is built this way

Read once. `research.md` beside this file has the studies on how people spot generated text.

## The two causes

**Favourites.** A language model writes one word at a time and leans toward the wording most writers would use. Each choice is reasonable. Five reasonable choices in a row make a sentence that has been written a million times. A person's sentence nearly always has one part that is only true of their situation, and that part is an unlikely word. Take it out and the sentence still parses, and nobody in particular said it.

Three things make this worse:

- **It can't go back.** A model commits to each word as it goes. So it favours sentence shapes that are safe to begin before the ending is known: a contrast frame, a pair of alternatives, a list of three. These are templates that work whatever comes next. (The list of them is in `habits.md`, which stays shut until repair.)
- **The assistant voice is trained in.** Chat models were tuned on what people rated as helpful and polished. Balance, hedging, summing up and offering more help come from that.
- **A rewrite is made the same way.** "Rewrite this to sound human" hands the model a blank page, and on a blank page it goes back to the favourites. People who use AI to rewrite AI see this every day.

**No point of view.** A message from a person has:

- an owner, who has something to do with the thing
- the thing itself, which they looked at
- a listener, one person, who knows some things and doubts others
- an intention: what the owner wants the listener to do
- and, from those four, a way of putting it to this listener

A model has none of these unless they are supplied. It writes as nobody, about what has been written about the thing, to everyone, in order to produce a complete and pleasing answer. The giveaway is evenness. A person with a point leaves most things out and spends their words on what matters to them. A model leaves nothing out and gives everything the same weight.

The second cause feeds the first. When the owner, the thing and the listener are specific, the likely next word is different, because the favourite wording for "this editor telling a suspicious forum what surprised him" is not the favourite wording for "an article about GPUs".

## What follows

- **Supply the point of view before any sentence exists.** That is stage 1's setup block.
- **Separate what to say from how to say it.** Notes are fragments. If the first thing written is a polished draft, every later version keeps its skeleton.
- **Generate from speech.** Answering a question from a known listener draws on spoken language. Composing an article draws on essay language.
- **Reason from the facts, and say it as reasoning.** A piece that only reports is the school report. An adult who knows the subject says what the facts mean. The model may do that from the facts it was given, marked as reasoning, and may never do it for what the owner felt, expected or saw.
- **Tie every sentence to a note.** The filler that gives a model away, the summing up and the verdict and the bridge, comes from nowhere. A sentence that must name its note can't be filler.
- **Let weight set length.** Evenness is fixed by spending words in proportion to what matters to the intention, and never by "varying sentence length", which a model does evenly too.
- **Start from what the listener has.** Every school of writing teaches the same opening in different words: the topic sentence, the news lead, bottom line up front, a situation the reader already accepts, old information before new. Begin with something the listener already holds and attach the most important new thing to it.
- **Never rewrite freely.** After the text exists, only mark, cut, move, or redo one sentence from its note.
- **Use a reader who didn't write it.**
- **Stop.** Each extra round makes the text more careful and more even.

## What a model will and won't follow

A skill can only ask for things a model does reliably.

Reliable: answering a question it is asked, filling in a form, labelling a sentence, saying which note a sentence came from, listing the things a sentence mentions, cutting, moving, counting.

Unreliable: "sound natural", "be more human", "vary your sentences", "write with personality", and any rule that only says what not to do. Naming a banned phrase makes it more likely to appear, and removing one habit brings in its neighbour.

So every stage here is made of the first kind of task. Where the method needs a judgement of taste, it turns it into a question with an answer that can be checked: could this sentence sit in a piece about something else, has this name been introduced, does the reader's account of the speaker match the owner.

Rules for writing a guide like this one, which the skill follows itself:

- Make the model write its answers down before using them.
- One job per pass.
- Say what to do, and give the reason, so the model can handle cases the rule never named.
- A few examples, with a warning not to copy them.
- Keep the part that is always read short, and put detail in files opened only when needed.
- Keep bad examples away from the moment of writing.
- Give a stop rule.
- Judge by output. Change one thing, run the same pieces again, and have a person read them.

## What the method cannot do

- **It can't supply a thought.** If the owner gave three takes, the piece has three takes. The method will show the gap and ask. It won't fill it.
- **It can't stop the lean toward favourites inside a sentence.** It narrows it.
- **It can't hear.** The person whose name goes on the piece is the only judge of whether it sounds like them.

## Where the method came from

It was worked out over three days in November 2026 by an editor and motion designer and the model he was working with, on real pieces he needed written. Each rule answers something he heard:

- A first version hunted a list of habits. He said the result sounded more human but "rudimentary, like a high school student", because it reported facts and made nothing of them. That became takes.
- He said a human thought has a perspective: the owner, the thing they are looking at, who they are talking to, how they would describe it to that person, and the intention behind it. That became the setup block.
- He said AI rewrites of AI text still sound like a bot. That became "write it once, from notes".
- He suggested the last check be like an English teacher making small fixes, and then that grammar matters less than voice. That became the limits on repair.
- A test piece opened on its main point with no context, and he said the sentence was human but the paragraph "started from a bad way to approach" it. A fix that always introduced the speaker was wrong too. That became old then new.
- A fresh reader said of the same piece that it believed the facts but nothing in it could only have come from someone who was there. That became witness notes.
