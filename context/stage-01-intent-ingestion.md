<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/01-intent-ingestion/stage.yaml + controls/ + directives/
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 1: Intent Ingestion — Context Bundle

> **Agent load file** — load this at Stage 1 entry for full context.

**Stage:** 01-Intent Ingestion
**Purpose:** Capture, validate, and enrich an incoming change request into a structured, approved feature specification. All downstream stages depend on this specification as their source of truth. No design work begins until Stage 1 is complete.

## Files to Load at Stage Entry

- `stages/01-intent-ingestion/stage.yaml` — stage definition (steps in: `stages/01-intent-ingestion/steps/`)
- `controls/sc/SC-03.yaml` — control definition *(Must run first — screens for adversarial inputs before any agent processing)*
- `controls/sc/SC-04.yaml` — control definition *(Applicable when the change processes personal data or involves profiling)*
- `controls/qc/QC-01.yaml` — control definition
- `controls/qc/QC-02.yaml` — control definition
- `controls/rc/RC-01.yaml` — control definition
- `controls/ac/AC-01.yaml` — control definition *(Applicable when the change involves an AI component)*
- `controls/ac/AC-02.yaml` — control definition *(Applicable when the change introduces or modifies use of a GPAI/foundation model)*
- `controls/gc/GC-05.yaml` — control definition

## Workflow Execution Order

| Step | Title | Control | Delegation |
|------|-------|---------|------------|
| 1.1 | Screen Incoming Request | `SC-03` | Fully automated |
| 1.2 | Draft Feature Specification | `QC-01` | Agent drafts → human approves |
| 1.3 | Conflict Analysis | `QC-02` | Agent analyses, human resolves |
| 1.4 | Risk Classification | `RC-01` | Agent classifies, human validates |
| 1.5 | AI Tier Classification (conditional) *(conditional)* | `AC-01` | Agent proposes, human confirms |
| 1.5b | Data Classification Screening *(conditional)* | `SC-04` | Agent classifies, SA reviews |
| 1.6 | Product Owner Sign-off | `GC-05` | Human required |

## Required Controls

| Control | Name | Notes |
|---------|------|-------|
| [`SC-03`](../controls/sc/SC-03.yaml) | Pre-Guardrails | Must run first — screens for adversarial inputs before any agent processing |
| [`SC-04`](../controls/sc/SC-04.yaml) | Data Classification & Sensitivity Screening | Applicable when the change processes personal data or involves profiling |
| [`QC-01`](../controls/qc/QC-01.yaml) | Specification Validation |  |
| [`QC-02`](../controls/qc/QC-02.yaml) | Coherence & Conflict Resolution |  |
| [`RC-01`](../controls/rc/RC-01.yaml) | Risk Classification |  |
| [`AC-01`](../controls/ac/AC-01.yaml) | AI Risk Tier Classification | Applicable when the change involves an AI component |
| [`AC-02`](../controls/ac/AC-02.yaml) | GPAI & Foundation Model Obligation Screening | Applicable when the change introduces or modifies use of a GPAI/foundation model |
| [`GC-05`](../controls/gc/GC-05.yaml) | Intent Traceability |  |

## Exit Criteria Checklist

- [ ] SC-03: Pre-guardrails passed — no injection patterns detected in incoming request
- [ ] SC-04: Data classification assigned (if applicable to change)
- [ ] QC-01: Feature specification approved by Product Owner
- [ ] QC-02: All blocking conflicts resolved; non-blocking conflicts documented
- [ ] RC-01: Risk classification tier assigned and logged
- [ ] AC-01: AI Act risk tier confirmed (or not-applicable documented)
- [ ] AC-02: GPAI obligation screening completed (if applicable)
- [ ] GC-05: Intent audit record written to immutable log

## Input Artifacts

- `artifacts/inputs/change-request.yaml`

## Output Artifacts

- `artifacts/outputs/QC-01-feature-spec.yaml`
- `artifacts/outputs/QC-02-conflict-resolution-record.yaml`
- `artifacts/outputs/RC-01-risk-classification.yaml`
- `artifacts/outputs/AC-01-ai-tier-classification.yaml`
- `artifacts/outputs/SC-04-data-classification-record.yaml`
- `artifacts/outputs/GC-05-intent-audit-record.yaml`

## Directives Injected at Stage Entry

*None specified*

## Feedback Loop Triggers

*This stage is not a direct feedback loop trigger source.*

---

**Last Updated:** 2026-03-13 14:19 UTC
