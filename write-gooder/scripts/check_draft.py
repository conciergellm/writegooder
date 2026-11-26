#!/usr/bin/env python3
"""Check a tagged WriteGooder draft (stage 2).

Usage:
  python check_draft.py <tagged text> [--notes <notes file>] [--clean <out file>]

The tagged text has the notes each sentence came from in brackets after it,
like [F3, T1]. This script contains no bad phrases, so it is safe to run
before the habit list is opened.

It reports, in at most eight plain flags:
  - sentences with no note behind them
  - paragraphs with no take, witness or quote note (facts only)
  - cause words in a sentence that has no take behind it
  - a short name used before its full name
  - sentences all about the same length, or no short sentence at all
  - a title that is a sentence
  - how many notes were left out, and takes that were never used (with --notes)
Then it prints the first sentence of every paragraph for the skim check.

--clean writes the text with the tags removed.
It is a net, not a judge. The exit code is always 0.
"""
import io
import re
import sys

TAG = re.compile(r"\s*\[((?:\s*[FTWQR]\d+[a-z]?\??\s*,?)+)\]")
NOTE_ID = re.compile(r"[FTWQR]\d+[a-z]?")
CAUSE = re.compile(r"\b(so|because|since|which is why|therefore|that's why|as a result)\b", re.I)


def split_sentences(text):
    # a sentence ends at . ! or ? only when white space or the end follows,
    # so "Qwen3.6" and "b11223." inside a line are not split in the middle
    out, end = [], 0
    for m in re.finditer(r".+?[.!?][\"')]*(?:\s*\[[^\]]*\])*(?=\s+|$)", text, flags=re.S):
        s = m.group(0).strip()
        if s:
            out.append(s)
        end = m.end()
    rest = text[end:].strip()
    if rest:
        out.append(rest)
    return out


def read_notes(path):
    ids, kinds = [], {}
    for line in io.open(path, encoding="utf-8").read().splitlines():
        m = re.match(r"\s*(?:[-*]\s*)?(?:\d+[.)]\s*)?([FTWQR]\d+[a-z]?)(\?)?\b", line)
        if m and not m.group(2):
            ids.append(m.group(1))
            kinds[m.group(1)] = m.group(1)[0]
    return ids, kinds


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    path = args[0]
    notes_path = args[args.index("--notes") + 1] if "--notes" in args else None
    clean_path = args[args.index("--clean") + 1] if "--clean" in args else None

    raw = io.open(path, encoding="utf-8").read()
    lines = raw.splitlines()

    title = None
    paragraphs = []  # list of str
    block = []
    table_tag_lines = 0
    for line in lines:
        s = line.strip()
        if title is None and not paragraphs and not block and (s.startswith("#") or re.match(r"(?i)subject:\s", s)):
            title = re.sub(r"(?i)^(?:#+\s*|subject:\s*)", "", s)
            continue
        # a greeting or a sign-off carries no note
        if len(s.split()) <= 5 and (s.endswith(",") or re.match(r"(?i)^(hi|hello|hey|dear|thanks|thank you|cheers|best|regards)\b", s) or (len(s.split()) <= 2 and not re.search(r"[.!?\]]$", s))):
            if block:
                paragraphs.append(" ".join(block))
                block = []
            continue
        if not s:
            if block:
                paragraphs.append(" ".join(block))
                block = []
            continue
        if s.startswith("|") or re.match(r"^#{1,6}\s", s) or s.startswith(">"):
            if block:
                paragraphs.append(" ".join(block))
                block = []
            continue
        if TAG.fullmatch(" " + s) or re.fullmatch(r"\[[^\]]*\]", s):
            table_tag_lines += 1
            continue
        block.append(s)
    if block:
        paragraphs.append(" ".join(block))

    flags = []
    used = set(NOTE_ID.findall(" ".join(re.findall(r"\[[^\]]*\]", raw))))

    untagged, cause_no_take, lengths = [], [], []
    facts_only = []
    for p in paragraphs:
        sents = split_sentences(p)
        para_kinds = set()
        for s in sents:
            ids = NOTE_ID.findall(" ".join(re.findall(r"\[[^\]]*\]", s)))
            bare = TAG.sub("", s).strip()
            n = len(bare.split())
            if n >= 3:
                lengths.append(n)
            if not ids and n >= 3:
                untagged.append(bare)
            kinds = set(i[0] for i in ids)
            para_kinds |= kinds
            if ids and CAUSE.search(bare) and not (kinds & set("TWQR")):
                cause_no_take.append((CAUSE.search(bare).group(1), bare))
        if len(sents) >= 2 and para_kinds and not (para_kinds & set("TWQR")):
            facts_only.append(TAG.sub("", sents[0]).strip())

    if untagged:
        flags.append("%d sentence(s) with no note behind them. Give the note or cut: \"%s\"" % (
            len(untagged), untagged[0][:90]))
    if facts_only:
        flags.append("%d paragraph(s) of facts only, with no take, witness, quote or reasoning note (an ask or a line of settings is fine). First one starts: \"%s\"" % (
            len(facts_only), facts_only[0][:80]))
    if cause_no_take:
        w, s = cause_no_take[0]
        flags.append("%d sentence(s) use a cause word with only fact notes behind it. Fine if a given fact states the cause; otherwise use \"and\". \"%s\" in: \"%s\"" % (
            len(cause_no_take), w, s[:80]))

    # a short name used before its full name
    clean_all = TAG.sub("", " ".join(paragraphs))  # the body only: a title introduces nothing
    longnames = set(re.findall(r"\b([A-Z][\w.]*[\w](?:[ -][\w.]*\d[\w.-]*)+)", clean_all))
    seen_short = set()
    for full in sorted(longnames, key=len, reverse=True):
        short = re.split(r"[ ]", full)[-1]
        if len(short) < 2 or short in seen_short:
            continue
        first_full = clean_all.find(full)
        m = re.search(r"\bthe " + re.escape(short) + r"\b", clean_all)
        if m and m.start() < first_full:
            seen_short.add(short)
            flags.append("\"the %s\" is used before \"%s\" has been named in full." % (short, full))

    if len(lengths) >= 8:
        mean = sum(lengths) / float(len(lengths))
        spread = (sum((c - mean) ** 2 for c in lengths) / len(lengths)) ** 0.5
        if spread / mean < 0.35:
            flags.append("Sentences are all about the same length (average %d words). Length should follow weight: fold a C fact into a neighbour, give an A point more." % mean)
        elif min(lengths) > 11:
            flags.append("No sentence under 12 words (shortest is %d). A short sentence that carries a take is how people talk." % min(lengths))

    if title:
        t_words = len(title.split())
        if title.rstrip().endswith((".", "!", "?")) or t_words > 14 or re.search(r":\s", title):
            flags.append("The title reads as a sentence or carries a payoff (%d words). A title is a plain label." % t_words)

    if notes_path:
        ids, kinds = read_notes(notes_path)
        if ids:
            left = [i for i in ids if i not in used]
            share = len(left) / float(len(ids))
            unused_takes = [i for i in left if kinds[i] in "TWQ"]
            if unused_takes:
                flags.append("Takes, witness notes or quotes not used: %s. These are usually the best material; fine if you weighed them C." % ", ".join(unused_takes))
            flags.append("%d of %d notes left out (%d%%)%s" % (
                len(left), len(ids), round(share * 100),
                ". With raw material expect a third or more; fine if the material was already chosen for you." if share < 0.2 else "."))
            own = [i for i in ids if kinds[i] in "TWQ"]
            if not own:
                flags.append("No take, witness or quote notes at all. Nothing in this piece is the owner's own view: say so at hand-over, and carry it with reasoning (R) notes.")
            unknown = sorted(i for i in used if i not in ids)
            if unknown:
                flags.append("Tags that match no note: %s." % ", ".join(unknown))

    print("== %s" % path)
    if not flags:
        print("   nothing flagged")
    for f in flags[:8]:
        print("   - " + f)
    if len(flags) > 8:
        print("   (%d more not shown)" % (len(flags) - 8))
    print("   Skim check, first sentence of each paragraph:")
    for k, p in enumerate(paragraphs, 1):
        first = split_sentences(p)[0] if split_sentences(p) else p
        print("     %d. %s" % (k, TAG.sub("", first).strip()[:150]))

    if clean_path:
        clean = TAG.sub("", raw)
        clean = "\n".join(l for l in clean.splitlines() if not re.fullmatch(r"\s*\[[^\]]*\]\s*", l) or not l.strip())
        clean = re.sub(r"\n{3,}", "\n\n", clean)
        io.open(clean_path, "w", encoding="utf-8").write(clean.rstrip() + "\n")
        print("   clean text written to %s" % clean_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
