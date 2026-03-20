---
stepsCompleted: [1, 2]
inputDocuments: []
session_topic: 'Modular multi-agent prompt system for BMAD workflows'
session_goals: 'Define agent prompt module structure, shared files, per-agent loading protocol, and clear file boundaries; include evidence sourcing from docs/evidence'
selected_approach: 'progressive-flow'
techniques_used: ['Rapid Ideation', 'Affinity Mapping', 'SCAMPER + Storyboard', 'Action Roadmap']
ideas_generated: []
context_file: ''
---
# Brainstorming Session Results

**Facilitator:** Tisone
**Date:** 2026-03-20T07:36:25
## Session Overview

**Topic:** A modular multi-agent prompt system for BMAD workflows — solving monolithic prompt risks (role collapse, context decay, agent confusion) in AI-driven development sessions.
**Goals:**
- Define module structure for all agent prompts (Advisor, Executor, Specialist, Coordinator)
- Define shared files that all agents consume
- Define loading protocol per agent
- Identify per-file contents so no file depends on another
- Capture evidence references in docs/evidence/

### Context Guidance
- Primary challenge: monolithic prompts degrade multi-agent clarity and state management.
- Target solution: modular, role-specific prompt components + robust load order and isolation.
- Evidence source: docs/evidence/ (to be referenced for rationale and decision-trace).

### Session Setup
This is a facilitation-focused ideation stage. I’ve noted the scope and success criteria, and I’m ready to proceed to technique selection and idea generation.

**Does this capture your intent?**

**Next:** choose a technique selection approach:
1) User-selected techniques (browse library)
2) AI-recommended techniques (customized)
3) Random technique selection (unexpected)
4) Progressive technique flow (broad-to-narrow)


## Technique Selection

**Approach:** Progressive Technique Flow
**Journey Design:** Systematic development from exploration to action

**Progressive Techniques:**

- **Phase 1 - Exploration:** Rapid Ideation (maximize idea generation, high energy)
- **Phase 2 - Pattern Recognition:** Affinity Mapping (organize insight clusters)
- **Phase 3 - Development:** SCAMPER + Storyboard (refine and expand top concepts)
- **Phase 4 - Action Planning:** Action Roadmap (implementable steps, resources, metrics)

**Journey Rationale:** This sequence takes our focus from divergent thinking to convergent planning, enabling a robust multi-agent prompt architecture with clear modular boundaries and implementation pathways.

**Next:** choose [C] Continue to begin phased execution, [Customize] to adjust technique choices, or [Back] to change approach.

## Technique Execution: Phase 1 - Expansive Exploration

**Technique Name:** Rapid Ideation
**Focus:** Generate as many role-safe, modular multi-agent prompt structure ideas as possible without judgment
**Energy:** High, expansive, boundary-breaking

**Facilitator Coaching Frame:**
Outstanding! Let's begin our first technique with true collaborative facilitation.

I'm excited to facilitate Rapid Ideation with you as a creative partner, not just a respondent. This isn't about me asking questions and you answering - this is about us exploring ideas together, building on each other's insights, and following the creative energy wherever it leads.

**My Coaching Approach:**
- I'll introduce one prompt structure idea at a time
- We'll explore it together through back-and-forth dialogue
- I'll build upon your ideas and help develop them further
- We'll dive deeper into concepts that spark your imagination
- You can always say "let's explore this more" before moving on
- **You're in control:** At any point, just say "next technique" or "move on" and we'll document current progress and start the next technique

**Ready to dive into creative exploration together?**

**First prompt:** Provide one concise modular agent prompt module for the Advisor role (purpose, inputs, outputs, constraints).

## Evidence Summary (docs/evidence)

- **MULTI_AGENT_PROMPT_SYSTEM_SPEC.md**: defines absolute architecture, module layout (shared/coordinator/advisor/executor/specialist), independent per-file semantics, and precise loading order. Emphasis on identity-first, shared reference files, and gate checklists to avoid role collapse, context decay, and policy drift.
- **ADVISOR_PROMPT_RESTRUCTURE_SPEC.md**: deep dive on splitting advisor prompt into focused files (identity, response rules, workflow gates, locked decisions, BMAD reference, session init), and precise ordering for resilience.
- **ADVISOR_SESSION_MISTAKES_001.md**: logged operational failure cases (wrong command, retracted but repeated recommendation, missing required summary, git commit verification failures, phase gate skipping) with fixed pre-response checklist rules.
- **ADVISOR_IDEAS.md**: tactical prompt improvements: mandatory session mistakes file every story cycle, extended commit checkpoint to all BMAD commands.
- **WINDSURF_SESSION.txt**: concrete session interaction record showing how command syntax confusion (story id vs path vs no arg), Builder/Executor command intent mismatches, the need for “verify before trust”, and the exact progress flow for Story 2-2 (Canvas/WebGL). Contains strong evidence of robust role enforcement and circuit-breaker style verification.
- **GEMINI_SESSION.md**: senior-advisor pre-session alignment dialogue, full locked decisions for SCR-003, and “read-only advisor” behavior patterns. Confirms requirement to filter out operational instructions and focus on decision validation, place in-phase structured handoffs, and strictly avoid flat-file anti-patterns.

**Key cross-document patterns**:
- Modular files per role + shared reference docs to avoid monolithic prompt decay.
- Identity-first loading and gate checklists to enforce separation of concerns.
- Locked decision management with session-based living document.
- Strong “check current state before next command” invariant.
- Validation-first culture: verify git/hash, summary article, phase boundaries.

**Completed:** Evidence review and synthesis are now part of our session context.
