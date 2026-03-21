---
stepsCompleted: ["step-01-init", "step-02-discovery", "step-02b-vision", "step-02c-executive-summary", "step-03-success", "step-04-journeys", "step-05-domain", "step-06-innovation", "step-07-project-type"]
inputDocuments:
  - "_bmad-output/planning-artifacts/product-brief-bmad-crew-2026-03-20.md"
  - "docs/evidence/MULTI_AGENT_PROMPT_SYSTEM_SPEC.md"
  - "docs/evidence/ADVISOR_PROMPT_RESTRUCTURE_SPEC.md"
  - "docs/evidence/ADVISOR_SESSION_MISTAKES_001.md"
  - "docs/evidence/ADVISOR_IDEAS.md"
  - "docs/evidence/WINDSURF_SESSION.txt"
  - "docs/evidence/GEMINI_SESSION.md"
workflowType: 'prd'
briefCount: 1
researchCount: 0
brainstormingCount: 0
projectDocsCount: 12
classification:
  projectType: developer_tool
  domain: AI workflow management
  complexity: medium
  projectContext: brownfield
---

# Product Requirements Document - bmad-crew

**Author:** Tisone
**Date:** 2026-03-21

<!-- Content will be appended sequentially through collaborative workflow steps -->

## Executive Summary

bmad-crew is a modular multi-agent prompt system for BMAD workflows that applies software engineering principles to prompt design, ensuring AI agents maintain consistent role identity under pressure. The system addresses the fundamental trust gap developers face with monolithic prompts that collapse during complex sessions, requiring constant supervision and correction.

### What Makes This Special

The core insight that prompts are software and should be engineered like software enables a breakthrough approach to agent reliability. By applying Single Responsibility Principle, dependency ordering, and interface segregation to prompt files, bmad-crew creates predictable, self-enforcing agent behavior. The transformation moment occurs when developers experience their first session where the Advisor catches mistakes automatically and enforces checkpoints without any human intervention - shifting from constant correction to focused building.

## Project Classification

- **Project Type:** developer_tool (markdown-based prompt organization system)
- **Domain:** AI workflow management
- **Complexity:** medium (novel architecture without regulatory concerns)
- **Project Context:** brownfield (building on existing BMAD framework)
- **Target Users:** BMAD developers and Coordinators specifically

## Success Criteria

### User Success

The primary success moment is the first full BMAD session where the Coordinator experiences zero corrections to the Advisor - the Advisor catches violations, enforces checkpoints, and provides direction before the Coordinator even needs to intervene. The ultimate success is when the Coordinator spends zero time thinking about what to tell any agent - the Advisor always provides the right answer or direction across brainstorming facilitation, planning decisions, architecture options, implementation triage, and code review findings.

### Business Success

Success is measured by organic adoption within the BMAD community rather than specific metrics. Growing usage by other BMAD users, community contributions of new agent modules, and citation in BMAD community discussions indicate the system is working. GitHub stars and forks serve as adoption signals but are not the primary success measure.

### Technical Success

Session log review by the Coordinator after each session shows the Advisor catching role violations and workflow errors before the Coordinator notices them. The modular prompt files maintain agent role identity under pressure, with zero role collapse incidents across all tested sessions.

### Measurable Outcomes

- **Coordinator Interventions:** Less than 1 intervention per session (target: 0 for successful sessions)
- **Role Collapse:** Zero incidents across all sessions using modular prompts
- **Advisor Proactivity:** Advisor catches violations before Coordinator notices them
- **Session Hygiene:** 100% compliance with new-chat-per-session rule
- **Community Adoption:** Growing usage and contributions by BMAD community members

## Product Scope

### MVP - Minimum Viable Product

Shared files (bmad-team-structure.md, bmad-workflow-reference.md) plus Advisor module (advisor-identity.md, advisor-response-rules.md, advisor-workflow-gates.md) working correctly in one live session. The Advisor must successfully guide a full BMAD workflow session with zero Coordinator corrections.

### Growth Features (Post-MVP)

Full modular ecosystem covering Executor, Coordinator, and Specialist modules with community contribution framework. Automated loading protocol tooling and CI/CD for prompt validation.

### Vision (Future)

bmad-crew becomes the default prompt system shipped with BMAD - as standard as project-context.md. The system evolves into a comprehensive prompt engineering framework that applies software engineering principles across all AI agent interactions.

## User Journeys

### Primary Journey: Alex - BMAD Developer/Coordinator

**Opening Scene:** Alex is mid-session in a complex BMAD implementation workflow. The Executor has just self-certified a story as complete without actually committing the changes. Alex catches this manually - again. This is the third time this session alone. Frustrated with spending 30% of their time correcting agent behavior instead of building, Alex searches for a better approach to agent management.

**Rising Action:** Alex discovers bmad-crew and decides to try it in a fresh session. They load the shared files (bmad-team-structure.md, bmad-workflow-reference.md) and the Advisor module (advisor-identity.md, advisor-response-rules.md, advisor-workflow-gates.md) as specified. The Advisor immediately establishes its role and requests context before proceeding. Alex shares the sprint status and current story file. Throughout the session, the Advisor helps Alex with multiple types of decisions: when the Executor presents implementation choices, the Advisor tells Alex exactly which option to pick; when a story file violates a locked architectural decision, the Advisor flags it immediately; when code review findings show scope creep, the Advisor identifies and rejects the out-of-scope items; and when phases complete cleanly, the Advisor provides the exact instruction to continue. The commit checkpoint enforcement is just one of many violations the Advisor catches automatically.

**Climax:** During the first full session with bmad-crew, Alex experiences the transformation moment. The Advisor provides the exact instruction to give the Executor every single time, catches workflow violations before Alex even notices them, and enforces checkpoints automatically across all decision types. Alex's only job becomes moving context between agents - they never have to think about what to tell the agents anymore.

**Resolution:** Alex's sessions become significantly faster and more focused. The Advisor maintains role boundaries throughout, catches self-certification attempts, prevents scope creep, and ensures proper session hygiene. Alex stops thinking about agent management entirely and can focus completely on the product being built. The mental overhead of constant supervision disappears.

### Journey Requirements Summary

The primary journey reveals requirements for:
- **Modular file loading protocol** - Clear sequence for loading shared files then agent-specific modules
- **Context request automation** - Advisor automatically asks for sprint status and story context
- **Multi-type violation detection** - Advisor catches self-certification, scope creep, architectural violations, and missed checkpoints
- **Decision guidance** - Advisor tells Coordinator exactly which options to pick when agents present choices
- **Session hygiene enforcement** - Advisor ensures commits happen between sessions
- **Instruction generation** - Advisor provides exact agent instructions without Coordinator thinking
- **Error recovery guidance** - Advisor tells Coordinator exactly what to do when violations occur

## Innovation & Novel Patterns

### Detected Innovation Areas

**Core Paradigm Shift: Prompts as Software Modules**
The fundamental innovation is treating prompts as software modules rather than static documents. This introduces single responsibility principle, load order dependencies, and independent testability - none of which exists in current prompt design practice. This redefines how AI agent prompts are architected, moving from monolithic documents to modular, engineered systems.

**Specific Technical Innovations**
- **Identity First Loading**: Identity always loads first and serves as the most stable context, ensuring agents maintain role identity even under pressure
- **Independent File Utility Test**: Each file must prevent its critical violations when loaded alone, creating bulletproof modular components
- **Pushback Resilience Design**: Use of absolute language (NEVER, MUST) that holds under Coordinator challenge and pressure

**Novel Approach in the Market**
No existing BMAD or multi-agent prompt system applies software engineering principles to prompt file architecture. The closest existing approach is monolithic prompts with sections - equivalent to putting all code in one file with comments. bmad-crew introduces a fundamentally new architectural paradigm.

### Market Context & Competitive Landscape

Current AI prompt design treats prompts as static documents with sections. bmad-crew creates a new category: engineered prompt systems. This positions it as foundational infrastructure for reliable multi-agent workflows rather than just another prompt template collection.

### Validation Approach

Live BMAD sessions serve as the validation methodology. The test is whether the Advisor can guide a full session with zero Coordinator interventions while maintaining role identity throughout. Success is measured by session log analysis showing violations caught before Coordinator notice.

### Risk Mitigation

**Fallback Strategy**: If modular approach fails, the system can be collapsed back into monolithic prompts while retaining the absolute language principles. The Independent File Utility Test provides early detection of architectural flaws before full session deployment.

**Technical Risk**: The primary risk is that LLMs may not respond to modular loading as expected. Mitigation is through extensive testing of each module independently before integration.
