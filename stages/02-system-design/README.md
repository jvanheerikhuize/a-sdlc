# Stage 2: System Design

Validated intent is translated into architecture, system design, and technical specifications. Agents may assist in generating design proposals, but **human architects retain final approval authority**.

Threat modelling, design completeness validation, and the injection of Core Security Directives into agent contexts all occur at this stage. No agent may begin coding (Stage 3) without first receiving the signed SC-2B directive payload.

## Key Tasks

- Translate validated specification into architecture: components, integrations, data flows
- Map every requirement to a specific architectural component
- Validate design against organisational patterns and technology standards
- Assess functional risk: what can go wrong, blast radius, affected systems
- Obtain design approval from appropriate authority based on risk classification
- Perform STRIDE threat analysis across all trust boundaries
- Prepare and sign the Core Security Directives payload for agent injection
- For AI components: document model selection, data governance, and explainability approach

## Controls

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| QC-2A | Design Completeness & Standards | Validates design addresses all requirements, follows architectural patterns, and meets standards. | Agent assists, human approves | DORA: Art. 8(4); DNB: Architecture review |
| RC-2A | Design Approval | Consolidated governance gate: design approval with functional risk classification. Determines sign-off authority. | Human required | DORA: Art. 8(1); DNB: Approval authority; AI Act: Art. 9 |
| SC-2A | Threat Model Validation | STRIDE-based analysis verifying design doesn't introduce insecure patterns. | Agent generates, human validates | DORA: Art. 8(3); DNB: Threat analysis; AI Act: Art. 15(3) |
| SC-2B | Directive Injection | Injects signed, immutable Core Security Directives into the agent before coding. Company policy cannot be overridden. | Fully automated (signed) | DORA: Art. 9(4)(c); DNB: Logical access management; AI Act: Art. 14(1) |
| AC-2A | AI Component Design Review | For AI systems: validates model selection, data pipelines, explainability, and human oversight mechanisms. | Agent assists, human approves | AI Act: Art. 11, Annex IV; Art. 13; Art. 14 |

Stage definition (required controls + exit criteria): [stage.yaml](stage.yaml)

Individual control definitions by track:
  - [AC-2A](../../controls/ac/AC-2A.yaml)
  - [QC-2A](../../controls/qc/QC-2A.yaml)
  - [RC-2A](../../controls/rc/RC-2A.yaml)
  - [SC-2A](../../controls/sc/SC-2A.yaml), [SC-2B](../../controls/sc/SC-2B.yaml)

## Stage Exit Criteria

All of the following must be true before progressing to Stage 3:

- [ ] QC-2A passed: design addresses all requirements and meets organisational standards
- [ ] RC-2A passed: design approved by appropriate authority per risk classification
- [ ] SC-2A passed: STRIDE threat model reviewed and accepted
- [ ] SC-2B executed: Core Security Directives signed and injected into agent context
- [ ] AC-2A passed (if AI component): model selection, data governance, and explainability documented and approved

## Key Artefacts

- [directives/core-security-directives.xml](directives/core-security-directives.xml) — SC-2B injection payload template
