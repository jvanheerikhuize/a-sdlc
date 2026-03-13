<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/04-testing-documentation/stage.yaml + controls/ + directives/
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 4: Testing & Documentation — Context Bundle

> **Agent load file** — load this at Stage 4 entry for full context.

**Stage:** 04-Testing & Documentation
**Purpose:** Validate the implementation against all acceptance criteria, security requirements, and documentation standards. RC-05 is the formal go/no-go gate for deployment. No change proceeds to Stage 5 without a passing or conditionally accepted RC-05 result.

## Files to Load at Stage Entry

- `stages/04-testing-documentation/stage.yaml` — stage definition (steps in: `stages/04-testing-documentation/steps/`)
- `controls/qc/QC-06.yaml` — control definition
- `controls/qc/QC-07.yaml` — control definition *(Applicable when the change involves an AI component)*
- `controls/qc/QC-08.yaml` — control definition
- `controls/sc/SC-12.yaml` — control definition
- `controls/sc/SC-13.yaml` — control definition
- `controls/sc/SC-14.yaml` — control definition *(Test all exposed APIs against OWASP API Security Top 10)*
- `controls/ac/AC-05.yaml` — control definition *(Applicable when the change involves an AI component)*
- `controls/sc/SC-15.yaml` — control definition *(Applicable for high-risk or security-critical AI deployments)*
- `controls/rc/RC-05.yaml` — control definition *(Final go/no-go gate — depends on all other Stage 4 controls)*

## Workflow Execution Order

| Step | Title | Control | Delegation |
|------|-------|---------|------------|
| 4.1 | SAST | `SC-12` | Fully automated |
| 4.2 | Functional & Non-Functional Testing | `QC-06` | Agent executes, QA reviews |
| 4.3 | DAST | `SC-13` | Fully automated |
| 4.4 | AI Output Validation *(conditional)* | `QC-07` | Agent executes, AGL reviews |
| 4.5 | Bias & Fairness Testing *(conditional)* | `AC-05` | Agent executes, AGL reviews |
| 4.6 | Documentation Completeness | `QC-08` | Agent checks, human approves |
| 4.2-api | API Security Testing | `SC-14` | Fully automated |
| 4.7-ai-adversarial | Adversarial AI Robustness Testing *(conditional)* | `SC-15` | Fully automated |
| 4.8 | Risk Threshold Evaluation | `RC-05` | Agent calculates, RO decides |

## Required Controls

| Control | Name | Notes |
|---------|------|-------|
| [`QC-06`](../controls/qc/QC-06.yaml) | Functional & Non-Functional Testing |  |
| [`QC-07`](../controls/qc/QC-07.yaml) | AI Output Validation | Applicable when the change involves an AI component |
| [`QC-08`](../controls/qc/QC-08.yaml) | Documentation Completeness |  |
| [`SC-12`](../controls/sc/SC-12.yaml) | SAST |  |
| [`SC-13`](../controls/sc/SC-13.yaml) | DAST |  |
| [`SC-14`](../controls/sc/SC-14.yaml) | API Security Testing | Test all exposed APIs against OWASP API Security Top 10 |
| [`AC-05`](../controls/ac/AC-05.yaml) | Bias & Fairness Testing | Applicable when the change involves an AI component |
| [`SC-15`](../controls/sc/SC-15.yaml) | Adversarial AI Robustness Testing | Applicable for high-risk or security-critical AI deployments |
| [`RC-05`](../controls/rc/RC-05.yaml) | Risk Threshold Evaluation | Final go/no-go gate — depends on all other Stage 4 controls |

## Exit Criteria Checklist

- [ ] QC-06: All acceptance criteria from Stage 1 have passing tests
- [ ] QC-07: AI output validation passed within defined accuracy thresholds (or not-applicable)
- [ ] QC-08: Documentation completeness confirmed and approved
- [ ] SC-12: SAST passed — no critical or high-severity findings unresolved
- [ ] SC-13: DAST passed — no critical or high-severity findings unresolved
- [ ] SC-14: API security testing passed — no OWASP API Top 10 violations unresolved
- [ ] AC-05: Bias & fairness test passed within defined thresholds (or not-applicable)
- [ ] SC-15: Adversarial robustness testing completed (if applicable for high-risk AI)
- [ ] RC-05: Go/no-go decision is PASS or CONDITIONAL PASS with formal risk acceptance

## Input Artifacts

- `../01-intent-ingestion/artifacts/outputs/QC-01-feature-spec.yaml`
- `../01-intent-ingestion/artifacts/outputs/AC-01-ai-tier-classification.yaml`
- `../03-coding-implementation/artifacts/outputs/QC-04-pull-request-record.yaml`

## Output Artifacts

- `artifacts/outputs/QC-06-test-results-report.yaml`
- `artifacts/outputs/SC-12-sast-scan-report.yaml`
- `artifacts/outputs/SC-13-dast-scan-report.yaml`
- `artifacts/outputs/QC-08-documentation-completeness-report.yaml`
- `artifacts/outputs/QC-07-ai-output-validation-report.yaml`
- `artifacts/outputs/AC-05-bias-fairness-report.yaml`
- `artifacts/outputs/RC-05-risk-threshold-evaluation.yaml`
- `artifacts/outputs/SC-14-api-security-report.yaml`
- `artifacts/outputs/SC-15-adversarial-robustness-report.yaml`

## Directives Injected at Stage Entry

*None specified*

## Feedback Loop Triggers

Failures in this stage may trigger a feedback loop. Execute Step FL.1 to classify:
- `AC-05` — failure triggers FL.1 path classification
- `QC-06` — failure triggers FL.1 path classification
- `QC-07` — failure triggers FL.1 path classification
- `QC-08` — failure triggers FL.1 path classification
- `RC-05` — failure triggers FL.1 path classification
- `SC-12` — failure triggers FL.1 path classification
- `SC-13` — failure triggers FL.1 path classification

See [`feedbackloops/feedback-loops.yaml`](../feedbackloops/feedback-loops.yaml) and [`feedbackloops/process.md`](../feedbackloops/process.md).

---

**Last Updated:** 2026-03-13 14:19 UTC
