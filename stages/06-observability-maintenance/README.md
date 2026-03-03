# Stage 6: Observability & Maintenance

The **only stage that never ends.** Provides continuous monitoring of operational health, security posture, risk evolution, and AI behaviour from the moment Stage 5 hands over to production.

Stage 6 feeds back into the lifecycle through two defined re-entry paths when issues requiring code changes are detected. See [feedbackloops/README.md](../../feedbackloops/README.md).

## Steps

Full step-by-step process with roles and decision points: [process.md](process.md)

| Step | Name | Delegation | Sequencing |
| ---- | ---- | ---------- | ---------- |
| [6.1](process.md#step-61--activate-monitoring) | Activate Monitoring | Fully automated | Runs once at Stage 5 handover |
| [6.2](process.md#step-62--slaslo-monitoring) | SLA/SLO Monitoring | Fully automated | Continuous after 6.1 |
| [6.3](process.md#step-63--risk--health-monitoring) | Risk & Health Monitoring | Automated, human escalation | Continuous after 6.1 |
| [6.4](process.md#step-64--incident-scanning--detection) | Incident Scanning & Detection | Automated, human escalation | Continuous after 6.1 |
| [6.5](process.md#step-65--runtime-anomaly-detection) | Runtime Anomaly Detection | Automated, human escalation | Continuous after 6.1 — feeds into 6.4 |
| [6.6](process.md#step-66--ai-post-market-surveillance-conditional) | AI Post-Market Surveillance *(conditional)* | Agent monitors, AGL reports | Continuous after 6.1 |

## Controls

Stage definition (required controls + exit criteria): [06-observability-maintenance.yaml](06-observability-maintenance.yaml)

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| [QC-6A](../../controls/qc/QC-6A.yaml) | SLA/SLO Monitoring | Continuous measurement of SLIs against SLOs. Error budget burn rate alerting. | Fully automated | DORA: Art. 10, Art. 8(4); DNB: Service level management |
| [RC-6A](../../controls/rc/RC-6A.yaml) | Risk & Health Monitoring | Config drift, SBOM vulnerabilities, app health, capacity, certificate expiry, dependency status. | Automated, human escalation | DORA: Art. 8(2), Art. 10; DNB: Continuous risk monitoring; AI Act: Art. 9(1) |
| [SC-6A](../../controls/sc/SC-6A.yaml) | Incident Scanning & Detection | Real-time SIEM with MITRE ATT&CK detection. DORA Art. 18 classification and reporting timelines. | Automated, human escalation | DORA: Art. 17, Art. 18, Art. 19; DNB: Incident reporting; AI Act: Art. 73 |
| [SC-6B](../../controls/sc/SC-6B.yaml) | Runtime Anomaly Detection | Statistical behavioural baselines. AI model drift, adversarial input detection. Feeds into SC-6A. | Automated, human escalation | DORA: Art. 10; DNB: Anomaly detection; AI Act: Art. 15(3), Art. 9(2)(b) |
| [AC-6A](../../controls/ac/AC-6A.yaml) | AI Post-Market Surveillance *(conditional)* | Art. 72 post-market monitoring: performance tracking, bias re-testing, serious incident reporting. | Agent monitors, AGL reports | AI Act: Art. 72, Art. 73, Art. 61 |

## Stage Exit Criteria

This stage does not have time-bounded exit criteria. It runs continuously for the operational lifetime of the system and ends only at decommissioning.

Escalations from any Stage 6 control may trigger a feedback loop into earlier stages:

| Condition | Path | Re-Entry |
| --------- | ---- | -------- |
| Easy, obvious, low-risk issue matching pre-approved template — root cause confirmed | Path A — Quick Fix | Stage 3 (minimum controls) |
| Any other condition — complex, architectural, or unclear root cause | Path B — Full Re-entry | Stage 1 |

See [feedbackloops/README.md](../../feedbackloops/README.md) for eligibility criteria and minimum control sets.

## DORA Incident Reporting Timelines

When SC-6A classifies a major incident, DORA Art. 19 reporting obligations are triggered:

| Notification Type | Deadline |
| ----------------- | -------- |
| Initial notification | Within 4 hours of major incident declaration |
| Intermediate report | Within 72 hours |
| Final report | Within 1 month of resolution |

## Artifacts

- **Process:** [process.md](process.md) — Step-by-step guide with roles, escalation paths, and feedback loop triggers
- **Directives:** [../../directives/stages/06-observability-maintenance.yaml](../../directives/stages/06-observability-maintenance.yaml) — SC-2B injection payload (immutable)

**Input (from Stage 5):**

- [deployment-integrity-record.yaml](../05-deployment-release/artifacts/outputs/deployment-integrity-record.yaml) — Stage 5 handover confirmation (SC-5B output)

**Outputs (ongoing records):**

- [artifacts/outputs/slo-monitoring-record.yaml](artifacts/outputs/slo-monitoring-record.yaml) — QC-6A output
- [artifacts/outputs/risk-health-monitoring-record.yaml](artifacts/outputs/risk-health-monitoring-record.yaml) — RC-6A output
- [artifacts/outputs/incident-detection-record.yaml](artifacts/outputs/incident-detection-record.yaml) — SC-6A output
- [artifacts/outputs/anomaly-detection-record.yaml](artifacts/outputs/anomaly-detection-record.yaml) — SC-6B output
- [artifacts/outputs/ai-surveillance-report.yaml](artifacts/outputs/ai-surveillance-report.yaml) — AC-6A output (if AI component)
