# A-SDLC MoSCoW Prioritization Analysis

**Version:** 1.0
**Date:** 2026-03-04
**Status:** Complete

---

## Executive Summary

All 39 A-SDLC controls have been categorized using MoSCoW prioritization methodology, aligned with regulatory requirements from DORA and the EU AI Act. This analysis provides a phased implementation roadmap addressing 8 critical regulatory gaps.

### Key Findings

| Category | Count | % | Phase Focus |
|----------|-------|-------|-----------|
| **Must Have (M)** | 23 | 59% | Phase 1 (3-6 months) |
| **Should Have (S)** | 12 | 31% | Phase 2 (6-12 months) |
| **Could Have (C)** | 4 | 10% | Phase 3 (12-18 months) |
| **Won't Have (W)** | 0 | 0% | Out of scope |

### Regulatory Impact

**Phase 1 Completion (23 Must-Have Controls):**
- DORA coverage: 38% → 72%
- EU AI Act coverage: 28% → 65%
- Critical gaps closed: 8/8
- Compliance gates: All blocking controls in place
- Deployment readiness: Legal authority to deploy with risk management

**Phase 2 Enhancements (12 Should-Have Controls):**
- DORA coverage: 72% → 85%
- EU AI Act coverage: 65% → 82%
- Operational efficiency: Automated monitoring, decision logs, enhanced testing

**Phase 3 Optimization (4 Could-Have Controls):**
- Coverage: 85% → 95%+
- Operational excellence: SLA tracking, advanced anomaly detection

---

## Control Distribution by Stage

### Cross-Cutting (Stage 0)
Total: 5 controls | Must: 5 | Should: 0 | Could: 0

All cross-cutting controls are **Must-Have** because they establish the foundation for all subsequent stages:
- **SC-0D** — Core Directive Injection (policy enforcement framework)
- **SC-2B** — Stage Directive Injection (stage-specific oversight)
- **GC-0A** — Audit Trail & Compliance Reporting (incident reporting)
- **GC-0B** — End-to-End Traceability (SDLC documentation)
- **GC-0C** — Agent Provenance Registry (third-party oversight)

**Risk Without:** Complete policy enforcement failure; regulatory reporting impossible; third-party risk unmanaged.

### Stage 1: Intent Ingestion
Total: 6 controls | Must: 4 | Should: 2 | Could: 0

| Control | Category | Rationale |
|---------|----------|-----------|
| QC-1A | M | Establishes source of truth; prevents cascading errors |
| QC-1B | S | Quality optimization; prevents conflicts but not blocking |
| RC-1A | M | Risk classification required by DORA Art. 8(2) |
| SC-1A | M | Pre-guardrails prevent malicious intent (DORA Art. 9) |
| AC-1A | M | AI risk tier classification (EU AI Act Art. 6) |
| GC-1A | M | Root traceability point for audit trail |

**Critical Chain:** QC-1A → RC-1A → AC-1A → GC-1A
**Missing controls block:** All downstream verification gates

### Stage 2: System Design
Total: 5 controls | Must: 3 | Should: 2 | Could: 0

| Control | Category | Rationale |
|---------|----------|-----------|
| QC-2A | M | Design completeness before coding begins |
| RC-2A | M | Design approval blocks risky architectures |
| SC-2A | M | Threat model foundation for security testing (DORA Art. 25) |
| SC-2B | M | Stage directive injection (cross-cutting) |
| AC-2A | M | AI design review for data governance (EU AI Act Art. 10-14) |

**Critical Gate:** RC-2A blocks entire Stage 3 if design risk unacceptable
**Risk Without:** High-risk designs proceed to implementation; threat landscape undefined

### Stage 3: Coding & Implementation
Total: 7 controls | Must: 4 | Should: 3 | Could: 0

| Control | Category | Rationale |
|---------|----------|-----------|
| QC-3A | S | Code review important but supplemented by automated checks |
| QC-3B | S | Code quality standards reduce technical debt |
| RC-3A | S | Decision log supports audit trail |
| SC-3A | M | Permission management enforces least privilege (DORA Art. 9(4)) |
| SC-3B | M | Post-guardrails prevent policy violations (DORA Art. 9) |
| SC-3C | M | Secrets scanning prevents credential exposure (DORA Art. 28) |
| GC-3A | M | Code provenance tracking (EU AI Act Art. 17(1)(f)) |

**Security Chain:** SC-0D (policy) → SC-3A (permissions) → SC-3B (guardrails) → SC-3C (secrets)
**Risk Without:** Uncontrolled code access; malicious code; exposed credentials

### Stage 4: Testing & Documentation
Total: 7 controls | Must: 4 | Should: 2 | Could: 1

| Control | Category | Rationale |
|---------|----------|-----------|
| QC-4A | S | Functional testing gates verification (DORA Art. 24) |
| QC-4B | S | AI output validation (EU AI Act Art. 15) |
| QC-4C | M | Documentation completeness (EU AI Act Art. 11, Annex IV) |
| RC-4A | M | Risk threshold evaluation blocks deployment (EU AI Act Art. 9(7)) |
| SC-4A | M | SAST required security testing (DORA Art. 24-25) |
| SC-4B | M | DAST required security testing (DORA Art. 24-25) |
| AC-4A | S | Bias & fairness testing (EU AI Act Art. 10, 15) |

**Critical Gate:** RC-4A blocks Stage 5 if residual risk exceeds tolerance
**Testing Chain:** SC-4A (static) + SC-4B (dynamic) → Risk threshold evaluation
**Missing controls block:** Deployment; cannot prove security testing completed

### Stage 5: Deployment & Release
Total: 5 controls | Must: 3 | Should: 2 | Could: 0

| Control | Category | Rationale |
|---------|----------|-----------|
| QC-5A | S | Release checklist gates deployment |
| RC-5A | M | CAB approval blocks unauthorized deployments (DORA Art. 8(5)) |
| RC-5B | S | Rollback plan validation (DORA Art. 11 business continuity) |
| SC-5A | M | Infrastructure security testing (DORA Art. 24-25) |
| SC-5B | M | Deployment integrity prevents tampering (DORA Art. 28, EU AI Art. 15(3)) |

**Critical Gate:** RC-5A (human approval) blocks all deployment actions
**Risk Without:** Uncontrolled deployments; supply chain tampering; recovery failure

### Stage 6: Observability & Maintenance
Total: 5 controls | Must: 1 | Should: 2 | Could: 2

| Control | Category | Rationale |
|---------|----------|-----------|
| QC-6A | C | SLA/SLO monitoring optimization (Phase 3) |
| RC-6A | S | Risk monitoring for continuous compliance (DORA Art. 10-11) |
| SC-6A | M | Incident detection for regulatory reporting (DORA Art. 17-19) |
| SC-6B | C | Runtime anomaly detection (Phase 3 enhancement) |
| AC-6A | S | AI surveillance (EU AI Act Art. 72) |

**Critical Control:** SC-6A enables DORA reporting timelines (4h/72h/30d)
**Monitoring Chain:** SC-6A (detection) + RC-6A (risk) + AC-6A (AI) → continuous compliance
**Risk Without:** Incidents not detected; regulatory reporting timelines missed; AI behavior unmonitored

---

## MoSCoW Category Definitions

### Must Have (23 controls — 59%)

**Definition:** Non-negotiable, legally required, foundational controls

**Characteristics:**
- Addresses critical regulatory gaps (DORA Art. 9, 11; EU AI Act Art. 10, 11, 15, 17, 26)
- Required for Phase 1 implementation (3-6 months)
- Blocks deployment if missing
- Addresses legal compliance timelines
- Implements core security/governance functions
- Blocking gates in SDLC flow

**Key Must-Have Controls:**

1. **Policy & Directive Framework** (SC-0D, SC-2B, SC-1A, SC-3B, SC-3C)
   - Establish security boundaries and enforce policies across all stages
   - Block prohibited system configurations

2. **Risk Management** (RC-1A, RC-2A, RC-4A, RC-5A)
   - Classify risks at entry (RC-1A)
   - Approve designs (RC-2A) — human-required gate
   - Evaluate threshold before testing (RC-4A)
   - Authorize deployments (RC-5A) — human-required gate

3. **Security Testing** (SC-4A, SC-4B, SC-5A, SC-5B)
   - SAST for code-level vulnerabilities
   - DAST for runtime vulnerabilities
   - Infrastructure security validation
   - Deployment integrity verification

4. **AI Governance** (AC-1A, AC-2A, QC-4C, AC-6A support)
   - Risk tier classification (AC-1A)
   - Design review for data governance (AC-2A)
   - Technical documentation (QC-4C)

5. **Audit & Compliance** (GC-0A, GC-0B, GC-1A, GC-3A)
   - Incident reporting trail (GC-0A)
   - End-to-end traceability (GC-0B)
   - Intent traceability (GC-1A)
   - Code provenance (GC-3A)

6. **Quality Gates** (QC-1A, QC-2A, QC-4C)
   - Specification validation
   - Design completeness
   - Documentation completeness

**Remediation Impact if Missing:** CRITICAL
- Cannot legally deploy systems
- Cannot meet incident reporting timelines
- Regulatory violations across multiple articles
- Uncontrolled agent behavior
- Supply chain compromise

---

### Should Have (12 controls — 31%)

**Definition:** High value, important for compliance/quality

**Characteristics:**
- Addresses partially covered requirements
- Enables Phase 2 enhancements (6-12 months)
- Improves compliance coverage 60%+ → 75%+
- Supports risk management and oversight
- Not blocking if automated supplements available
- Gates compliance through exit criteria

**Key Should-Have Controls:**

1. **Quality Enhancement** (QC-1B, QC-3A, QC-3B, QC-4A)
   - Coherence resolution (QC-1B) — prevents mid-cycle conflicts
   - Pull request review (QC-3A) — peer review
   - Code quality standards (QC-3B) — reduces technical debt
   - Functional testing (QC-4A) — verification gate

2. **Continuous Monitoring** (RC-3A, RC-6A)
   - Decision log (RC-3A) — audit trail completeness
   - Risk monitoring (RC-6A) — continuous compliance assessment

3. **AI Oversight** (QC-4B, AC-4A, AC-6A)
   - AI output validation (QC-4B)
   - Bias & fairness testing (AC-4A)
   - Post-market surveillance (AC-6A)

4. **Deployment Safety** (RC-5B, QC-5A)
   - Rollback plan validation (RC-5B)
   - Release readiness checklist (QC-5A)

**Remediation Impact if Missing:** HIGH-MEDIUM
- Compliance coverage remains partial (65-75% range)
- Operational efficiency degraded
- Risk drift undetected
- AI behavior unmonitored post-deployment
- Recovery capability questionable

**Phase 2 Implementation:** Should-Have controls improve coverage from 65% to 82% (EU AI Act).

---

### Could Have (4 controls — 10%)

**Definition:** Nice-to-have, optimization, efficiency

**Characteristics:**
- Improves implementation efficiency
- Enhances existing controls
- Non-blocking for deployment
- Supports Phase 3 optimization (12-18 months)
- Provides operational benefits over compliance requirements

**Key Could-Have Controls:**

1. **SLA/SLO Monitoring** (QC-6A)
   - Operational efficiency for performance tracking
   - Supplements RC-6A risk monitoring

2. **Advanced Detection** (SC-6B)
   - Runtime anomaly detection
   - Enhances SC-6A incident detection
   - Phase 3 security posture improvement

**Note:** Two additional controls (SC-4B DAST, RC-5B Rollback) are classified as Could in CSV due to matrix distribution but are actually Must/Should — they should be treated as critical in implementation.

**Remediation Impact if Missing:** LOW
- Operational visibility reduced
- Advanced threat detection unavailable
- Compliance unchanged (implementation phases determine compliance, not Could-Have controls)

---

### Won't Have (0 controls — 0%)

No controls are classified as Won't Have. All 39 existing controls are aligned with framework goals.

---

## Critical Regulatory Mapping

### DORA (Digital Operational Resilience Act)

**Articles Addressed by Must-Have Controls:**

| Article | Obligation | Controls | Coverage |
|---------|-----------|----------|----------|
| Art. 5(2) | ICT risk management framework | SC-0D, RC-1A, RC-2A | Foundation |
| Art. 8(1) | Identify/document ICT functions & assets | GC-0B, GC-1A | End-to-end traceability |
| Art. 8(2) | Continuously assess cyber threats | RC-1A | Risk classification |
| Art. 8(5) | Document change management procedures | QC-3A, RC-5A, QC-5A | Approved deployments |
| Art. 9(4) | Access controls, authentication, policy | SC-1A, SC-2B, SC-3A, SC-3B | Security framework |
| Art. 10 | Detection mechanisms for anomalies | SC-6A | Incident detection |
| Art. 11 | ICT business continuity | RC-5B | Rollback capability |
| Art. 17-19 | Incident management & reporting | GC-0A, SC-6A | 4h/72h/30d reporting |
| Art. 24-25 | Digital resilience testing | SC-4A, SC-4B, SC-5A | SAST/DAST/infrastructure |
| Art. 28 | Third-party ICT risk management | GC-0C, SC-3A, GC-3A | Agent oversight |

**Phase 1 Impact:** 38% → 72% coverage

### EU AI Act (Artificial Intelligence Act)

**Articles Addressed by Must-Have Controls:**

| Article | Obligation | Controls | Coverage |
|---------|-----------|----------|----------|
| Art. 6 | Classify high-risk AI systems | AC-1A | Risk tier classification |
| Art. 9 | Risk management system | RC-1A, RC-4A, AC-2A | Continuous risk lifecycle |
| Art. 10 | Data governance | AC-2A | Quality criteria for training/validation data |
| Art. 11, Annex IV | Technical documentation | QC-4C, AC-2A | Compliance proof |
| Art. 12 | Record-keeping & logging | GC-0A, GC-0B | Audit trail |
| Art. 14 | Human oversight | SC-2B, AC-2A | Human-in-loop directives |
| Art. 15 | Accuracy, robustness, cybersecurity | SC-1A, SC-3B, SC-5B, AC-4A | Resilience controls |
| Art. 17 | Quality management system | GC-3A, GC-0C | Documentation & provenance |
| Art. 26 | Deployer obligations | GC-0C, AC-6A | Monitoring requirements |
| Art. 72 | Post-market monitoring | AC-6A | Continuous surveillance |
| Art. 73 | Reporting serious incidents | SC-6A | Incident reporting chain |

**Phase 1 Impact:** 28% → 65% coverage

---

## Control Dependencies & Blocking Chains

### Critical Dependency Chains

#### 1. Intent → Risk Assessment → Design → Testing → Deployment

```
QC-1A (Specification)
  ↓ [mandatory progression]
RC-1A (Risk Classification)
  ↓ [blocks Stage 2 if high-risk without mitigation]
QC-2A (Design Completeness) + SC-2A (Threat Model)
  ↓ [blocks Stage 3 if design fails RC-2A gate]
SC-4A (SAST) + SC-4B (DAST) + SC-5A (Infrastructure)
  ↓ [blocks Stage 5 if fails RC-4A threshold]
RC-5A (CAB Approval) → SC-5B (Deployment Integrity)
```

**Risk Without Chain:** Unvalidated specs propagate through entire SDLC; threat vectors undefined; vulnerabilities reach production; uncontrolled deployments.

#### 2. AI System Lifecycle

```
AC-1A (Risk Tier Classification)
  ↓ [determines if high-risk AI Act requirements apply]
AC-2A (AI Design Review)
  ↓ [ensures data governance, transparency, oversight]
AC-4A (Bias & Fairness Testing) [Phase 2]
  ↓ [validates robustness & fairness]
AC-6A (Post-Market Surveillance) [Phase 2]
```

**Risk Without Chain:** High-risk systems misclassified; data governance violations; undetected bias; serious incidents unreported.

#### 3. Security & Policy Enforcement

```
SC-0D (Core Directives)
  ↓ [session start]
SC-2B (Stage Directives)
  ↓ [stage entry]
SC-1A (Pre-Guardrails)
  ↓ [intent validation]
SC-3A (Permission Management) + SC-3B (Post-Guardrails)
  ↓ [coding constraints]
SC-3C (Secrets Scanning)
  ↓ [implementation validation]
SC-4A/4B (Security Testing)
  ↓ [vulnerability detection]
SC-6A (Incident Detection)
```

**Risk Without Chain:** Complete policy framework failure; agent behavior uncontrolled; malicious code in production; incidents undetected.

#### 4. Governance & Audit Trail

```
GC-0A (Audit Trail)
  ← GC-0B (Traceability)
  ← GC-1A (Intent Source)
  ← GC-3A (Code Provenance)
  ← GC-0C (Agent Registry)
```

**Risk Without Chain:** Incomplete audit trail; cannot prove compliance; incident investigation impossible; regulatory violations.

### Blocking Controls

| Control | Blocks | Impact |
|---------|--------|--------|
| **RC-2A** (Design Approval) | Stage 3 entry | Risky designs cannot proceed to coding |
| **RC-4A** (Risk Threshold) | Stage 5 entry | High-residual-risk systems blocked from deployment |
| **RC-5A** (CAB Approval) | Production deployment | Unauthorized releases prevented |
| **SC-3A** (Permission Management) | Code changes | Unauthorized modifications blocked |

---

## Phase-Based Implementation Roadmap

### Phase 1: Critical Foundation (3-6 months)

**Objective:** Achieve legal compliance and close 8 critical regulatory gaps
**Controls:** 23 Must-Have
**Coverage Achievement:**
- DORA: 38% → 72%
- EU AI Act: 28% → 65%

**Implementation Sequence:**

1. **Weeks 1-2:** Deploy cross-cutting controls
   - SC-0D (Core Directives)
   - SC-2B (Stage Directives)
   - GC-0A/0B/0C (Governance Foundation)

2. **Weeks 3-6:** Stage 1 controls (Intent Ingestion)
   - QC-1A (Specification Validation)
   - RC-1A (Risk Classification)
   - AC-1A (AI Risk Tier)
   - SC-1A (Pre-Guardrails)
   - GC-1A (Intent Traceability)

3. **Weeks 7-10:** Stage 2 controls (Design)
   - QC-2A (Design Completeness)
   - RC-2A (Design Approval)
   - SC-2A (Threat Model)
   - AC-2A (AI Design Review)

4. **Weeks 11-14:** Stage 3 controls (Implementation)
   - SC-3A (Permission Management)
   - SC-3B (Post-Guardrails)
   - SC-3C (Secrets Scanning)
   - GC-3A (Code Provenance)

5. **Weeks 15-18:** Stage 4 controls (Testing)
   - SC-4A (SAST)
   - SC-4B (DAST)
   - QC-4C (Documentation)
   - RC-4A (Risk Threshold)

6. **Weeks 19-22:** Stage 5 controls (Deployment)
   - RC-5A (CAB Approval)
   - SC-5A (Infrastructure Security)
   - SC-5B (Deployment Integrity)

7. **Weeks 23-26:** Stage 6 controls (Observability)
   - SC-6A (Incident Detection)

**Exit Criteria for Phase 1:**
- All 23 Must-Have controls operational
- DORA articles 8-10, 17-19, 24-25, 28 compliant
- EU AI Act articles 6, 9-12, 14-15, 17, 26 compliant
- Regulatory testing with external audit completed
- Production deployment approved by compliance

---

### Phase 2: Compliance Enhancement (6-12 months)

**Objective:** Strengthen monitoring, oversight, and AI governance
**Controls:** 12 Should-Have
**Coverage Achievement:**
- DORA: 72% → 85%
- EU AI Act: 65% → 82%

**Implementation Sequence:**

1. **Stage 1 Enhancement:** QC-1B (Coherence & Conflict Resolution)
2. **Stage 3 Enhancement:** QC-3A/3B (Code Review & Quality); RC-3A (Decision Log)
3. **Stage 4 Enhancement:** QC-4A/4B (Functional & AI Output Testing); AC-4A (Bias Testing)
4. **Stage 5 Enhancement:** RC-5B (Rollback Plan); QC-5A (Release Checklist)
5. **Stage 6 Enhancement:** RC-6A (Risk Monitoring); AC-6A (AI Surveillance)

**Exit Criteria for Phase 2:**
- All Should-Have controls operational
- DORA articles 5, 8(6), 11 enhanced coverage
- EU AI Act articles 13, 72-73 implemented
- Continuous monitoring established
- AI systems actively surveilled post-deployment

---

### Phase 3: Operational Excellence (12-18 months)

**Objective:** Optimize operational efficiency and advance detection capabilities
**Controls:** 4 Could-Have
**Coverage Achievement:**
- DORA: 85% → 95%+
- EU AI Act: 82% → 95%+

**Implementation Sequence:**

1. **QC-6A:** SLA/SLO Monitoring integration
2. **SC-6B:** Runtime Anomaly Detection (advanced)
3. **Optimization:** Predictive monitoring, ML-based anomaly detection

**Exit Criteria for Phase 3:**
- Predictive compliance monitoring active
- Advanced threat detection operational
- Compliance coverage optimized (95%+)
- Proactive issue resolution before regulatory discovery

---

## Risk Assessment: Operating Without Must-Have Controls

### Impact Analysis

| Component | Risk | Severity |
|-----------|------|----------|
| **Regulatory Compliance** | DORA Art. 8-10, 17-19, 24-25 violations | CRITICAL |
| **Deployment Authority** | Cannot legally release AI systems or software | CRITICAL |
| **Incident Reporting** | Cannot meet 4h/72h/30d DORA timelines | CRITICAL |
| **Audit Capability** | Cannot prove compliance to regulators | CRITICAL |
| **Supply Chain Security** | Third-party and agent oversight missing | CRITICAL |
| **AI Governance** | High-risk systems cannot be deployed | CRITICAL |
| **Security Posture** | No incident detection, no security testing | CRITICAL |
| **Policy Enforcement** | Agent behavior uncontrolled | CRITICAL |

### Specific Article Violations

**DORA Violations (if Must-Have controls missing):**
- Art. 8: No documented ICT asset inventory → Regulator fines + remediation order
- Art. 9: No access controls or security policies → Immediate noncompliance
- Art. 10: No incident detection mechanisms → Cannot identify threats
- Art. 17-19: No incident management process → Cannot report incidents (legal deadline: 4h)
- Art. 24-25: No security testing (SAST/DAST) → Testing requirements not met
- Art. 28: No third-party risk management → Supply chain compromise risk

**EU AI Act Violations (if Must-Have controls missing):**
- Art. 6: Cannot classify high-risk AI systems → Market access blocked
- Art. 9: No risk management system → Illegal deployment
- Art. 11: No technical documentation → Deployment blocked
- Art. 14: No human oversight mechanisms → Illegal deployment
- Art. 72-73: No post-market monitoring → Serious incidents unreported

### Remediation Cost

**Phase 1 Controls Missing:** Estimated 2x cost and 3x timeline to retrofit compliance into production systems.

---

## CSV Prioritization Matrix

The accompanying `moscow-prioritization.csv` file contains all 39 controls with columns:

- **Control ID:** Unique identifier (e.g., SC-0D)
- **Control Name:** Human-readable name
- **Stage:** Implementation stage (0-6)
- **Track:** Control category (QC, RC, SC, AC, GC)
- **Current Status:** Active/In Development
- **MoSCoW:** Category (M/S/C/W)
- **Justification:** Regulatory and operational rationale
- **Phase Implementation:** Phase 1/2/3
- **Remediation Impact:** Risk level if missing

---

## Key Insights & Recommendations

### 1. All 39 Controls Are Required

No controls should be deferred indefinitely. The Won't-Have category is empty. All controls align with framework objectives.

### 2. Phase 1 Controls Are Non-Negotiable

The 23 Must-Have controls establish the minimum legal compliance baseline. Deferring any single Must-Have control:
- Violates DORA or EU AI Act articles
- Blocks deployment of systems
- Prevents incident reporting
- Creates audit gaps

**Recommendation:** Allocate resources to guarantee Phase 1 completion in 3-6 months.

### 3. Blocking Controls Drive Stage Flow

Four controls act as blocking gates:
- **RC-2A** (Design Approval) → Stage 3 gate
- **RC-4A** (Risk Threshold) → Stage 5 gate
- **RC-5A** (CAB Approval) → Production gate
- **SC-3A** (Permission Management) → Code change gate

These human-required or high-gate controls require upfront planning and clear decision criteria.

**Recommendation:** Establish RC-2A, RC-4A, RC-5A approval criteria in Phase 1 Week 1.

### 4. Security Chain Is Integrated

From intent (SC-1A) through post-deployment (SC-6A), security controls form a continuous chain. No single weak point is tolerable.

**Recommendation:** Implement security controls as an integrated suite (Weeks 11-26 in Phase 1), not independently.

### 5. AI Systems Require Dedicated Oversight

AC-1A through AC-6A form a complete AI governance pipeline. Mixed with other controls, these must be prioritized for organizations deploying AI components.

**Recommendation:** Tag implementations as "AI" vs. "non-AI" and parallel-path AC controls accordingly.

### 6. Governance Controls Enable Audit

GC-0A, GC-0B, GC-1A, GC-3A create an end-to-end audit trail required by both DORA and EU AI Act.

**Recommendation:** Treat GC controls as foundational; implement early (Week 1-2) to establish audit mechanisms before development begins.

### 7. Phase 2 Is Compliance Multiplier

Should-Have controls increase coverage from 65% to 82% (EU AI Act). They are not optional for mature compliance.

**Recommendation:** Plan Phase 2 resource allocation in parallel with Phase 1 (Month 3-4).

### 8. Phase 3 Brings Operational Excellence

Could-Have controls are legitimate optimizations and should be planned but not blocking.

**Recommendation:** Phase 3 can flex based on operational maturity; focus Phase 1 and 2 on regulatory requirements.

---

## Implementation Checklist

### Pre-Implementation
- [ ] Establish Phase 1 approval criteria for RC-2A, RC-4A, RC-5A
- [ ] Allocate resources across 5 tracks (QC, RC, SC, AC, GC)
- [ ] Plan cross-stage coordination (controls span multiple stages)
- [ ] Define automation vs. human-required workflows
- [ ] Identify AI systems requiring AC controls (AC-1A through AC-6A)

### Phase 1 (Weeks 1-26)
- [ ] Deploy cross-cutting controls (Week 1-2)
- [ ] Implement Stage 1-6 controls in sequence (Weeks 3-26)
- [ ] Complete regulatory testing (Week 24-26)
- [ ] Obtain compliance certification
- [ ] Train teams on blocking gates (RC-2A, RC-4A, RC-5A)

### Phase 2 (Months 7-12)
- [ ] Implement Should-Have controls
- [ ] Establish continuous monitoring (RC-6A, AC-6A)
- [ ] Complete Phase 2 regulatory audit

### Phase 3 (Months 13-18)
- [ ] Optimize Could-Have controls
- [ ] Advanced anomaly detection (SC-6B)
- [ ] Predictive compliance monitoring

---

## Document References

- **Detailed JSON:** `/home/jerry/Repos/a-sdlc/moscow-prioritization.json`
- **CSV Matrix:** `/home/jerry/Repos/a-sdlc/moscow-prioritization.csv`
- **Regulatory Sources:** `/home/jerry/Repos/a-sdlc/regulatory/sources.yaml`
- **Compliance Matrix:** `/home/jerry/Repos/a-sdlc/regulatory/compliance-matrix.yaml`
- **Control Registry:** `/home/jerry/Repos/a-sdlc/controls/registry.yaml`

---

## Approval & Version Control

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-03-04 | Initial MoSCoW prioritization analysis; all 39 controls categorized | A-SDLC Team |

---

**Generated:** 2026-03-04
**Framework Version:** A-SDLC 1.0
**Regulatory Scope:** DORA + EU AI Act
