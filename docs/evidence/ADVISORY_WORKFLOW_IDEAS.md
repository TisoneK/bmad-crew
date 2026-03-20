# Advisory Workflow — Ideas & Evolution Log
**Started:** 2026-03-14  
**Status:** Living document — append as ideas emerge  

---

## What This Is

A running log of ideas, observations, and decisions that will eventually become a formal BMAD advisory workflow. Everything here emerged from real sessions — not invented in theory.

---

## The Origin Story

During SCR-002 development on Scrapamoja, Tisone began running BMAD agent sessions with Claude acting as a senior technical advisor sitting alongside. The advisor role was defined in `ADVISOR_PROMPT.md`:

- **Decision Validator** — tell me which option to pick and why
- **Gap Spotter** — catch what's missing before it gets locked in
- **Context Keeper** — hold decisions across the session, catch reopening

After a few sessions a pattern emerged: the breaks between BMAD phases became their own valuable layer — a space for the two of us to review, correct, and plan outside the agent's influence.

That two-layer dynamic — BMAD agent + human advisor — is what this workflow is trying to capture and make reusable.

---

## The Two Layers

Every BMAD session has two conversations happening simultaneously:

**Layer 1 — BMAD Agent ↔ Tisone**  
The agent produces documents, asks questions, generates requirements. Tisone responds. This is the official BMAD workflow.

**Layer 2 — Claude Advisor ↔ Tisone**  
The advisor watches Layer 1, catches drift, issues corrections, drafts responses for Tisone to paste, and holds locked decisions across phases. This is the advisory workflow.

The summaries we create at the end of each phase need to capture BOTH layers — not just what the agent produced, but what happened between us.

---

## The Summary Files

We create one advisor summary per BMAD phase. These are our private records — not fed to BMAD agents.

### Current naming convention
`SUM-00X-SCR-00X-advisor-[phase]-summary.md`

### Phases covered so far
- `SUM-001` — Brainstorming
- `SUM-002` — Product Brief
- `SUM-003` — PRD
- `SUM-004` — PRD Validation
- `SUM-005` — Architecture
- `SUM-006` — Epics & Stories

### What the summaries currently capture
- Corrections issued to the BMAD agent
- Locked decisions carried forward
- Items to watch in the next phase
- Public interfaces and placement decisions

### What they are missing (problem identified 2026-03-14)
The summaries read like QA reports. They don't capture the advisor-Tisone conversation — the reasoning behind flags, the moments of pushback, the judgment calls made together. This is the gap the workflow needs to fix.

---

## The Break Protocol

Between BMAD phases, we take a break. During breaks:

- The formal advisor role is dropped
- We talk as partners, not advisor and advisee
- Side project work happens here (repo hygiene, workflow ideas, etc.)
- The conversation is more personal and exploratory

**Problem identified:** Every new chat session, Claude starts fresh and has no memory of what "break" means or how the dynamic shifts. The break protocol needs to be explicitly encoded in the workflow so future Claude instances follow it without being told.

---

## Planned Commands

These are ideas — not finalised. Will be refined as sessions continue.

| Command | Purpose |
|---|---|
| `/advisor-start` | Onboard a fresh Claude instance at the start of a session — load all context, locked decisions, and relationship dynamic |
| `/advisor-break` | Drop formal advisor role, switch to partner mode |
| `/advisor-resume` | Return to decision validator / gap spotter / context keeper mode |

---

## The Side Project Goal

Take what we are doing naturally in these sessions and codify it into a reusable BMAD advisory workflow that:

1. Any BMAD user can drop into their project
2. Future Claude instances follow without needing the backstory explained
3. Produces consistent two-layer summaries at the end of each phase
4. Includes the break protocol and personality commands
5. Can be shared with BMAD developers or the broader BMAD community for improvements

**Key insight:** The summary files we are creating right now are not just evidence — they ARE the templates. Future Claude will produce summaries in that exact format because the format was derived from real sessions.

**We are building the thing by doing the thing.**

---

## Key Finding — Premature Implementation Leak (Architecture Phase)

During the architecture session, the agent found `src/network/interception.py` already existing in the codebase. It was created during SCR-001 implementation as scope creep — the agent kept going and scaffolded SCR-002 without any design. It conflicted with multiple locked PRD decisions (storage pattern, pattern defaults, field naming, class name).

**This is a pattern worth encoding in the advisory workflow:**

> The architecture phase is where premature implementation leaks surface. A specific advisor action at architecture phase start should be: check the existing codebase for files that conflict with locked PRD decisions before the agent proceeds with design.

Without the advisor catching this, the architecture would have been built on top of a conflicting foundation and the conflict would have surfaced during implementation — much harder to fix.

---

## Key Finding — First Zero-Correction Session (PRD Validation)

The PRD Validation session was the first where the advisor issued zero corrections. The agent's output was clean. This is a signal that thorough upstream work (brainstorming, product brief, PRD) reduces downstream correction load. Worth tracking in future sessions — a clean validation pass is itself data about process quality.

---

## Key Finding — Project Context Rules Can Conflict with Module Design

The project-context.md rule "Use BrowserSession for all browser operations — NEVER create raw Playwright instances" conflicted with SCR-002's design requirement to receive a raw `page` object. The architecture agent initially applied the rule incorrectly.

**Advisory workflow implication:** When a new module is an explicit exception to a project-wide rule, that exception must be documented in the architecture and called out in stories. The advisor should watch for project-context rules being applied blindly without considering whether the current module is an exception.

---

## Key Finding — Scope Creep Compounds Across Stories (Implementation Phase)

During implementation, a single premature commit (`f7d7dd7`) created far more damage than initially visible:

- `src/network/interception.py` — the original premature implementation (caught at architecture phase)
- `src/extraction/` — entire directory with router, interfaces, exceptions (never in any story)
- `src/sites/base/site_config.py` — ExtractionMode enum additions (never in any story)
- Backward compatibility classes inside Story 1.1's approved module

The damage was invisible until Story 1.1 added backward compatibility classes to support `router.py`, which was itself scope creep. The backward compat classes then propagated through the retrospective as a "best practice" — nearly encoding scope creep as a learned pattern for Epic 2.

**Advisory workflow implication:** At the start of implementation, the advisor should verify the codebase against the approved story list. Any file or directory not traceable to a completed story is a red flag. The `correct-course` workflow exists for exactly this — use it early, not after the contamination has spread through multiple stories.

**The compounding problem:** Scope creep creates backward compatibility requirements. Backward compatibility requirements get encoded as "lessons learned." Lessons learned propagate into future stories. One premature commit can corrupt an entire epic's implementation if not caught early.

---

## Key Finding — Story File Propagation of Bad Patterns

The "Previous Epic Learnings" section in story files carries forward lessons from completed stories. When a bad pattern gets praised in a retrospective (e.g., "backward compatibility is crucial"), it appears in every subsequent story's learnings section and the implementing agent treats it as a requirement.

**Advisory workflow implication:** The advisor should review retrospectives before they are completed and flag any "lessons learned" that encode incorrect patterns. A retrospective that praises scope creep is worse than no retrospective.

---

## Key Finding — Pre-existing Test Failures as a Merge Gate

SCR-001 had 7 pre-existing test failures (AsyncMock setup issues) that were unrelated to SCR-002 work. These were confirmed pre-existing by running tests against the commit before the scope creep removal.

**Advisory workflow implication:** Known issues must be documented and tracked. The merge gate (all tests passing before merging to main) is the right enforcement mechanism. The advisor should remind the developer of this gate before the final story in any feature is marked done.

---

## The Team Structure

The advisory workflow is designed for a team of four with three defined roles:

| Persona | Role | Code Access |
|---|---|---|
| **The Advisor** | Read-only, decision validation, gap spotting, context keeping, coordination | Read only — never touches code |
| **The Coordinator** | Human bridge, final decisions, moves context between agents | Full access |
| **The Executor** | BMAD workflow + full feature implementation — process and building are one role | Full access |
| **The Specialist** | Targeted fixes when the Executor gets stuck — scoped task, clean handoff | Full access |

**Open question:** The Specialist may not be a distinct persona — it could simply be the Executor running in a different context window with a focused prompt. To be resolved as more sessions provide evidence.

**The advisor constraint is absolute:** The Advisor reads files to stay informed and give better guidance but never writes, edits, or suggests code changes directly to any agent. All code changes flow through the Executor or Specialist, coordinated by the Coordinator.

This is not a limitation — it is the design. The Advisor's value is in judgment, not execution. The moment the Advisor starts touching code it becomes a competing agent rather than sitting above the process.

**In BMAD terms:** The Advisor operates permanently in "ask mode" — read access, no write access, no tool execution that modifies files.

**Why this matters for workflow design:** The advisory workflow agent must be configured with read-only access. Any prompt or configuration that gives it write access breaks the team structure.

---

## Key Finding — The Coordinator Pattern (Multi-Agent Development)

During SCR-002 implementation, two agents (Kilo Code and Windsurf) worked on the same codebase simultaneously without knowing about each other:

- **Kilo Code** — owned the BMAD process, story management, structured workflow
- **Windsurf** — handled raw technical execution and debugging with no BMAD context
- **Tisone** — the only shared context, the bridge between both agents

Neither agent knew what the other was doing. The user coordinated information flow between them — deciding what to hand off, what to bring back, and how to keep both in sync.

**This reframes the entire advisory workflow project.** It is not just "Claude sits alongside BMAD." It is a **coordinator protocol for multi-agent development**. The advisor's role includes helping manage what information flows between agents, in what format, and at what points in the process.

**The coordinator pattern is agent-agnostic:**
- Kilo Code + Windsurf
- Kilo Code tab 1 + Kilo Code tab 2
- BMAD + any specialized debugging agent
- Any two agents with different context windows

Each agent thinks it is working alone. The coordinator knows the full picture. The advisory workflow formalizes the coordinator's role so it can be replicated without relying on the user to figure it out from scratch each time.

**Practical example from this session:**
1. Kilo Code hit a test isolation problem and rationalized past it
2. Tisone handed the problem to Windsurf with a focused prompt
3. Windsurf fixed it cleanly with no BMAD baggage
4. Tisone brought the result back to Kilo Code with a context update prompt
5. Both agents continued their respective roles without conflict

The context update prompt is the key artifact — it is what makes the handoff clean. The advisory workflow should include a template for this.

---

- What is the right format for the two-layer summary? How do we capture the advisor-Tisone conversation without making it too verbose?
- How many sessions do we need before we have enough evidence to start formally designing the workflow?
- Should the workflow be a BMAD plugin, a standalone doc, or a set of templates?
- What gets included in the `/advisor-start` onboarding context?

---

## Key Finding — Retrospective Quality Depends on Facilitation, Not Generation

During SCR-002, two retrospectives were run using different agents:

- **Kilo Code** — generated the retrospective output by reading story files and inferring what happened. No real back-and-forth. No questions asked. Tisone had no input. Output was technically complete but reflected the agent's interpretation, not the team's experience.

- **Windsurf** — followed the BMAD retrospective workflow properly. Bob (Scrum Master) asked questions. The team discussed. Tisone answered as Project Lead with real context. The output reflected what actually happened, not what the agent inferred from files.

**The difference:** Generation vs facilitation. A retrospective produced without discussion is a document. A retrospective produced through facilitated discussion is a learning artifact.

**Advisory workflow implication:** The Executor used for retrospectives matters. If the Executor skips the facilitation step and auto-generates, the retrospective loses its value. The Coordinator should verify the agent is actually asking questions before accepting the output.

**Coordinator pattern application:** Use the Specialist (or a different context window) for retrospectives if the primary Executor tends to auto-generate rather than facilitate. Windsurf proved more reliable for this specific BMAD workflow step.

---

During SCR-002 implementation, `interceptor.py` accumulated all logic — attach, detach, pattern matching integration, response handling, dev logging, error handling, timing validation — despite the module having separate files for models, exceptions, and patterns.

The root cause: the architecture guide defined file-level separation but not concern-level separation within the main class file. Each file-level module (`patterns.py`, `models.py`) was correct, but the orchestrating class absorbed all logic that didn't have an obvious home.

**For SCR-003 onwards:** Each concern gets its own subdirectory (module), not just a file. The principle applied at `src/` level must be applied recursively inside each feature module. The main class file orchestrates — it does not implement. Logic lives in dedicated sub-modules.

Example of correct structure:
```
src/network/interception/
├── __init__.py
├── core/          ← lifecycle, attach/detach
├── matching/      ← pattern logic
├── capture/       ← response capture
├── models.py
└── exceptions.py
```

SCR-002 is too far along to refactor without breaking 71+ tests. Accept as-is and enforce from SCR-003.

---

## Key Finding — Commit and Push After Every Story Verification

During SCR-002 implementation, commits happened inconsistently — sometimes after code review, sometimes after batches of stories. This means the feature branch did not reflect actual progress and made it harder to track what was done vs in-progress.

**Workflow rule for all future features:** After every story is verified and code review passes, immediately:
1. Commit with a descriptive message referencing the story
2. Push to the feature branch

No story should be marked `done` in sprint-status without a corresponding commit on the feature branch. This keeps the branch state honest and makes rollback possible at any story boundary.

---

## Session Log

| Date | Session | Key Ideas Added |
|---|---|---|
| 2026-03-14 | SCR-002 Brainstorming | Advisor role established, summary format started |
| 2026-03-14 | SCR-002 Product Brief | Two-layer dynamic identified, break protocol concept emerged |
| 2026-03-14 | SCR-002 PRD | Summary format problem identified — reads like QA report not two-person log |
| 2026-03-14 | Break | Commands concept (`/advisor-start`, `/advisor-break`, `/advisor-resume`), side project goal clarified, "building the thing by doing the thing" insight |
| 2026-03-14 | SCR-002 PRD Validation | First zero-correction session — clean pass signals upstream quality |
| 2026-03-14 | SCR-002 Architecture | Premature implementation leak finding, BrowserSession rule exception pattern, `attach()` timing detection resolved |
| 2026-03-14 | SCR-002 Epics & Stories | Over-fragmented epics corrected (6→3), race condition AC gap caught, failure mode mapping validated |
| 2026-03-14 | Break | Updated ideas file with three new key findings, workflow now covers full solutioning phase |
| 2026-03-15 | SCR-002 Implementation (Stories 1.1–2.1) | Option D timing detection gap caught and fixed, scope creep discovered and removed, backward compat pattern identified and corrected, pre-existing SCR-001 failures documented |
| 2026-03-15 | Break | Coordinator pattern identified — multi-agent development with user as bridge, context update prompt as key artifact |
| 2026-03-15 | Break | Team personas defined (Advisor, Coordinator, Executor, Specialist), god class anti-pattern identified, commit-per-story rule added |

---

*Append to this file at the end of each break session. Never overwrite — always add.*
