# Stage 6 — Observability & Maintenance

> **Auto-generated from `stages/06-observability-maintenance/06-observability-maintenance.yaml`** · Agent context bundle · All controls and workflow in one file

Operate, monitor, and maintain the deployed system. Controls in this stage run continuously, not per-change. Escalations from Stage 6 controls may trigger feedback loops back into earlier stages for remediation.

---

## Quick Load

Load these files for this stage:

```
- stages/06-observability-maintenance/06-observability-maintenance.yaml
- directives/stages/06-observability-and-maintenance.yaml
```

---

## Workflow — Execution Order

| Step | Title | Control | Actors | Delegation | Depends On |
| ---- | ----- | ------- | ------ | ---------- | ---------- |
| 6.1 | Activate Monitoring | None | OPS, AGT, AGT, OPS | Fully automated | — |
| 6.2 | SLA/SLO Monitoring | QC-6A | AGT, AGT, OPS, OPS | Agent monitors, OPS responds | n-handover |
| 6.3 | Risk & Health Monitoring | RC-6A | AGT, AGT, AGT, RO, RO | Automated with human escalation | n-handover |
| 6.3-3rd-party | Third-Party Risk Monitoring | RC-6B | AGT, AGT, RO | Fully automated | n-handover |
| 6.4 | Incident Scanning & Detection | SC-6A | AGT, AGT, AGT, SA, CO | Automated with human escalation | n-handover, n-sc6b |
| 6.5 | Runtime Anomaly Detection | SC-6B | AGT, AGT, AGT, SA | Automated with human escalation | n-handover |
| 6.6 | AI Post-Market Surveillance | AC-6A | AGT, AGT, AGT, AGT, AGL, AGL | Agent monitors, AGL reports | n-handover |

---

## Controls — What Agent and Human Do

| ID | Name | Delegation | Agent Does | Human Does |
| -- | ---- | ---------- | ---------- | ---------- |
| QC-6A | SLA/SLO Monitoring | fully_automated | Continuously measure SLIs; compute error budget consumption; trigger alerts when burn rate thresholds are exceeded. | Respond to alerts; make decisions on service degradation; initiate feedback loop if code change is needed. |
| RC-6A | Risk & Health Monitoring | automated_with_human_escalation | Continuously monitor all risk and health indicators; detect drift, vulnerabilities, and capacity risks; alert on threshold breaches. | Respond to escalations; make decisions on risk acceptance or remediation; initiate feedback loops. |
| RC-6B | Third-Party Continuous Risk Monitoring | agent_monitors_human_reports | Continuously monitor critical third-party providers: subscribe to their security advisories, track vulnerability disclosures, check compliance certification renewal status, monitor SLA performance (uptime, latency). Aggregate risk indicators. Alert on material risk changes (critical advisory, certification expiry, SLA breach). | Review alerts. When a third-party risk is identified: assess impact on deployed systems, determine escalation path (contact vendor, request patch, plan migration), and update risk register. Report material third-party risks to senior management. |
| SC-6A | Incident Scanning & Detection | automated_with_human_escalation | Monitor SIEM continuously; detect and classify incidents; trigger reporting timelines; prepare incident reports. | Validate incident classification; approve regulatory reports; make escalation decisions. |
| SC-6B | Runtime Anomaly Detection | automated_with_human_escalation | Maintain behavioural baselines; apply statistical anomaly detection; detect AI model drift and adversarial inputs; escalate on anomaly. | Investigate escalated anomalies; determine whether anomaly represents a security incident or requires code change. |
| AC-6A | AI Post-Market Surveillance | agent_monitors_human_reports | Track AI performance metrics continuously; schedule and execute bias re-testing; detect performance degradation; prepare incident reports. | Review AI performance trends; file serious incident reports to regulators; make decisions on retraining or rollback. |
---

## Exit Criteria (Stage 6 Complete When)

- [ ] Not a time-bounded stage — exits only when the system is decommissioned.
- [ ] Escalations from any Stage 6 control may trigger a feedback loop into earlier stages.

---

## Artifact I/O

**Inputs from Prior Stage:**
- ../05-deployment-release/artifacts/outputs/SC-5B-deployment-integrity-record.yaml

**Outputs to Next Stage:**
- artifacts/outputs/QC-6A-slo-monitoring-record.yaml
- artifacts/outputs/RC-6A-risk-health-monitoring-record.yaml
- artifacts/outputs/SC-6A-incident-detection-record.yaml
- artifacts/outputs/SC-6B-anomaly-detection-record.yaml
- artifacts/outputs/AC-6A-ai-surveillance-report.yaml
- artifacts/outputs/RC-6B-third-party-risk-monitoring.yaml

---

## Feedback Loop Triggers

Controls in this stage that can trigger re-entry:

None

For full feedback loop definitions, see [`feedbackloops/feedback-loops.yaml`](../../feedbackloops/feedback-loops.yaml).

---

**Last Updated:** 2026-03-05 22:29 UTC