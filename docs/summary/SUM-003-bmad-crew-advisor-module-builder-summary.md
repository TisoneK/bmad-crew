# SUM-003-bmad-crew-advisor-module-builder-summary.md
**Phase:** Module Build (Workflow Builder + Agent Builder + Module Builder)
**Date:** 2026-03-21
**Project:** bmad-crew

---

## Corrections Issued During This Phase

1. Workflow builder proposed headless mode — rejected, interactive only
2. Agent builder proposed violation-scanner.py and memory-validator.py scripts — rejected, violation detection requires LLM judgment not pattern matching
3. Module builder draft hardcoded author name — corrected to use {user_name} variable
4. identity.md was initially 49 lines with descriptive sections — corrected to 4 lines NEVER-only language with three absolute rules
5. workflow-gates.md had bypass conditions — removed entirely, gates are absolute
6. Script references used python3 — corrected to python for Windows compatibility
7. Executor self-reported fixes without sharing updated files — required zip verification each time

---

## Locked Decisions Carrying Forward

- Module code: crew, installed to _bmad/crew/
- 5 separate skills preserved — no consolidation
- Identity file: NEVER-only language, three absolute rules, loaded first structurally via SKILL.md
- Gates: absolute, no bypass, no exceptions
- Scripts: python (not python3) for Windows
- Memory sidecar: _bmad/_memory/bmad-crew-agent-advisor-sidecar/
- Locked decisions: _bmad/bmad-crew/locked-decisions.md
- Session reports: {bmad_builder_output_folder}/bmad-crew-sessions/
- Version: 0.1.0 MVP

---

## Items to Watch in Next Phase

- Module has not been tested in a live session yet — this is the critical next step
- _bmad-output/skills/ contains duplicate copies of skills — these are build artifacts, not the installed module. The live module is in _bmad/crew/
- The crew module is not yet registered in _bmad/_config/ manifests — may need manual registration for IDE integration
- Python scripts use #!/usr/bin/env python3 shebangs — harmless on Windows but worth noting for cross-platform users

---

## Open Questions Deferred

- Does the crew module need to be registered in _bmad/_config/manifest.yaml to appear in IDE skill lists?
- How does the BMAD installer handle custom local modules vs npm-published modules?
- Testing protocol: what is the minimum viable live session test for the Advisor?
