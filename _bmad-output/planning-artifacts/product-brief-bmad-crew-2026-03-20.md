---
stepsCompleted: [1, 2, 3, 4, 5, 6]
inputDocuments:
  - "_bmad-output/brainstorming/brainstorming-session-2026-03-20.md"
  - "docs/evidence/MULTI_AGENT_PROMPT_SYSTEM_SPEC.md"
  - "docs/evidence/ADVISOR_PROMPT_RESTRUCTURE_SPEC.md"
  - "docs/evidence/ADVISOR_SESSION_MISTAKES_001.md"
  - "docs/evidence/ADVISOR_IDEAS.md"
  - "docs/evidence/ADVISOR_PROMPT_v3.md"
  - "docs/evidence/WINDSURF_SESSION.txt"
  - "docs/evidence/GEMINI_SESSION.md"
date: 2026-03-20
author: Tisone
status: complete
---

# Product Brief: bmad-crew

<!-- Content will be appended sequentially through collaborative workflow steps -->

## Executive Summary

A modular multi-agent prompt system for BMAD workflows that applies software engineering principles to prompt design, ensuring AI agents maintain consistent role identity under pressure.

---

## Core Vision

### Problem Statement

Monolithic agent prompts cause LLMs to lose role identity under pressure, leading to role collapse (Advisor becoming Executor, self-certification, etc.). This affects both AI agent session quality AND developer experience in maintaining prompts.

### Problem Impact

- Agents fail during execution: role boundaries blur, self-certification occurs, checkpoints get skipped
- Developers struggle: hard to maintain identity in monolithic prompts, no composability, difficult to test

### Why Existing Solutions Fall Short

Current solutions treat prompts as static documents rather than software modules. No existing BMAD workflow system applies software engineering principles (Single Responsibility Principle, dependency inversion, interface segregation) to prompt file design. No system has the Independent File Utility Test or Pushback Resilience design.

### Proposed Solution

A modular prompt system where each file has one job, loads in the right order, and holds under pressure. Files are independently useful (tested in isolation), use absolute language (NEVER, MUST), and follow Identity First Loading Principle.

### Key Differentiators

A unified system combining: (1) Identity First Loading - identity always loads first and is bulletproof, (2) Independent File Utility - each file is independently useful tested in isolation, (3) Pushback Resilience - agents resist pressure to break role using absolute language.

---

## Target Users

### Primary Users

**BMAD Developers/Coordinators**
- Role: Developers building custom multi-agent workflows using BMAD framework
- Context: Working on AI automation projects, managing multiple agent roles (Advisor, Executor, Specialist, Coordinator)
- Motivation: Reduce cognitive load during BMAD development sessions - less correcting, less re-explaining, less fighting agent drift
- Problem Experience: Currently spend significant effort correcting agent role drift, re-explaining context, catching missed checkpoints, fighting self-certification
- Success Vision: The first session where the Advisor catches a mistake automatically and the developer realizes they did not have to intervene - that's the "aha!" moment

### Secondary Users

1. **BMAD Framework Users** - Any BMAD user who adopts the modular prompt framework for their own agents
2. **New Team Members** - Use prompts as onboarding resource for understanding agent roles
3. **BMAD Contributors** - Maintain and evolve prompt standards

### User Journey

**Primary Journey (Most Common):**
1. **Discovery:** Developer hits role collapse issues in BMAD sessions, loses time correcting agents
2. **Onboarding:** Searches for better approach, finds bmad-crew modular prompt system
3. **Core Usage:** Loads identity files first, configures agent sessions with modular prompts
4. **Success Moment:** First session where Advisor catches a mistake automatically - no manual intervention needed
5. **Long-term:** Prompts become part of standard BMAD development practice

**Secondary Journeys:**
- New BMAD user wanting best practices from the start
- Developer inheriting messy monolithic prompts needing refactoring

---

## Success Metrics

### Primary Proof of Success

The modular prompt system guides real Advisor sessions correctly. The Advisor catches role violations, enforces commit checkpoints, produces summary files, and maintains locked decisions without the Coordinator having to intervene. If the system works in a live session the way it worked in the bmad-crew development session itself, it is succeeding.

### User Success Metrics

1. **Reduced Coordinator Interventions** - Advisor catches mistakes automatically without human intervention
2. **Zero Role Collapse Incidents** - Sessions using modular prompts show no role boundary violations
3. **Faster Development Sessions** - Less time correcting agents, more time building
4. **Adoption & Retention** - Developers keep using modular prompts after first session rather than reverting to monolithic
5. **Prompt Maintainability** - Developers can update one file without breaking others
6. **Session Hygiene** - Agents always start new sessions in new chats, no context bleed between sessions

### Business Objectives

As an open-source community contribution to the BMAD ecosystem:
- GitHub stars and forks as adoption signal
- Community contributions (new agent modules, new prompt files)
- Usage by BMAD community members in their own projects
- Citation/reference in BMAD community discussions

### Key Performance Indicators

| KPI | Target | Measurement |
|-----|--------|-------------|
| Live Advisor session success | Works as designed | Session log review |
| Role collapse incidents per session | 0 | Session log review |
| Coordinator intervention frequency | < 1 per session | Session log count |
| Developer retention (post-first session) | > 80% | Usage tracking |
| Session hygiene compliance | 100% | Session start check |
| Community contributions | Growing | GitHub activity |
| GitHub stars/forks | Adoption growth | GitHub metrics |

---

## MVP Scope

### Core Features (MVP)

- **Shared Files (P0):** shared/bmad-team-structure.md, shared/bmad-workflow-reference.md
- **Advisor Module (P1):** advisor/advisor-identity.md, advisor/advisor-response-rules.md, advisor/advisor-workflow-gates.md
- Rationale: Advisor directly reduces Coordinator cognitive load; shared files must come first

### Out of Scope for MVP

- Executor, Coordinator, Specialist modules (post-MVP)
- Advanced testing framework
- Community contributions framework
- Automated loading protocol tooling
- CI/CD for prompt validation
- GUI/dashboard for managing prompt files
- MVP is plain markdown files that developers load manually

### MVP Success Criteria

- Live Advisor session works correctly
- Advisor catches role violations automatically
- Coordinator interventions reduced to < 1 per session
- Developers adopt and continue using after first session
- Session hygiene maintained (new chats for new sessions)

### Future Vision

1. **Phase 2:** Full modular ecosystem covering all agent types with community contributions
2. **Phase 3:** Tooling layer - CI/CD, automated validation, loading protocol automation
3. **Phase 4:** Becomes default prompt system shipped with BMAD - bmad-crew becomes standard like project-context.md
