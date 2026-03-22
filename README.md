# bmad-crew

A BMAD custom module that sits beside the Coordinator during development sessions, telling them exactly what to type next so they never have to think about process management again.

---

## The Problem

In a BMAD multi-agent session, the Coordinator directs the Builder through every phase of development. This means the Coordinator must constantly:

- Know which BMAD command to run next
- Catch when the Builder self-certifies without committing
- Verify git status before opening new sessions
- Decide which option to pick when the Builder presents choices
- Produce summary files at phase boundaries
- Track locked decisions so the Builder doesn't re-open them

This cognitive overhead accumulates. The Coordinator ends up managing process instead of building product.

---

## The Solution

```
Advisor → Coordinator (developer) ← Builder
```

bmad-crew adds an **Advisor** agent to the session. The Advisor reads context automatically, validates every Builder output before the Coordinator acts on it, enforces every checkpoint, and gives one precise instruction at a time.

The Coordinator's only job becomes moving context between agents.

---

## What's New in v0.2.0

v0.2.0 implements all 14 improvements identified from real session usage. The Advisor now:

| Improvement | What changed |
|-------------|-------------|
| **Auto-discovery** | Reads sprint-status.yaml, story files, locked decisions, and project context automatically on activation — no manual loading |
| **Document verification gates** | Reads and validates every Builder output before the Coordinator acts. Never accepts a completion claim without reading the file |
| **Full lifecycle commit checkpoints** | Enforces commits after every output-producing command (brainstorming, PRD, architecture, epics, story, dev-story, code-review, retrospective) — not just dev-story |
| **BMAD workflow knowledge** | Knows the complete command sequence, which commands need a new chat, which take no arguments, and what each command produces |
| **Output format discipline** | One line of plain text + command in a code block. No options menus. No step-by-step when one line covers it |
| **Git auto-validation** | Runs git-validator.py directly — never asks the Coordinator to run git commands and paste back |
| **Code review escalation paths** | Handles patch / defer / intent_gap / bad_spec with distinct escalation for each. Blocks progression on bad_spec |
| **Pushback rules** | Holds firm on process violations. Yields only on genuine scope confusion (finding belongs to a future story) |
| **Locked decisions re-reference** | Re-reads locked-decisions.md before every next-command recommendation — not just at session start |
| **Phase summary files** | Mandatory SUM-00X summary before any "open a new chat" instruction |
| **Session-end detection** | Detects session endings beyond phase boundaries and triggers summary before exit |
| **Mistakes files** | Auto-generates ADVISOR_SESSION_MISTAKES_NNN.md after each completed story cycle |
| **Scope detection** | Distinguishes current-story scope from future-story scope in code review findings |
| **Self-doubt flag** | Flags complex validation results (intent_gap, bad_spec) for Coordinator review before action |

---

## Module Contents

```
_bmad/crew/
├── config.yaml
├── module-help.csv
└── skills/
    ├── bmad-crew-agent-advisor/         # Main Advisor agent — start here
    │   ├── SKILL.md
    │   ├── session-init.md              # Auto-discovery + context loading
    │   ├── violation-detection.md       # Role, process, quality violations + pushback rules
    │   ├── checkpoint-enforcement.md    # Full lifecycle gates + summary files + session-end
    │   ├── instruction-generation.md    # One-line output format + escalation paths
    │   ├── document-verification.md     # Read-before-validate for all Builder outputs
    │   ├── mistakes-file.md             # Per-cycle ADVISOR_SESSION_MISTAKES_NNN.md
    │   ├── save-memory.md
    │   ├── references/
    │   │   ├── bmad-workflow-reference.md  # Full BMAD command sequence and syntax rules
    │   │   ├── memory-system.md
    │   │   └── access-boundaries.md
    │   └── scripts/
    │       ├── git-validator.py         # Git state validation (runs automatically)
    │       ├── session-validator.py     # Artifact discovery + context validation
    │       ├── mistakes-generator.py    # Mistakes file generation
    │       ├── document-verifier.py     # Document quality validation
    │       └── run-tests.sh             # Full test suite
    ├── bmad-crew-advisor/               # Advisor workflow skill
    ├── bmad-crew-session-validator/     # Session state validator
    ├── bmad-crew-checkpoint-enforcer/   # Checkpoint compliance enforcer
    └── bmad-crew-locked-decisions/      # Locked decisions manager
```

---

## Installation

### Installing into an existing BMAD project

#### Step 1 — Copy the module

```bash
cp -r bmad-crew/_bmad/crew/ your-project/_bmad/crew/
```

#### Step 2 — Copy skills to your IDE

**Windsurf:**
```bash
cp -r bmad-crew/.windsurf/skills/bmad-crew-* your-project/.windsurf/skills/
```

**Kiro:**
```bash
cp -r bmad-crew/.kiro/skills/bmad-crew-* your-project/.kiro/skills/
```

**GitHub Copilot:**
```bash
cp -r bmad-crew/.github/skills/bmad-crew-* your-project/.github/skills/
```

**Kilo Code:**
```bash
cp -r bmad-crew/.kiro/skills/bmad-crew-* your-project/.kilocode/skills/
```

#### Step 3 — Register the module

Add to your project's `_bmad/_config/manifest.yaml`:

```yaml
- name: crew
  version: 0.2.0
  source: local
  npmPackage: null
  repoUrl: null
```

#### Step 4 — Register skills

Append the contents of `_bmad/crew/module-help.csv` to your project's `_bmad/_config/bmad-help.csv`.

Add to `_bmad/_config/skill-manifest.csv`:

```csv
"bmad-crew-agent-advisor","bmad-crew-agent-advisor","Vigilant BMAD session supervisor with memory.","crew","_bmad/crew/skills/bmad-crew-agent-advisor/SKILL.md","true"
"bmad-crew-advisor","bmad-crew-advisor","Interactive session advisor for BMAD workflow monitoring.","crew","_bmad/crew/skills/bmad-crew-advisor/SKILL.md","true"
"bmad-crew-session-validator","bmad-crew-session-validator","Validates BMAD session state for violations.","crew","_bmad/crew/skills/bmad-crew-session-validator/SKILL.md","true"
"bmad-crew-checkpoint-enforcer","bmad-crew-checkpoint-enforcer","Enforces BMAD checkpoints and completion requirements.","crew","_bmad/crew/skills/bmad-crew-checkpoint-enforcer/SKILL.md","true"
"bmad-crew-locked-decisions","bmad-crew-locked-decisions","Manages locked decisions and pushback rules.","crew","_bmad/crew/skills/bmad-crew-locked-decisions/SKILL.md","false"
```

#### Step 5 — Restart your IDE

Restart so it discovers the new skills, then activate:

```
/bmad-crew-agent-advisor
```

---

## Usage

Open a dedicated chat for the Advisor at the start of every BMAD session:

```
/bmad-crew-agent-advisor
```

The Advisor will:
1. Automatically scan for artifacts (sprint status, story files, locked decisions, project context)
2. Present what it found and confirm the current state
3. Run git validation
4. Give you the single correct next command

From that point, every instruction you give the Builder comes from the Advisor. You move context. The Advisor handles everything else.

### What the output looks like

```
Story 3.1 validated — no violations. Commit the file, then open a new chat and run:

/bmad-bmm-dev-story
```

No options. No numbered lists. One line of context, one command.

### Violation handling

When something is wrong:

```
VIOLATION: Process — Builder self-certified without commit

What happened: Builder said "done" but git log shows no new commit.
Rule: Never accept completion claims without commit hash verification.
Required action: Run git log --oneline -3 and paste the output here.
```

---

## Available Skills

| Command | Purpose |
|---------|---------|
| `/bmad-crew-agent-advisor` | Main Advisor with memory — **start here** |
| `/bmad-crew-advisor` | Advisor workflow (stateless) |
| `/bmad-crew-session-validator` | Validate session state on demand |
| `/bmad-crew-checkpoint-enforcer` | Enforce checkpoint compliance on demand |
| `/bmad-crew-locked-decisions` | Manage locked decisions document |

---

## Absolute Rules

The Advisor operates under five rules that cannot be overridden:

1. **Never confirm a document without reading it**
2. **Never accept git claims without log verification**
3. **Never cross the Coordinator/Builder boundary**
4. **Never present options when the correct next step is known**
5. **Yield only on scope confusion — never on process violations**

---

## Automated Scripts

The Advisor runs these scripts directly. The Coordinator never needs to run them manually.

| Script | Runs when |
|--------|-----------|
| `git-validator.py` | Session start, every checkpoint, after Builder completion claims |
| `session-validator.py` | Activation — discovers all project artifacts automatically |
| `mistakes-generator.py` | After each completed story cycle |
| `document-verifier.py` | After any BMAD command produces output |

Run the test suite to verify your installation:

```bash
bash _bmad/crew/skills/bmad-crew-agent-advisor/scripts/run-tests.sh
```

---

## Works With

- Windsurf
- Kiro
- GitHub Copilot
- Kilo Code
- Any IDE supported by BMAD v6

---

## Version History

**v0.2.0** — Full implementation. All 14 improvements from session experience. Auto-discovery, document verification, full lifecycle checkpoints, workflow knowledge, output format discipline, git automation, code review escalation, pushback rules, locked decisions re-reference, phase summaries, session-end detection, mistakes files, scope detection, self-doubt flag.

**v0.1.0** — MVP. Core Advisor agent with basic violation detection, checkpoint enforcement, and locked decisions management.

### Roadmap

- Executor module — automates Builder-side execution
- Coordinator module — handles Coordinator-side orchestration
- npm publishing for BMAD installer integration

---

## Built With

- [BMAD Method v6](https://docs.bmad-method.org) — built using `/bmad-agent-builder`

---

## License

MIT
