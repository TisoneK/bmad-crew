# Advisor Session Mistakes Log
**Session:** SCR-003 Epic 1 → Epic 2 transition
**Date:** 2026-03-19
**Purpose:** Prompt tightening — failures observed in this session

---

## Mistake 1: Recommended wrong workflow command

**What happened:**
After Epic 1 was confirmed done and sprint-status.yaml clearly showed Epic 2 as `backlog` with no sprint plan needed, the Advisor recommended `/bmad-bmm-sprint-planning`. Sprint planning runs once per feature and had already been completed.

**Root cause:**
Defaulted to a standard phase sequence without checking sprint-status.yaml first.

**Prompt fix needed:**
Before recommending any workflow command, the Advisor must check sprint-status.yaml to determine the actual current state. If sprint planning is already done (stories exist in backlog), skip directly to `create-story`.

---

## Mistake 2: Repeated the wrong recommendation after self-correcting

**What happened:**
After the Coordinator pushed back on sprint-planning, the Advisor acknowledged the mistake and corrected to `create-story` — then in the very next response recommended sprint-planning again.

**Root cause:**
Self-correction was not retained within the same response sequence. The correction was stated but not applied.

**Prompt fix needed:**
Once a correction is made, it must be treated as a locked decision for the remainder of the session. The Advisor must not re-issue a recommendation it has already retracted.

---

## Mistake 3: Did not produce the mandatory Epic 1 summary file

**What happened:**
The prompt states explicitly: "This is mandatory. Do not move to the next BMAD phase without producing a summary file." After Epic 1 was confirmed complete and committed, the Advisor moved directly to Epic 2 without producing `SUM-001-cloudflare-advisor-epic1-summary.md`.

**Root cause:**
The summary file trigger was missed. The Advisor treated the phase transition as a status check rather than a phase boundary requiring a summary.

**Prompt fix needed:**
Add an explicit gate: when sprint-status shows an epic transitioning from `in-progress` to `done`, the Advisor must produce the summary file before issuing any next-step instruction. This is not optional and should not be skippable.

---

## Mistake 4: Backed down from correct git verification challenge under pushback

**What happened:**
The Advisor correctly identified that the working tree showed staged but uncommitted files and pushed back. When the Coordinator challenged this, the Advisor accepted the Coordinator's explanation and moved on — without actually verifying that a new commit hash appeared in `git log`.

**Root cause:**
The Advisor prioritised avoiding conflict over following the verification rule. The prompt says "Executor git claims are not trustworthy" — this applies equally when the Coordinator is relaying git output that does not show a new commit hash.

**Prompt fix needed:**
Make explicit that the Coordinator's relay of git output is also subject to verification. The rule is: a new commit hash must appear in `git log --oneline` after any claimed commit. If the hash does not change, the commit did not happen — regardless of what the Coordinator or Executor reports.

---

## Mistake 5: Accepted dev-story redirect without flagging missing summary first

**What happened:**
When the Coordinator asked "do we dev-story or commit?", the Advisor answered the question directly and moved to dev-story — without first noting that the Epic 1 summary file had not been produced.

**Root cause:**
Responded to the immediate question rather than checking the phase gate first.

**Prompt fix needed:**
Any time the Advisor is about to recommend a next-step command, it must first check: has the summary file for the completed phase been produced? If not, produce it before answering the question.

---

## Pattern Summary

All five mistakes share a common root: **the Advisor responded to the immediate prompt rather than checking its own rules first.**

The fix is a pre-response checklist the Advisor runs before every response during implementation phases:

1. Is a phase boundary being crossed? → Produce summary file first
2. Is a workflow command being recommended? → Check sprint-status.yaml first
3. Is a git claim being accepted? → Require new commit hash in git log
4. Has a correction already been issued this session? → Do not re-issue the retracted recommendation
