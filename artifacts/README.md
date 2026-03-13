<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/*/[stage].yaml + feedbackloops/feedback-loops.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Artifact Catalog

Index of all output artifact templates produced across the A-SDLC lifecycle.

**Total artifacts:** 45

Artifact templates define the required fields for each output. Templates live alongside their producing stage in `stages/NN-name/artifacts/outputs/`. A ✓ means the template file exists in the repository.


## Stage 1: Intent Ingestion

| Artifact | Template | Control |
|----------|----------|---------|
| `QC-01-feature-spec.yaml` | ✓ | [`QC-01`](../controls/qc/QC-01.yaml) |
| `QC-02-conflict-resolution-record.yaml` | ✓ | [`QC-02`](../controls/qc/QC-02.yaml) |
| `RC-01-risk-classification.yaml` | ✓ | [`RC-01`](../controls/rc/RC-01.yaml) |
| `AC-01-ai-tier-classification.yaml` | ✓ | [`AC-01`](../controls/ac/AC-01.yaml) |
| `SC-04-data-classification-record.yaml` | ✓ | [`SC-04`](../controls/sc/SC-04.yaml) |
| `GC-05-intent-audit-record.yaml` | ✓ | [`GC-05`](../controls/gc/GC-05.yaml) |

## Stage 2: System Design

| Artifact | Template | Control |
|----------|----------|---------|
| `QC-03-design-document.yaml` | ✓ | [`QC-03`](../controls/qc/QC-03.yaml) |
| `SC-05-stride-threat-model.yaml` | ✓ | [`SC-05`](../controls/sc/SC-05.yaml) |
| `RC-02-design-approval-decision.yaml` | ✓ | [`RC-02`](../controls/rc/RC-02.yaml) |
| `SC-02-directive-injection-confirmation.yaml` | ✓ | [`SC-02`](../controls/sc/SC-02.yaml) |
| `AC-03-ai-component-design-review.yaml` | ✓ | [`AC-03`](../controls/ac/AC-03.yaml) |
| `RC-03-privacy-impact-assessment.yaml` | ✓ | [`RC-03`](../controls/rc/RC-03.yaml) |
| `SC-06-zero-trust-validation.yaml` | ✓ | [`SC-06`](../controls/sc/SC-06.yaml) |
| `AC-04-ai-model-governance-record.yaml` | ✓ | [`AC-04`](../controls/ac/AC-04.yaml) |

## Stage 3: Coding & Implementation

| Artifact | Template | Control |
|----------|----------|---------|
| `QC-04-pull-request-record.yaml` | ✓ | [`QC-04`](../controls/qc/QC-04.yaml) |
| `QC-05-quality-gate-report.yaml` | ✓ | [`QC-05`](../controls/qc/QC-05.yaml) |
| `SC-07-permission-enforcement-log.yaml` | ✓ | [`SC-07`](../controls/sc/SC-07.yaml) |
| `SC-08-post-guardrail-scan.yaml` | ✓ | [`SC-08`](../controls/sc/SC-08.yaml) |
| `SC-09-secrets-scan-report.yaml` | ✓ | [`SC-09`](../controls/sc/SC-09.yaml) |
| `RC-04-decision-log.yaml` | ✓ | [`RC-04`](../controls/rc/RC-04.yaml) |
| `SC-10-sca-report.yaml` | ✓ | [`SC-10`](../controls/sc/SC-10.yaml) |
| `SC-11-container-iac-security-report.yaml` | ✓ | [`SC-11`](../controls/sc/SC-11.yaml) |
| `GC-03-code-provenance-record.yaml` | ✓ | [`GC-03`](../controls/gc/GC-03.yaml) |

## Stage 4: Testing & Documentation

| Artifact | Template | Control |
|----------|----------|---------|
| `QC-06-test-results-report.yaml` | ✓ | [`QC-06`](../controls/qc/QC-06.yaml) |
| `SC-12-sast-scan-report.yaml` | ✓ | [`SC-12`](../controls/sc/SC-12.yaml) |
| `SC-13-dast-scan-report.yaml` | ✓ | [`SC-13`](../controls/sc/SC-13.yaml) |
| `QC-08-documentation-completeness-report.yaml` | ✓ | [`QC-08`](../controls/qc/QC-08.yaml) |
| `QC-07-ai-output-validation-report.yaml` | ✓ | [`QC-07`](../controls/qc/QC-07.yaml) |
| `AC-05-bias-fairness-report.yaml` | ✓ | [`AC-05`](../controls/ac/AC-05.yaml) |
| `RC-05-risk-threshold-evaluation.yaml` | ✓ | [`RC-05`](../controls/rc/RC-05.yaml) |
| `SC-14-api-security-report.yaml` | ✓ | [`SC-14`](../controls/sc/SC-14.yaml) |
| `SC-15-adversarial-robustness-report.yaml` | ✓ | [`SC-15`](../controls/sc/SC-15.yaml) |

## Stage 5: Deployment & Release

| Artifact | Template | Control |
|----------|----------|---------|
| `QC-09-release-readiness-checklist.yaml` | ✓ | [`QC-09`](../controls/qc/QC-09.yaml) |
| `RC-06-change-approval-record.yaml` | ✓ | [`RC-06`](../controls/rc/RC-06.yaml) |
| `RC-07-rollback-plan.yaml` | ✓ | [`RC-07`](../controls/rc/RC-07.yaml) |
| `SC-16-infrastructure-security-report.yaml` | ✓ | [`SC-16`](../controls/sc/SC-16.yaml) |
| `SC-17-deployment-integrity-record.yaml` | ✓ | [`SC-17`](../controls/sc/SC-17.yaml) |
| `SC-18-secrets-management-report.yaml` | ✓ | [`SC-18`](../controls/sc/SC-18.yaml) |

## Stage 6: Observability & Maintenance

| Artifact | Template | Control |
|----------|----------|---------|
| `QC-10-slo-monitoring-record.yaml` | ✓ | [`QC-10`](../controls/qc/QC-10.yaml) |
| `RC-08-risk-health-monitoring-record.yaml` | ✓ | [`RC-08`](../controls/rc/RC-08.yaml) |
| `SC-19-incident-detection-record.yaml` | ✓ | [`SC-19`](../controls/sc/SC-19.yaml) |
| `SC-20-anomaly-detection-record.yaml` | ✓ | [`SC-20`](../controls/sc/SC-20.yaml) |
| `AC-06-ai-surveillance-report.yaml` | ✓ | [`AC-06`](../controls/ac/AC-06.yaml) |
| `RC-09-third-party-risk-monitoring.yaml` | ✓ | [`RC-09`](../controls/rc/RC-09.yaml) |

## Feedback Loops

| Artifact | Template | Notes |
|----------|----------|-------|
| `feedback-loop-activation-record.yaml` | ✓ | Feedback loop activation |


---

**Last Updated:** 2026-03-13 14:19 UTC
