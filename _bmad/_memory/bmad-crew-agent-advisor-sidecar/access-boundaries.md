# Access Boundaries for BMAD Crew Advisor

## Read Access
- {project-root}/_bmad/bmad-crew/
- {bmad_builder_output_folder}/bmad-crew-sessions/
- User-provided context documents

## Write Access
- {project-root}/_bmad/_memory/bmad-crew-agent-advisor-sidecar/
- {bmad_builder_output_folder}/bmad-crew-sessions/
- {project-root}/_bmad/bmad-crew/locked-decisions.md

## Deny Zones
- Direct code execution
- Git operations (validation only)
- Coordinator/Executor boundary crossing
