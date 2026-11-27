#!/bin/sh
# WriteGooder 2.1 installer for Mac and Linux.
# From the makers of Concierge LLM: conciergellm.com/writegooder
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/write-gooder"

echo
echo " WriteGooder 2.1"
echo " Makes Claude and other assistants write like a person."
echo

if [ ! -f "$SRC/SKILL.md" ]; then
  echo " The write-gooder folder is missing. Unzip the whole download first, then run this again."
  exit 1
fi

DONE=0
for APP in claude codex; do
  if [ -d "$HOME/.$APP" ]; then
    mkdir -p "$HOME/.$APP/skills"
    rm -rf "$HOME/.$APP/skills/write-gooder"
    cp -R "$SRC" "$HOME/.$APP/skills/write-gooder"
    if [ "$APP" = "claude" ]; then echo " Installed for Claude Code."; else echo " Installed for Codex."; fi
    DONE=1
  fi
done

if [ "$DONE" = "0" ]; then
  echo " Claude Code and Codex were not found on this computer, so nothing was copied."
fi

cat <<'EOF'

 Two more ways to use it, if you want them:

  The Claude app or claude.ai:
    Settings, then Capabilities, then Skills. Upload write-gooder.skill from this folder.

  ChatGPT or any other assistant:
    Open WriteGooder_For_ChatGPT.txt, copy all of it, and paste it into
    a project's instructions.

 To use it, start a new chat and say: use WriteGooder to write this.
 To remove it, delete the write-gooder folder from .claude/skills in your home folder.

EOF
