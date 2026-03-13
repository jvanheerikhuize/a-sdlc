<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/06-observability-maintenance/06-observability-maintenance.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 6: Observability & Maintenance — Process

**Stage:** 06-Observability & Maintenance
**Purpose:** Operate, monitor, and maintain the deployed system. Controls in this stage run continuously, not per-change. Escalations from Stage 6 controls may trigger feedback loops back into earlier stages for remediation.

## Roles

| Code | Name | Mode | Responsibilities |
|------|------|------|------------------|
| SRE | Site Reliability Engineer | Autonomous | Executes continuous monitoring; detects anomalies; classifies incidents; prepares regulatory reports; triggers alerts |
| OPS | Operations / SRE | Gated | Activates monitoring at handover; responds to SLO and health alerts; initiates feedback loops for code changes |
| SA | Security Architect | Gated | Responds to incident and anomaly escalations; approves DORA Art. 19 classification; investigates security events |
| RO | Risk Officer | Gated | Responds to risk escalations from RC-08; makes risk acceptance decisions; approves feedback loop triggers |
| AGL | AI Governance Lead | Gated | Reviews AI post-market surveillance results; files serious AI incident reports per Art. 73 |
| CO | Compliance Officer | Gated | Reviews all regulatory incident reports; ensures DORA and AI Act reporting obligations are met |

## Process Steps

### Step 6.1 — Activate Monitoring

**Control:** none (procedural) · **Delegation:** Fully automated

System handover (handoff from Stage 5 - triggers all monitoring)

| Actor | Action |
|-------|--------|
| `OPS` | Confirm Stage 5 deployment integrity record is present and status is verified |
| `AGT` | Activate all monitoring profiles — SLO dashboards, health checks, SIEM rules, anomaly baselines |
| `AGT` | Confirm all monitoring channels are emitting data; alert on any silent channel |
| `OPS` | Confirm monitoring activation and enter hypercare window |

**Input:** Deployment integrity record (Stage 5 SC-17 output)

**Output:** Monitoring activation confirmed; all Stage 6 controls enter continuous operation


### Step 6.2 — SLA/SLO Monitoring

**Control:** [`QC-10`](../../controls/qc/QC-10.yaml) · **Delegation:** Agent monitors, OPS responds

SLA/SLO monitoring (continuous)

| Actor | Action |
|-------|--------|
| `AGT` | Continuously measure all defined SLIs against SLOs: availability, latency, error rate, throughput |
| `AGT` | Compute error budget consumption rate; alert when burn rate exceeds defined thresholds |
| `OPS` | Respond to burn rate alerts; make decisions on service degradation |
| `OPS` | Initiate feedback loop if SLO degradation requires a code change |

**Output:** SLO monitoring record (artifacts/outputs/slo-monitoring-record.yaml) — continuously updated


### Step 6.3 — Risk & Health Monitoring

**Control:** [`RC-08`](../../controls/rc/RC-08.yaml) · **Delegation:** Automated with human escalation

Risk and health monitoring (continuous)

| Actor | Action |
|-------|--------|
| `AGT` | Monitor configuration drift against approved baseline |
| `AGT` | Cross-reference SBOM against vulnerability databases; alert on new CVEs affecting dependencies |
| `AGT` | Monitor application health indicators, capacity trends, certificate expiry, dependency health |
| `RO` | Respond to risk threshold escalations; make risk acceptance or remediation decisions |
| `RO` | Initiate feedback loop if risk requires a code or configuration change |

**Output:** Risk & health monitoring record (artifacts/outputs/risk-health-monitoring-record.yaml) — continuously updated


### Step 6.3-3rd-party — Third-Party Risk Monitoring

**Control:** [`RC-09`](../../controls/rc/RC-09.yaml) · **Delegation:** Fully automated

> **Conditional:** Applicable for AI component deployments — monitors third-party provider risk posture

Third-party continuous risk monitoring (continuous)

| Actor | Action |
|-------|--------|
| `AGT` | Monitor third-party providers (cloud vendors, SaaS platforms) for compliance and security events |
| `AGT` | Track provider security posture, incident reports, and compliance changes |
| `RO` | Escalate if provider risk exceeds acceptable thresholds |

**Output:** Third-party risk monitoring record (artifacts/outputs/third-party-risk-monitoring.yaml)


### Step 6.4 — Incident Scanning & Detection

**Control:** [`SC-19`](../../controls/sc/SC-19.yaml) · **Delegation:** Automated with human escalation

Incident scanning and detection (continuous, DORA Art. 17-19 reporting)

| Actor | Action |
|-------|--------|
| `AGT` | Monitor SIEM continuously using MITRE ATT&CK detection patterns |
| `AGT` | Detect and classify all security events per DORA Art. 18 taxonomy |
| `AGT` | For major incidents: start reporting timelines and prepare initial notification |
| `SA` | Validate incident classification; approve escalation decisions |
| `CO` | Approve and submit regulatory incident reports per DORA Art. 19 timelines |

**Output:** Incident detection record (artifacts/outputs/incident-detection-record.yaml) — continuously updated


### Step 6.5 — Runtime Anomaly Detection

**Control:** [`SC-20`](../../controls/sc/SC-20.yaml) · **Delegation:** Automated with human escalation

Runtime anomaly detection (continuous, feeds into SC-19)

| Actor | Action |
|-------|--------|
| `AGT` | Maintain statistical behavioural baselines for all system components |
| `AGT` | Detect deviations: AI model drift, adversarial inputs, abnormal resource patterns, unexpected call graphs |
| `AGT` | Escalate anomalies exceeding defined thresholds to SC-19 (Step 6.4) incident process |
| `SA` | Investigate high-severity anomalies; determine whether anomaly is a security incident or requires code change |

**Output:** Anomaly detection record (artifacts/outputs/anomaly-detection-record.yaml) — continuously updated


### Step 6.6 — AI Post-Market Surveillance

**Control:** [`AC-06`](../../controls/ac/AC-06.yaml) · **Delegation:** Agent monitors, AGL reports

> **Conditional:** Only applicable when the deployed system includes AI components.

AI post-market surveillance (continuous, conditional on ai_component)

| Actor | Action |
|-------|--------|
| `AGT` | Continuously track AI performance metrics against Stage 4 QC-07 baselines |
| `AGT` | Execute scheduled bias re-testing at defined intervals |
| `AGT` | Maintain incident log for any serious AI incidents |
| `AGT` | Keep AI Act technical documentation current |
| `AGL` | Review surveillance reports; make decisions on retraining or rollback |
| `AGL` | File serious AI incident reports to relevant authorities per Art. 73 |

**Output:** AI post-market surveillance report (artifacts/outputs/ai-surveillance-report.yaml) — periodic


## Exit Criteria

- Not a time-bounded stage — exits only when the system is decommissioned.
- Escalations from any Stage 6 control may trigger a feedback loop into earlier stages.


## Output Artifacts

- `artifacts/outputs/QC-10-slo-monitoring-record.yaml`
- `artifacts/outputs/RC-08-risk-health-monitoring-record.yaml`
- `artifacts/outputs/SC-19-incident-detection-record.yaml`
- `artifacts/outputs/SC-20-anomaly-detection-record.yaml`
- `artifacts/outputs/AC-06-ai-surveillance-report.yaml`
- `artifacts/outputs/RC-09-third-party-risk-monitoring.yaml`


## References

- Stage definition: `06-observability-maintenance.yaml`
- Controls: See `required_controls` in stage YAML.

---

**Last Updated:** 2026-03-13 12:43 UTC
