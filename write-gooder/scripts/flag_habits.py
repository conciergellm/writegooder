#!/usr/bin/env python3
"""Flag the mechanical AI writing habits in a text file.

Usage: python flag_habits.py <file> [more files]

This is a net, not a judge. It finds dashes, bold lead-ins, header count,
contrast patterns, very short sentences, stock words and a few openers and
closers. It cannot hear a sentence, so a clean result does not mean the text
sounds like a person, and a flag is a place to look, not always a fault.
The exit code is always 0. Flags are places to look, not failures.
"""
import io
import re
import sys

STOCK = (
    "delve|dive in|deep dive|leverage|unlock|elevate|streamline|seamless(?:ly)?|robust|"
    "crucial|vital|landscape|journey|game.changer|testament|navigate|harness|tapestry|realm|"
    "effortless(?:ly)?|frictionless|cutting.edge|in today's|at the end of the day|"
    "when it comes to|honestly|truly|genuinely|needless to say|quietly|load.bearing|lean into|unpack|"
    "a testament to|plays? a (?:key|crucial|vital|pivotal) role|pivotal|multifaceted|dependable"
)
ANNOUNCE = (
    "it'?s worth noting|here are the|so here are|it is worth noting|worth mentioning|here'?s what|here'?s the thing|"
    "here'?s the catch|let'?s break|let'?s dive|the short answer|short answer:|the bottom line|"
    "in short,|in summary|in conclusion|to sum up|quick note"
)
READER = (
    "than you'?d think|you might be wondering|you may be wondering|if you'?re like most|"
    "we'?ve all been|whether you'?re|surprisingly|it turns out"
)
OPENERS = (
    "great question|good question|i hope this (?:email|message|note) finds|"
    "i wanted to reach out|i'?m reaching out|thanks for reaching out|just wanted to"
)
CLOSERS = (
    "hope this helps|let me know if|don'?t hesitate|feel free to|happy to (?:share|help|answer)|"
    "looking forward to hearing"
)
CONTRAST = (
    r",\s+not\s+\w+|\bnot just\b|\bnot only\b|\bisn'?t (?:just |about )?[^.?!]{1,60}[.;,]\s*it'?s\b|"
    r"\bless about\b|\brather than\b|\bas opposed to\b|\bmore than just\b"
)
NO_SUBJECT = r"^(?:Fewer|Most|Others|Some|The rest|Many|Few|The same goes)\s+(?!of\b)[a-z]+"


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def strip_md(line):
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
    return re.sub(r"[*_`>#]", "", line).strip()


def check(path):
    raw = io.open(path, encoding="utf-8").read()
    lines = raw.splitlines()
    flags = []

    def flag(n, kind, text):
        flags.append((n, kind, text.strip()[:110]))

    in_code = False
    front = bool(lines) and lines[0].strip() == "---"
    headers = 0
    paragraphs = []  # (line number, word count, text)
    all_sents = []
    block, block_start = [], 0

    def end_block():
        if block:
            text = " ".join(block)
            paragraphs.append((block_start, len(text.split()), text))
            block.clear()

    for i, line in enumerate(lines, 1):
        if front:
            if i > 1 and line.strip() == "---":
                front = False
            continue
        if line.strip().startswith("```"):
            in_code = not in_code
            end_block()
            continue
        if in_code:
            continue
        s = line.strip()
        if not s:
            end_block()
            continue
        if s.startswith("|"):
            end_block()
            continue
        if (re.match(r"#\s", s) or re.match(r"(?i)subject:\s", s)) and not paragraphs and not block and headers == 0:
            continue  # the title or an email's subject line
        if re.match(r"#{1,6}\s", s):
            headers += 1
            end_block()
            if s.rstrip().endswith("?") or len(s.split()) > 6:
                flag(i, "header that is a sentence or a question", s)
            continue
        if re.match(r"\*\*[^*]+\*\*\s*$", s):
            headers += 1
            flag(i, "bold line used as a header", s)
            end_block()
            continue

        if "—" in s:
            flag(i, "em dash", s)
        if re.search(r"\s[–-]\s", s) and not re.match(r"[-*]\s", s[:2] + " "):
            flag(i, "spaced dash doing an em dash's job", s)
        elif re.search(r"\w\s[–-]\s\w", s[2:]):
            flag(i, "spaced dash doing an em dash's job", s)
        if re.match(r"(?:[-*+]|\d+[.)])?\s*\*\*[^*]+\*\*", s) or re.match(
            r"(?:[-*+]|\d+[.)])\s*[*_][^*_]+[*_][:.]", s
        ):
            flag(i, "bold or italic lead-in", s)
        if re.search(r'"[^"]{8,}"\s+(?:posts?|articles?|guides?|videos?|threads?|people|crowd|approach|mindset|questions?|advice|moment|kind|type)\b', s):
            flag(i, "quoted phrase used as an adjective", s)
        if re.search(r"\w;\s", s):
            flag(i, "semicolon (often an em dash in disguise)", s)

        is_item = bool(re.match(r"(?:[-*+]|\d+[.)])\s", s))
        plain = strip_md(re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", s))
        plain = re.sub(r"^\d+[.)]\s+", "", plain)
        for sent in sentences(plain):
            words = sent.split()
            if 1 <= len(words) <= 4 and not re.match(r"^(?:Hi|Hello|Hey|Thanks|Thank you|Dear|Cheers|Best|Regards)\b", sent) and re.search(r"[.!]$", sent):
                flag(i, "very short sentence (is it there for effect?)", sent)
            if sent.endswith("?") and len(words) <= 9:
                flag(i, "short question (asked so you can answer it?)", sent)
            if re.search(NO_SUBJECT, sent):
                flag(i, "sentence may lean on the one before for its subject", sent)
            if not is_item and re.search(r":\s+\S", sent) and len(sent.split(":")[0].split()) <= 4 and not re.match(r"^(?:Subject|Title|Re|To|From|PS|P\.S)", sent):
                flag(i, "colon reveal", sent)
        for name, pat in (
            ("contrast line", CONTRAST),
            ("stock word", r"\b(?:" + STOCK + r")\b"),
            ("announcing", r"\b(?:" + ANNOUNCE + r")"),
            ("telling the reader what they think", r"\b(?:" + READER + r")"),
            ("opener", r"\b(?:" + OPENERS + r")"),
            ("closer", r"\b(?:" + CLOSERS + r")"),
        ):
            for m in re.finditer(pat, plain, flags=re.I):
                flag(i, name, plain[max(0, m.start() - 30): m.end() + 30])
        for m in re.finditer(r",\s+(?:highlighting|underscoring|emphasizing|ensuring|reflecting|making|allowing|enabling|showcasing|demonstrating|providing|creating|leaving|giving|turning|proving)\b[^.?!]*", plain):
            flag(i, "-ing tail (end the sentence when the fact ends)", m.group(0))
        for m in re.finditer(r"\b(?:serves?|stands?|acts?|functions?) as\b|\bboasts?\b", plain, flags=re.I):
            flag(i, "dressed-up is or has", plain[max(0, m.start() - 30): m.end() + 30])
        for m in re.finditer(r"\b(?:that'?s|this is) (?:what|the part|the real|where it gets)[^.?!]{0,40}[.!]|\band that matters\b|\blet that sink in\b|\bhere'?s the kicker\b|\bhonestly\?", plain, flags=re.I):
            flag(i, "verdict line", m.group(0))
        all_sents.extend((i, x) for x in sentences(plain) if len(x.split()) >= 3)
        for m in re.finditer(r"\b(\w+), (\w+),? and (\w+)\b", plain):
            flag(i, "three in a row (were there really three?)", m.group(0))

        if not re.match(r"(?:[-*+]|\d+[.)])\s", s):
            if not block:
                block_start = i
            block.append(plain)
        else:
            end_block()
    end_block()

    prose = [p for p in paragraphs if p[1] >= 8]
    if headers and len(prose) and headers >= max(3, len(prose) * 0.5):
        flag(0, "headers", "%d headers over %d paragraphs" % (headers, len(prose)))
    if len(prose) >= 4:
        counts = [p[1] for p in prose]
        mean = sum(counts) / float(len(counts))
        spread = (sum((c - mean) ** 2 for c in counts) / len(counts)) ** 0.5
        if mean and spread / mean < 0.25:
            flag(0, "paragraphs all about the same size", "word counts: " + ", ".join(map(str, counts)))
    run = 1
    for k in range(1, len(all_sents)):
        same = all_sents[k][1].split()[0].lower() == all_sents[k - 1][1].split()[0].lower()
        run = run + 1 if same else 1
        if run == 3:
            flag(all_sents[k][0], "three sentences in a row start the same way", all_sents[k][1].split()[0] + " ... " + all_sents[k][1][:60])
    if len(all_sents) >= 8:
        lens = [len(x.split()) for _, x in all_sents]
        mean = sum(lens) / float(len(lens))
        spread = (sum((c - mean) ** 2 for c in lens) / len(lens)) ** 0.5
        if spread / mean < 0.35:
            flag(0, "sentences all about the same length", "average %d words, little variation" % mean)
    bullets = sum(1 for l in lines if re.match(r"\s*(?:[-*+]|\d+[.)])\s", l))
    body = sum(1 for l in lines if l.strip())
    if body and bullets >= 4 and bullets / float(body) > 0.4:
        flag(0, "mostly bullets", "%d of %d lines are list items" % (bullets, body))

    print("== %s  (%d headers, %d paragraphs)" % (path, headers, len(prose)))
    if not flags:
        print("   nothing flagged (still read it aloud)")
    for n, kind, text in sorted(flags):
        where = "line %d" % n if n else "whole text"
        print("   %-10s %s: %s" % (where, kind, text))
    if paragraphs:
        print("   last lines, check by eye: " + sentences(paragraphs[-1][2])[-1][:140])
    return len(flags)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    total = sum(check(p) for p in sys.argv[1:])
    print("%d places to look" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
