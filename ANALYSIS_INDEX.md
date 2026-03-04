# A-SDLC Regulatory Gap Analysis — Complete Index

**Analysis Date:** 2026-03-04  
**Framework:** A-SDLC (Agentic Software Development Life Cycle)  
**Regulatory Scope:** DORA (EU 2022/2554) + EU AI Act (EU 2024/1689)  
**Total Deliverables:** 4 documents, 92 KB of comprehensive analysis

---

## Quick Navigation

### For Different Audiences

**Executive Summary (5 min read)**
→ Start with [GAP_ANALYSIS_README.md](./GAP_ANALYSIS_README.md) — Overview section

**Key Findings (15 min read)**
→ Read [REGULATORY_COVERAGE_MATRIX.md](./REGULATORY_COVERAGE_MATRIX.md) — All tables

**Detailed Recommendations (30 min read)**
→ Review [GAP_ANALYSIS_SUMMARY.md](./GAP_ANALYSIS_SUMMARY.md) — Full analysis

**Machine-Readable Data (Integration)**
→ Import [gap-analysis-output.json](./gap-analysis-output.json) — JSON structure

---

## Deliverable Descriptions

### 1. GAP_ANALYSIS_README.md (14 KB)
**Purpose:** Entry point and orientation guide for the complete analysis  
**Audience:** Everyone (executives, architects, compliance teams)  
**Content:**
- Overview of DORA and EU AI Act
- Key findings summary
- Critical gaps identified
- Implementation roadmap (3 phases)
- How to use the deliverables
- Control summary by track

**Time to Read:** 10-15 minutes  
**Use For:** Onboarding, stakeholder communication, decision-making

---

### 2. REGULATORY_COVERAGE_MATRIX.md (14 KB)
**Purpose:** Quick-reference matrix tables for rapid assessment  
**Audience:** Compliance officers, architects, planning teams  
**Content:**
- DORA coverage table (11 articles, status, % coverage)
- EU AI Act coverage table (14 articles, status, % coverage)
- Coverage by control track (SC, QC, RC, AC, GC)
- Critical gaps requiring immediate implementation
- Regulatory timeline compliance gaps (CRITICAL finding)
- Control mapping tables (Article → Control)
- Implementation priority matrix
- Compliance readiness by use case
- Timeline for regulatory compliance

**Time to Read:** 15-20 minutes  
**Use For:** Planning, status reporting, compliance audits, board presentations

---

### 3. GAP_ANALYSIS_SUMMARY.md (26 KB)
**Purpose:** Comprehensive detailed analysis with full context  
**Audience:** Architects, compliance teams, framework designers  
**Content:**

**Part 1: DORA Analysis (11 articles)**
- 1 well-covered article
- 2 partially-covered articles
- 6 poorly-covered articles
- 2 NOT-covered articles (CRITICAL)
- For each: requirement, current coverage, gap details, rationale, recommendations

**Part 2: EU AI Act Analysis (14 articles + 2 annexes)**
- 1 well-covered article
- 2 partially-covered articles
- 5 poorly-covered articles
- 6 NOT-covered articles (CRITICAL)
- Same structure as DORA analysis

**Part 3: Cross-Framework Findings**
- Incident reporting timeline gaps (DORA Art. 19, AI Act Art. 73)
- Legally mandated timelines (4h/72h/1m and 15/10/2 days)
- Regulatory risk assessment

**Part 4: Feedback Loops Analysis**
- Path A coverage (expedited remediation)
- Path B coverage (full lifecycle)
- Strengths and weaknesses
- Enhancement recommendations

**Part 5: Control Track Assessment**
- SC (Security) — 45% coverage
- QC (Quality) — 35% coverage
- RC (Risk) — 32% coverage
- AC (AI) — 42% coverage
- GC (Governance) — 38% coverage

**Part 6: Remediation Roadmap**
- Phase 1 (3-6 months): Critical gaps
- Phase 2 (6-12 months): High-priority enhancements
- Phase 3 (12-18 months): Optimization

**Time to Read:** 45-60 minutes  
**Use For:** Detailed gap analysis, control design, remediation planning

---

### 4. gap-analysis-output.json (32 KB)
**Purpose:** Machine-readable structured data for integration  
**Audience:** Developers, automation systems, compliance tracking tools  
**Content:**
```json
{
  "metadata": { ... },
  "dora_analysis": {
    "well_covered": [...],     // 90% coverage
    "partially_covered": [...], // 66% coverage
    "poorly_covered": [...],    // 33% coverage
    "not_covered": [...]        // 0% coverage
  },
  "eu_ai_act_analysis": { ... },
  "feedback_loop_gaps": {
    "covered": [...],
    "uncovered": [...]
  },
  "summary": {
    "dora_coverage_percent": 38,
    "eu_ai_act_coverage_percent": 28,
    "critical_gaps": [...]
  }
}
```

**Fields per Gap:**
- article: "Art. XX"
- title: Article title
- requirement: Abbreviated requirement text
- controls: List of mapped controls
- coverage_percentage: Estimated coverage (0, 33, 66, or 90)
- rationale: Why this coverage level was assigned
- gaps: Specific missing elements

**Time to Process:** Integration-dependent  
**Use For:** Spreadsheet imports, dashboard population, compliance tracking, automated reporting

---

## Key Findings Overview

### Critical Statistics

| Metric | Value | Status |
|--------|-------|--------|
| **Total Articles Analyzed** | 25 | — |
| **Total Controls Analyzed** | 39 | — |
| **DORA Coverage** | 38% | MODERATE-HIGH RISK |
| **EU AI Act Coverage** | 28% | HIGH RISK |
| **Combined Coverage** | 33% | HIGH RISK |

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

### CRITICAL Regulatory Timeline Gap

Both DORA and EU AI Act require **legally mandated incident reporting with specific timelines**:

**DORA Art. 19:**
- Initial: 4 hours
- Intermediate: 72 hours
- Final: 1 month
- Status: ❌ NOT CONTROLLED

**EU AI Act Art. 73:**
- Normal: 15 days
- Death: 10 days
- Widespread: 2 days
- Status: ❌ NOT CONTROLLED

---

## Implementation Roadmap at a Glance

### Phase 1: CRITICAL (3-6 months)
**Create 6 new controls:**
1. SC-7A: Incident Reporting (DORA Art. 19)
2. RC-7A/7B/7C: Business Continuity (DORA Art. 11)
3. AC-3A: Data Governance (AI Act Art. 10)
4. AC-5A: AI Robustness Testing (AI Act Art. 15)
5. AC-5B: Technical Documentation (AI Act Art. 11)
6. GC-4A: Quality Management System (AI Act Art. 17)

**Expected Result:** 60% DORA, 45% AI Act coverage

### Phase 2: HIGH-PRIORITY (6-12 months)
**Enhance 5+ controls for partial coverage gaps**
- Governance, incident management, testing, third-party risk
- Additional AI-specific controls

**Expected Result:** 75% DORA, 65% AI Act coverage

### Phase 3: OPTIMIZATION (12-18 months)
**Complete remaining gaps and integration**

**Expected Result:** 90% DORA, 85% AI Act coverage

---

## Files Reference

| File | Size | Type | Purpose |
|------|------|------|---------|
| **GAP_ANALYSIS_README.md** | 14 KB | Markdown | Navigation & overview |
| **REGULATORY_COVERAGE_MATRIX.md** | 14 KB | Markdown | Quick reference tables |
| **GAP_ANALYSIS_SUMMARY.md** | 26 KB | Markdown | Detailed analysis |
| **gap-analysis-output.json** | 32 KB | JSON | Machine-readable data |
| **ANALYSIS_INDEX.md** | This file | Markdown | Index & navigation |

**Total:** 92 KB of comprehensive analysis

---

## How to Use This Analysis

### Step 1: Orient Yourself
1. Read [GAP_ANALYSIS_README.md](./GAP_ANALYSIS_README.md) overview
2. Scan [REGULATORY_COVERAGE_MATRIX.md](./REGULATORY_COVERAGE_MATRIX.md) tables
3. Note the critical gaps and timelines

### Step 2: Select Your Path

**Path A: Executive/Compliance Decision-Making**
1. Review key findings summary in README
2. Study critical gaps table in MATRIX
3. Review compliance readiness assessment
4. Use implementation roadmap for planning

**Path B: Technical Implementation**
1. Review detailed gap analysis in SUMMARY
2. Study control track assessment
3. Review remediation roadmap
4. Export JSON for integration

**Path C: Detailed Research**
1. Read full GAP_ANALYSIS_SUMMARY.md
2. Study specific article analysis (DORA and AI Act sections)
3. Review control-to-article mapping in MATRIX
4. Cross-reference with [/regulatory/sources.yaml](./regulatory/sources.yaml) for full text

### Step 3: Take Action

**Immediate (Next 30 days):**
- Share analysis with compliance team
- Prioritize SC-7A (incident reporting)
- Schedule design review for Phase 1 controls

**Short-term (3-6 months):**
- Implement Phase 1 critical controls
- Update feedback-loops.yaml with regulatory triggers
- Achieve 60% DORA, 45% AI Act coverage

**Medium-term (6-12 months):**
- Implement Phase 2 enhancements
- Achieve 75% DORA, 65% AI Act coverage

**Long-term (12-18 months):**
- Complete Phase 3
- Achieve 90%+ coverage
- Prepare for regulatory audit

---

## Supporting Documents Reference

These documents are referenced but not included in deliverables:

- **[/regulatory/sources.yaml](./regulatory/sources.yaml)** — Full text of all DORA and EU AI Act articles analyzed (source of truth)
- **[/controls/**/*.yaml](./controls/)** — All 39 control definitions (analyzed for regulatory mappings)
- **[/feedbackloops/feedback-loops.yaml](./feedbackloops/feedback-loops.yaml)** — Feedback loop definitions (analyzed for regulatory alignment)
- **[/asdlc.yaml](./asdlc.yaml)** — A-SDLC framework manifest

---

## Questions & Clarifications

### What does "coverage percentage" mean?
- **0% (NOT COVERED):** No controls address this requirement
- **33% (POORLY COVERED):** Only 1-2 controls address the requirement; significant gaps remain
- **66% (PARTIALLY COVERED):** 2-3 controls address the requirement; some gaps remain
- **90% (WELL COVERED):** Multiple controls (3+) comprehensively address the requirement

### What are "critical gaps"?
Requirements with **0% coverage** (no controls mapped) or requirements with **legally mandated timelines** that lack automation.

### What is the remediation timeline?
- **Phase 1 (CRITICAL):** 3-6 months — Address NOT COVERED articles
- **Phase 2 (HIGH):** 6-12 months — Enhance POORLY COVERED articles
- **Phase 3 (OPTIMIZATION):** 12-18 months — Complete integration and optimization

### Is the framework compliant today?
- **DORA:** ⚠️ 38% coverage — MODERATE-HIGH RISK (non-compliance on critical articles)
- **EU AI Act:** ❌ 28% coverage — HIGH RISK (multiple critical gaps)
- **Recommendation:** Implement Phase 1 before regulated deployment

### How do I integrate this analysis?
1. Import `gap-analysis-output.json` into compliance tracking systems
2. Reference tables in `REGULATORY_COVERAGE_MATRIX.md` for dashboards
3. Use detailed analysis from `GAP_ANALYSIS_SUMMARY.md` for planning
4. Share README with stakeholders

---

## Next Steps

1. **Share:** Distribute to governance, compliance, and architecture teams
2. **Discuss:** Review findings in team meetings
3. **Prioritize:** Identify Phase 1 control implementation owners
4. **Plan:** Create project plan for remediation roadmap
5. **Track:** Monitor progress against implementation timeline

---

**Analysis Date:** 2026-03-04  
**Analyzed By:** A-SDLC Gap Analysis Framework  
**Data Sources:** DORA (EU 2022/2554), EU AI Act (EU 2024/1689), A-SDLC controls and processes  
**Confidence Level:** HIGH (comprehensive control-to-requirement mapping)  
**Last Updated:** 2026-03-04  
**Version:** 1.0
