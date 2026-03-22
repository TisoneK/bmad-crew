# Session Init

## Purpose
Initialize advisory session with automatic artifact discovery. The Coordinator never loads context manually — the Advisor reads first, then asks only what it cannot determine on its own.

## On Activation

### Step 1 — Load Memory
- Load `{project-root}/_bmad/_memory/bmad-crew-agent-advisor-sidecar/session-state.md`
- Load access boundaries from `access-boundaries.md`
- If session already in progress: read state and resume from last completed gate

### Step 2 — Auto-Discovery and File Reading (IDEA-003)

Run discovery script to find available artifacts:
```
{python} {project-root}/_bmad/crew/skills/bmad-crew-agent-advisor/scripts/session-validator.py --discover
```

The script returns a list of file paths. **You must open and read each file — not just list their names.**

**Read in this priority order — do not skip any that exist:**

1. `sprint-status.yaml` (project root) — read fully, extract sprint number and story statuses
2. `{project-root}/_bmad/bmad-crew/stories/*.md` — read each story with status ready-for-dev or in-progress
3. `project-context.md` (project root) — read fully
4. `{project-root}/_bmad/bmad-crew/locked-decisions.md` — read fully
5. `_bmad-output/planning-artifacts/*.md` — read each file found (PRD, product brief, architecture)
6. `_bmad-output/brainstorming/*.md` — read the most recent session
7. Any `docs/`, `proposals/`, files matching `*.proposal.md`, `FEATURE_*.md`

**After reading each file, extract:**
- What phase is the project in (brainstorming / planning / implementation)?
- What is the most recent completed artifact?
- What is the logical next step?

Do not summarise as "N files found". Name each file you read and state what it contains in one line.

### Step 3 — Re-load Locked Decisions (IDEA-012)
After discovery, explicitly re-read `locked-decisions.md` even if loaded from memory. Long sessions cause context drift — the file is the source of truth.

### Step 4 — Present Findings

Show what was read (not just found) with one-line summaries:
```
Read:
- sprint-status.yaml: [found/missing] — [sprint N, X stories / no active sprint]
- locked-decisions.md: [found/missing] — [N decisions / empty]
- prd.md: [one-line summary of what it contains]
- product-brief-*.md: [one-line summary]
- [each additional file read with one-line summary]

1. Continue — [specific summary: phase, last artifact, recommended next command]
2. New session — [only if genuinely no artifacts or all work complete]
3. Something else — tell me
```

The option 1 summary must be specific — name the phase and the exact next command.
Present exactly these three options. Wait for Coordinator choice.

### Step 5 — Route Based on Choice

**Option 1 — Continue:**
- Load all discovered artifacts
- Determine current state from sprint-status.yaml + story files
- Re-read locked-decisions.md (already done in Step 3)
- Run git validation automatically: `{python} {project-root}/_bmad/crew/skills/bmad-crew-agent-advisor/scripts/git-validator.py --check-clean`
- If git is dirty: flag it before anything else
- Announce readiness and give the single correct next command

**Option 2 — New session:**
- Verify no active work (no in-progress stories, clean git)
- Initialize fresh session-state.md
- Ask for sprint goals if starting from scratch

**Option 3 — Something else:**
- Load specific requested artifacts
- Proceed with targeted advisory

### Step 6 — Update Session State
Write to `{project-root}/_bmad/_memory/bmad-crew-agent-advisor-sidecar/session-state.md`:
```markdown
## Current Phase
- Phase: [detected from sprint-status.yaml]
- Last Completed Gate: [session-init]
- Session Start: [timestamp]

## Context Loaded
- Sprint Status: [loaded/missing] — Sprint [N]
- Active Stories: [list]
- Locked Decisions: [N loaded]
- Additional Context: [list]

## Git State
- Status: [clean/dirty]
- Last Commit: [hash and message]
```

## Error Handling

**locked-decisions.md missing:**
```
locked-decisions.md not found. I'll have reduced enforcement on architectural decisions.
Proceed anyway, or tell me where the file is.
```

**sprint-status.yaml missing:**
```
No sprint-status.yaml found. Tell me what we're working on, or provide the file path.
```

**Git is dirty at session start:**
```
VIOLATION: Uncommitted changes detected before session start.
Run: git status
Commit or stash all changes before we proceed.
```
