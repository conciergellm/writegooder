# Stage 3: the listener reads

A model can't judge text it just wrote. It knows what it meant, so every sentence seems clear. The reader must be someone who has seen only the text.

## The brief

Start a separate agent and give it this brief, filled in, with the text (note tags removed). Give it nothing else: not the notes, not the setup block's other lines, not this skill.

```
You are the reader this was written for.

Who you are: <the LISTENER line>
What you already have in your head: <the STARTS WITH line>
Where you are reading it: <the WHERE line>

Read the text below once, the way that person would. Change nothing and
rewrite nothing. Answer these, and quote the exact sentences you mean:

1. Who is talking? What kind of person?
2. What do they want from me? Could I do it with what they told me?
3. Where did I not know yet what they were talking about?
4. Which sentences did I have to read twice?
5. Which sentences would nobody say out loud to me?
6. What didn't I need?
7. What do I still need?
8. Is there anything here that only someone who was there could have
   told me? Quote it, or say there is nothing.
9. Look at the whole thing without reading the words. Are the sentences
   all about the same length? Do the paragraphs come in the order a
   template would put them?
10. Does it read like (a) a person who did this telling me about it,
    (b) a careful school report, or (c) a model's text with the obvious
    habits removed? Say which, and which sentences decided it.

A loose, blunt or spoken sentence is intended. Don't mark grammar unless
a sentence can be misread. Don't be polite: if nothing is wrong with a
sentence leave it alone, and if something is, say so plainly.

<the text>
```

## Reading the answers

- **1 and 2 against OWNER and INTENTION.** If the reader describes a different kind of person, or "a company" or "nobody in particular", or gets the intention wrong, the choice of notes or the angle was wrong. Go back to "Choose" in stage 2, once. If the reader understood the ask and says it couldn't act on it, the last sentence needs to name what is wanted.
- **3 and 4** are known-before-new and broken references. Usually a move fixes them.
- **5** goes back to its note and is answered again, or is cut.
- **6** is cut. If the reader didn't need half a sentence, cut the half.
- **7** is the delicate one. If a note you left out answers it, use the note. If no note answers it, it is a question for the person. Don't write an answer.
- **8.** If the answer is "nothing", look for a `W` note you didn't use. If there is none, this goes at the top of the open questions at hand-over: "what did you see happen?"
- **9** can't be fixed sentence by sentence. See the weight rule in stage 4.
- **10.** An (a) with reservations is a pass. A (b) usually means facts with no takes. A (c) usually means every fact got its own even sentence. Both point back at "Choose and weigh", and often at missing takes that only the person has.

The reader is advice. It is one read by one model. Don't remove something that is part of the voice because the reader found it blunt, and don't add things because the reader is curious. The person is the judge.

## Without a separate agent

Reread your text from the top as the listener and answer the same ten questions in writing. You will be too kind to it. Two things help a little: answer question 2 before rereading the setup block, and for question 3 list every name and term in the first three sentences and ask where the listener met each one. Say at hand-over that no fresh reader checked it.
