# SUM-002-bmad-crew-advisor-product-brief-summary.md
**Phase:** Product Brief
**Date:** 2026-03-20
**Project:** bmad-crew

---

## Corrections Issued During This Phase

1. Executor framed the product as "workflows" — corrected to modular prompt system (prompt files, not workflow tooling)
2. User segment was incomplete — corrected to clarify AI agents are consumers not users; primary user is BMAD developer/Coordinator
3. Three differentiators were treated as separate options — corrected to capture all three as one unified system
4. Most critical success metric was missing — added Primary Proof of Success: system guides real sessions the way it guided this session
5. Future vision options were treated as alternatives — corrected to sequential phases

---

## Locked Decisions Carrying Forward

- Product type: modular prompt system — plain markdown files, not tooling, not workflows
- Primary user: BMAD developers/Coordinators reducing cognitive load during sessions
- MVP scope: shared files (P0) + Advisor module (P1) only
- Out of scope for MVP: Executor, Coordinator, Specialist modules, all tooling, CI/CD, GUI
- Three unified differentiators: Identity First Loading + Independent File Utility + Pushback Resilience
- Primary proof of success: Advisor catches violations in live sessions without Coordinator intervention
- Future phases: ecosystem → tooling → default BMAD system

---

## Items to Watch in Planning and PRD

- advisor/advisor-session-init.md and advisor/advisor-pushback-rules.md are P2 — must NOT appear in MVP scope in PRD
- PRD must not drift into tooling or automation requirements — those are Phase 3
- PRD must capture the session hygiene requirement: agents always start new sessions in new chats

---

## Open Questions Deferred

- How is adoption measured for an open-source prompt file project with no analytics?
- What is the minimum viable test for pushback resilience — who runs it and how?
