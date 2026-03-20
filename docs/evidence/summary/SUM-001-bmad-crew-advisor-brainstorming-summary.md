# SUM-001-bmad-crew-advisor-brainstorming-summary.md
**Phase:** Brainstorming
**Date:** 2026-03-20
**Project:** bmad-crew

---

## Corrections Issued During This Phase

1. Kiro was used initially — switched to Kilo Code after Kiro started fresh without evidence context
2. Facilitator looped back to Morphological Analysis instead of advancing to SCAMPER — corrected by explicit instruction
3. Evidence files were not loaded automatically — had to explicitly instruct the Executor to read docs/evidence/ before starting

---

## Locked Decisions Carrying Forward

- File structure: shared/, coordinator/, advisor/, executor/, specialist/
- Loading order: Identity → Session Init → Response Rules → Workflow Gates → BMAD Reference → Locked Decisions → Project Context
- Identity files: max 5 lines, NEVER-only language, zero workflow references, exactly 3 absolute rules
- File granularity: one concern, one failure mode, one agent action prevented per file
- Shared files: zero duplication tolerance
- Dependency Inversion: identity contains zero git or workflow references
- Build order: shared → advisor → coordinator → executor → specialist (5 weeks)
- Success metric: 0 role collapse incidents per session

---

## Items to Watch in Planning

- Executor may try to expand identity files beyond 5 lines — hold the limit
- Shared files must not be copied into agent-specific modules — enforce zero duplication
- Coordinator module is being built from scratch — no existing reference to draw from
- Executor and Specialist modules are also new — planning must define them carefully

---

## Open Questions Deferred

- What exactly goes in coordinator/coordinator-context-handoff.md — needs planning phase to define
- How locked decisions file gets updated mid-session — dynamic vs static not fully resolved
- Testing protocol for pushback resilience — defined conceptually but not procedurally
