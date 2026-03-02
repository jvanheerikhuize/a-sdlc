# Cross-Cutting Controls

Three governance controls span all six stages of the A-SDLC lifecycle. They are always active regardless of which stage is being executed. Together they provide the audit and compliance trails required for regulatory examination under DORA, DNB, and the EU AI Act.

## Controls

| ID | Name | What It Does | Who Decides |
| -- | ---- | ------------ | ----------- |
| GC-0A | Audit Trail & Compliance Reporting | Every control execution logged: timestamp, actor, outcome, evidence. Examination artefacts on demand. | Fully automated |
| GC-0B | End-to-End Traceability | Bidirectional traceability from intent through deployment and monitoring. Supports impact analysis. | Fully automated |
| GC-0C | Agent Provenance Registry | Centralised registry of all agent contributions: what they produced, decisions made, humans who approved. | Fully automated |

Full control definitions: [controls.yaml](controls.yaml)

## Feedback Loops

When Stage 6 detects an issue requiring a code change, the work re-enters the lifecycle via one of two defined paths. See [feedback-loops.yaml](feedback-loops.yaml) for the full definitions.

| Path | Trigger | Re-Entry Point | Description |
| ---- | ------- | -------------- | ----------- |
| Path A | Incident → Autofix | Stage 3 | Low-risk, pre-approved patterns only. Upgrades to Path B if issue doesn't match template exactly. |
| Path B | Bug/Change | Stage 3 or Stage 1 | Quickfixes re-enter Stage 3 with full controls + RC-5A. Feature changes re-enter Stage 1. |
