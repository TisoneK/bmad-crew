# BMAD Workflow Reference

Load this file on every activation. The Advisor must know the complete workflow to give correct next-command recommendations and detect out-of-order execution.

---

## Complete Workflow Sequence

### Phase 1 — Analysis
| Command | New chat? | Produces output? | Output type |
|---------|-----------|-----------------|-------------|
| `/bmad-analyst` | Yes | Yes | Research, briefs |
| `/bmad-pm` (brainstorming) | Yes | Yes | Brainstorming session file |

### Phase 2 — Planning
| Command | New chat? | Produces output? | Output type |
|---------|-----------|-----------------|-------------|
| `/bmad-pm` (create-prd) | Yes | Yes | PRD file |
| `/bmad-architect` (create-architecture) | Yes | Yes | Architecture doc |
| `/bmad-pm` (create-epics-and-stories) | Yes | Yes | Epics + story files |
| `/bmad-pm` (create-story) | Yes | Yes | Single story file |

### Phase 3 — Implementation (story lifecycle — repeats per story)
| Command | New chat? | Produces output? | Output type |
|---------|-----------|-----------------|-------------|
| `/bmad-bmm-dev-story` | **Yes — always** | Yes | Code + updated story |
| `/bmad-bmm-code-review` | **Yes — always** | Yes | Code review triage |
| `/bmad-bmm-retrospective` | Yes | Yes | Retrospective report |

### Phase 4 — Anytime
| Command | New chat? | Produces output? | Output type |
|---------|-----------|-----------------|-------------|
| `/bmad-sm` (sprint status) | No | Sometimes | sprint-status.yaml update |

---

## The Story Lifecycle (Implementation)

This is the atomic unit of implementation work. The Advisor enforces every gate.

```
create-story → [Advisor validates] → commit → dev-story (new chat)
    → [Advisor validates code] → code-review (new chat)
    → [Advisor validates triage] → patches committed
    → mistakes file generated → next create-story
```

### Gate-by-gate rules

**After create-story:**
1. Advisor reads the actual story file — never accepts Builder's claim
2. Validates against locked decisions, architecture, project-context.md
3. If issues: flag, block commit, instruct correction
4. If clean: instruct commit, then give dev-story command in new chat

**After dev-story:**
1. Verify git: uncommitted changes exist (Builder produced output)
2. Advisor reads changed files to assess quality
3. If clean: instruct commit, then give code-review command in new chat

**After code-review:**
1. Advisor reads the triage output — never accepts Builder's claim
2. Applies escalation paths per finding classification (see instruction-generation.md)
3. Once all findings resolved and patches committed:
   - Generate mistakes file (IDEA-001)
   - Instruct commit with hash
   - Give next create-story command

---

## Command Syntax Rules

**These commands take NO arguments — they read sprint-status.yaml automatically:**
- `/bmad-bmm-dev-story`
- `/bmad-bmm-code-review`
- `/bmad-bmm-retrospective`
- `/bmad-bmm-create-story`

**Wrong:** `/bmad-bmm-dev-story story-3.1` — never add a story name
**Right:** `/bmad-bmm-dev-story`

**These commands require explicit context or flags:**
- `/bmad-pm` — requires capability selection (brainstorming, create-prd, etc.)
- `/bmad-architect` — requires capability selection

---

## Commands That Require a New Chat

**Always new chat:**
- dev-story
- code-review
- retrospective
- Any planning-phase command that produces a document

**Same chat OK:**
- Sprint status checks
- Advisor session (Advisor lives in its own persistent chat)
- Quick queries to the PM or Architect without document output

---

## Commit Checkpoint — All Output-Producing Commands (IDEA-002)

Every command that produces output files must be followed by a commit before a new session opens. This is non-negotiable regardless of phase.

**Covered commands:**
- brainstorming → commit
- create-prd → commit
- create-architecture → commit
- create-epics-and-stories → commit
- create-story → commit
- dev-story → commit
- code-review (patches) → commit
- retrospective → commit

**The gate:** Advisor verifies git log shows a commit after each command before instructing the next session open. Run `scripts/git-validator.py --check-commits-after-output` to validate.

---

## Output Format for Next-Step Instructions

After any gate passes, the Advisor gives exactly this format:

```
[One sentence: what passed and what the Coordinator needs to do]

[Command in its own code block]
```

Example:
```
Story 3.1 is clean. Commit the file, then open a new chat and run:

/bmad-bmm-dev-story
```

Never: options lists, "would you like me to...", multi-step instructions when one line covers it.
