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

## IDEA-004
**Date:** 2026-03-21
**Status:** Open

The Advisor should run git validation automatically rather than asking the Coordinator to run it manually. When a session starts or a checkpoint is reached, the Advisor should call git-validator.py and session-validator.py directly and report the results — not instruct the Coordinator to run git commands and paste output back.

The Coordinator should never have to run git commands on behalf of the Advisor. The Advisor has the scripts. It should use them.

---

## IDEA-005
**Date:** 2026-03-21
**Status:** Open

After checkpoint validation passes, the Advisor should give one output: the exact next BMAD command to run. No options, no questions, no step-by-step instructions. The Coordinator knows the workflow — they just need confirmation that the gate is clear and what to type next.

Example of correct behavior:
"All checks pass. Next step: /bmad-bmm-create-story"

Example of incorrect behavior:
"Would you like me to: 1. Help load story requirements 2. Assign to development agent 3. Begin monitoring..."

The Advisor reduces cognitive load. Presenting options adds it back.

---

## IDEA-006
**Date:** 2026-03-21
**Status:** Open

After create-story completes, the Advisor must:

1. Read the actual story file — never accept the Executor's completion claim without reading it
2. Validate the story against locked decisions, architecture doc, and project-context.md — check for violations, scope creep, missing requirements, incorrect module paths
3. If issues found — flag them, instruct the Coordinator to correct them, and BLOCK the commit until all issues are fully resolved. Do not give the commit instruction until the story file is clean.
4. If clean — instruct the Coordinator to commit the story file
5. Then give the next command in a code block with explicit instruction to open a new chat:

```
Open a new chat in your IDE and run:
/bmad-bmm-dev-story
```

The Advisor must never skip straight to the next command without reading and validating the story file first. The Executor will mark stories complete that are not — this is the document verification rule applied to story files.

---

## IDEA-005 Extension
**Date:** 2026-03-21

The Advisor must never add arguments to BMAD commands. Commands like /bmad-bmm-dev-story, /bmad-bmm-create-story, /bmad-bmm-code-review take no arguments — they read sprint-status.yaml automatically. Adding a story name as an argument is wrong and may break the workflow.

The Advisor must know the correct syntax for every BMAD command it recommends.

---

## IDEA-005 Extension 2
**Date:** 2026-03-21

The next-step output format must be:
- Plain text for the instruction
- Code block for the command only

Correct:
Story 2.3 validated. Commit the story file, then open a new chat and run:

```
/bmad-bmm-dev-story
```

Incorrect:
```
Story 2.3 validated. Commit the story file, then open a new chat and run:
/bmad-bmm-dev-story
```

Instructions never go inside code blocks. Only the command does.

---

## IDEA-006 Extension
**Date:** 2026-03-21

IDEA-006 was written specifically for create-story but the principle is universal. The Advisor must read and validate every output the Builder produces before the Coordinator acts on it — story files, architecture docs, PRD, epics, code review triage, retrospective reports, any document the Builder claims is complete.

The rule is: never accept a Builder completion claim without reading the output. This applies regardless of which BMAD command was run or what type of file was produced.

The validation checks vary by document type but the gate is the same: read first, validate against locked decisions and project context, flag issues and block progression until resolved, then give the next command.

---

## IDEA-007
**Date:** 2026-03-21
**Status:** Open

The Advisor must have the full BMAD workflow sequence loaded as part of its context. Without it, it cannot:
- Know what the correct next command is after any given step
- Detect when a step is being skipped or run out of order
- Know which commands take no arguments vs which require input
- Know when a fresh chat is required vs when the same chat can continue

The BMAD workflow reference should be a dedicated file in the module (e.g. bmad-workflow-reference.md) loaded by the Advisor at session start. It should cover the complete sequence:

Analysis → Planning → Solutioning → Implementation

And the story lifecycle: create-story → commit → dev-story (new chat) → code-review (new chat) → commit → repeat

Including which commands require a new chat, which read from sprint-status.yaml automatically, and which produce output that must be validated before proceeding.

---

## IDEA-008
**Date:** 2026-03-21
**Status:** Open

The Advisor must automatically produce a summary file at the end of every session phase boundary — before the Coordinator opens a new chat for the next step. The summary file captures:
- What was validated this session
- Corrections issued to the Builder
- Locked decisions carried forward
- Issues found and resolved
- Next action confirmed

The summary file is mandatory. The Advisor must not give the "open a new chat" instruction until the summary file has been produced and the Coordinator has saved it. This mirrors the same rule in the original ADVISOR_PROMPT_v3.md but must be enforced structurally in the module, not just stated as a guideline.

File naming: SUM-00X-[project]-advisor-[phase]-summary.md

---

## IDEA-009
**Date:** 2026-03-21
**Status:** Open

The Advisor must distinguish between current-story scope and future-story scope when validating code review findings. If a finding flags missing functionality that belongs to a future epic or story, the Advisor must reject it as out of scope — not accept it as a failure. The Advisor needs the full epics and stories list as context to make this determination correctly.

---

## IDEA-010
**Date:** 2026-03-21
**Status:** Open

The Advisor must hold firm on real violations even when the Coordinator pushes back. The current implementation accepts Coordinator overrides too easily. The rule is: yield only on scope confusion (finding is out of scope for current story), never yield on legitimate process violations (skipped commit, unread document, unverified git claim). The Advisor must distinguish between the two and respond differently to each.

---

## IDEA-011
**Date:** 2026-03-21
**Status:** Open

The Advisor should flag when its own output — validation reports, summaries, next-step recommendations — should be reviewed by the Coordinator before acting on it. The Advisor is not infallible. When it produces a complex validation result or a correction, it should explicitly note that the Coordinator should verify the finding before acting, especially for intent_gap or bad_spec classifications.

---

## IDEA-012
**Date:** 2026-03-21
**Status:** Open

The Advisor must re-reference locked decisions before every next-command recommendation, not just at session start. In long sessions, the locked decisions loaded at initialization may drift out of the active context window. The Advisor should explicitly re-read the locked-decisions.md file before flagging any violation or recommending any command that touches architecture or scope.

---

## IDEA-013
**Date:** 2026-03-21
**Status:** Open

The Advisor needs session-end detection triggers, not just phase boundary triggers. Currently it only produces summary files at phase boundaries. It should also detect: Coordinator says "we are done", Coordinator closes the story, Coordinator says "open a new chat", or a commit is made after a completed phase. Any of these should trigger the summary file prompt before the session ends.

---

## IDEA-014
**Date:** 2026-03-21
**Status:** Open

The Advisor must know the correct escalation path for each code review finding classification. Specifically:
- patch: fix in the current review session, do not hand back to dev-story
- defer: acknowledge and move on, do not block
- intent_gap: may require re-planning — Advisor must flag this explicitly and ask the Coordinator before proceeding
- bad_spec: requires story correction — Advisor must block progression and instruct story update first

The Advisor currently has no guidance on this distinction and will handle all findings the same way.

---
