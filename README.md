# bmad-crew

A BMAD custom module that sits beside the Coordinator during development sessions, guiding every decision and instruction so the Coordinator never has to think about what to tell the Builder.

---

## The Problem

In a BMAD multi-agent session, the Coordinator (developer) directs the Builder (Executor) through every phase of development. This means the Coordinator must constantly:

- Know which BMAD command to run next
- Catch when the Builder self-certifies without committing
- Remember to verify git status before opening new sessions
- Decide which option to pick when the Builder presents choices
- Produce summary files at phase boundaries
- Track locked decisions so the Builder doesn't re-open them

This cognitive overhead accumulates. The Coordinator ends up spending more time managing the process than building the product.

---

## The Solution

```
Advisor → Coordinator (developer) ← Builder
```

bmad-crew adds an **Advisor** to the session. The Advisor sits beside the Coordinator and handles the process management layer:

- Tells the Coordinator exactly what to tell the Builder at each step
- Catches process violations before the Coordinator notices them
- Enforces checkpoints so the Coordinator never skips a gate
- Tracks locked decisions so nothing gets re-opened
- Verifies Builder claims independently before the Coordinator acts on them

The Coordinator's only job becomes moving context between agents. The Advisor handles the rest.

---

## Module Contents

```
_bmad/crew/
├── config.yaml
├── module-help.csv
└── skills/
    ├── bmad-crew-agent-advisor/         # Main Advisor agent (start here)
    ├── bmad-crew-advisor/               # Advisor workflow skill
    ├── bmad-crew-session-validator/     # Detects role, process, quality violations
    ├── bmad-crew-checkpoint-enforcer/   # Validates commits, summaries, code reviews
    └── bmad-crew-locked-decisions/      # Manages locked decisions document
```

---

## Installation

### Step 1 — Copy the module into your project

```
your-project/
└── _bmad/
    └── crew/        ← copy from bmad-crew/_bmad/crew/
```

### Step 2 — Copy skills to your IDE

**Windsurf:**
```
.windsurf/skills/bmad-crew-agent-advisor/
.windsurf/skills/bmad-crew-advisor/
.windsurf/skills/bmad-crew-session-validator/
.windsurf/skills/bmad-crew-checkpoint-enforcer/
.windsurf/skills/bmad-crew-locked-decisions/
```

**Kilo Code:**
```
.kilocode/skills/   ← same structure
```

### Step 3 — Register the module

Add to `_bmad/_config/manifest.yaml`:

```yaml
- name: crew
  version: 0.1.0
  source: local
  npmPackage: null
  repoUrl: null
```

Add skills to `_bmad/_config/bmad-help.csv` — see `_bmad/crew/module-help.csv` for the entries.

---

## Usage

At the start of any BMAD session, activate the Advisor in a separate chat:

```
/bmad-crew-agent-advisor
```

The Advisor will:
1. Load identity and memory
2. Greet the Coordinator by name
3. Ask for minimum context (sprint status or story file)
4. Begin guiding the Coordinator once context is loaded

From that point, every instruction the Coordinator gives to the Builder comes from the Advisor — not from the Coordinator having to figure it out themselves.

---

## Available Skills

| Command | Purpose |
|---------|---------|
| `/bmad-crew-agent-advisor` | Main Advisor — start here |
| `/bmad-crew-advisor` | Advisor workflow skill |
| `/bmad-crew-session-validator` | Validate session state |
| `/bmad-crew-checkpoint-enforcer` | Enforce checkpoint compliance |
| `/bmad-crew-locked-decisions` | Manage locked decisions |

---

## Core Rules

The Advisor operates under three absolute rules that cannot be overridden:

1. **NEVER confirm a document without reading it**
2. **NEVER accept Builder git claims without log verification**
3. **NEVER cross the Coordinator/Builder boundary**

---

## Works With

- Windsurf
- Kilo Code
- GitHub Copilot
- Any IDE supported by BMAD v6

---

## Version

**v0.1.0** — MVP. Covers the Advisor agent and supporting utility skills.

Post-MVP roadmap:
- Executor module
- Coordinator module
- Specialist module
- npm publishing for BMAD installer integration

---

## Built With

- [BMAD Method v6](https://docs.bmad-method.org) — BMad Builder (bmb) module
- Built using `/bmad-workflow-builder`, `/bmad-agent-builder`, `/bmad-module-builder`

---

## License

MIT
