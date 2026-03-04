# A-SDLC Regulatory Gap Analysis — Complete Deliverables

**Analysis Date:** 2026-03-04  
**Analyzed Frameworks:** DORA (Regulation EU 2022/2554) and EU AI Act (Regulation EU 2024/1689)  
**Total Controls Analyzed:** 39  
**Total Regulatory Requirements Analyzed:** 25 articles/annexes

---

## Overview

This comprehensive gap analysis evaluates how well the A-SDLC framework controls address regulatory requirements from two critical EU regulations:

1. **DORA (Digital Operational Resilience Act)** — Effective January 17, 2025
   - Applies to: Financial entities, payment institutions, investment firms, insurance companies, pension funds, and ICT service providers
   - Focus: ICT risk management, testing, incident reporting, third-party risk

2. **EU AI Act (Artificial Intelligence Act)** — Effective August 1, 2024
   - Applies to: AI system providers, deployers, importers, distributors
   - Focus: High-risk AI systems, data governance, quality management, post-market monitoring

## Key Findings

### Overall Coverage
- **DORA:** 38% coverage (9 of 11 articles with some controls; 2 critical gaps)
- **EU AI Act:** 28% coverage (8 of 14 articles with some controls; 6 critical gaps)
- **Combined:** 33% coverage

### Critical Gaps (NOT COVERED - 0%)
**DORA:**
- Art. 9: Protection and prevention
- Art. 11: Response and recovery

**EU AI Act:**
- Art. 10: Data and data governance
- Art. 11: Technical documentation
- Art. 15: Accuracy, robustness and cybersecurity
- Art. 17: Quality management system
- Art. 26: Obligations of deployers

### High-Priority Gaps (POORLY COVERED - 33%)
**DORA:**
- Art. 5: Governance and organisation
- Art. 17-19: Incident management and reporting (including legally mandated timelines)
- Art. 25: Testing of systems
- Art. 28: Third-party risk management

**EU AI Act:**
- Art. 6: Classification rules
- Art. 13: Transparency and information
- Art. 14: Human oversight
- Art. 72: Post-market monitoring
- Art. 73: Serious incident reporting
- Annex III: High-risk AI systems
- Annex IV: Technical documentation elements

---

## Deliverables

### 1. **gap-analysis-output.json** (32 KB)
Machine-readable JSON output with complete gap analysis structure:
- Article-by-article coverage assessment
- Control-to-requirement mapping
- Coverage percentages (0%, 33%, 66%, 90%)
- Specific gap descriptions
- Critical gaps summary with recommendations
- Feedback loop analysis

**Usage:** Import into spreadsheets, dashboards, or compliance tracking systems.

**Structure:**
```json
{
  "metadata": { ... },
  "dora_analysis": {
    "well_covered": [...],
    "partially_covered": [...],
    "poorly_covered": [...],
    "not_covered": [...]
  },
  "eu_ai_act_analysis": { ... },
  "feedback_loop_gaps": { ... },
  "summary": {
    "dora_coverage_percent": 38,
    "eu_ai_act_coverage_percent": 28,
    "critical_gaps": [...]
  }
}
```

### 2. **REGULATORY_COVERAGE_MATRIX.md** (15 KB)
Quick-reference matrix tables for rapid assessment:
- Coverage summary tables (DORA and EU AI Act)
- Article-by-control mapping
- Control track coverage breakdown (SC, QC, RC, AC, GC)
- Critical control gaps requiring immediate implementation
- Regulatory timeline compliance gaps
- Control mapping (Article → Control)
- Implementation priority matrix
- Compliance risk assessment by use case
- Timeline for regulatory compliance

**Usage:** Present to stakeholders, planning, compliance audits, board reporting.

**Key Sections:**
- Coverage by article (status, controls, percentage, priority)
- Coverage by control track (strengths, gaps)
- Missing controls (NOT COVERED - 0%)
- Partially covered articles (enhancement needs)
- Regulatory timeline compliance gaps (CRITICAL - both frameworks)

### 3. **GAP_ANALYSIS_SUMMARY.md** (26 KB)
Comprehensive detailed report with full context:

**Sections:**
1. **Executive Summary** — High-level findings and status
2. **DORA Analysis** — Article-by-article breakdown with:
   - Coverage status
   - Current control mapping
   - Detailed gap analysis
   - Impact assessment
   - Specific recommendations
3. **EU AI Act Analysis** — Complete article coverage with same structure
4. **Cross-Framework Findings** — Including critical incident reporting timeline gaps
5. **Feedback Loops Analysis** — Strengths, weaknesses, enhancement recommendations
6. **Control Track Coverage** — Assessment of each control track (SC, QC, RC, AC, GC)
7. **Remediation Roadmap** — Phased implementation plan
8. **Summary Table** — All gaps by severity

**Usage:** Management review, detailed gap remediation planning, regulatory compliance documentation.

---

## Critical Findings Summary

### Immediate Action Required (Phase 1 - 3-6 months)

**DORA Gaps:**
| Article | Gap | Control Needed | Impact |
|---------|-----|----------------|--------|
| Art. 9 | NO protection/prevention policy | SC-9A: ICT Security Policy Framework | Core security obligation unmapped |
| Art. 11 | NO business continuity | RC-7A/7B/7C: Business Continuity Controls | Critical operational resilience gap |
| Art. 19 | NO regulatory reporting timelines | SC-7A: Incident Reporting Workflow | **LEGAL COMPLIANCE RISK** |

**EU AI Act Gaps:**
| Article | Gap | Control Needed | Impact |
|---------|-----|----------------|--------|
| Art. 10 | NO data governance | AC-3A: Data Governance Framework | Foundation for AI compliance missing |
| Art. 11 | NO Annex IV documentation | AC-5B: Technical Documentation Control | Pre-market requirement blocker |
| Art. 15 | NO accuracy/robustness testing | AC-5A: AI Robustness Testing | AI safety requirement missing |
| Art. 17 | NO unified QMS | GC-4A: AI Quality Management System | Comprehensive oversight gap |
| Art. 26 | NO deployer obligations | GC-5A: Deployer Obligations Control | Deployer responsibility unaddressed |

### Regulatory Timeline Compliance Gaps (CRITICAL)

Both DORA and EU AI Act impose **legally mandated incident reporting timelines** with **NO automated controls**:

**DORA Art. 19:**
- Initial notification: 4 hours from classification
- Intermediate: 72 hours from initial
- Final: 1 month from intermediate
- Current state: ❌ NOT CONTROLLED (SC-6A detects but doesn't report)

**EU AI Act Art. 73:**
- Normal serious incidents: 15 days
- If death involved: 10 days
- Widespread infringements: 2 days
- Current state: ❌ NOT CONTROLLED (AC-6A detects but doesn't report)

**Recommendation:** Create **SC-7A: Incident Reporting and Regulatory Notification** with automated timeline tracking.

---

## Compliance Readiness Assessment

### By Use Case

| Scenario | DORA Ready | AI Act Ready | Recommendation |
|----------|-----------|--------------|-----------------|
| Non-AI financial system | ⚠️ 38% | N/A | Implement Phase 1 before production |
| AI system for regulated sector | ⚠️ 38% | ❌ 28% | **DO NOT DEPLOY** until critical gaps closed |
| Non-AI consumer system | ✅ Adequate | N/A | Framework sufficient |
| AI system for consumers | ⚠️ 38% | ❌ 28% | Implement Art. 10, 11, 15, 17 controls |

### Regulatory Risk Level

- **DORA Compliance:** MODERATE-HIGH RISK (2 critical gaps on core obligations)
- **EU AI Act Compliance:** HIGH RISK (6 critical gaps, 5+ high-priority gaps)
- **Overall Assessment:** Framework provides good foundation but **significant remediation required** before regulated deployment

---

## Implementation Roadmap

### Phase 1: CRITICAL (3-6 months) — Address Legally Mandated Gaps

**Create New Controls:**
1. **SC-7A**: Incident Reporting and Regulatory Notification
   - Automate DORA Art. 19 timelines (4h/72h/1 month)
   - Automate EU AI Act Art. 73 timelines (15/10/2 days)
   - Include authority notification and client communication

2. **RC-7A**: ICT Business Continuity Policy and Planning
   - Address DORA Art. 11 fundamental gap
   - Include BIA, RTO/RPO, critical function identification

3. **AC-3A**: Data Governance and Quality Management
   - Address EU AI Act Art. 10 foundation gap
   - Include data quality criteria, bias assessment, preparation procedures

4. **AC-5A**: AI Model Accuracy, Robustness, and Adversarial Resilience
   - Address EU AI Act Art. 15 safety gap
   - Include accuracy metrics, robustness testing, adversarial attack simulation

5. **AC-5B** or enhance **QC-4C**: AI Act Technical Documentation
   - Address EU AI Act Art. 11 and Annex IV
   - Explicit mapping to all Annex IV elements

6. **GC-4A**: Quality Management System for High-Risk AI
   - Address EU AI Act Art. 17 comprehensive QMS requirement
   - Consolidate scattered QMS elements

**Expected Result:** Increase coverage to ~60% DORA, ~45% EU AI Act

### Phase 2: HIGH-PRIORITY (6-12 months) — Enhance Partial Coverage

- Enhance Art. 5 (governance) with management body accountability
- Enhance Art. 17-18 (incident management) with root cause analysis
- Enhance Art. 25 (testing) with open source and physical security testing
- Enhance Art. 28 (third-party) with vendor management
- Create additional AI-specific controls for deployer obligations, transparency

**Expected Result:** Increase coverage to ~75% DORA, ~65% EU AI Act

### Phase 3: OPTIMIZATION (12-18 months) — Integration & Audit Readiness

- Complete remaining gap controls
- Implement regulatory timeline automation across incident reporting
- Create cross-functional controls for third-party coordination
- Add regulatory reporting artifacts to control outputs
- Prepare for regulatory audit

**Expected Result:** Achieve ~90% DORA, ~85% EU AI Act coverage

---

## How to Use These Deliverables

### For Executives & Compliance Officers
1. Start with **REGULATORY_COVERAGE_MATRIX.md** — Quick overview and status
2. Review **Executive Summary** in **GAP_ANALYSIS_SUMMARY.md** — Understand risks
3. Use **Implementation Priority Matrix** to plan remediation timeline
4. Present **Compliance Risk Assessment by Use Case** to stakeholders

### For Framework Architects & Developers
1. Review **gap-analysis-output.json** for machine-readable mapping
2. Study **Control Track Coverage** in **GAP_ANALYSIS_SUMMARY.md**
3. Use **Detailed Gap Analysis** for specific control enhancement needs
4. Implement **Phase 1 Critical Controls** first
5. Reference **Remediation Roadmap** for sequencing

### For Regulatory & Audit Teams
1. Use **gap-analysis-output.json** for compliance tracking
2. Reference **Critical Gaps Summary Table** for audit prep
3. Track implementation against **Implementation Roadmap**
4. Use **Regulatory Timeline Compliance Gaps** for incident response procedures
5. Update feedback-loops.yaml with findings

### For Project Planning
1. Review **Implementation Priority Matrix** for timeline
2. Assess Phase 1 (3-6 months) effort for CRITICAL gaps
3. Plan Phase 2 (6-12 months) enhancement work
4. Schedule Phase 3 (12-18 months) optimization

---

## Key Recommendations

### Immediate Actions (Next 30 days)
1. ✅ Review this gap analysis with compliance and architecture teams
2. ✅ Prioritize **SC-7A: Incident Reporting** (addresses legally mandated timelines)
3. ✅ Begin design of **RC-7A: Business Continuity** (DORA Art. 11)
4. ✅ Start **AC-3A: Data Governance** design (AI Act Art. 10)
5. ✅ Update feedback-loops.yaml with regulatory incident triggers

### 3-6 Month Milestones
- ✅ Implement Phase 1 critical controls
- ✅ Achieve ~60% DORA, ~45% EU AI Act coverage
- ✅ Establish automated incident reporting workflows
- ✅ Enable deployment in regulated financial environments (with caveats)

### Longer-term (12-18 months)
- ✅ Complete Phase 2 & 3 enhancements
- ✅ Achieve ~90% coverage of both frameworks
- ✅ Pass regulatory audit
- ✅ Establish framework as industry best practice

---

## Appendix: Control Summary

### Controls Well-Aligned with Regulatory Requirements
- **SC-6A/6B**: Incident detection and monitoring (DORA Art. 10, 17-19)
- **SC-4A/4B**: Security testing (DORA Art. 24-25)
- **GC-0A/0B/3A**: Record-keeping and traceability (DORA Art. 8, AI Act Art. 12)
- **AC-4A**: Bias and fairness testing (AI Act Art. 10, 15)
- **RC-4A**: Risk threshold evaluation (AI Act Art. 9)

### Controls Requiring Enhancement
- **RC-5A**: Add governance framework and management body accountability
- **QC-4C**: Enhance for AI Act technical documentation (Annex IV)
- **AC-1A**: Add explicit Annex III category mapping
- **AC-2A**: Add instructions for use and deployer documentation

### Controls Missing Entirely (NOT COVERED)
- Business continuity and recovery planning (Art. 11)
- Comprehensive protection policies (Art. 9)
- Data governance framework (AI Act Art. 10)
- Unified quality management system (AI Act Art. 17)
- Deployer obligations (AI Act Art. 26)
- Regulatory incident reporting workflow (Art. 19, 73)

---

## Questions or Clarifications?

For detailed information on any gap:
1. **Machine-readable:** See `gap-analysis-output.json` for structured data
2. **Quick reference:** See `REGULATORY_COVERAGE_MATRIX.md` for tables and status
3. **Detailed analysis:** See `GAP_ANALYSIS_SUMMARY.md` for comprehensive explanations
4. **Source materials:** See `/regulatory/sources.yaml` for full article text

---

**Analysis Tool:** Python gap analysis script with YAML parsing
**Data Sources:**
- `/regulatory/sources.yaml` — DORA and EU AI Act article definitions
- `/controls/**/*.yaml` — All 39 control definitions with regulatory mappings
- `/feedbackloops/feedback-loops.yaml` — Feedback loop process definitions
- `/asdlc.yaml` — Framework manifest

**Next Steps:**
1. Share with governance and compliance teams
2. Prioritize Phase 1 control implementation
3. Update A-SDLC README with compliance status
4. Schedule regulatory gap remediation work
