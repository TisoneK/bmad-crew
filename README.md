# bmad-crew

A BMAD custom module that reduces Coordinator cognitive load during multi-agent development sessions. The Advisor agent monitors for violations, enforces checkpoints, and provides exact instructions so you never have to think about what to tell an agent.

---

## The Problem

When running multi-agent BMAD sessions, the Coordinator spends significant effort:

- Correcting agents that step outside their role
- Catching self-certified completions that were never committed
- Remembering to produce summary files at phase boundaries
- Deciding what to tell the Executor when it presents options
- Verifying git claims before opening new sessions

bmad-crew handles all of this automatically.

---

## How It Works

The **BMAD Crew Advisor** is a session supervisor that loads alongside your development session. It:

1. Asks for context before starting (sprint status, story file, architecture doc)
2. Monitors for role, process, and quality violations in real time
3. Enforces checkpoints before phase transitions
4. Provides exact copy-pasteable instructions to the Coordinator
5. Maintains locked decisions across sessions via persistent memory

The Coordinator's only job becomes moving context between agents. The Advisor handles the rest.

---

## Module Contents

```
_bmad/crew/
├── config.yaml                          # Module configuration
├── module-help.csv                      # Skill registry
└── skills/
    ├── bmad-crew-agent-advisor/         # Main Advisor agent (start here)
    ├── bmad-crew-advisor/               # Advisor workflow skill
    ├── bmad-crew-session-validator/     # Detects role, process, quality violations
    ├── bmad-crew-checkpoint-enforcer/   # Validates commits, summaries, code reviews
    └── bmad-crew-locked-decisions/      # Manages locked decisions document
```

---

## Installation

### Option 1: Clone into your project

Copy the `_bmad/crew/` folder into your project's `_bmad/` directory:

```
_your-project/
└── _bmad/
    └── crew/        ← copy this from bmad-crew
```

Then copy the skills to your IDE's skill directory:

**Windsurf:**
```
.windsurf/skills/bmad-crew-advisor/
.windsurf/skills/bmad-crew-agent-advisor/
.windsurf/skills/bmad-crew-session-validator/
.windsurf/skills/bmad-crew-checkpoint-enforcer/
.windsurf/skills/bmad-crew-locked-decisions/
```

**Kilo Code:**
```
.kilocode/skills/   ← same structure
```

### Option 2: Register in manifest

Add to your project's `_bmad/_config/manifest.yaml`:

```yaml
- name: crew
  version: 0.1.0
  source: local
  npmPackage: null
  repoUrl: null
```

Add to `_bmad/_config/bmad-help.csv` — see `_bmad/crew/module-help.csv` for the entries.

---

## Usage

Activate the Advisor at the start of any BMAD session:

```
/bmad-crew-agent-advisor
```

The Advisor will:
1. Load identity and memory
2. Greet you by name
3. Ask for minimum context (sprint status or story file)
4. Begin monitoring once context is loaded

### Available Skills

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
2. **NEVER accept git claims without log verification**
3. **NEVER cross the Coordinator/Executor boundary**

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
