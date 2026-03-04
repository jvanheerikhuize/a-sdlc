# A-SDLC Regulatory Coverage Matrix

## Quick Reference: DORA and EU AI Act Article Coverage

**Analysis Date:** 2026-03-04
**Overall Framework Coverage:** 33% (Combined DORA + EU AI Act)

---

## DORA Coverage Summary

| Article | Title | Status | Controls | Coverage % | Priority |
|---------|-------|--------|----------|-----------|----------|
| **Art. 5** | Governance and organisation | POORLY_COVERED | RC-5A | 33% | HIGH |
| **Art. 8** | Identification | PARTIALLY_COVERED | RC-1A, GC-0B | 66% | MEDIUM |
| **Art. 9** | Protection and prevention | **NOT_COVERED** | — | **0%** | **CRITICAL** |
| **Art. 10** | Detection | WELL_COVERED | SC-6A, SC-6B, QC-6A, RC-6A | 90% | LOW |
| **Art. 11** | Response and recovery | **NOT_COVERED** | — | **0%** | **CRITICAL** |
| **Art. 17** | ICT-related incident management | POORLY_COVERED | SC-6A | 33% | HIGH |
| **Art. 18** | Classification of incidents | POORLY_COVERED | SC-6A | 33% | HIGH |
| **Art. 19** | Reporting of major incidents | POORLY_COVERED | SC-6A, GC-0A | 33% | **CRITICAL** |
| **Art. 24** | Digital resilience testing | PARTIALLY_COVERED | SC-4A, SC-4B, SC-5A | 66% | MEDIUM |
| **Art. 25** | Testing of systems | POORLY_COVERED | SC-4B | 33% | HIGH |
| **Art. 28** | Third-party risk management | POORLY_COVERED | GC-0C, SC-3A, SC-5B | 33% | HIGH |

**DORA Overall: 38% Coverage** (9/11 articles with some coverage; 2 critical gaps)

---

## EU AI Act Coverage Summary

| Article | Title | Status | Controls | Coverage % | Priority |
|---------|-------|--------|----------|-----------|----------|
| **Art. 6** | Classification rules | POORLY_COVERED | AC-1A | 33% | HIGH |
| **Art. 9** | Risk management system | PARTIALLY_COVERED | AC-1A, RC-4A, AC-6A | 66% | MEDIUM |
| **Art. 10** | Data and data governance | **NOT_COVERED** | — | **0%** | **CRITICAL** |
| **Art. 11** | Technical documentation | **NOT_COVERED** | — | **0%** | **CRITICAL** |
| **Art. 12** | Record-keeping | WELL_COVERED | GC-0A, GC-0B, GC-1A, GC-3A | 90% | LOW |
| **Art. 13** | Transparency and information | POORLY_COVERED | AC-2A | 33% | HIGH |
| **Art. 14** | Human oversight | POORLY_COVERED | AC-2A, SC-2B | 33% | HIGH |
| **Art. 15** | Accuracy, robustness, cybersecurity | **NOT_COVERED** | — | **0%** | **CRITICAL** |
| **Art. 17** | Quality management system | **NOT_COVERED** | — | **0%** | **CRITICAL** |
| **Art. 26** | Deployer obligations | **NOT_COVERED** | — | **0%** | **CRITICAL** |
| **Art. 72** | Post-market monitoring | POORLY_COVERED | AC-6A | 33% | HIGH |
| **Art. 73** | Reporting serious incidents | PARTIALLY_COVERED | AC-6A, SC-6A | 66% | MEDIUM |
| **Annex III** | High-risk AI systems | POORLY_COVERED | AC-1A | 33% | HIGH |
| **Annex IV** | Technical documentation elements | **NOT_COVERED** | — | **0%** | **CRITICAL** |

**EU AI Act Overall: 28% Coverage** (8/14 articles with some coverage; 6 critical gaps)

---

## Coverage by Control Track

### SC (Security Controls) — 45% Coverage
**13 Controls:** SC-0D, SC-1A, SC-2A, SC-2B, SC-3A, SC-3B, SC-3C, SC-4A, SC-4B, SC-5A, SC-5B, SC-6A, SC-6B

**Well-Mapped Articles:**
- DORA Art. 10 (Detection)
- DORA Art. 24-25 (Testing)
- AIACT Art. 15 (partial: cybersecurity component)

**Major Gaps:**
- DORA Art. 9 (Protection and prevention) — CRITICAL
- DORA Art. 19 (Regulatory reporting timelines) — CRITICAL

---

### QC (Quality Controls) — 35% Coverage
**10 Controls:** QC-1A, QC-1B, QC-2A, QC-3A, QC-3B, QC-4A, QC-4B, QC-4C, QC-5A, QC-6A

**Well-Mapped Articles:**
- DORA Art. 8 (Identification)
- DORA Art. 10 (Detection)

**Major Gaps:**
- DORA Art. 11 (Business continuity) — CRITICAL
- AIACT Art. 10 (Data governance) — CRITICAL
- AIACT Art. 11 (Technical documentation) — CRITICAL

---

### RC (Risk Controls) — 32% Coverage
**7 Controls:** RC-1A, RC-2A, RC-3A, RC-4A, RC-5A, RC-5B, RC-6A

**Well-Mapped Articles:**
- DORA Art. 10 (Detection)
- AIACT Art. 9 (Risk management)

**Major Gaps:**
- DORA Art. 5 (Governance) — HIGH
- DORA Art. 11 (Recovery) — CRITICAL
- AIACT Art. 17 (Quality management system) — CRITICAL

---

### AC (AI Controls) — 42% Coverage
**4 Controls:** AC-1A, AC-2A, AC-4A, AC-6A

**Well-Mapped Articles:**
- AIACT Art. 12 (Record-keeping)
- AIACT Art. 73 (Incident reporting) — partial

**Major Gaps:**
- AIACT Art. 10 (Data governance) — CRITICAL
- AIACT Art. 15 (Accuracy/robustness) — CRITICAL
- AIACT Art. 26 (Deployer obligations) — CRITICAL

---

### GC (Governance Controls) — 38% Coverage
**5 Controls:** GC-0A, GC-0B, GC-0C, GC-1A, GC-3A

**Well-Mapped Articles:**
- AIACT Art. 12 (Record-keeping)
- DORA Art. 8 (Identification)

**Major Gaps:**
- DORA Art. 5 (Management body accountability) — HIGH
- AIACT Art. 17 (Quality management system) — CRITICAL

---

## Critical Control Gaps Requiring Immediate Implementation

### Missing Controls (NOT COVERED - 0%)

| ID | Framework | Article | Title | Recommendation |
|----|-----------|---------|-------|-----------------|
| DORA-001 | DORA | Art. 9 | Protection and prevention | Create **SC-9A: ICT Security Policy Framework** |
| DORA-002 | DORA | Art. 11 | Response and recovery | Create **RC-7A: Business Continuity Planning** |
| DORA-003 | DORA | Art. 19 | Regulatory incident reporting | Create **SC-7A: Incident Reporting Workflow** |
| AIACT-001 | EU AI Act | Art. 10 | Data governance | Create **AC-3A: Data Governance Framework** |
| AIACT-002 | EU AI Act | Art. 11 | Technical documentation | Create **AC-5B: AI Act Documentation Control** |
| AIACT-003 | EU AI Act | Art. 15 | Accuracy/robustness | Create **AC-5A: AI Robustness Testing** |
| AIACT-004 | EU AI Act | Art. 17 | Quality management | Create **GC-4A: AI Quality Management System** |
| AIACT-005 | EU AI Act | Art. 26 | Deployer obligations | Create **GC-5A: Deployer Obligations** |

---

## Regulatory Timeline Compliance Gaps

Both DORA and EU AI Act impose **legally mandated reporting timelines** that are currently NOT controlled:

### DORA Art. 19: Incident Reporting Timelines

| Notification | Timeline | Current Control |
|--------------|----------|-----------------|
| **Initial Notification** | 4 hours from classification as major | ❌ Not automated |
| **Intermediate Notification** | 72 hours from initial notification | ❌ Not tracked |
| **Final Notification** | 1 month from intermediate report | ❌ Not tracked |
| **Client Notification** | Without undue delay | ❌ No procedure |

**Gap:** SC-6A detects incidents but does not automate DORA reporting timelines.

### EU AI Act Art. 73: Serious Incident Reporting

| Scenario | Timeline | Current Control |
|----------|----------|-----------------|
| **Normal Reporting** | 15 days of awareness | ❌ Not automated |
| **If Death Involved** | 10 days of awareness | ❌ Not automated |
| **Widespread Infringements** | 2 days | ❌ Not automated |

**Gap:** AC-6A and SC-6A detect incidents but lack automated timeline tracking.

**Recommendation:** Create **SC-7A: Incident Reporting and Regulatory Notification** with:
- Automated incident classification triggering regulatory reporting
- Timeline tracking dashboards (4h, 72h, 1m for DORA; 15/10/2 days for AI Act)
- Authority notification workflow
- Client notification procedures
- Escalation authority assignment and SLA tracking

---

## Partially Covered Articles Requiring Enhancement

### DORA Articles

| Article | Current Controls | Coverage | Enhancement Needed |
|---------|------------------|----------|-------------------|
| Art. 5 | RC-5A | 33% | Add: Management body training, risk appetite definition, board reporting |
| Art. 8 | RC-1A, GC-0B | 66% | Add: Asset inventory, vulnerability scanning, change impact analysis |
| Art. 17 | SC-6A | 33% | Add: Root cause analysis, corrective action tracking, post-incident review |
| Art. 18 | SC-6A | 33% | Add: DORA taxonomy automation, impact criteria assessment |
| Art. 24 | SC-4A, SC-4B, SC-5A | 66% | Add: Test independence verification, penetration testing, trend analysis |
| Art. 25 | SC-4B | 33% | Add: Open source analysis (SBOM), network testing, scenario-based testing |
| Art. 28 | GC-0C, SC-3A, SC-5B | 33% | Add: Vendor register, due diligence, exit strategy, concentration risk |

### EU AI Act Articles

| Article | Current Controls | Coverage | Enhancement Needed |
|---------|------------------|----------|-------------------|
| Art. 6 | AC-1A | 33% | Add: Annex III category mapping, product harmonisation assessment |
| Art. 9 | AC-1A, RC-4A, AC-6A | 66% | Add: Iterative risk process, foreseeable misuse scenarios |
| Art. 13 | AC-2A | 33% | Add: Instructions for use documentation, deployer communication |
| Art. 14 | AC-2A, SC-2B | 33% | Add: Human oversight role definition, competency requirements |
| Art. 72 | AC-6A | 33% | Add: Monitoring plan documentation, metric definition, trend analysis |
| Art. 73 | AC-6A, SC-6A | 66% | Add: AI-specific incident classification, timeline automation |

---

## Control Mapping: Article → Control

### DORA Coverage Map

```
Art. 5  Governance                 → RC-5A
Art. 8  Identification             → RC-1A, GC-0B
Art. 9  Protection & Prevention    → ❌ NOT COVERED
Art. 10 Detection                  → SC-6A, SC-6B, QC-6A, RC-6A
Art. 11 Response & Recovery        → ❌ NOT COVERED
Art. 17 Incident Management        → SC-6A
Art. 18 Incident Classification    → SC-6A
Art. 19 Incident Reporting         → SC-6A, GC-0A (insufficient)
Art. 24 Resilience Testing         → SC-4A, SC-4B, SC-5A
Art. 25 Testing Tools & Systems    → SC-4B
Art. 28 Third-Party Risk           → GC-0C, SC-3A, SC-5B
```

### EU AI Act Coverage Map

```
Art. 6   Classification             → AC-1A
Art. 9   Risk Management            → AC-1A, RC-4A, AC-6A
Art. 10  Data Governance            → ❌ NOT COVERED
Art. 11  Technical Documentation    → ❌ NOT COVERED
Art. 12  Record-keeping             → GC-0A, GC-0B, GC-1A, GC-3A
Art. 13  Transparency               → AC-2A
Art. 14  Human Oversight            → AC-2A, SC-2B
Art. 15  Accuracy/Robustness        → ❌ NOT COVERED
Art. 17  Quality Management         → ❌ NOT COVERED
Art. 26  Deployer Obligations       → ❌ NOT COVERED
Art. 72  Post-Market Monitoring     → AC-6A
Art. 73  Serious Incident Reporting → AC-6A, SC-6A
Ann. III High-Risk Categories       → AC-1A
Ann. IV  Documentation Elements     → ❌ NOT COVERED
```

---

## Implementation Priority Matrix

### Quadrant 1: CRITICAL & HIGH EFFORT (Do First)
- **DORA Art. 11**: Business continuity (requires 2-3 new controls: RC-7A, RC-7B, RC-7C)
- **AIACT Art. 17**: Quality management system (requires unified GC control: GC-4A)

### Quadrant 2: CRITICAL & LOW EFFORT (Do Immediately)
- **DORA Art. 9**: Protection/prevention (map existing SC controls explicitly)
- **DORA Art. 19**: Regulatory reporting (create SC-7A with timeline automation)
- **AIACT Art. 10**: Data governance (create AC-3A)
- **AIACT Art. 15**: Accuracy/robustness (create AC-5A)

### Quadrant 3: HIGH PRIORITY & LOW EFFORT (Do Soon)
- **DORA Art. 5**: Governance (enhance RC-5A)
- **DORA Art. 17-18**: Incident management (enhance SC-6A)
- **DORA Art. 25**: Testing (enhance SC-4B)
- **DORA Art. 28**: Third-party (enhance GC-0C)
- **AIACT Art. 6, 13, 14**: Classification/transparency/oversight (enhance AC controls)

### Quadrant 4: MEDIUM PRIORITY & MEDIUM EFFORT (Plan Ahead)
- **DORA Art. 8**: Identification (enhance RC-1A, GC-0B)
- **DORA Art. 24**: Testing requirements (enhance SC-4A, SC-4B, SC-5A)
- **AIACT Art. 11**: Technical documentation (create/enhance AC-5B)
- **AIACT Art. 26**: Deployer obligations (create GC-5A)

---

## Compliance Risk Assessment

### Regulatory Framework Status

| Framework | Coverage | Risk Level | Assessment |
|-----------|----------|-----------|-----------|
| **DORA** | 38% | MODERATE-HIGH | 2 critical gaps (Art. 9, 11); 5 high-priority gaps |
| **EU AI Act** | 28% | HIGH | 6 critical gaps; 5 high-priority gaps |
| **Combined** | 33% | HIGH | Multiple critical gaps; significant implementation needed |

### Compliance Readiness by Use Case

| Use Case | DORA Ready? | AI Act Ready? | Recommendation |
|----------|-----------|--------------|-----------------|
| **Non-AI systems in regulated financial sector** | ⚠️ Partial | N/A | Implement Phase 1 controls before production deployment |
| **AI systems for financial sector** | ⚠️ Partial | ❌ No | **DO NOT DEPLOY** until critical AI Act gaps resolved |
| **Non-AI systems in non-regulated sector** | ⚠️ Partial | N/A | Framework provides good governance foundation |
| **AI systems for consumer applications** | ⚠️ Partial | ⚠️ Partial | Implement Art. 10, 11, 15, 17 controls minimum |

### Timeline for Regulatory Compliance

**Current State:** Framework provides foundational controls; **NOT compliant** with DORA or EU AI Act without gap remediation.

**3-6 Month Timeline (Critical Phase):**
- Implement SC-7A, RC-7A, AC-3A, AC-5A, AC-5B, GC-4A
- Update feedback loops with regulatory triggers
- Achieve ~60% DORA, ~45% AI Act coverage

**6-12 Month Timeline (Enhancement Phase):**
- Implement high-priority enhancements (Art. 5, 17-18, 25, 28, etc.)
- Add missing deployability controls
- Achieve ~75% DORA, ~65% AI Act coverage

**12-18 Month Timeline (Optimization Phase):**
- Complete remaining gap controls
- Achieve ~90% DORA, ~85% AI Act coverage
- Ready for regulatory audit

---

## References

- **DORA:** Regulation (EU) 2022/2554 — https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng
- **EU AI Act:** Regulation (EU) 2024/1689 — https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- **A-SDLC Regulatory Sources:** `/regulatory/sources.yaml`
- **Detailed Gap Analysis:** `/gap-analysis-output.json`
- **Full Summary Report:** `/GAP_ANALYSIS_SUMMARY.md`
