# A-SDLC MoSCoW Quick Reference Guide

**Generated:** 2026-03-04 | **Framework:** A-SDLC 1.0 | **Scope:** DORA + EU AI Act

---

## At-a-Glance Categories

### Must-Have (23 controls — 59%)
Non-negotiable, legally required, foundational. Missing ANY control violates DORA or EU AI Act.

**Cross-Cutting (5):** SC-0D, SC-2B, GC-0A, GC-0B, GC-0C
**Stage 1 (4):** QC-1A, RC-1A, SC-1A, AC-1A, GC-1A
**Stage 2 (3):** QC-2A, RC-2A, SC-2A, AC-2A
**Stage 3 (4):** SC-3A, SC-3B, SC-3C, GC-3A
**Stage 4 (4):** SC-4A, SC-4B, QC-4C, RC-4A
**Stage 5 (3):** RC-5A, SC-5A, SC-5B
**Stage 6 (1):** SC-6A

### Should-Have (12 controls — 31%)
High value, important for compliance/quality. Gates through exit criteria or operational benefit.

**Stage 1 (1):** QC-1B
**Stage 2 (1):** [listed below]
**Stage 3 (2):** QC-3A, QC-3B, RC-3A
**Stage 4 (2):** QC-4A, QC-4B, AC-4A
**Stage 5 (2):** RC-5B, QC-5A
**Stage 6 (2):** RC-6A, AC-6A

### Could-Have (4 controls — 10%)
Nice-to-have, optimization, efficiency. Non-blocking for compliance.

**Stage 4 (1):** [Noted as enhancement]
**Stage 6 (2):** QC-6A, SC-6B

---

## Critical Blocking Controls (Stage Gates)

| Control | Blocks | Decision | Approval Path |
|---------|--------|----------|---------------|
| **RC-2A** | Stage 3 entry | Design risk acceptable? | Risk Management (human-required) |
| **RC-4A** | Stage 5 entry | Residual risk below threshold? | Risk Management + Stakeholders |
| **RC-5A** | Production deploy | Release authorized? | Change Advisory Board (human-required) |
| **SC-3A** | Code changes | Permission granted? | Automated policy enforcement |

---

## Phase Implementation Timeline

### Phase 1: Critical Foundation (3-6 months)
**Goal:** Achieve legal compliance; close 8 critical regulatory gaps
**Coverage:** DORA 38%→72%, EU AI Act 28%→65%
**Controls:** All 23 Must-Have

```
Weeks 1-2:    Cross-Cutting (5)
Weeks 3-6:    Stage 1 (6)
Weeks 7-10:   Stage 2 (5)
Weeks 11-14:  Stage 3 (7)
Weeks 15-18:  Stage 4 (7)
Weeks 19-22:  Stage 5 (5)
Weeks 23-26:  Stage 6 (5)
```

### Phase 2: Compliance Enhancement (6-12 months)
**Goal:** Strengthen monitoring, AI oversight
**Coverage:** DORA 72%→85%, EU AI Act 65%→82%
**Controls:** All 12 Should-Have

### Phase 3: Operational Excellence (12-18 months)
**Goal:** Optimize efficiency, advanced detection
**Coverage:** DORA 85%→95%+, EU AI Act 82%→95%+
**Controls:** All 4 Could-Have

---

## Regulatory Articles & Control Mapping

### DORA (Digital Operational Resilience Act)

**Art. 5(2):** ICT risk framework → SC-0D, RC-1A, RC-2A
**Art. 8(1):** Document ICT assets → GC-0B, GC-1A
**Art. 8(2):** Assess cyber threats → RC-1A
**Art. 8(5):** Change management procedures → QC-3A, RC-5A, QC-5A
**Art. 9(4):** Access controls, security policies → SC-1A, SC-2B, SC-3A, SC-3B
**Art. 10:** Detect anomalies → SC-6A
**Art. 11:** Business continuity → RC-5B
**Art. 17-19:** Incident management & reporting → GC-0A, SC-6A
**Art. 24-25:** Security testing (SAST/DAST) → SC-4A, SC-4B, SC-5A
**Art. 28:** Third-party risk management → GC-0C, SC-3A, GC-3A

### EU AI Act (Artificial Intelligence Act)

**Art. 6:** High-risk AI classification → AC-1A
**Art. 9:** Risk management system → RC-1A, RC-4A, AC-2A
**Art. 10:** Data governance → AC-2A
**Art. 11, Annex IV:** Technical documentation → QC-4C, AC-2A
**Art. 12:** Record-keeping & logging → GC-0A, GC-0B
**Art. 14:** Human oversight → SC-2B, AC-2A
**Art. 15:** Accuracy, robustness, cybersecurity → SC-1A, SC-3B, SC-5B, AC-4A
**Art. 17:** Quality management system → GC-3A, GC-0C
**Art. 26:** Deployer obligations → GC-0C, AC-6A
**Art. 72:** Post-market monitoring → AC-6A
**Art. 73:** Reporting serious incidents → SC-6A

---

## Control Dependencies

### Critical Chains (Execution Order)

**Intent Flow Chain**
```
QC-1A (Spec Validation)
  → RC-1A (Risk Classification)
  → QC-2A (Design Completeness)
  → SC-2A (Threat Model)
  → SC-4A/4B (Security Testing)
  → RC-4A (Risk Threshold)
  → RC-5A (CAB Approval)
  → SC-6A (Incident Detection)
```

**AI System Chain**
```
AC-1A (Risk Tier) → AC-2A (Design Review) → AC-4A (Bias Testing) → AC-6A (Surveillance)
```

**Security Enforcement Chain**
```
SC-0D (Directives) → SC-2B (Stage Directives) → SC-1A (Pre-Guardrails)
  → SC-3A (Permissions) → SC-3B (Post-Guardrails) → SC-3C (Secrets)
  → SC-4A/4B (Testing) → SC-6A (Incident Detection)
```

**Governance & Audit Chain**
```
GC-0A (Audit Trail) ← GC-0B (Traceability) ← GC-1A (Intent Source)
  ← GC-3A (Code Provenance) ← GC-0C (Agent Registry)
```

---

## Risk Profile: Missing Must-Have Controls

| Dimension | If Missing | Severity |
|-----------|-----------|----------|
| **Legal** | DORA/EU AI Act violation; fines, remediation orders | CRITICAL |
| **Deployment** | Cannot legally release systems | CRITICAL |
| **Incidents** | Cannot meet 4h/72h/30d reporting timelines | CRITICAL |
| **Audit** | Cannot prove compliance to regulators | CRITICAL |
| **Security** | No incident detection, testing, or access control | CRITICAL |
| **Supply Chain** | Third-party/agent oversight missing | CRITICAL |
| **AI Systems** | High-risk AI deployment blocked; serious incidents undetected | CRITICAL |

---

## Control Track Distribution

| Track | Name | Total | M | S | C |
|-------|------|-------|---|---|---|
| **QC** | Quality Controls | 10 | 4 | 5 | 1 |
| **RC** | Risk Controls | 7 | 4 | 2 | 1 |
| **SC** | Security Controls | 13 | 8 | 2 | 3 |
| **AC** | AI Controls | 4 | 2 | 2 | 0 |
| **GC** | Governance Controls | 5 | 5 | 1 | 0 |
| **TOTAL** | | **39** | **23** | **12** | **4** |

---

## Key Decisions & Approval Criteria

### RC-2A (Design Approval) Decision
**Approval Required:** Risk Management Lead + Architecture Lead
**Criteria:** Design threat model complete? Data governance plan clear? Human oversight mechanisms defined?
**Blocks:** Stage 3 implementation start

### RC-4A (Risk Threshold Evaluation) Decision
**Approval Required:** Risk Management + Business Stakeholders
**Criteria:** All identified risks have mitigation? Residual risk within tolerance? Security testing complete?
**Blocks:** Stage 5 deployment approval

### RC-5A (CAB Approval) Decision
**Approval Required:** Change Advisory Board (human-required)
**Criteria:** Release checklist complete? Rollback plan validated? Deployment integrity verified?
**Blocks:** Production deployment execution

---

## Implementation Checklist

### Pre-Implementation (Week 0)
- [ ] Review all 39 control definitions in `/controls/[track]/` directory
- [ ] Establish approval criteria for RC-2A, RC-4A, RC-5A
- [ ] Assign control owners from each track (QC, RC, SC, AC, GC)
- [ ] Identify AI systems requiring AC controls

### Phase 1 Weeks 1-2 (Cross-Cutting)
- [ ] Deploy SC-0D (Core Directives)
- [ ] Deploy SC-2B (Stage Directives)
- [ ] Establish GC-0A (Audit Trail)
- [ ] Establish GC-0B (Traceability)
- [ ] Deploy GC-0C (Agent Provenance Registry)

### Phase 1 Weeks 3-26 (Stages 1-6)
- [ ] Implement Stage 1 controls (Intent Ingestion)
- [ ] Implement Stage 2 controls (Design)
- [ ] Implement Stage 3 controls (Implementation)
- [ ] Implement Stage 4 controls (Testing)
- [ ] Implement Stage 5 controls (Deployment)
- [ ] Implement Stage 6 controls (Observability)

### Phase 1 Completion (Week 26)
- [ ] All 23 Must-Have controls operational
- [ ] Regulatory testing completed
- [ ] External compliance audit passed
- [ ] Teams trained on blocking gates

---

## Files & References

| File | Purpose | Location |
|------|---------|----------|
| **moscow-prioritization.json** | Detailed JSON with all 39 controls, dependencies, phases | `/home/jerry/Repos/a-sdlc/moscow-prioritization.json` |
| **moscow-prioritization.csv** | 39-row spreadsheet for sorting/filtering | `/home/jerry/Repos/a-sdlc/moscow-prioritization.csv` |
| **MOSCOW-PRIORITIZATION-README.md** | Comprehensive 7,000+ word guide | `/home/jerry/Repos/a-sdlc/MOSCOW-PRIORITIZATION-README.md` |
| **MOSCOW-QUICK-REFERENCE.md** | This file (quick lookup) | `/home/jerry/Repos/a-sdlc/MOSCOW-QUICK-REFERENCE.md` |
| **asdlc.yaml** | Full framework manifest | `/home/jerry/Repos/a-sdlc/asdlc.yaml` |
| **compliance-matrix.yaml** | DORA/EU AI Act article mapping | `/home/jerry/Repos/a-sdlc/regulatory/compliance-matrix.yaml` |
| **controls/registry.yaml** | Flat index of all 39 controls | `/home/jerry/Repos/a-sdlc/controls/registry.yaml` |

---

## Quick Lookup by Control ID

**SC-0D** (M) Core Directives
**SC-1A** (M) Pre-Guardrails
**SC-2A** (M) Threat Model Validation
**SC-2B** (M) Stage Directives
**SC-3A** (M) Permission Management
**SC-3B** (M) Post-Guardrails
**SC-3C** (M) Secrets Scanning
**SC-4A** (M) SAST
**SC-4B** (M) DAST
**SC-5A** (M) Infrastructure Security
**SC-5B** (M) Deployment Integrity
**SC-6A** (M) Incident Detection
**SC-6B** (C) Runtime Anomaly Detection

**QC-1A** (M) Specification Validation
**QC-1B** (S) Coherence Resolution
**QC-2A** (M) Design Completeness
**QC-3A** (S) Pull Request Review
**QC-3B** (S) Code Quality Standards
**QC-4A** (S) Functional Testing
**QC-4B** (S) AI Output Validation
**QC-4C** (M) Documentation Completeness
**QC-5A** (S) Release Readiness Checklist
**QC-6A** (C) SLA/SLO Monitoring

**RC-1A** (M) Risk Classification
**RC-2A** (M) Design Approval [GATE]
**RC-3A** (S) Decision Log
**RC-4A** (M) Risk Threshold [GATE]
**RC-5A** (M) CAB Approval [GATE]
**RC-5B** (S) Rollback Plan Validation
**RC-6A** (S) Risk & Health Monitoring

**AC-1A** (M) AI Risk Tier Classification
**AC-2A** (M) AI Design Review
**AC-4A** (S) Bias & Fairness Testing
**AC-6A** (S) AI Post-Market Surveillance

**GC-0A** (M) Audit Trail
**GC-0B** (M) End-to-End Traceability
**GC-0C** (M) Agent Provenance Registry
**GC-1A** (M) Intent Traceability
**GC-3A** (M) Code Provenance Tracking

**Legend:** (M)=Must-Have, (S)=Should-Have, (C)=Could-Have, [GATE]=Blocking control

---

**Generated:** 2026-03-04 | **Version:** 1.0 | **Framework:** A-SDLC 1.0
