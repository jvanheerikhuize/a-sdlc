# Stage 2 — System Design

> **Auto-generated from `stages/02-system-design/02-system-design.yaml`** · Agent context bundle · All controls and workflow in one file

Translate the approved specification into a complete, approved system design. Security directives are injected before coding begins. No implementation may start without RC-2A (design approval) and SC-2B directive injection confirmation.

---

## Quick Load

Load these files for this stage:

```
- stages/02-system-design/02-system-design.yaml
- directives/stages/02-system-design.yaml
```

---

## Workflow — Execution Order

| Step | Title | Control | Actors | Delegation | Depends On |
| ---- | ----- | ------- | ------ | ---------- | ---------- |
| 2.1 | Draft System Design | QC-2A | AGT, AGT, AGT, AGT | Agent drafts | — |
| 2.2 | Design Validation | QC-2A | LAD, LAD, LAD | Agent validates, LAD approves | n-qc2a-draft |
| 2.3 | STRIDE Threat Modelling | SC-2A | AGT, AGT, SA, SA | Agent generates, SA validates | n-qc2a-draft |
| 2.4 | AI Component Design Review | AC-2A | AGT, AGT, AGL | Agent assists, AGL approves | n-qc2a-draft |
| 2.3b | Privacy Impact Assessment | RC-2B | AGT, AGT, LAD | Agent generates, LAD reviews | n-qc2a-draft |
| 2.3c | Zero-Trust Architecture Validation | SC-2C | AGT, AGT, SA | Fully automated | n-qc2a-draft |
| 2.5 | Design Approval | RC-2A | AGT, RO, RO, RO | Human required | n-qc2a-validate, n-sc2a, n-ac2a, n-rc2b, n-sc2c |
| 2.6 | AI Model Governance and Version Control | AC-2B | AGT, AGT, AGL | Agent registers, AGL approves | n-rc2a |
| 2.7 | Stage Directive Injection | SC-2B | AGT, AGT | Fully automated | n-rc2a, n-ac2b |

---

## Controls — What Agent and Human Do

| ID | Name | Delegation | Agent Does | Human Does |
| -- | ---- | ---------- | ---------- | ---------- |
| QC-2A | Design Completeness & Standards | agent_drafts_human_approves | Validate design coverage against specification; flag gaps, pattern deviations, and standards violations. | Review validation report; approve design or request revisions before sign-off. |
| RC-2A | Design Approval | human_required | Prepare design approval package with functional risk classification, risk summary, and supporting evidence. | Make the formal approval decision. This control cannot be delegated to an agent under any circumstances. |
| RC-2B | Privacy Impact Assessment Gate | agent_analyses_human_resolves | Review the design for personal data processing. Identify data types, processing activities, and potential privacy risks. Recommend mitigation measures: data minimisation, purpose limitation, consent mechanisms, encryption, access controls, retention limits. Draft a PIA/DPIA summary. | Review the agent analysis. Engage DPO for high-risk processing (biometric data, sensitive categories, large-scale profiling). Determine: is the processing compliant with GDPR, DORA, and AI Act? What additional controls are needed? Approve or request design changes to address privacy risks. |
| SC-2A | Threat Model Validation | agent_drafts_human_approves | Generate STRIDE threat model across all trust boundaries; propose mitigations for each identified threat. | Validate threat model completeness; approve mitigations or require design changes. |
| SC-2C | Zero-Trust Architecture Validation | agent_analyses_human_resolves | Review the architecture design (diagrams, component specifications, authentication flows). Analyse for zero-trust compliance: Are all service-to-service connections using mTLS or equivalent? Is there explicit deny-by-default network policy? Are lateral movement controls documented? Identify gaps and propose design changes. | Review agent analysis. For any identified gap, decide: redesign to implement zero-trust (preferred), accept the architectural risk and document exception, or adjust the design scope. Sign off on final architecture against zero-trust criteria. |
| SC-2B | Stage Directive Injection | automated_policy_enforced | At each stage entry, receive and acknowledge the signed stage directive payload for that stage. Log acknowledgement with stage number, timestamp, and agent identifier before performing any stage work. | Security Architect authors, signs, and publishes each stage directive payload. Reviews directive violation logs periodically. Triggers re-injection after any directive update. |
| AC-2A | AI Component Design Review | agent_drafts_human_approves | Validate AI component design against AI Act requirements; identify gaps in explainability, data governance, or human oversight provisions. | Review AI design validation; approve or require revisions before implementation proceeds. |
| AC-2B | AI Model Governance & Version Control | agent_creates_human_reviews | Create model registry entry for each AI model. Populate: model ID, version, provider, training data description, performance metrics, bias test results, known limitations. For model updates: propose new version with change rationale. Track model dependency in deployment configuration. | Review model registry entry. Validate training data provenance and licensing. Approve model version for use. For model updates: approve change or request rollback. Monitor for performance degradation. |
---

## Exit Criteria (Stage 2 Complete When)

- [ ] QC-2A: Design validated and approved by Lead Architect
- [ ] RC-2A: Design approval granted and logged
- [ ] RC-2B: Privacy Impact Assessment completed (if applicable)
- [ ] SC-2A: STRIDE threat model validated and all critical threats mitigated
- [ ] SC-2C: Zero-trust architecture principles validated
- [ ] SC-2B: Stage 2 and Stage 3 directive bundles injected and acknowledged by agent
- [ ] AC-2A: AI component design review approved (or not-applicable documented)
- [ ] AC-2B: AI model registry entry created with version pinning (if applicable)

---

## Artifact I/O

**Inputs from Prior Stage:**
- ../01-intent-ingestion/artifacts/outputs/QC-1A-feature-spec.yaml
- ../01-intent-ingestion/artifacts/outputs/RC-1A-risk-classification.yaml

**Outputs to Next Stage:**
- artifacts/outputs/QC-2A-design-document.yaml
- artifacts/outputs/SC-2A-stride-threat-model.yaml
- artifacts/outputs/RC-2A-design-approval-decision.yaml
- artifacts/outputs/SC-2B-directive-injection-confirmation.yaml
- artifacts/outputs/AC-2A-ai-component-design-review.yaml
- artifacts/outputs/RC-2B-privacy-impact-assessment.yaml
- artifacts/outputs/SC-2C-zero-trust-validation.yaml
- artifacts/outputs/AC-2B-ai-model-governance-record.yaml

---

## Feedback Loop Triggers

Controls in this stage that can trigger re-entry:

None

For full feedback loop definitions, see [`feedbackloops/feedback-loops.yaml`](../../feedbackloops/feedback-loops.yaml).

---

**Last Updated:** 2026-03-05 22:51 UTC