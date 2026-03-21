---
stepsCompleted: [1, 2]
inputDocuments: []
session_topic: 'bmad-crew as a BMAD custom module — a packaged, npm-installable module that applies software engineering principles to multi-agent prompt design, reducing Coordinator cognitive load across all BMAD workflow sessions.'
session_goals: 'Define the correct module structure for bmad-crew as a BMAD custom module (module.yaml, agents/, workflows/); Define how the Advisor agent is packaged inside the module; Define how shared prompt files are distributed as part of the module; Define the loading protocol when installed via BMAD installer; Identify what changes from the previous brainstorming session now that distribution is npm + BMAD installer'
selected_approach: 'ai-recommended'
techniques_used: ['First Principles Thinking', 'Morphological Analysis', 'SCAMPER Method']
context_file: 'docs/evidence/'
---

# Brainstorming Session Results

## Session Overview

**Topic:** bmad-crew as a BMAD custom module — a packaged, npm-installable module that applies software engineering principles to multi-agent prompt design, reducing Coordinator cognitive load across all BMAD workflow sessions.
**Goals:** Define the correct module structure for bmad-crew as a BMAD custom module (module.yaml, agents/, workflows/); Define how the Advisor agent is packaged inside the module; Define how shared prompt files are distributed as part of the module; Define the loading protocol when installed via BMAD installer; Identify what changes from the previous brainstorming session now that distribution is npm + BMAD installer

### Context Guidance

Context loaded from docs/evidence/: Key files include MULTI_AGENT_PROMPT_SYSTEM_SPEC.md, ADVISOR_PROMPT_RESTRUCTURE_SPEC.md, ADVISOR_SESSION_MISTAKES_001.md, ADVISOR_IDEAS.md, WINDSURF_SESSION.txt, GEMINI_SESSION.md, product-brief-bmad-crew-2026-03-20.md, brainstorming-session-2026-03-20.md, and partial PRD. These contain the foundational modular prompt system architecture, failure evidence from monolithic prompts, and previous brainstorming results for manual file-based approach.

**Key Insights from Context:**
- **Previous State**: Manual file-based modular system with shared/, advisor/, coordinator/, executor/, specialist/ directories
- **Core Problem**: Monolithic prompts cause role collapse under pressure; modular system prevents this through Identity First Loading, Independent File Utility, and Pushback Resilience
- **Distribution Shift**: Moving from manual file management to npm + BMAD installer distribution changes packaging, loading protocol, and update mechanisms
- **Module Structure**: Must follow BMAD custom module conventions (module.yaml, agents/, workflows/) while preserving modular prompt principles
- **Critical Requirements**: Identity files load first, each file independently useful, absolute language for pushback resilience, shared files never duplicated

### Session Setup

Based on your responses, I understand we're focusing on transforming bmad-crew from a manual file-based modular prompt system into a distributable BMAD custom module using npm + BMAD installer, while preserving all the architectural principles that prevent agent role collapse.

## Technique Selection

**Approach:** AI-Recommended Techniques
**Analysis Context:** bmad-crew as a BMAD custom module with focus on transforming manual file-based modular prompt system into npm-installable module while preserving core architectural principles

**Recommended Techniques:**

- **First Principles Thinking:** Strip away assumptions about module packaging and rebuild from fundamental truths about what makes modular prompts effective in distributed form
- **Morphological Analysis:** Systematically explore all parameter combinations for module structure (module.yaml formats, agent packaging, loading protocols, distribution mechanisms)
- **SCAMPER Method:** Transform manual system through systematic improvement lenses (Substitute files with module packaging, Combine agent definitions, Adapt loading protocols)

**AI Rationale:** These three techniques work together to first establish core principles that must be preserved, then systematically explore all architectural options, and finally generate concrete implementation steps through structured creative transformation.

**Facilitator:** Tisone
**Date:** 2026-03-21T04:18:00
