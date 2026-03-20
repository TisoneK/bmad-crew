# Multi-Agent Prompt System — Restructure Spec
**Date:** 2026-03-19
**Author:** Tisone
**Purpose:** Define the full modular prompt system for all agents in the BMAD workflow
**Status:** Draft

---

## Problem Statement

All agent prompts are currently monolithic single files. An LLM cannot reliably
hold role identity, workflow rules, gate checks, and session state simultaneously
in one file. Under pressure or pushback, rules decay. Agents collapse roles.
Executors self-certify. Advisors become Executors. The Coordinator has no clear
reference for their own responsibilities.

The solution is a modular prompt system — each concern in its own file, each file
independently useful, all files organized into agent-specific modules.

---

## System Structure

```
bmad-prompts/
├── shared/                  # Consumed by all agents
├── coordinator/             # Tisone's own reference
├── advisor/                 # Senior Technical Advisor
├── executor/                # Primary implementation agent
└── specialist/              # Targeted fix agent
```

---

## Module Breakdown

### shared/
Files every agent references. Never duplicated per-agent.

- `bmad-workflow-reference.md`     — Full BMAD command sequence, what each does, when
- `bmad-team-structure.md`         — Who each agent is, what they own, what they never do
- `bmad-locked-decisions.md`       — Living document, updated each session
- `project-context.md`             — Project rules and tech stack (already exists)

---

### coordinator/
Tisone's reference. Not a prompt — a personal workflow guide.

- `coordinator-responsibilities.md` — What the Coordinator does at each phase
- `coordinator-context-handoff.md`  — How to move context between agents correctly
- `coordinator-session-checklist.md`— Pre-session and post-session checklist
- `coordinator-gate-rules.md`       — When to stop and verify before proceeding

---

### advisor/
Split from current ADVISOR_PROMPT_v3.md into focused files.

- `advisor-identity.md`            — Role, what advisor never does, permanent rules
- `advisor-response-rules.md`      — Format, length, code blocks, tell WHAT not HOW
- `advisor-workflow-gates.md`      — Pre-response checklist, commit gates, summary triggers
- `advisor-session-init.md`        — How to start a session, context request sequence
- `advisor-pushback-rules.md`      — Scope confusion, locked decision enforcement
- `advisor-break-resume.md`        — /advisor-break and /advisor-resume behavior

---

### executor/
Currently no structured prompt exists. Needs to be built.

- `executor-identity.md`           — Role, what executor never does, permanent rules
- `executor-implementation-rules.md`— Sub-module structure, async patterns, integration rules
- `executor-git-rules.md`          — Commit rules, what to commit, when, verification
- `executor-review-rules.md`       — How to handle code-review findings, patch vs defer
- `executor-session-init.md`       — How to start a dev-story or code-review session

---

### specialist/
Currently no structured prompt exists. Needs to be built.

- `specialist-identity.md`         — Role, when called in, what specialist never does
- `specialist-handoff-rules.md`    — How to receive context, what to fix, handoff back
- `specialist-scope-rules.md`      — Stay in lane, do not re-architect, targeted fixes only

---

## Loading Protocol per Agent

### Advisor loads:
1. `advisor/advisor-identity.md`
2. `advisor/advisor-session-init.md`
3. `advisor/advisor-response-rules.md`
4. `advisor/advisor-workflow-gates.md`
5. `advisor/advisor-pushback-rules.md`
6. `shared/bmad-team-structure.md`
7. `shared/bmad-workflow-reference.md`
8. `shared/bmad-locked-decisions.md`
9. `shared/project-context.md`
10. `ADVISOR_IDEAS.md`
11. `ADVISOR_SESSION_MISTAKES_00X.md`

### Executor loads:
1. `executor/executor-identity.md`
2. `executor/executor-session-init.md`
3. `executor/executor-implementation-rules.md`
4. `executor/executor-git-rules.md`
5. `executor/executor-review-rules.md`
6. `shared/bmad-team-structure.md`
7. `shared/bmad-workflow-reference.md`
8. `shared/bmad-locked-decisions.md`
9. `shared/project-context.md`

### Specialist loads:
1. `specialist/specialist-identity.md`
2. `specialist/specialist-handoff-rules.md`
3. `specialist/specialist-scope-rules.md`
4. `shared/bmad-team-structure.md`
5. `shared/project-context.md`

### Coordinator references:
1. `coordinator/coordinator-responsibilities.md`
2. `coordinator/coordinator-context-handoff.md`
3. `coordinator/coordinator-session-checklist.md`
4. `coordinator/coordinator-gate-rules.md`

---

## Key Principles

**Each file must be independently useful.**
If an LLM loses all other context, reading one file must be enough to prevent
the most critical violations for that role.

**Shared files are never duplicated.**
If a rule applies to all agents it lives in shared/. No copy-pasting between
agent modules.

**Identity files are loaded first, always.**
Role identity is the most stable context. It must be the first thing loaded
and the last thing an LLM should drift from.

**Gate files are the most important during implementation.**
advisor-workflow-gates.md and executor-git-rules.md must be treated as
active checklists, not background context.

---

## Build Order

1. `shared/` files first — everything depends on these
2. `advisor/` files — already partially written in ADVISOR_PROMPT_v3.md, needs splitting
3. `coordinator/` files — needs to be written from scratch
4. `executor/` files — needs to be written from scratch
5. `specialist/` files — lowest priority, write last

---

## What This Solves

| Problem | File that fixes it |
|---------|--------------------|
| Advisor becomes Executor | advisor-identity.md |
| Executor self-certifies completion | executor-git-rules.md |
| Advisor gives HOW not WHAT | advisor-response-rules.md |
| Coordinator skips commit checkpoint | coordinator-gate-rules.md |
| Agent collapses roles | shared/bmad-team-structure.md |
| Locked decisions re-opened | shared/bmad-locked-decisions.md |
| Context lost between agents | coordinator-context-handoff.md |
| Specialist re-architects instead of fixing | specialist-scope-rules.md |
| Summary/mistakes files skipped | advisor-workflow-gates.md |
