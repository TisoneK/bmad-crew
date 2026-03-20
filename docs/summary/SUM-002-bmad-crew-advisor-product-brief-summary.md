# Product Brief Phase Summary

**Date:** 2026-03-20  
**Phase:** Product Brief Creation  
**Project:** bmad-crew (Modular Multi-Agent Prompt System)

---

## Executive Summary

A modular multi-agent prompt system for BMAD workflows that applies software engineering principles to prompt design, ensuring AI agents maintain consistent role identity under pressure.

---

## Core Problem Solved

Monolithic agent prompts cause LLMs to lose role identity under pressure, leading to role collapse (Advisor becoming Executor, self-certification, etc.). This affects both AI agent session quality AND developer experience in maintaining prompts.

---

## Key Principles Discovered

1. **Identity First Loading** - Identity always loads first and is bulletproof
2. **Independent File Utility** - Each file is independently useful tested in isolation
3. **Pushback Resilience** - Agents resist pressure to break role using absolute language

---

## Target Users

- **Primary:** BMAD Developers/Coordinators seeking reduced cognitive load during sessions
- **Secondary:** BMAD framework users, new team members (onboarding), BMAD contributors

---

## MVP Scope

### Core Features (P0-P1)
- Shared files: bmad-team-structure.md, bmad-workflow-reference.md
- Advisor module: advisor-identity.md, advisor-response-rules.md, advisor-workflow-gates.md

### Out of Scope
- Executor, Coordinator, Specialist modules (post-MVP)
- Tooling, CI/CD, GUI/dashboard

---

## Success Metrics

### Primary Proof of Success
The modular prompt system guides real Advisor sessions correctly. The Advisor catches role violations, enforces commit checkpoints, produces summary files, and maintains locked decisions without the Coordinator having to intervene.

### KPIs
- Role collapse incidents: 0 per session
- Coordinator intervention frequency: < 1 per session
- Developer retention: > 80%
- Session hygiene compliance: 100%

---

## Future Vision

1. **Phase 2:** Full modular ecosystem covering all agent types with community contributions
2. **Phase 3:** Tooling layer - CI/CD, automated validation
3. **Phase 4:** Becomes default prompt system shipped with BMAD

---

## Output Document

`_bmad-output/planning-artifacts/product-brief-bmad-crew-2026-03-20.md`

---

## Next Steps

- Create PRD (Product Requirements Document) from this brief
- Begin implementation of shared files and Advisor module
