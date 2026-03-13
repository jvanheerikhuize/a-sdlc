<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/*/[stage].yaml workflow nodes
     Regenerate: bash scripts/generate-docs.sh -->

# Role-Control Responsibility Matrix

Maps each actor role to the controls they execute or approve, derived from workflow node actor definitions across all 6 lifecycle stages.

**Total role-control assignments:** 162

## By Role

### `AGL`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`AC-01`](../controls/ac/AC-01.yaml) | AI Risk Tier Classification | Stage 1: Intent Ingestion | Agent proposes, human confirms |
| [`AC-03`](../controls/ac/AC-03.yaml) | AI Component Design Review | Stage 2: System Design | Agent assists, AGL approves |
| [`AC-04`](../controls/ac/AC-04.yaml) | AI Model Governance & Version Control | Stage 2: System Design | Agent registers, AGL approves |
| [`AC-05`](../controls/ac/AC-05.yaml) | Bias & Fairness Testing | Stage 4: Testing & Documentation | Agent executes, AGL reviews |
| [`QC-07`](../controls/qc/QC-07.yaml) | AI Output Validation | Stage 4: Testing & Documentation | Agent executes, AGL reviews |
| [`AC-06`](../controls/ac/AC-06.yaml) | AI Post-Market Surveillance | Stage 6: Observability & Maintenance | Agent monitors, AGL reports |


### `AGT`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`AC-01`](../controls/ac/AC-01.yaml) | AI Risk Tier Classification | Stage 1: Intent Ingestion | Agent proposes, human confirms |
| [`QC-01`](../controls/qc/QC-01.yaml) | Specification Validation | Stage 1: Intent Ingestion | Agent drafts → human approves |
| [`QC-02`](../controls/qc/QC-02.yaml) | Coherence & Conflict Resolution | Stage 1: Intent Ingestion | Agent analyses, human resolves |
| [`RC-01`](../controls/rc/RC-01.yaml) | Risk Classification | Stage 1: Intent Ingestion | Agent classifies, human validates |
| [`SC-03`](../controls/sc/SC-03.yaml) | Pre-Guardrails | Stage 1: Intent Ingestion | Fully automated |
| [`SC-04`](../controls/sc/SC-04.yaml) | Data Classification & Sensitivity Screening | Stage 1: Intent Ingestion | Agent classifies, SA reviews |
| [`AC-03`](../controls/ac/AC-03.yaml) | AI Component Design Review | Stage 2: System Design | Agent assists, AGL approves |
| [`AC-04`](../controls/ac/AC-04.yaml) | AI Model Governance & Version Control | Stage 2: System Design | Agent registers, AGL approves |
| [`QC-03`](../controls/qc/QC-03.yaml) | Design Completeness & Standards | Stage 2: System Design | Agent drafts |
| [`RC-02`](../controls/rc/RC-02.yaml) | Design Approval | Stage 2: System Design | Human required |
| [`RC-03`](../controls/rc/RC-03.yaml) | Privacy Impact Assessment Gate | Stage 2: System Design | Agent generates, LAD reviews |
| [`SC-02`](../controls/sc/SC-02.yaml) | Stage Directive Injection | Stage 2: System Design | Fully automated |
| [`SC-05`](../controls/sc/SC-05.yaml) | Threat Model Validation | Stage 2: System Design | Agent generates, SA validates |
| [`SC-06`](../controls/sc/SC-06.yaml) | Zero-Trust Architecture Validation | Stage 2: System Design | Fully automated |
| [`GC-03`](../controls/gc/GC-03.yaml) | Agent Provenance Registry | Stage 3: Coding & Implementation | Fully automated |
| [`QC-04`](../controls/qc/QC-04.yaml) | Pull Request Creation & Review | Stage 3: Coding & Implementation | Agent creates, humans review |
| [`QC-05`](../controls/qc/QC-05.yaml) | Code Quality Standards | Stage 3: Coding & Implementation | Agent implements, DEV authors |
| [`RC-04`](../controls/rc/RC-04.yaml) | Decision Log | Stage 3: Coding & Implementation | Agent logs, DEV reviews |
| [`SC-07`](../controls/sc/SC-07.yaml) | Permission Management | Stage 3: Coding & Implementation | Fully automated |
| [`SC-08`](../controls/sc/SC-08.yaml) | Post-Guardrails | Stage 3: Coding & Implementation | Fully automated |
| [`SC-09`](../controls/sc/SC-09.yaml) | Secrets & Credentials Scanning | Stage 3: Coding & Implementation | Fully automated |
| [`SC-10`](../controls/sc/SC-10.yaml) | Software Composition Analysis & SBOM Generation | Stage 3: Coding & Implementation | Fully automated |
| [`SC-11`](../controls/sc/SC-11.yaml) | Container & IaC Security Scanning | Stage 3: Coding & Implementation | Fully automated |
| [`AC-05`](../controls/ac/AC-05.yaml) | Bias & Fairness Testing | Stage 4: Testing & Documentation | Agent executes, AGL reviews |
| [`QC-06`](../controls/qc/QC-06.yaml) | Functional & Non-Functional Testing | Stage 4: Testing & Documentation | Agent executes, QA reviews |
| [`QC-07`](../controls/qc/QC-07.yaml) | AI Output Validation | Stage 4: Testing & Documentation | Agent executes, AGL reviews |
| [`QC-08`](../controls/qc/QC-08.yaml) | Documentation Completeness | Stage 4: Testing & Documentation | Agent checks, human approves |
| [`RC-05`](../controls/rc/RC-05.yaml) | Risk Threshold Evaluation | Stage 4: Testing & Documentation | Agent calculates, RO decides |
| [`SC-12`](../controls/sc/SC-12.yaml) | SAST | Stage 4: Testing & Documentation | Fully automated |
| [`SC-13`](../controls/sc/SC-13.yaml) | DAST | Stage 4: Testing & Documentation | Fully automated |
| [`SC-14`](../controls/sc/SC-14.yaml) | API Security Testing | Stage 4: Testing & Documentation | Fully automated |
| [`SC-15`](../controls/sc/SC-15.yaml) | Adversarial AI Robustness Testing | Stage 4: Testing & Documentation | Fully automated |
| [`QC-09`](../controls/qc/QC-09.yaml) | Release Readiness Checklist | Stage 5: Deployment & Release | Agent compiles, REL approves |
| [`RC-06`](../controls/rc/RC-06.yaml) | CAB Approval | Stage 5: Deployment & Release | Human required |
| [`RC-07`](../controls/rc/RC-07.yaml) | Rollback Plan Validation | Stage 5: Deployment & Release | Agent validates, REL approves |
| [`SC-16`](../controls/sc/SC-16.yaml) | Infrastructure Security | Stage 5: Deployment & Release | Fully automated |
| [`SC-17`](../controls/sc/SC-17.yaml) | Deployment Integrity | Stage 5: Deployment & Release | Fully automated |
| [`SC-18`](../controls/sc/SC-18.yaml) | Secrets & Key Management Lifecycle | Stage 5: Deployment & Release | Fully automated |
| [`AC-06`](../controls/ac/AC-06.yaml) | AI Post-Market Surveillance | Stage 6: Observability & Maintenance | Agent monitors, AGL reports |
| [`QC-10`](../controls/qc/QC-10.yaml) | SLA/SLO Monitoring | Stage 6: Observability & Maintenance | Agent monitors, OPS responds |
| [`RC-08`](../controls/rc/RC-08.yaml) | Risk & Health Monitoring | Stage 6: Observability & Maintenance | Automated with human escalation |
| [`RC-09`](../controls/rc/RC-09.yaml) | Third-Party Continuous Risk Monitoring | Stage 6: Observability & Maintenance | Fully automated |
| [`SC-19`](../controls/sc/SC-19.yaml) | Incident Scanning & Detection | Stage 6: Observability & Maintenance | Automated with human escalation |
| [`SC-20`](../controls/sc/SC-20.yaml) | Runtime Anomaly Detection | Stage 6: Observability & Maintenance | Automated with human escalation |


### `CO`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`SC-19`](../controls/sc/SC-19.yaml) | Incident Scanning & Detection | Stage 6: Observability & Maintenance | Automated with human escalation |


### `DEV`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`QC-04`](../controls/qc/QC-04.yaml) | Pull Request Creation & Review | Stage 3: Coding & Implementation | Agent creates, humans review |
| [`QC-05`](../controls/qc/QC-05.yaml) | Code Quality Standards | Stage 3: Coding & Implementation | Agent implements, DEV authors |
| [`RC-04`](../controls/rc/RC-04.yaml) | Decision Log | Stage 3: Coding & Implementation | Agent logs, DEV reviews |
| [`SC-09`](../controls/sc/SC-09.yaml) | Secrets & Credentials Scanning | Stage 3: Coding & Implementation | Fully automated |


### `LAD`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`QC-03`](../controls/qc/QC-03.yaml) | Design Completeness & Standards | Stage 2: System Design | Agent validates, LAD approves |
| [`RC-03`](../controls/rc/RC-03.yaml) | Privacy Impact Assessment Gate | Stage 2: System Design | Agent generates, LAD reviews |


### `OPS`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`QC-10`](../controls/qc/QC-10.yaml) | SLA/SLO Monitoring | Stage 6: Observability & Maintenance | Agent monitors, OPS responds |


### `PO`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`GC-05`](../controls/gc/GC-05.yaml) | Intent Traceability | Stage 1: Intent Ingestion | Human required |
| [`QC-02`](../controls/qc/QC-02.yaml) | Coherence & Conflict Resolution | Stage 1: Intent Ingestion | Agent analyses, human resolves |


### `QA`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`QC-06`](../controls/qc/QC-06.yaml) | Functional & Non-Functional Testing | Stage 4: Testing & Documentation | Agent executes, QA reviews |
| [`QC-08`](../controls/qc/QC-08.yaml) | Documentation Completeness | Stage 4: Testing & Documentation | Agent checks, human approves |


### `REL`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`QC-09`](../controls/qc/QC-09.yaml) | Release Readiness Checklist | Stage 5: Deployment & Release | Agent compiles, REL approves |
| [`RC-07`](../controls/rc/RC-07.yaml) | Rollback Plan Validation | Stage 5: Deployment & Release | Agent validates, REL approves |


### `RO`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`RC-01`](../controls/rc/RC-01.yaml) | Risk Classification | Stage 1: Intent Ingestion | Agent classifies, human validates |
| [`RC-02`](../controls/rc/RC-02.yaml) | Design Approval | Stage 2: System Design | Human required |
| [`RC-05`](../controls/rc/RC-05.yaml) | Risk Threshold Evaluation | Stage 4: Testing & Documentation | Agent calculates, RO decides |
| [`RC-06`](../controls/rc/RC-06.yaml) | CAB Approval | Stage 5: Deployment & Release | Human required |
| [`RC-08`](../controls/rc/RC-08.yaml) | Risk & Health Monitoring | Stage 6: Observability & Maintenance | Automated with human escalation |
| [`RC-09`](../controls/rc/RC-09.yaml) | Third-Party Continuous Risk Monitoring | Stage 6: Observability & Maintenance | Fully automated |


### `SA`

| Control | Name | Stage | Delegation |
|---------|------|-------|------------|
| [`SC-03`](../controls/sc/SC-03.yaml) | Pre-Guardrails | Stage 1: Intent Ingestion | Fully automated |
| [`SC-04`](../controls/sc/SC-04.yaml) | Data Classification & Sensitivity Screening | Stage 1: Intent Ingestion | Agent classifies, SA reviews |
| [`SC-05`](../controls/sc/SC-05.yaml) | Threat Model Validation | Stage 2: System Design | Agent generates, SA validates |
| [`SC-06`](../controls/sc/SC-06.yaml) | Zero-Trust Architecture Validation | Stage 2: System Design | Fully automated |
| [`SC-07`](../controls/sc/SC-07.yaml) | Permission Management | Stage 3: Coding & Implementation | Fully automated |
| [`SC-08`](../controls/sc/SC-08.yaml) | Post-Guardrails | Stage 3: Coding & Implementation | Fully automated |
| [`SC-10`](../controls/sc/SC-10.yaml) | Software Composition Analysis & SBOM Generation | Stage 3: Coding & Implementation | Fully automated |
| [`SC-11`](../controls/sc/SC-11.yaml) | Container & IaC Security Scanning | Stage 3: Coding & Implementation | Fully automated |
| [`SC-12`](../controls/sc/SC-12.yaml) | SAST | Stage 4: Testing & Documentation | Fully automated |
| [`SC-13`](../controls/sc/SC-13.yaml) | DAST | Stage 4: Testing & Documentation | Fully automated |
| [`SC-14`](../controls/sc/SC-14.yaml) | API Security Testing | Stage 4: Testing & Documentation | Fully automated |
| [`SC-15`](../controls/sc/SC-15.yaml) | Adversarial AI Robustness Testing | Stage 4: Testing & Documentation | Fully automated |
| [`SC-16`](../controls/sc/SC-16.yaml) | Infrastructure Security | Stage 5: Deployment & Release | Fully automated |
| [`SC-18`](../controls/sc/SC-18.yaml) | Secrets & Key Management Lifecycle | Stage 5: Deployment & Release | Fully automated |
| [`SC-19`](../controls/sc/SC-19.yaml) | Incident Scanning & Detection | Stage 6: Observability & Maintenance | Automated with human escalation |
| [`SC-20`](../controls/sc/SC-20.yaml) | Runtime Anomaly Detection | Stage 6: Observability & Maintenance | Automated with human escalation |


---

**Last Updated:** 2026-03-13 12:43 UTC
