<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/06-observability-maintenance/stage.yaml + controls/ + directives/
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 6: Observability & Maintenance — Context Bundle

> **Agent load file** — load this at Stage 6 entry for full context.

**Stage:** 06-Observability & Maintenance
**Purpose:** Operate, monitor, and maintain the deployed system. Controls in this stage run continuously, not per-change. Escalations from Stage 6 controls may trigger feedback loops back into earlier stages for remediation.

## Files to Load at Stage Entry

- `stages/06-observability-maintenance/stage.yaml` — stage definition (steps in: `stages/06-observability-maintenance/steps/`)
- `controls/qc/QC-10.yaml` — control definition *(Continuous — runs throughout the operational lifetime)*
- `controls/rc/RC-08.yaml` — control definition *(Continuous — runs throughout the operational lifetime)*
- `controls/rc/RC-09.yaml` — control definition *(Applicable for AI component deployments — monitors third-party provider risk posture)*
- `controls/sc/SC-19.yaml` — control definition *(Continuous — DORA Art. 17–19 reporting obligations)*
- `controls/sc/SC-20.yaml` — control definition *(Continuous — feeds anomalies into SC-19 incident process)*
- `controls/ac/AC-06.yaml` — control definition *(Applicable when deployed system includes AI components)*

## Workflow Execution Order

| Step | Title | Control | Delegation |
|------|-------|---------|------------|
| 6.1 | Activate Monitoring | `—` | Fully automated |
| 6.2 | SLA/SLO Monitoring | `QC-10` | Agent monitors, OPS responds |
| 6.3 | Risk & Health Monitoring | `RC-08` | Automated with human escalation |
| 6.3-3rd-party | Third-Party Risk Monitoring *(conditional)* | `RC-09` | Fully automated |
| 6.4 | Incident Scanning & Detection | `SC-19` | Automated with human escalation |
| 6.5 | Runtime Anomaly Detection | `SC-20` | Automated with human escalation |
| 6.6 | AI Post-Market Surveillance *(conditional)* | `AC-06` | Agent monitors, AGL reports |

## Required Controls

| Control | Name | Notes |
|---------|------|-------|
| [`QC-10`](../controls/qc/QC-10.yaml) | SLA/SLO Monitoring | Continuous — runs throughout the operational lifetime |
| [`RC-08`](../controls/rc/RC-08.yaml) | Risk & Health Monitoring | Continuous — runs throughout the operational lifetime |
| [`RC-09`](../controls/rc/RC-09.yaml) | Third-Party Continuous Risk Monitoring | Applicable for AI component deployments — monitors third-party provider risk posture |
| [`SC-19`](../controls/sc/SC-19.yaml) | Incident Scanning & Detection | Continuous — DORA Art. 17–19 reporting obligations |
| [`SC-20`](../controls/sc/SC-20.yaml) | Runtime Anomaly Detection | Continuous — feeds anomalies into SC-19 incident process |
| [`AC-06`](../controls/ac/AC-06.yaml) | AI Post-Market Surveillance | Applicable when deployed system includes AI components |

## Exit Criteria Checklist

- [ ] Not a time-bounded stage — exits only when the system is decommissioned.
- [ ] Escalations from any Stage 6 control may trigger a feedback loop into earlier stages.

## Input Artifacts

- `../05-deployment-release/artifacts/outputs/SC-17-deployment-integrity-record.yaml`

## Output Artifacts

- `artifacts/outputs/QC-10-slo-monitoring-record.yaml`
- `artifacts/outputs/RC-08-risk-health-monitoring-record.yaml`
- `artifacts/outputs/SC-19-incident-detection-record.yaml`
- `artifacts/outputs/SC-20-anomaly-detection-record.yaml`
- `artifacts/outputs/AC-06-ai-surveillance-report.yaml`
- `artifacts/outputs/RC-09-third-party-risk-monitoring.yaml`

## Directives Injected at Stage Entry

*None specified*

## Feedback Loop Triggers

Failures in this stage may trigger a feedback loop. Execute Step FL.1 to classify:
- `AC-06` — failure triggers FL.1 path classification
- `QC-10` — failure triggers FL.1 path classification
- `RC-08` — failure triggers FL.1 path classification
- `SC-19` — failure triggers FL.1 path classification
- `SC-20` — failure triggers FL.1 path classification

See [`feedbackloops/feedback-loops.yaml`](../feedbackloops/feedback-loops.yaml) and [`feedbackloops/process.md`](../feedbackloops/process.md).

---

**Last Updated:** 2026-03-13 14:19 UTC
