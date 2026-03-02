# Stage 1: Intent Ingestion

The Intent Ingestion phase is the entry point between human ambition and machine execution. High-level business goals or "intents" are captured, disambiguated, and transformed into structured technical requirements.

During this stage, humans or agents interact with stakeholders to clarify nuances, analyse existing system constraints, and map dependencies — ensuring the initial idea is translated into a comprehensive, machine-readable specification. By automating the discovery of edge cases and identifying potential architectural conflicts at the point of entry, this phase establishes the **source of truth** that ensures all subsequent agentic actions are aligned with the user's original objective.

## Key Tasks

- Receive and parse the incoming change request into structured format
- Validate completeness: every requirement has acceptance criteria and non-functional attributes
- Cross-reference all requirements to detect conflicts, contradictions, and competing priorities
- Present conflict map to stakeholders with severity ratings and resolution options
- Obtain stakeholder decisions on all blocking and significant conflicts
- Classify non-functional risk exposure using the NF-RED methodology
- If AI components are involved: classify the EU AI Act risk tier
- Log all inputs, transformations, decisions, and outputs for traceability

## Controls

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| QC-1A | Specification Validation | Confirms the request has been correctly captured with complete acceptance criteria and NFRs. | Agent drafts, human approves | DORA: Art. 8; DNB: IT change management |
| QC-1B | Coherence & Conflict Resolution | Detects contradictions between requirements. Forces stakeholders to resolve trade-offs before design. | Agent analyses, human resolves | DORA: Art. 8; DNB: Risk assessment; AI Act: Art. 9 |
| RC-1A | Risk Classification (NF-RED) | Classifies non-functional risk exposure and determines governance intensity for the entire change. | Agent classifies, human validates | DORA: Art. 8(1); DNB: Risk-based governance; AI Act: Art. 9(2) |
| SC-1A | Pre-Guardrails | Screens incoming requests for prompt injection attacks that could manipulate agent interpretation. | Fully automated | DORA: Art. 9(2); DNB: Integrity of IT processing; AI Act: Art. 15(4) |
| AC-1A | AI Risk Tier Classification | For AI changes: classifies EU AI Act risk tier and triggers corresponding compliance requirements. | Agent proposes, human confirms | AI Act: Art. 6, Annex III |
| GC-1A | Intent Traceability | Logs original request, all agent transformations, and validated output. First link in the audit chain. | Fully automated | DORA: Art. 8(6); DNB: Auditability; AI Act: Art. 12 |

Full control definitions: [controls.yaml](controls.yaml)

## Stage Exit Criteria

All of the following must be true before progressing to Stage 2:

- [ ] QC-1A passed: specification has complete acceptance criteria and NFRs
- [ ] QC-1B passed: all blocking conflicts resolved by stakeholders
- [ ] RC-1A completed: NF-RED risk tier assigned and validated
- [ ] SC-1A passed: no prompt injection detected in the incoming request
- [ ] AC-1A completed (if AI component): EU AI Act risk tier classified and confirmed
- [ ] GC-1A confirmed: intent traceability record created

## Templates

- [templates/feature-spec.yaml](templates/feature-spec.yaml) — Feature/change specification template (FEAT-XXXX)
