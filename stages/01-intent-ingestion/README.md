# Stage 1: Intent Ingestion

The Intent Ingestion phase is the entry point between human ambition and machine execution. High-level business goals or "intents" are captured, disambiguated, and transformed into structured technical requirements.

During this stage, humans or agents interact with stakeholders to clarify nuances, analyse existing system constraints, and map dependencies — ensuring the initial idea is translated into a comprehensive, machine-readable specification. By automating the discovery of edge cases and identifying potential architectural conflicts at the point of entry, this phase establishes the **source of truth** that ensures all subsequent agentic actions are aligned with the user's original objective.

## Steps

Full step-by-step process with roles and decision points: [process.md](process.md)

| Step | Name | Delegation | Sequencing |
| ---- | ---- | ---------- | ---------- |
| [1.1](process.md#step-11--screen-incoming-request) | Screen Request | Fully automated | Runs first — blocks all other steps if flagged |
| [1.2](process.md#step-12--draft-feature-specification) | Draft Feature Specification | Agent drafts | After 1.1 |
| [1.3](process.md#step-13--conflict-analysis) | Conflict Analysis | Agent analyses, PO resolves | Parallel with 1.4 and 1.5 |
| [1.4](process.md#step-14--risk-classification) | Risk Classification | Agent classifies, RO validates | Parallel with 1.3 and 1.5 |
| [1.5](process.md#step-15--ai-tier-classification-conditional) | AI Tier Classification *(conditional)* | Agent proposes, AGL confirms | Parallel with 1.3 and 1.4 |
| [1.6](process.md#step-16--product-owner-sign-off) | Product Owner Sign-off | Human required | After 1.3, 1.4, and 1.5 |
| [1.7](process.md#step-17--traceability-log) | Traceability Log | Fully automated | After 1.6 |

## Controls

Stage definition (required controls + exit criteria): [01-intent-ingestion.yaml](01-intent-ingestion.yaml)

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| [SC-1A](../../controls/sc/SC-1A.yaml) | Pre-Guardrails | Screens incoming requests for prompt injection attacks that could manipulate agent interpretation. | Fully automated | DORA: Art. 9(2); AI Act: Art. 15(4) |
| [QC-1A](../../controls/qc/QC-1A.yaml) | Specification Validation | Confirms the request has been correctly captured with complete acceptance criteria and NFRs. | Agent drafts, human approves | DORA: Art. 8 |
| [QC-1B](../../controls/qc/QC-1B.yaml) | Coherence & Conflict Resolution | Detects contradictions between requirements. Forces stakeholders to resolve trade-offs before design. | Agent analyses, human resolves | DORA: Art. 8; AI Act: Art. 9 |
| [RC-1A](../../controls/rc/RC-1A.yaml) | Risk Classification | Classifies non-functional risk exposure and determines governance intensity for the entire change. | Agent classifies, human validates | DORA: Art. 8(1); AI Act: Art. 9(2) |
| [AC-1A](../../controls/ac/AC-1A.yaml) | AI Risk Tier Classification | For AI changes: classifies EU AI Act risk tier and triggers corresponding compliance requirements. | Agent proposes, human confirms | AI Act: Art. 6, Annex III |
| [GC-1A](../../controls/gc/GC-1A.yaml) | Intent Traceability | Logs original request, all agent transformations, and validated output. First link in the audit chain. | Fully automated | DORA: Art. 8(6); AI Act: Art. 12 |

## Stage Exit Criteria

All of the following must be true before progressing to Stage 2:

- [ ] QC-1A passed: specification has complete acceptance criteria and NFRs
- [ ] QC-1B passed: all blocking conflicts resolved by stakeholders
- [ ] RC-1A completed: risk classification risk tier assigned and validated
- [ ] SC-1A passed: no prompt injection detected in the incoming request
- [ ] AC-1A completed (if AI component): EU AI Act risk tier classified and confirmed
- [ ] GC-1A confirmed: intent traceability record created

## Artifacts

- **Process:** [process.md](process.md) — Step-by-step guide with roles, dependencies, and decision points

**Inputs:**
- [artifacts/inputs/change-request.yaml](artifacts/inputs/change-request.yaml) — Change request template (CR-XXXX)

**Outputs:**
- [artifacts/outputs/feature-spec.yaml](artifacts/outputs/feature-spec.yaml) — Feature specification (FEAT-XXXX)
- [artifacts/outputs/conflict-resolution-record.yaml](artifacts/outputs/conflict-resolution-record.yaml) — QC-1B output
- [artifacts/outputs/risk-classification.yaml](artifacts/outputs/risk-classification.yaml) — RC-1A output
- [artifacts/outputs/ai-tier-classification.yaml](artifacts/outputs/ai-tier-classification.yaml) — AC-1A output (if AI component)
- [artifacts/outputs/intent-audit-record.yaml](artifacts/outputs/intent-audit-record.yaml) — GC-1A output
