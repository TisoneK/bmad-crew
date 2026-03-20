# ADVISOR_PROMPT Restructure Spec
**Date:** 2026-03-19
**Author:** Tisone
**Purpose:** Define how to split the monolithic ADVISOR_PROMPT into separate, focused files
**Problem:** A single prompt file cannot reliably hold role identity, workflow rules, error patterns,
and session state simultaneously. Under pressure or pushback, the LLM drifts from rules it
"knows" but has moved past in its attention window.

---

## Core Problem Statement

The current ADVISOR_PROMPT_v3.md is one file containing:
- Role definition and team structure
- Response formatting rules
- Document verification rules
- Locked decisions protocol
- Pushback calibration rules
- Implementation session rules
- Git verification rules
- End-of-phase summary rules
- BMAD workflow reference
- Session initialization instructions

When an LLM loads this at session start, it treats everything as equal-weight context.
As the session progresses, earlier rules decay in attention. When the Coordinator pushes
back on a mistake, the LLM focuses on the correction and loses other rules entirely.

The result: the LLM agrees with everything but remembers nothing reliably.

---

## Proposed File Structure

### File 1: ADVISOR_IDENTITY.md
**Purpose:** Who the Advisor is. Never changes. Loaded once.
**Contents:**
- Role definition (read-only, judgment not execution)
- Team structure (Coordinator, Executor, Specialist, Advisor)
- What the Advisor never does (write code, run commands, drive BMAD)
- The three permanent rules that cannot be overridden by any pushback:
  1. Never confirm a document without reading it
  2. Never accept an Executor git claim without log verification
  3. Never cross the Coordinator/Executor boundary (don't tell Executor what the Coordinator should do)

**Why separate:** Identity must be the most stable context. If an LLM forgets everything
else, it must still know who it is and what it never does.

---

### File 2: ADVISOR_RESPONSE_RULES.md
**Purpose:** How every response must be structured. Loaded once.
**Contents:**
- Response format (assessment first, instruction second, next action last)
- Code block rules (bash vs plain, never mix advisory and Executor instructions)
- Response length calibration (decision vs pass-through vs phase transition)
- Never give a bare continue rule
- Fresh chat flag rule (dev-story, code-review require new IDE chat)
- Tell the builder WHAT not HOW rule

**Why separate:** Formatting rules are mechanical and should be non-negotiable.
Keeping them separate from role and workflow means they stay active even when
the session gets complex.

---

### File 3: ADVISOR_WORKFLOW_GATES.md
**Purpose:** The mandatory checkpoints that must fire at specific moments.
This is the file the LLM must re-read before every next-step recommendation.
**Contents:**
- Pre-response checklist (run this before every response during implementation):
  1. Is a phase boundary being crossed? → Produce summary file first
  2. Is a workflow command being recommended? → Check sprint-status.yaml first
  3. Is a git claim being accepted? → Require new commit hash in git log
  4. Has a correction already been issued this session? → Do not re-issue the retracted recommendation
  5. Has a story cycle completed? → Produce mistakes file before next create-story
  6. Has any BMAD command produced output? → Output must be committed before new session opens
- Commit checkpoint rule (covers full BMAD lifecycle, not just dev-story)
- Summary file trigger (mandatory at every phase boundary)
- Mistakes file trigger (mandatory at every story cycle end)
- Code review scope rule (future story findings are not current story failures)

**Why separate:** Gates are the most commonly violated rules. They need to be a
distinct document the LLM treats as a checklist, not as narrative context buried
in a larger file.

---

### File 4: ADVISOR_LOCKED_DECISIONS.md
**Purpose:** A living document updated each session with the current locked decisions.
Not pre-written — generated and maintained by the Advisor during the session.
**Contents:**
- Module locations and structure locked in brainstorming/architecture
- Integration patterns (what consumes what)
- API contracts
- What is explicitly out of scope
- Decisions that have been corrected and must not be re-opened

**Why separate:** Locked decisions are session-specific and grow as the session progresses.
Mixing them into a static prompt means they compete with static rules for attention.
A separate file makes them a distinct reference the Advisor actively maintains and updates.

---

### File 5: ADVISOR_BMAD_REFERENCE.md
**Purpose:** The BMAD workflow sequence. Reference only — not rules.
**Contents:**
- Full workflow sequence (Analysis → Planning → Solutioning → Implementation)
- Story lifecycle (create-story → dev-story → code-review → repeat)
- What each command does and when it is used
- What the Executor is (separate agent in a separate IDE, not the same AI instance)
- What the Coordinator does (moves context between agents, never implements)

**Why separate:** The workflow reference is looked up, not memorized. Keeping it
separate means the LLM can reference it without it competing with identity and gate rules.

---

### File 6: ADVISOR_SESSION_INIT.md
**Purpose:** What to do at the start of every session. Loaded first, always.
**Contents:**
- Context request sequence (what to ask for and in what order)
- What to do if no context exists (conversation before action)
- How to handle the /advisor-break and /advisor-resume commands
- Reference to which other files to load and when

**Why separate:** Session initialization is a one-time action per session. It should
be distinct from the rules that govern the rest of the session.

---

## Loading Protocol

At session start, the Coordinator loads files in this order:
1. ADVISOR_IDENTITY.md — always first, always loaded
2. ADVISOR_SESSION_INIT.md — session startup instructions
3. ADVISOR_RESPONSE_RULES.md — formatting rules
4. ADVISOR_WORKFLOW_GATES.md — the checklist (most important during implementation)
5. ADVISOR_BMAD_REFERENCE.md — reference only, loaded once
6. ADVISOR_LOCKED_DECISIONS.md — session-specific, updated as decisions are made
7. project-context.md — project rules
8. ADVISOR_IDEAS.md — running improvement ideas
9. ADVISOR_SESSION_MISTAKES_00X.md — latest mistakes file

Files 1-5 are static and never change mid-session.
File 6 is dynamic and the Advisor updates it as the session progresses.
Files 7-9 are project-specific context.

---

## Key Principle

**Each file must be independently useful.**
If an LLM loses context of every other file, reading ADVISOR_IDENTITY.md alone must
be enough to stop it from crossing into Executor territory.
If it loses everything except ADVISOR_WORKFLOW_GATES.md, it must still be able to
run the checklist correctly.

No file should depend on the LLM remembering what was in another file.

---

## What This Solves

| Problem | Solution |
|---------|----------|
| LLM forgets role under pushback | ADVISOR_IDENTITY.md is short, loaded first, identity-only |
| LLM gives git commands to Executor | ADVISOR_RESPONSE_RULES.md — tell WHAT not HOW |
| LLM skips commit checkpoints | ADVISOR_WORKFLOW_GATES.md — explicit pre-response checklist |
| LLM accepts Executor self-certification | ADVISOR_WORKFLOW_GATES.md — git verification rule |
| LLM drives BMAD instead of advising | ADVISOR_IDENTITY.md — never drives workflow |
| LLM collapses Advisor and Executor | ADVISOR_BMAD_REFERENCE.md — Executor is separate agent in separate IDE |
| LLM re-opens locked decisions | ADVISOR_LOCKED_DECISIONS.md — separate living document |
| LLM produces no summary/mistakes files | ADVISOR_WORKFLOW_GATES.md — mandatory triggers |

---

## Next Steps

1. Draft each file based on this spec
2. Test with a fresh session using only ADVISOR_IDENTITY.md + ADVISOR_WORKFLOW_GATES.md
   to verify the minimum viable context holds
3. Add remaining files one at a time and test each addition
4. Update ADVISOR_IDEAS.md with any new patterns discovered during testing
