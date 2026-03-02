# Stage 2: System Design

Validated intent is translated into architecture, system design, and technical specifications. Agents may assist in generating design proposals, but **human architects retain final approval authority**.

Threat modelling, design completeness validation, and the injection of Core Security Directives into agent contexts all occur at this stage. No agent may begin coding (Stage 3) without first receiving the signed SC-2B directive payload.

## Steps

Full step-by-step process with roles and decision points: [process.md](process.md)

| Step | Name | Delegation | Sequencing |
| ---- | ---- | ---------- | ---------- |
| [2.1](process.md#step-21--draft-system-design) | Draft System Design | Agent drafts | After Stage 1 completion |
| [2.2](process.md#step-22--design-validation) | Design Validation | Agent validates, LAD approves | Parallel with 2.3 and 2.4 |
| [2.3](process.md#step-23--stride-threat-modelling) | STRIDE Threat Modelling | Agent generates, SA validates | Parallel with 2.2 and 2.4 |
| [2.4](process.md#step-24--ai-component-design-review-conditional) | AI Component Design Review *(conditional)* | Agent assists, AGL approves | Parallel with 2.2 and 2.3 |
| [2.5](process.md#step-25--design-approval) | Design Approval | Human required | After 2.2, 2.3, and 2.4 |
| [2.6](process.md#step-26--directive-injection) | Directive Injection | Fully automated | After 2.5 |

## Controls

Stage definition (required controls + exit criteria): [02-system-design.yaml](02-system-design.yaml)

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| [QC-2A](../../controls/qc/QC-2A.yaml) | Design Completeness & Standards | Validates design addresses all requirements, follows architectural patterns, and meets standards. | Agent validates, LAD approves | DORA: Art. 8(4); DNB: Architecture review |
| [SC-2A](../../controls/sc/SC-2A.yaml) | Threat Model Validation | STRIDE-based analysis verifying design does not introduce insecure patterns. | Agent generates, SA validates | DORA: Art. 8(3); DNB: Threat analysis; AI Act: Art. 15(3) |
| [AC-2A](../../controls/ac/AC-2A.yaml) | AI Component Design Review | For AI systems: validates model selection, data pipelines, explainability, and human oversight mechanisms. | Agent assists, AGL approves | AI Act: Art. 11, Annex IV; Art. 13; Art. 14 |
| [RC-2A](../../controls/rc/RC-2A.yaml) | Design Approval | Consolidated governance gate: design approval with functional risk classification. Sign-off authority determined by risk tier. | Human required | DORA: Art. 8(1); DNB: Approval authority; AI Act: Art. 9 |
| [SC-2B](../../controls/sc/SC-2B.yaml) | Directive Injection | Injects signed, immutable Core Security Directives into the agent before coding. Cannot be overridden by any instruction. | Fully automated (signed) | DORA: Art. 9(4)(c); DNB: Logical access management; AI Act: Art. 14(1) |

## Stage Exit Criteria

All of the following must be true before progressing to Stage 3:

- [ ] QC-2A passed: design addresses all requirements and meets organisational standards
- [ ] SC-2A passed: STRIDE threat model reviewed and all critical threats mitigated
- [ ] AC-2A passed (if AI component): model selection, data governance, and explainability documented and approved
- [ ] RC-2A passed: design approved by appropriate authority per risk classification
- [ ] SC-2B executed: Core Security Directives signed and injected into agent context

## Artifacts

- **Process:** [process.md](process.md) — Step-by-step guide with roles, dependencies, and decision points
- **Directives:** [directives/core-security-directives.xml](directives/core-security-directives.xml) — SC-2B injection payload (immutable)

**Input (from Stage 1):**

- [feature-spec.yaml](../01-intent-ingestion/artifacts/outputs/feature-spec.yaml) — Approved feature specification (FEAT-XXXX)

**Outputs:**

- [artifacts/outputs/design-document.yaml](artifacts/outputs/design-document.yaml) — QC-2A output
- [artifacts/outputs/stride-threat-model.yaml](artifacts/outputs/stride-threat-model.yaml) — SC-2A output
- [artifacts/outputs/design-approval-decision.yaml](artifacts/outputs/design-approval-decision.yaml) — RC-2A output
- [artifacts/outputs/directive-injection-confirmation.yaml](artifacts/outputs/directive-injection-confirmation.yaml) — SC-2B output
- [artifacts/outputs/ai-component-design-review.yaml](artifacts/outputs/ai-component-design-review.yaml) — AC-2A output (if AI component)
