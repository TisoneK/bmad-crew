# Advisory Module Upgrade Plan: v0.1.0 → v0.2.0

## Phase 1: Core Architecture Enhancement

**1. Two-Layer Summary System**
- `bmad-agent-builder` → Edit Agent → `bmad-crew-agent-advisor`
- **Focus**: Transform current QA-style summaries to capture advisor-Tisone conversations
- **Key change**: Add reasoning, pushback moments, and judgment calls to summary format

**2. Break Protocol Implementation**
- `bmad-workflow-builder` → Edit Workflow → Create `/advisor-break` and `/advisor-resume` commands
- **Focus**: Encode personality shifts between formal advisor and partner modes
- **Add**: Dynamic context switching for break periods

## Phase 2: Process Enforcement Features

**3. Premature Implementation Detection**
- `bmad-agent-builder` → Edit Agent → Add architecture phase validation
- **Focus**: Check codebase against locked PRD decisions before architecture design
- **Implementation**: File conflict detection at architecture phase start

**4. Scope Creep Prevention**
- `bmad-agent-builder` → Edit Agent → Add implementation start validation
- **Focus**: Verify codebase against approved story list
- **Implementation**: Red flag files not traceable to completed stories

**5. Retrospective Quality Control**
- `bmad-agent-builder` → Edit Agent → Add facilitation validation
- **Focus**: Ensure retrospectives use discussion vs auto-generation
- **Implementation**: Agent selection guidelines for retrospectives

## Phase 3: Multi-Agent Coordination

**6. Coordinator Protocol**
- `bmad-workflow-builder` → Create Workflow → Multi-agent coordination template
- **Focus**: Context update prompt templates for agent handoffs
- **Implementation**: Standardized information flow protocols

**7. Team Structure Enforcement**
- `bmad-agent-builder` → Edit Agent → Add read-only constraint validation
- **Focus**: Ensure Advisor never touches code directly
- **Implementation**: Access boundary validation

## Phase 4: Structural Improvements

**8. God Class Prevention**
- `bmad-agent-builder` → Edit Agent → Add architectural concern separation
- **Focus**: Validate concern-level separation within modules
- **Implementation**: Subdirectory structure validation

**9. Commit Discipline**
- `bmad-workflow-builder` → Create Workflow → Commit-per-story enforcement
- **Focus**: Immediate commit and push after story verification
- **Implementation**: Git state validation at story boundaries

## Phase 5: Documentation & Training

**10. Context Update Templates**
- `bmad-workflow-builder` → Create Workflow → Standardized handoff templates
- **Focus**: Clean agent handoffs with preserved context
- **Implementation**: Template library for common scenarios

**11. Session Management**
- `bmad-agent-builder` → Edit Agent → Enhanced session initialization
- **Focus**: `/advisor-start` onboarding with full context
- **Implementation**: Comprehensive context loading system

## Implementation Priority

**High Priority** (Core functionality):
1. Two-layer summary system
2. Break protocol commands
3. Premature implementation detection
4. Scope creep prevention

**Medium Priority** (Process enhancement):
5. Retrospective quality control
6. Coordinator protocol
7. Team structure enforcement

**Low Priority** (Optimization):
8. God class prevention
9. Commit discipline
10. Context update templates
11. Session management

## Key Insights to Implement

- **"Building the thing by doing the thing"** — Use existing summary files as templates
- **Coordinator pattern** — Multi-agent development requires formal protocols
- **Zero-correction sessions** — Track upstream quality metrics
- **Compounding scope creep** — Early detection prevents cascade failures

This upgrade transforms the advisory module from a simple supervisor to a comprehensive session management system that enforces BMAD methodology while reducing Coordinator cognitive load.
