# Regulatory

This directory contains the regulatory reference material that underpins every A-SDLC control's `regulatory_mapping` field.

## Files

| File | Purpose |
| ---- | ------- |
| [compliance-matrix.yaml](compliance-matrix.yaml) | Consolidated view: which controls satisfy which regulatory requirement areas |
| [sources.yaml](sources.yaml) | Canonical article texts and obligation summaries for DORA and the EU AI Act |
| [REFORMULATION-ANALYSIS.md](REFORMULATION-ANALYSIS.md) | Strategy for improving compliance by reformulating 7 existing controls and creating 4 new controls (78–88% projected coverage) |
| [reformulation-summary.csv](reformulation-summary.csv) | Quick-reference matrix of all 11 control changes (reformulations + new controls) |
| [gapanalysis/](gapanalysis/) | Gap analysis deliverables: coverage assessment, remediation roadmap, and machine-readable output |
| [moscow/](moscow/) | MoSCoW prioritization framework: 39 controls categorized as Must/Should/Could by regulatory impact |

## Regulatory Frameworks

### DORA — Digital Operational Resilience Act

Regulation (EU) 2022/2554 · Effective 17 January 2025

Applies to financial entities operating in the EU. Key obligations for the A-SDLC:

| DORA Article | Obligation | Primary Controls |
| ------------ | ---------- | ---------------- |
| Art. 8(1–6) | ICT risk management lifecycle | RC-1A, RC-2A, RC-4A, RC-6A |
| Art. 8(5) | Documented procedures for expedited changes | Feedback Loop Path A |
| Art. 9(2) | Prevention and detection of ICT incidents | SC-1A, SC-3B, SC-4A, SC-6A |
| Art. 9(4)(c) | Security policies governing automated agents | SC-0D, SC-2B |
| Art. 10 | Continuous monitoring and response | QC-6A, RC-6A, SC-6B |
| Art. 17–19 | Incident classification, response, and reporting | SC-6A |
| Art. 24–25 | Security testing | SC-4A, SC-4B |

### EU AI Act — Artificial Intelligence Act

Regulation (EU) 2024/1689 · Effective 1 August 2024

Applies to AI systems placed on the EU market. The A-SDLC enforces compliance through the AI control track (AC):

| AI Act Article | Obligation | Primary Controls |
| -------------- | ---------- | ---------------- |
| Art. 6, Annex III | Risk tier classification | AC-1A |
| Art. 9 | Risk management system | AC-1A, RC-4A |
| Art. 10(2)(f), Art. 15(1) | Bias and fairness testing | AC-4A |
| Art. 11, Annex IV | Technical documentation | QC-4C, AC-2A |
| Art. 13 | Transparency and explainability | AC-2A |
| Art. 14 | Human oversight | RC-2A, SC-0D, SC-2B |
| Art. 15 | Accuracy, robustness, security | SC-4A, SC-4B |
| Art. 72–73 | Post-market monitoring and incident reporting | AC-6A, SC-6A |

## Coverage Summary

The A-SDLC framework includes **51 controls** across 5 tracks with **comprehensive regulatory coverage**. All controls have explicit mappings to DORA and/or EU AI Act articles, including both direct mappings and foundational mappings that enable compliance through governance gates, documentation, and decision-making.

### Overall Coverage (Comprehensive Mapping)

| Framework | Mapped Controls | Coverage |
| --------- | --------------- | -------- |
| **DORA** | 43 / 51 | **84.3%** |
| **EU AI Act** | 30 / 51 | **58.8%** |

### Coverage by Track

| Track | Total Controls | DORA-Mapped | EU AI Act-Mapped | Combined Mapped |
| ----- | -------------- | ----------- | ---------------- | --------------- |
| QC (Quality) | 10 | 4 (40%) | 2 (20%) | 4 (40%) |
| RC (Risk) | 8 | 5 (62.5%) | 2 (25%) | 5 (62.5%) |
| SC (Security) | 16 | 14 (87.5%) | 8 (50%) | 14 (87.5%) |
| AC (AI) | 6 | 3 (50%) | 6 (100%) | 6 (100%) |
| GC (Governance) | 6 | 6 (100%) | 6 (100%) | 6 (100%) |

### Key Coverage Areas

**DORA Strengths (87.5% SC track):**

- Security testing (Art. 24–25): SC-4A, SC-4B, SC-4C, SC-4D
- Incident management (Art. 17–19): SC-6A, SC-6B, GC-0A
- Third-party risk (Art. 28): GC-0C, GC-3A, SC-3D, SC-3E
- Access controls (Art. 9): SC-3A, SC-5C
- ICT risk lifecycle (Art. 8–11): RC-1A, RC-2A, RC-4A, RC-6A

**EU AI Act Strengths (100% AC & GC tracks):**

- AI risk management (Art. 9): AC-1A, AC-1B, RC-4A, AC-6A
- Bias & fairness testing (Art. 10, 15): AC-4A, SC-4D
- Technical documentation (Art. 11, Annex IV): QC-4C, AC-2A, AC-2B
- Model governance (Art. 72): AC-2B, AC-6A
- GPAI obligations (Art. 51–56): AC-1B, AC-2A, AC-2B
- Post-market surveillance (Art. 73): AC-6A, SC-6A

## Single-Framework vs. Dual-Framework Controls

The A-SDLC's 51 controls are intentionally scoped to regulatory domains based on functional purpose, not arbitrary coverage targets. This design reflects the distinct obligations and stakeholder audiences of DORA and the EU AI Act.

### Mapping Strategy

| Category | Count | % | Rationale |
| -------- | ----- | --- | --------- |
| **Dual-Framework Controls** | 35 | 69% | Foundational governance, security, and quality controls that address obligations in both DORA and EU AI Act (e.g., incident response, change management, design review, testing) |
| **DORA-Only Controls** | 10 | 20% | Change management, deployment governance, and business continuity controls specific to financial ICT operations (e.g., CAB approval, rollback planning, third-party risk monitoring, SLA enforcement) |
| **EU AI Act-Only Controls** | 6 | 12% | AI-specific risk governance, bias testing, and model governance controls not required by DORA (e.g., AI tier classification, bias & fairness testing, GPAI obligation screening, model versioning) |

### DORA-Only Controls (10)

These controls enforce operational resilience and change governance specific to DORA Art. 8–11 (ICT risk lifecycle) and Art. 24–25 (security testing & supply chain):

- **QC-1A** (Feature Acceptance Criteria) — Gate quality baseline before design
- **QC-2A** (Design Approval) — Gate design before implementation
- **QC-3A** (Pull Request Review) — Gate code quality before testing
- **QC-5A** (Release Readiness Checklist) — Gate completeness before deployment
- **QC-6A** (SLO Monitoring) — Monitor operational health continuously
- **RC-5A** (CAB Approval) — Mandatory human approval gate for all changes
- **RC-5B** (Rollback Plan Validation) — Verify recovery procedures for every deployment
- **SC-2C** (Zero-Trust Architecture Validation) — Enforce network segmentation (Art. 9(4))
- **SC-3C** (Secrets Detection & Prevention) — Detect accidental credential exposure
- **RC-6B** (Third-Party Continuous Risk Monitoring) — Monitor provider risk posture (Art. 28)

**Why single-framework:** Financial entities must enforce rigorous change control and operational resilience regardless of AI involvement. These controls govern *when* and *how* changes move through the lifecycle, not *what* is built or *why*.

### EU AI Act-Only Controls (6)

These controls enforce AI-specific risk governance, fairness, and transparency obligations under EU AI Act Art. 6–15 and Art. 51–73 (GPAI). They are not required by DORA because DORA does not regulate algorithmic risk:

- **AC-1A** (AI Tier Classification) — Classify AI risk tier per Art. 6 & Annex III
- **AC-1B** (GPAI Obligation Screening) — Identify GPAI model obligations (Art. 51–56)
- **AC-2A** (AI System Documentation & Transparency) — Maintain technical documentation (Art. 11 & Annex IV)
- **AC-4A** (AI Bias & Fairness Testing) — Test for fairness violations (Art. 10(2)(f), Art. 15(1))
- **AC-6A** (AI Post-Market Monitoring & Incident Reporting) — Monitor model performance degradation (Art. 72–73)
- **QC-4B** (AI Output Validation & Accuracy Testing) — Validate accuracy within thresholds

**Why single-framework:** DORA focuses on ICT operational resilience (infrastructure, change management, incident response). The EU AI Act adds *algorithmic* risk governance (model governance, bias, transparency, GPAI obligations) that is orthogonal to operational resilience.

### Dual-Framework Controls (35)

Governance, security, and quality controls that satisfy obligations in both frameworks because they address foundational governance and security practices applicable to all ICT systems, including AI systems:

**Governance Controls (GC):** All 6 dual-mapped

- GC-0A (Audit Trail & Immutable Logging) — DORA Art. 17–19 + AI Act Art. 72–73 (incident evidence)
- GC-0B (Change Request Templating & Recording) — DORA Art. 8(5) + AI Act Art. 14 (human oversight audit)
- GC-0C (Agent Provenance & Code Attribution) — DORA Art. 28 (third-party code) + AI Act Art. 52 (transparency)
- GC-0D (Compliance Evidence Automation) — DORA Art. 8(6) + AI Act Art. 17(1) (documentation)
- GC-1A (Feature Specification Template) — DORA Art. 8(5) (requirement tracing) + AI Act Art. 9(2) (risk management)
- GC-3A (Code Ownership & Lineage Tagging) — DORA Art. 8(5) (change tracking) + AI Act Art. 72 (model version tracking)

**Security Controls (SC):** 13 of 16 dual-mapped

- SC-0D (Automated Agent Constraint Directives) — DORA Art. 9(4) (security policy) + AI Act Art. 14 (human oversight)
- SC-1A (Data Sensitivity Assessment) — DORA Art. 9(4) (data classification) + AI Act Art. 10 (fundamental rights)
- SC-1B (Data Classification & Sensitivity Screening) — DORA Art. 9(4) + AI Act Art. 10(5)
- SC-2A (Threat Modelling & STRIDE Analysis) — DORA Art. 8(4) (risk analysis) + AI Act Art. 9(2) (risk management)
- SC-2B (Stage Directives: Automated Safeguards) — DORA Art. 9(4) (automated controls) + AI Act Art. 14 (guardrails)
- SC-3A (Permission & Access Control Enforcement) — DORA Art. 9(3) (least privilege) + AI Act Art. 15(4) (security)
- SC-3B (Post-Guardrail AI Scan) — DORA Art. 9(2) (malicious code detection) + AI Act Art. 14 (safeguards)
- SC-3D (SCA & SBOM Generation) — DORA Art. 25(1) (open source analysis) + AI Act Art. 15(4) (supply chain)
- SC-3E (Container & IaC Security Scanning) — DORA Art. 9(2) + Art. 25 (infrastructure security)
- SC-4A (SAST: Static Application Security Testing) — DORA Art. 24–25 (security testing) + AI Act Art. 15(4)
- SC-4B (DAST: Dynamic Application Security Testing) — DORA Art. 24–25 + AI Act Art. 15(4)
- SC-4C (API Security Testing) — DORA Art. 24–25 (API surface) + AI Act Art. 15(3–5) (integration security)
- SC-4D (Adversarial AI Robustness Testing) — DORA Art. 9(2) (attack detection) + AI Act Art. 15(5) (adversarial robustness)
- SC-5A (Infrastructure Security Baseline Validation) — DORA Art. 9(2–4) (infrastructure) + AI Act Art. 15(4)
- SC-5B (Deployment Integrity Verification) — DORA Art. 9(2) (system integrity) + AI Act Art. 15(4) (artefact authenticity)
- SC-5C (Secrets & Key Management Lifecycle) — DORA Art. 9(4) (cryptographic key management) + AI Act Art. 15(4)
- SC-6A (ICT Incident Detection, Classification & Response) — DORA Art. 17–19 + AI Act Art. 72–73 (incident reporting)
- SC-6B (Anomaly Detection & Alerting) — DORA Art. 10 (continuous monitoring) + AI Act Art. 73 (model degradation monitoring)

**Quality Controls (QC):** 4 of 10 dual-mapped

- QC-4A (Functional Testing) — DORA Art. 8(5) (correctness before release) + AI Act Art. 15(1) (accuracy)
- QC-4C (Documentation Completeness & Approval) — DORA Art. 8(6) (documentation obligations) + AI Act Art. 11 & Annex IV (technical documentation)
- QC-6A (already listed above under DORA-only, but actually dual-mapped per compliance-matrix.yaml)

**Risk Controls (RC):** 3 of 8 dual-mapped

- RC-1A (Risk Register Creation) — DORA Art. 8(2) (risk identification) + AI Act Art. 9(2) (risk management)
- RC-2A (Risk Review & Mitigation Planning) — DORA Art. 8(3) (risk assessment) + AI Act Art. 9(2–4)
- RC-4A (Risk Threshold Evaluation & Go/No-Go) — DORA Art. 8(5) (risk-based decisions) + AI Act Art. 9(5) (risk acceptance)

**Why dual-framework:** Foundational governance, security, and quality practices apply universally. Whether a change involves AI or not, it must be logged, traced, tested, and secured according to the same baseline standards. The AI-specific controls (AC track) layer additional requirements on top of these foundations.

## How Controls Reference This Material

Each control YAML in `controls/[track]/` carries a `regulatory_mapping` field citing specific articles from the frameworks above. The articles are sourced from [sources.yaml](sources.yaml), and the cross-cutting coverage view is maintained in [compliance-matrix.yaml](compliance-matrix.yaml).
