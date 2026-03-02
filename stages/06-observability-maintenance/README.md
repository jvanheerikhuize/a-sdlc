# Stage 6: Observability & Maintenance

The **only stage that never ends.** Provides continuous monitoring of operational health, security posture, risk evolution, and AI behaviour from the moment Stage 5 hands over to production.

Stage 6 feeds back into the lifecycle through two defined re-entry paths when issues requiring code changes are detected. See [cross-cutting/feedback-loops.yaml](../../cross-cutting/feedback-loops.yaml).

## Key Tasks

- Activate full monitoring profile upon Stage 5 handover
- Measure SLIs continuously; track error budget consumption
- Monitor application health: heartbeats, resource trends, dependency health, data pipeline integrity
- Monitor certificates, credentials, and capacity trends proactively
- Cross-reference SBOM against vulnerability databases daily
- Detect configuration drift against approved baseline
- Classify incidents per DORA taxonomy; initiate reporting timelines for major incidents
- For AI components: scheduled performance re-validation and bias re-testing
- Route issues through appropriate feedback loop when code changes are needed

## Controls

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| QC-6A | SLA/SLO Monitoring | Continuous monitoring of availability, latency, error rates, throughput. Error budget burn rate alerting. | Fully automated | DORA: Art. 10, Art. 8(4); DNB: Service level management |
| RC-6A | Risk & Health Monitoring | Monitors config drift, vulnerabilities, threat landscape, app health, capacity, certificate expiry, dependency status. | Automated + human escalation | DORA: Art. 8(2), Art. 10; DNB: Continuous risk monitoring; AI Act: Art. 9(1) |
| SC-6A | Incident Scanning & Detection | Real-time SIEM monitoring. MITRE ATT&CK detection. DORA Art. 18 classification and reporting timelines. | Automated + human escalation | DORA: Art. 17, Art. 18, Art. 19; DNB: Incident reporting; AI Act: Art. 73 |
| SC-6B | Runtime Anomaly Detection | Behavioural baselines, statistical anomaly detection, AI model drift, adversarial input detection. | Automated + human escalation | DORA: Art. 10; DNB: Anomaly detection; AI Act: Art. 15(3), Art. 9(2)(b) |
| AC-6A | AI Post-Market Surveillance | Art. 72: ongoing performance tracking, bias re-testing, incident logging, and documentation maintenance. | Agent monitors, human reports | AI Act: Art. 72, Art. 73, Art. 61 |

Full control definitions: [controls.yaml](controls.yaml)

## DORA Incident Classification & Reporting Timelines

When SC-6A detects a major incident, DORA reporting obligations are triggered:

| Threshold | Notification Type | Deadline |
| --------- | ----------------- | -------- |
| Major incident declared | Initial notification | Within 4 hours |
| Major incident confirmed | Intermediate report | Within 72 hours |
| Incident resolved | Final report | Within 1 month |

## Feedback Loop Triggers

| Condition | Path | Re-Entry |
| --------- | ---- | -------- |
| Low-risk issue matching pre-approved template | Path A | Stage 3 |
| Bug requiring targeted code fix | Path B (Quickfix) | Stage 3 |
| Issue requiring new functionality or architectural change | Path B (Feature) | Stage 1 |
