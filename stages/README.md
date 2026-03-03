# Stages

The six lifecycle stages of the A-SDLC. Each stage directory contains the stage definition, process guide, and artifact templates.

## Stages

| Directory | Stage | Name | Controls |
| --------- | ----- | ---- | -------- |
| [01-intent-ingestion/](01-intent-ingestion/) | 1 | Intent Ingestion | QC-1A, QC-1B, RC-1A, SC-1A, AC-1A, GC-1A |
| [02-system-design/](02-system-design/) | 2 | System Design | QC-2A, RC-2A, SC-2A, SC-2B, AC-2A |
| [03-coding-implementation/](03-coding-implementation/) | 3 | Coding & Implementation | QC-3A, QC-3B, RC-3A, SC-3A, SC-3B, SC-3C, GC-3A |
| [04-testing-documentation/](04-testing-documentation/) | 4 | Testing & Documentation | QC-4A, QC-4B, QC-4C, RC-4A, SC-4A, SC-4B, AC-4A |
| [05-deployment-release/](05-deployment-release/) | 5 | Deployment & Release | QC-5A, RC-5A, RC-5B, SC-5A, SC-5B |
| [06-observability-maintenance/](06-observability-maintenance/) | 6 | Observability & Maintenance | QC-6A, RC-6A, SC-6A, SC-6B, AC-6A |

Cross-cutting controls (SC-0D, SC-2B, GC-0A, GC-0B, GC-0C) apply to every stage and are not listed per-stage above. See [../controls/README.md](../controls/README.md).

## Stage Directory Structure

Each stage directory follows the same layout:

```text
NN-stage-name/
├── NN-stage-name.yaml    ← Stage definition: required controls + exit criteria
├── README.md             ← Human overview: steps, controls table, artifacts
├── process.md            ← Detailed process: roles, step-by-step, decision points
└── artifacts/
    ├── inputs/           ← Input artifact templates (from previous stages)
    └── outputs/          ← Output artifact templates produced by this stage
```

## Stage Definition Files

`NN-stage-name.yaml` conforms to [../schema/stage.schema.json](../schema/stage.schema.json):

```yaml
number: 1
name: Intent Ingestion
description: ...
required_controls:
  - id: QC-1A
  - id: SC-1A
    note: ...
exit_criteria:
  - "QC-1A: ..."
next_stage: 2
process: process.md
artifacts:
  inputs:  [...]
  outputs: [...]
```

This file is the authoritative gate definition. Only the controls listed here are enforced at this stage. Full control definitions live in `../controls/[track]/[ID].yaml`.

## Roles

[roles.yaml](roles.yaml) — canonical role definitions referenced by all `process.md` files:

| Code | Role | Scope |
| ---- | ---- | ----- |
| REQ | Requester | Submits change requests |
| AGT | Agent | Automated AI agent |
| PO | Product Owner | Business decision authority |
| RO | Risk Officer | Risk classification and approval |
| SA | Security Architect | Security escalations and directive authorship |
| AGL | AI Governance Lead | EU AI Act compliance (AC-track) |
| LAD | Lead Architect | Architectural decisions and design approval |
| QA | QA Lead | Test oversight and Stage 4 findings |
| OPS | Operations / SRE | Stage 6 monitoring and Stage 3 re-entry |
| CO | Compliance Officer | Audit records and regulatory reporting |

## Feedback Loops

When Stage 4 or Stage 6 detects an issue requiring a code change, re-entry is governed by [../feedbackloops/](../feedbackloops/):

- **Path A** — easy, obvious, low-risk → re-enter at Stage 3 (minimum controls)
- **Path B** — otherwise → re-enter at Stage 1 (full lifecycle)
