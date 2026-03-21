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

---

## IDEA-003
**Date:** 2026-03-21
**Status:** Open

On activation, the Advisor should automatically read available artifacts before asking the Coordinator anything. Specifically: read sprint-status.yaml, any story files in ready-for-dev or in-progress status, project-context.md, and the latest brainstorming or planning artifacts if present. After reading, present three options:

1. Continue from current state — based on what was read, summarize where we are and what the next step is
2. Start a new session — if no artifacts exist or all stories are done
3. Something else — open question for the Coordinator

The Coordinator should never have to manually tell the Advisor what files to load. The Advisor reads first, then asks only what it cannot determine on its own.

---

## IDEA-003 Extension
**Date:** 2026-03-21

Extend IDEA-003 with context discovery. After reading standard artifacts (sprint status, story files, project-context.md), the Advisor should scan the project for additional context files — proposals, feature specs, design documents, brainstorming sessions, architecture docs — and present what it found to the Coordinator:

"I found these additional files that may be relevant: [list]. Should I include them as context?"

This is especially useful at the start of brainstorming or planning phases where proposal files and feature specs exist but are not part of the standard artifact set. The Advisor discovers them, the Coordinator approves inclusion. This removes the burden of manually feeding context files at session start.

The discovery should be intelligent — not every file in the repo, but files in known locations (docs/, proposals/, _bmad-output/) and files matching known patterns (*.proposal.md, FEATURE_*.md, brainstorming-*.md).

---
