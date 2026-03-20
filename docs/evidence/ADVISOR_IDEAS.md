# Advisor Prompt — Running Ideas File
**Purpose:** Capture prompt improvement ideas as they emerge across sessions.
**How to use:** Share this file at the start of each session alongside project-context.md and ADVISOR_PROMPT. Append new ideas as they are discovered. Never overwrite existing entries.

---

## IDEA-001
**Date:** 2026-03-19
**Status:** Open

Add a section to ADVISOR_PROMPT instructing the Advisor to automatically produce a mistakes file at the end of each story cycle (after code-review patches are committed, before the next create-story). The mistakes file should be named `ADVISOR_SESSION_MISTAKES_00X.md` with an incrementing number. The Advisor must not wait to be asked — producing it is a mandatory step in the story lifecycle, the same way the summary file is mandatory at phase boundaries.

---

## IDEA-002
**Date:** 2026-03-19
**Status:** Open

Expand the commit checkpoint rule to cover the full BMAD lifecycle, not just dev-story and code-review. Every BMAD command that produces output — brainstorming, create-prd, create-architecture, create-epics-and-stories, create-story, dev-story, code-review, retrospective — must be followed by a commit before a new session opens. The Advisor must enforce this checkpoint after every command that produces files, not only during implementation.

---
