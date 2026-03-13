<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/02-system-design/02-system-design.yaml + controls/ + directives/
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 2: System Design — Context Bundle

> **Agent load file** — load this at Stage 2 entry for full context.

**Stage:** 02-System Design
**Purpose:** Translate the approved specification into a complete, approved system design. Security directives are injected before coding begins. No implementation may start without RC-02 (design approval) and SC-02 directive injection confirmation.

## Files to Load at Stage Entry

- `stages/02-system-design/02-system-design.yaml` — stage definition and workflow DAG
- `controls/qc/QC-03.yaml` — control definition
- `controls/rc/RC-02.yaml` — control definition *(Human-required gate — cannot be delegated to an agent)*
- `controls/rc/RC-03.yaml` — control definition *(Applicable when the change involves personal data, profiling, or high-risk AI systems)*
- `controls/sc/SC-05.yaml` — control definition
- `controls/sc/SC-06.yaml` — control definition *(Validate zero-trust architecture principles in design)*
- `controls/sc/SC-02.yaml` — control definition *(Directive injection must be confirmed before Stage 3 begins)*
- `controls/ac/AC-03.yaml` — control definition *(Applicable when the change involves an AI component)*
- `controls/ac/AC-04.yaml` — control definition *(Applicable when the change involves AI models — register in model registry)*
- `directives/stages/02-system-design.yaml` — stage directive payload
- `directives/stages/03-coding-implementation.yaml` — stage directive payload

## Workflow Execution Order

| Step | Title | Control | Delegation |
|------|-------|---------|------------|
| 2.1 | Draft System Design | `QC-03` | Agent drafts |
| 2.2 | Design Validation | `QC-03` | Agent validates, LAD approves |
| 2.3 | STRIDE Threat Modelling | `SC-05` | Agent generates, SA validates |
| 2.4 | AI Component Design Review *(conditional)* | `AC-03` | Agent assists, AGL approves |
| 2.3b | Privacy Impact Assessment *(conditional)* | `RC-03` | Agent generates, LAD reviews |
| 2.3c | Zero-Trust Architecture Validation | `SC-06` | Fully automated |
| 2.5 | Design Approval | `RC-02` | Human required |
| 2.6 | AI Model Governance and Version Control *(conditional)* | `AC-04` | Agent registers, AGL approves |
| 2.7 | Stage Directive Injection | `SC-02` | Fully automated |

## Required Controls

| Control | Name | Notes |
|---------|------|-------|
| [`QC-03`](../controls/qc/QC-03.yaml) | Design Completeness & Standards |  |
| [`RC-02`](../controls/rc/RC-02.yaml) | Design Approval | Human-required gate — cannot be delegated to an agent |
| [`RC-03`](../controls/rc/RC-03.yaml) | Privacy Impact Assessment Gate | Applicable when the change involves personal data, profiling, or high-risk AI systems |
| [`SC-05`](../controls/sc/SC-05.yaml) | Threat Model Validation |  |
| [`SC-06`](../controls/sc/SC-06.yaml) | Zero-Trust Architecture Validation | Validate zero-trust architecture principles in design |
| [`SC-02`](../controls/sc/SC-02.yaml) | Stage Directive Injection | Directive injection must be confirmed before Stage 3 begins |
| [`AC-03`](../controls/ac/AC-03.yaml) | AI Component Design Review | Applicable when the change involves an AI component |
| [`AC-04`](../controls/ac/AC-04.yaml) | AI Model Governance & Version Control | Applicable when the change involves AI models — register in model registry |

## Exit Criteria Checklist

- [ ] QC-03: Design validated and approved by Lead Architect
- [ ] RC-02: Design approval granted and logged
- [ ] RC-03: Privacy Impact Assessment completed (if applicable)
- [ ] SC-05: STRIDE threat model validated and all critical threats mitigated
- [ ] SC-06: Zero-trust architecture principles validated
- [ ] SC-02: Stage 2 and Stage 3 directive bundles injected and acknowledged by agent
- [ ] AC-03: AI component design review approved (or not-applicable documented)
- [ ] AC-04: AI model registry entry created with version pinning (if applicable)

## Input Artifacts

- `../01-intent-ingestion/artifacts/outputs/QC-01-feature-spec.yaml`
- `../01-intent-ingestion/artifacts/outputs/RC-01-risk-classification.yaml`

## Output Artifacts

- `artifacts/outputs/QC-03-design-document.yaml`
- `artifacts/outputs/SC-05-stride-threat-model.yaml`
- `artifacts/outputs/RC-02-design-approval-decision.yaml`
- `artifacts/outputs/SC-02-directive-injection-confirmation.yaml`
- `artifacts/outputs/AC-03-ai-component-design-review.yaml`
- `artifacts/outputs/RC-03-privacy-impact-assessment.yaml`
- `artifacts/outputs/SC-06-zero-trust-validation.yaml`
- `artifacts/outputs/AC-04-ai-model-governance-record.yaml`

## Directives Injected at Stage Entry

- `directives/stages/02-system-design.yaml`
- `directives/stages/03-coding-implementation.yaml`


## Feedback Loop Triggers

*This stage is not a direct feedback loop trigger source.*

---

**Last Updated:** 2026-03-13 12:43 UTC
