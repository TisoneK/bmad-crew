---
stepsCompleted: [1, 2, 3, 4]
inputDocuments: []
session_topic: 'Modular multi-agent prompt system for BMAD workflows'
session_goals: 'Define module structure for all agent prompts (Advisor, Executor, Specialist, Coordinator); Define shared files all agents consume; Define loading protocol per agent; Ensure each file is independently useful with no cross-dependencies'
selected_approach: 'progressive-flow'
techniques_used: ['First Principles Thinking', 'Morphological Analysis', 'SCAMPER Method', 'Solution Matrix']
ideas_generated: ['Role Boundary Fundamentalism', 'Identity First Loading Principle', 'Independent File Utility Test', 'File Granularity Principle', 'Failure Prevention Matrix', 'Pushback Resilience Design', 'SCAMPER: Substitute - Extract embedded content to separate files', 'SCAMPER: Combine - Merge gates and pushback rules', 'SCAMPER: Adapt - Software patterns to prompt files', 'SCAMPER: Modify - 5-line absolute identity', 'SCAMPER: Put to other uses - Onboarding as alternate use', 'SCAMPER: Eliminate - 100+ lines removable', 'SCAMPER: Reverse - Confirms identity-first loading principle', 'Solution Matrix: Implementation Priority Framework', 'Solution Matrix: Risk Assessment Matrix', 'Solution Matrix: Decision Framework for Future Changes', 'Solution Matrix: Build Order (5-week plan)', 'Solution Matrix: Success Metrics']
context_file: 'docs/evidence/'
---

# Brainstorming Session Results

**Facilitator:** Tisone
**Date:** 2026-03-20

## Session Overview

**Topic:** Modular multi-agent prompt system for BMAD workflows
**Goals:** Define module structure for all agent prompts (Advisor, Executor, Specialist, Coordinator); Define shared files all agents consume; Define loading protocol per agent; Ensure each file is independently useful with no cross-dependencies

### Context Guidance
Context loaded from docs/evidence/: Key files include MULTI_AGENT_PROMPT_SYSTEM_SPEC.md, ADVISOR_PROMPT_RESTRUCTURE_SPEC.md, ADVISOR_SESSION_MISTAKES_001.md, ADVISOR_IDEAS.md, WINDSURF_SESSION.txt, GEMINI_SESSION.md. These contain the problem definition, failure evidence, and initial architecture for the multi-agent prompt system.

**Key Insights from Context:**
- **Core Problem:** Monolithic agent prompts cause LLMs to lose role identity under pressure, leading to role collapse (Advisor becoming Executor, self-certification, etc.)
- **Solution Approach:** Modular system with separate files for each concern, organized by agent type (shared/, coordinator/, advisor/, executor/, specialist/)
- **Key Principles:** Each file must be independently useful; shared files never duplicated; identity files loaded first; gate files treated as active checklists
- **Critical Files Needed:** Identity (role definition), response rules (formatting), workflow gates (checklists), session init, BMAD reference, locked decisions
- **Loading Protocol:** Identity → Session Init → Response Rules → Workflow Gates → BMAD Reference → Locked Decisions → Project Context → Ideas/Mistakes files
- **Proven Benefits:** Prevents role confusion, ensures proper verification, maintains WHAT not HOW guidance, stops skipped checkpoints

### Session Setup
Based on your responses, I understand we're focusing on creating a modular multi-agent prompt system for BMAD workflows with goals around defining module structure, shared files, loading protocols, and ensuring independent usefulness of each file.

## Technique Selection

**Approach:** Progressive Technique Flow
**Journey Design:** Systematic development from exploration to action

**Progressive Techniques:**

- **Phase 1 - Exploration:** First Principles Thinking for maximum idea generation
- **Phase 2 - Pattern Recognition:** Morphological Analysis for organizing insights
- **Phase 3 - Development:** SCAMPER Method for refining concepts
- **Phase 4 - Action Planning:** Solution Matrix for implementation planning

**Journey Rationale:** This progressive flow mirrors natural creative processes for designing complex systems like the modular multi-agent prompt system. Starting with First Principles Thinking allows us to break down the prompt system to fundamental truths and generate diverse architectural approaches. Morphological Analysis helps systematically explore all possible combinations of prompt modules, shared files, and loading protocols. SCAMPER Method enables us to refine and enhance strong concepts through structured improvement lenses. Finally, Solution Matrix transforms our designs into actionable implementation plans with clear decision frameworks for building the bmad-prompts/ directory structure.

## Technique Execution: Phase 1 - First Principles Thinking

**Let's explore First Principles Thinking together!**

I'm excited to facilitate **First Principles Thinking** with you as a creative partner, not just a respondent. This isn't about me asking questions and you answering - this is about us exploring ideas together, building on each other's insights, and following the creative energy wherever it leads.

**Technique Focus:** Strip away assumptions to rebuild from fundamental truths - essential for breakthrough innovation by asking 'What do we know for certain?' 'What are the fundamental truths?' and 'If we started from scratch?'
**Energy:** High energy, expansive thinking

### Key Discoveries from Phase 1

**[Category #1]: Role Boundary Fundamentalism**
_Concept_: Agent prompts must define immutable NEVER DO boundaries rather than descriptive role guidelines, as boundaries fail when written as permissions rather than hard stops that agents refuse under pressure.
_Novelty_: Focuses on negative constraints (what agents must never do) as the foundation of role integrity, tested by pushback resistance rather than unpressured compliance.

**[Category #2]: Identity First Loading Principle**
_Concept_: Identity rules must be loaded first, be under one page, use exclusively negative framing, contain zero workflow references, and contain exactly three permanent rules stated as absolutes with no exceptions.
_Novelty_: Treats identity as a stability anchor that must be maximally resistant to context decay through minimalism, negative framing, and absolute rule formulation.

**[Category #3]: Independent File Utility Test**
_Concept_: Each prompt file must prevent the single most critical violation for its agent type when loaded in isolation: Advisor prevents role collapse (becoming Executor), Executor prevents self-certification, Specialist prevents re-architecting, Coordinator prevents premature session opening. Resilience under pushback is the true test.
_Novelty_: Defines usefulness as failure prevention under pressure rather than feature completeness, with a concrete test method of isolated file loading and adversarial challenge.

**Creative Breakthrough from Phase 1:** The realization that role boundaries must be defined as NEVER DO actions rather than role descriptions, and that true usefulness is measured by resilience under pressure rather than feature completeness.

---

## Technique Execution: Phase 2 - Morphological Analysis

**Now exploring Morphological Analysis!**

This technique helps us systematically explore all possible combinations of the parameters we've identified for our modular multi-agent prompt system.

**Technique Focus:** Systematically explore all possible parameter combinations for complex systems requiring comprehensive solution mapping - identify key parameters, list options for each, try different combinations, and identify emerging patterns
**Energy:** Analytical, structured thinking

### Key Discoveries from Phase 2

**[Category #4]: File Granularity Principle**
_Concept_: Optimal file size contains one concern, one failure mode, and one agent action prevented - too small if it merely restates existing content, too large if it contains contradictory rules across pages. Measured by readability in under 2 minutes and complete internalization.
_Novelty_: Defines granularity by cognitive load and contradiction prevention rather than arbitrary line counts, focusing on mental model integrity.

**[Category #5]: Failure Prevention Matrix**
_Concept_: Systematic mapping of agent-file interactions showing what each combination prevents: Advisor+identity prevents role collapse, Advisor+gates prevents skipped checkpoints, Executor+identity prevents self-execution, Executor+git rules prevents false success reporting, Specialist+identity prevents re-architecting, Coordinator+responsibilities prevents doing agent work, Coordinator+gate rules prevents premature sessions, Shared+team structure prevents role collapse, Shared+locked decisions prevents re-opening decisions.
_Novelty_: Creates a comprehensive failure prevention map that ensures every critical violation has a dedicated file responsible for preventing it.

**[Category #6]: Pushback Resilience Design**
_Concept_: Resilient files use absolute language (NEVER, MUST) with no exceptions, while non-resilient files use advisory language (SHOULD, RECOMMENDED) that folds under pressure. Key design feature is standalone rules that don't depend on remembering other rules. Tested by simulating Coordinator challenges and verifying agent compliance under direct pressure.
_Novelty_: Defines resilience as maintaining compliance under adversarial challenge rather than normal conditions, with concrete testing methodology.

**Creative Breakthrough from Phase 2:** The realization that optimal file design balances granularity (one concern per file), comprehensive failure prevention mapping, and pushback resilience through absolute language and standalone rules.

---

## Technique Execution: Phase 3 - SCAMPER Method

**Starting SCAMPER Method for our Modular Multi-Agent Prompt System**

SCAMPER is a powerful creative thinking technique that prompts us to look at existing designs from seven different perspectives:

| Letter | Question | Application to Our Prompt System |
|--------|----------|----------------------------------|
| **S** | Substitute? | What if we substituted agent roles? What if we swapped file structures? |
| **C** | Combine? | Could we combine Advisor + Coordinator functions? Merge shared utilities? |
| **A** | Adapt? | How would enterprise patterns adapt? How would small team patterns adapt? |
| **M** | Modify/Magnify? | What if we magnified role boundaries? What if we modified loading order? |
| **P** | Put to other uses? | Could prompt files be used for testing? For documentation? For onboarding? |
| **E** | Eliminate? | What happens if we eliminate shared dependencies? Remove Coordinator mediation? |
| **R** | Reverse/Rearrange? | What if loading was reverse order? What if boundaries were inverted? |

**Let's explore these dimensions systematically.** I'll guide you through each SCAMPER element, and we'll capture the most innovative ideas.

**Start with Substitute:** Can you think of any substitutions that might dramatically improve our current design? For example:
- What if we substituted the role boundary definition method?
- What if we used a different file organization strategy?
- What if the identity loading principle worked differently?

**Share your most radical substitution idea, and let's explore it together!**

---

---

## Technique Execution: Phase 4 - Solution Matrix

**Starting Solution Matrix for Implementation Planning**

The Solution Matrix transforms our brainstormed ideas into an actionable implementation plan. We'll create decision frameworks that guide the actual building of the bmad-prompts/ directory structure.

### Solution Matrix Framework

| Dimension | Option A | Option B | Option C | Decision Criteria |
|-----------|----------|----------|----------|-------------------|
| **File Granularity** | Ultra-fine (1 rule per file) | Fine (1 concern per file) | Medium (1 phase per file) | Must be readable in <2 min, contain 1 failure mode |
| **Identity Loading** | Identity first (current) | Identity interleaved | Identity last | ONLY Identity First works - all others cause role collapse |
| **Shared Files Duplication** | Zero tolerance | Allow with warning | Accept duplication | ZERO tolerance - shared files never duplicated |
| **Failure Prevention** | Matrix mapping (current) | Ad-hoc rules | No explicit mapping | Matrix mapping required - each violation needs owner |
| **Language Strength** | Absolute (NEVER, MUST) | Advisory (SHOULD) | Permissive (CAN) | ONLY Absolute works under pushback |
| **Onboarding Use** | Primary design goal | Secondary benefit | Not considered | Secondary benefit - files designed for independence automatically serve onboarding |

### Implementation Priority Matrix

| Priority | File | From Which Idea | Dependencies | Estimated Effort |
|----------|------|-----------------|--------------|------------------|
| P0 | shared/bmad-team-structure.md | First Principles + SCAMPER-Adapt | None | 1 hr |
| P0 | shared/bmad-workflow-reference.md | SCAMPER-Eliminate | None | 2 hr |
| P0 | advisor/advisor-identity.md | First Principles + SCAMPER-Modify | None | 1 hr |
| P1 | advisor/advisor-response-rules.md | SCAMPER-Substitute | advisor-identity | 2 hr |
| P1 | advisor/advisor-workflow-gates.md | SCAMPER-Combine + Morphological | advisor-identity | 3 hr |
| P2 | advisor/advisor-pushback-rules.md | SCAMPER-Combine | advisor-identity | 2 hr |
| P2 | advisor/advisor-session-init.md | SCAMPER-Substitute | advisor-identity | 1 hr |
| P2 | shared/bmad-locked-decisions.md | Morphological | None | 1 hr |
| P3 | coordinator/ files | Multi-Agent Spec | All shared files | 8 hr |
| P3 | executor/ files | Multi-Agent Spec | All shared files | 8 hr |
| P4 | specialist/ files | Multi-Agent Spec | All shared files | 4 hr |

### Risk Assessment Matrix

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Identity rules diluted by context | HIGH | CRITICAL | Keep identity file <5 lines, load first, NEVER language only |
| Shared files duplicated | MEDIUM | HIGH | Zero-tolerance policy, automated check in build |
| Gate rules forgotten under pressure | HIGH | HIGH | Re-read gates before EVERY response (enforced by protocol) |
| Role collapse under pushback | HIGH | CRITICAL | Standalone rules, no cross-references, absolute language |
| Files become too granular | MEDIUM | MEDIUM | 2-min read rule, one failure mode per file |
| Onboarding value not realized | LOW | LOW | By design - independent files automatically serve onboarding |

### Decision Framework for Future Changes

When adding new prompt files, answer these questions:

1. **Is this one concern?** → If no, split further
2. **Does it prevent one failure mode?** → If no, reconsider scope
3. **Can it work in isolation?** → Test with only this file loaded
4. **Does it use absolute language?** → If SHOULD/RECOMMENDED, upgrade to NEVER/MUST
5. **Does it depend on other files?** → If yes, rewrite to be standalone
6. **Is it duplicating shared content?** → If yes, move to shared/

### Build Order Confirmation

Following the Multi-Agent Spec and our brainstorming:

1. **Week 1:** shared/ files (team-structure, workflow-reference, locked-decisions, project-context)
2. **Week 2:** advisor/ files split from ADVISOR_PROMPT_v3.md
3. **Week 3:** coordinator/ files from scratch
4. **Week 4:** executor/ files from scratch
5. **Week 5:** specialist/ files from scratch
6. **Ongoing:** Testing and refinement

### Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Role collapse incidents | 0 per session | Human review of session logs |
| Identity file size | <5 lines | Line count of advisor-identity.md |
| File independence | 100% | Each file tested in isolation |
| Pushback resilience | Pass | Coordinator challenges tested |
| Onboarding time | <30 min | New agent loads only identity |

---

## SCAMPER Analysis Results

Based on analysis of the current ADVISOR_PROMPT_v3.md (361 lines, monolithic) and the target modular system defined in MULTI_AGENT_PROMPT_SYSTEM_SPEC.md, here are concrete SCAMPER insights:

### S - Substitute: What in the current monolithic prompt can be replaced with a better mechanism?

| Current Element | Substitute With | Why Better |
|-----------------|-----------------|------------|
| "How You Respond" section (lines 44-104) | Separate advisor-response-rules.md | Formatting rules are mechanical and non-negotiable - keeping them separate prevents them from being lost when session gets complex |
| BMAD workflow reference embedded (lines 290-322) | shared/bmad-workflow-reference.md | Reference material should be lookup, not embedded context that competes for attention |
| Context request sequence (lines 327-356) | advisor-session-init.md | Session initialization is one-time per session - distinct file prevents it from being skipped |

### C - Combine: Which files or concerns can be merged without causing context decay?

| Current Elements | Combined File | Rationale |
|------------------|---------------|------------|
| Locked Decisions Protocol + Document Verification Rule | advisor-workflow-gates.md | Both are checkpoints that must fire at specific moments - combining creates a single source of truth for mandatory stops |
| Pushback Calibration + Implementation Session Rules | advisor-pushback-rules.md | Both govern session behavior under pressure - combining ensures consistent boundary enforcement |

**Warning:** Do NOT combine identity with any other concern. The Identity First Loading Principle requires it to remain isolated.

### A - Adapt: What patterns from software module design apply directly to prompt file design?

| Software Design Pattern | Prompt File Application |
|------------------------|------------------------|
| **Single Responsibility Principle** | Each file does ONE thing: identity, response rules, gates, session init. One concern, one failure mode, one action prevented. |
| **Interface Segregation** | Advisor doesn't need all files loaded simultaneously. Loading protocol (identity → session-init → response-rules → gates) = interface that shows only what's needed when needed. |
| **Dependency Inversion** | High-level rules (identity = "who I am") must not depend on low-level details (git commands). Identity file contains ZERO workflow references. |
| **Open/Closed Principle** | Files are open for extension (adding new rules) but closed for modification (identity rules never change). |

### M - Modify: What happens if identity files are made even shorter and more absolute?

Current advisor-identity.md (~18 lines from restructure spec):
```
- Role: read-only, judgment not execution
- Team: Coordinator, Executor, Specialist, Advisor  
- NEVER: write code, run commands, drive BMAD
- 3 Permanent Rules (subject to change based on analysis)
```

**Modified version - 5 lines maximum:**
```
# ADVISOR_IDENTITY.md
You are the Advisor. You NEVER: write code, run commands, drive BMAD workflow.
Rule 1: NEVER confirm a document you have not read.
Rule 2: NEVER accept git claims without log verification.
Rule 3: NEVER cross the Coordinator/Executor boundary.
```

**What breaks:** Nothing. Making identity shorter and more absolute INCREASES resilience under pressure. The current version has explanatory text that dilutes the message. The modified version uses ONLY absolute language (NEVER, MUST) with zero exceptions - exactly what Pushback Resilience Design requires.

### P - Put to other uses: Can the same prompt files serve as onboarding docs for new team members?

| File | Alternate Use | How |
|------|---------------|-----|
| advisor-identity.md | Onboarding for new Advisor agents | New Advisor LLM loads only this file first - serves as instant role understanding |
| advisor-workflow-gates.md | QA checklist for session auditing | Human reviewer checks gates after session to verify compliance |
| shared/bmad-team-structure.md | Team documentation | Reference for anyone learning BMAD multi-agent system |
| shared/bmad-workflow-reference.md | Onboarding for new BMAD users | Sequential reference for learning the workflow |

**Key insight:** Files designed for independent usefulness automatically become useful for onboarding. If advisor-identity.md alone prevents role collapse, it alone is enough to onboard a new Advisor.

### E - Eliminate: What in ADVISOR_PROMPT_v3.md can be removed entirely without losing value?

| Section | Lines | Can Eliminate? | Reason |
|---------|-------|----------------|--------|
| BMAD Workflow Reference | 290-322 | **YES - Move to shared/** | Reference material, not rule. Looked up, not memorized. |
| Session Init Instructions | 327-361 | **YES - Move to advisor-session-init.md** | Context-dependent, should be dynamically loaded |
| "What You Are Not Doing" | 279-287 | **YES - Redundant** | Already covered in Read-Only Constraint (lines 108-118) |
| Examples in response rules | 64-76 | **PARTIAL** | Keep ONE example, remove the rest to reduce noise |

**Total eliminable content:** ~100 lines moved to modular files, ~8 lines redundant content removed.

### R - Reverse: What if the Executor loaded identity last instead of first - what breaks?

**Scenario:** Executor loads identity file LAST in the loading order.

**What breaks:**
1. **Role collapse immediate** - Executor starts working without knowing what it should never do. First context is implementation rules, not identity.
2. **Self-certification unpreventable** - executor-identity.md (which contains "NEVER self-certify completion") is buried under 8 other files. When Coordinator challenges, identity is already decayed.
3. **Fundamental principle violated** - First Principles Thinking established that identity must be the most stable context, loaded first because it's the last thing that should drift. Loading last inverts this.

**Reverse is anti-pattern** - This is exactly what the current monolithic prompt suffers from (identity buried among 361 lines), and exactly what the modular system fixes by loading identity FIRST.

---

**Key SCAMPER Insight:** The monolithic ADVISOR_PROMPT_v3.md is essentially a "reverse identity loading" problem - identity is buried at the start but surrounded by 350+ lines of other content. The modular system fixes this by physically separating identity into its own file that loads FIRST. SCAMPER confirms: Substitute (extract embedded content), Combine (merge related gates), Adapt (software patterns), Modify (make identity shorter), Put to other uses (onboarding), Eliminate (redundant sections), Reverse (don't do this - breaks everything).

---

## Session Summary So Far

**Ideas Generated:**
1. **Role Boundary Fundamentalism** - NEVER DO boundaries rather than descriptive guidelines
2. **Identity First Loading Principle** - Identity rules loaded first with three absolute rules
3. **Independent File Utility Test** - Each file must prevent critical violation when isolated
4. **File Granularity Principle** - One concern, one failure mode, one action prevented per file
5. **Failure Prevention Matrix** - Systematic mapping of agent-file interactions
6. **Pushback Resilience Design** - Absolute language and standalone rules

**Energy and Engagement:** High - we've systematically analyzed the key parameters for effective prompt file design through collaborative exploration.

**All Four Phases Complete!**

Our Progressive Technique Flow brainstorming session is now complete:
- ✅ Phase 1: First Principles Thinking
- ✅ Phase 2: Morphological Analysis  
- ✅ Phase 3: SCAMPER Method
- ✅ Phase 4: Solution Matrix

The session document contains all insights, decisions, and implementation plans ready for execution.
1. **Substitute** - What's one substitution that could dramatically improve the design?
2. **Combine** - What two things could we combine for better effect?
3. **Adapt** - How would different contexts (enterprise vs. small team) adapt this?
4. **Modify** - What if we magnified a particular aspect?
5. **Put to other uses** - What else could these prompt files be used for?
6. **Eliminate** - What would happen if we removed a key element?
7. **Reverse** - What if we inverted a fundamental assumption?

**Share your ideas to continue building our solution!**
