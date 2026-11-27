@echo off
setlocal
title Install WriteGooder
echo.
echo  WriteGooder 2.1
echo  Makes Claude and other assistants write like a person.
echo  From the makers of Concierge LLM: conciergellm.com/writegooder
echo.

set "SRC=%~dp0write-gooder"
if not exist "%SRC%\SKILL.md" (
  echo  The write-gooder folder is missing. Unzip the whole download first, then run this again.
  echo.
  pause
  exit /b 1
)

set DONE=0

if exist "%USERPROFILE%\.claude" (
  if exist "%USERPROFILE%\.claude\skills\write-gooder" rmdir /s /q "%USERPROFILE%\.claude\skills\write-gooder"
  xcopy "%SRC%" "%USERPROFILE%\.claude\skills\write-gooder\" /e /i /q /y >nul
  echo  Installed for Claude Code.
  set DONE=1
)

if exist "%USERPROFILE%\.codex" (
  if exist "%USERPROFILE%\.codex\skills\write-gooder" rmdir /s /q "%USERPROFILE%\.codex\skills\write-gooder"
  xcopy "%SRC%" "%USERPROFILE%\.codex\skills\write-gooder\" /e /i /q /y >nul
  echo  Installed for Codex.
  set DONE=1
)

if "%DONE%"=="0" (
  echo  Claude Code and Codex were not found on this computer, so nothing was copied.
)

echo.
echo  Two more ways to use it, if you want them:
echo.
echo   The Claude app or claude.ai:
echo     Settings, then Capabilities, then Skills. Upload write-gooder.skill from this folder.
echo.
echo   ChatGPT or any other assistant:
echo     Open WriteGooder_For_ChatGPT.txt, copy all of it, and paste it into
echo     a project's instructions.
echo.
echo  To use it, start a new chat and say: use WriteGooder to write this.
echo  To remove it, delete the write-gooder folder from .claude\skills in your user folder.
echo.
pause
