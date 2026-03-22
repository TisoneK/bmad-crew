# Session Init

## Purpose
Initialize advisory session with automatic artifact discovery. The Coordinator never loads context manually — the Advisor reads first, then asks only what it cannot determine on its own.

## On Activation

### Step 1 — Load Memory
- Load `{project-root}/_bmad/_memory/bmad-crew-agent-advisor-sidecar/session-state.md`
- Load access boundaries from `access-boundaries.md`
- If session already in progress: read state and resume from last completed gate

### Step 2 — Auto-Discovery (IDEA-003)

Run discovery script to find available artifacts:
```
python3 scripts/session-validator.py --discover
```

Scan in this order:
1. `sprint-status.yaml` (project root)
2. `{project-root}/_bmad/bmad-crew/stories/*.md` (filter: ready-for-dev, in-progress)
3. `project-context.md` (project root)
4. `{project-root}/_bmad/bmad-crew/locked-decisions.md`
5. Additional context: `docs/`, `proposals/`, `_bmad-output/`, files matching `*.proposal.md`, `FEATURE_*.md`, `brainstorming-*.md`

Read each discovered file. Do not ask the Coordinator to load them.

### Step 3 — Re-load Locked Decisions (IDEA-012)
After discovery, explicitly re-read `locked-decisions.md` even if loaded from memory. Long sessions cause context drift — the file is the source of truth.

### Step 4 — Present Findings

Show what was found concisely:
```
Found:
- sprint-status.yaml: [sprint N, X stories in-progress / ready-for-dev]
- locked-decisions.md: [N decisions]
- [any additional context files found]

1. Continue — [summary of where we are and recommended next step]
2. New session — [if no active work found]
3. Something else — tell me
```

Present exactly these three options. No more, no less. Wait for Coordinator choice.

### Step 5 — Route Based on Choice

**Option 1 — Continue:**
- Load all discovered artifacts
- Determine current state from sprint-status.yaml + story files
- Re-read locked-decisions.md (already done in Step 3)
- Run git validation automatically: `python3 scripts/git-validator.py --check-clean`
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
