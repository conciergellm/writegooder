# WriteGooder

A free skill for Claude Code, Codex and the Claude app, with a short version you can paste into ChatGPT. WriteGooder does its work before any writing starts. The model has to find out who you are in the piece, who you're writing to and what you think about it, and only then does it write, once, from notes. It doesn't take a finished draft and strip the AI phrases out.

The same post opening, from the same test results, written by the same model:

> **Asked the usual way:** Most "best local LLM for a 3090" posts tell you what fits in 24 GB. Fewer tell you what the model can finish once it's loaded. Tokens per second tells you how fast a model talks. It doesn't tell you whether it can do a job.

> **With WriteGooder:** We tested three Qwen models as agents on a PC with two RTX 3090s, and the one that fits on a single card finished the same jobs in about half the time of the one that needs both. I'd expected the two-card one to be the better agent, because it was bigger. I can't pin the difference on the models alone. The bigger one was allowed four times the thinking per turn, and we haven't rerun them matched.

## Install

**Claude Code**, from inside Claude Code:

```
/plugin marketplace add conciergellm/writegooder
/plugin install write-gooder@writegooder
```

**Codex, or Claude Code without the plugin system**

```
git clone https://github.com/conciergellm/writegooder
```

Then run `Install_WriteGooder.cmd` on Windows or `sh install.sh` on a Mac or Linux. Both copy the `write-gooder` folder into `~/.claude/skills` and `~/.codex/skills`, replacing any older copy, or you can copy the folder there yourself. Start a new chat afterwards. It should start on its own when you ask for a post, an email or a reply that goes out under your name, and you can also ask for it by name: "use WriteGooder to write this."

**The Claude app or claude.ai.** Download `write-gooder.skill` from the [latest release](https://github.com/conciergellm/writegooder/releases/latest) and upload it under Settings, Capabilities, Skills.

**ChatGPT or another assistant.** Paste the contents of [`WriteGooder_For_ChatGPT.txt`](WriteGooder_For_ChatGPT.txt) into a project's instructions. It has no second reader, and we haven't tested it yet.

## How it works

Before writing, it notes who is speaking and the one person who'll read it, and it asks you up to three questions where it would otherwise have to guess what you think. It's told never to make up a view, a story or a feeling for you. Then it writes from its notes as you talking to that reader, and a sentence it can't trace back to a note gets deleted. A fresh copy of the model reads the result as the reader, and the sentences it trips on are fixed one at a time. We don't let it rewrite the whole piece, because every time it did, the AI sound came back.

A list of 28 patterns we collected from our own drafts and from public lists is only used at the very end, as a cleanup. Two scripts check the draft along the way. They need Python 3 and nothing else, and the skill still works without them, minus those checks.

## What to expect

We tested it with Claude on three pieces, and a fresh copy of the same model judged each one. That's the model grading itself, so take it as a first look. An email written from the owner's own notes read to it as a person telling you what happened. A forum post with one opinion of the owner's in it read as a person, only just. A company reply written from a bare fact sheet still read as AI text with the patterns cleaned off. We haven't compared it with any other skill.

If you give it nothing of your own, it can make the text clearer, and that's as far as it goes. It does better if you say the thing out loud, roughly, and paste the transcript in, because then it mostly cuts and orders your own words.

A piece takes a few minutes, so keep it for things that go out under your name. It isn't built to get past AI detectors, and we haven't tested it against any. Nobody has run it on a small local model yet.

## Who made it

Markus, a video editor and motion designer, made it with Claude over three days of trying to get an AI to write our own posts. In his words it's "just for anyone who wants their LLM to not sound like an AI." The longer write-up is at [conciergellm.com/writegooder](https://conciergellm.com/writegooder/?s=github&c=writegooder). It's on the Concierge LLM site because we'd like you to know Concierge exists.

MIT licence, copyright 2026 Movemint LLC.
