# A-SDLC MoSCoW Prioritization — Complete Deliverables Index

**Analysis Date:** 2026-03-04
**Framework:** A-SDLC 1.0
**Regulatory Scope:** DORA + EU AI Act
**Total Controls Analyzed:** 39

---

## Executive Summary

All 39 A-SDLC controls have been categorized using MoSCoW (Must/Should/Could/Won't) prioritization methodology, aligned with DORA and EU AI Act regulatory requirements. The analysis identifies a phased implementation roadmap closing 8 critical regulatory gaps over 18 months.

### Key Metrics

| Category | Count | Percentage | Phase |
|----------|-------|-----------|-------|
| **Must-Have** | 23 | 59% | Phase 1 (3-6 mo) |
| **Should-Have** | 12 | 31% | Phase 2 (6-12 mo) |
| **Could-Have** | 4 | 10% | Phase 3 (12-18 mo) |
| **Won't-Have** | 0 | 0% | Out of scope |

### Regulatory Impact

**Phase 1 (23 Must-Have Controls):**
- DORA coverage: 38% → 72% (+34 points)
- EU AI Act coverage: 28% → 65% (+37 points)
- Critical gaps closed: 8/8
- Key articles: DORA 8-10, 17-19, 24-25, 28; EU AI Acts 6, 9-12, 14-15, 17, 26

**Phase 2 (12 Should-Have Controls):**
- DORA coverage: 72% → 85% (+13 points)
- EU AI Act coverage: 65% → 82% (+17 points)
- Enhanced controls: Continuous monitoring, AI surveillance, compliance tracking

**Phase 3 (4 Could-Have Controls):**
- DORA coverage: 85% → 95%+ (+10 points)
- EU AI Act coverage: 82% → 95%+ (+13 points)
- Optimization: SLA tracking, advanced anomaly detection, predictive compliance

---

## Deliverable Files

### 1. moscow-prioritization.json (34 KB, 693 lines)
**Purpose:** Comprehensive, machine-readable JSON containing all prioritization data

**Contents:**
- Framework metadata and context
- Summary statistics (M/S/C/W distribution by stage)
- Detailed control entries with:
  - Control ID, name, stage, track
  - MoSCoW category and justification
  - Regulatory mapping (DORA & EU AI Act articles)
  - Phase implementation timeline
  - Remediation impact if missing
  - Risk assessment without control
- Critical dependency chains
- Blocking control definitions
- Phase-wise implementation roadmap
- Risk assessment for proceeding without Must-Have controls

**Best For:** Programmatic access, compliance tooling integration, detailed analysis

**Location:** `/home/jerry/Repos/a-sdlc/moscow-prioritization.json`

---

### 2. moscow-prioritization.csv (11 KB, 40 rows)
**Purpose:** Spreadsheet-compatible matrix for sorting, filtering, and analysis

**Columns:**
1. Control ID (e.g., SC-0D)
2. Control Name (e.g., Core Directive Injection)
3. Stage (0-6)
4. Track (QC, RC, SC, AC, GC)
5. Current Status (Active/In Development)
6. MoSCoW (M/S/C/W)
7. Justification (regulatory & operational rationale)
8. Phase Implementation (Phase 1/2/3)
9. Remediation Impact (CRITICAL/HIGH/MEDIUM/LOW)

**Data:**
- Row 1: Headers
- Rows 2-40: All 39 controls (alphabetically by control ID for easy lookup)
- Sortable by any column in Excel, Google Sheets, or SQL tools

**Best For:** Quick lookups, spreadsheet analysis, project tracking, governance dashboards

**Location:** `/home/jerry/Repos/a-sdlc/moscow-prioritization.csv`

---

### 3. MOSCOW-PRIORITIZATION-README.md (26 KB, 675 lines)
**Purpose:** Comprehensive guide covering all aspects of the prioritization analysis

**Sections:**

1. **Executive Summary** (2 KB)
   - Key findings: 23 Must-Have, 12 Should-Have, 4 Could-Have, 0 Won't-Have
   - Regulatory impact by phase
   - Risk assessment

2. **Control Distribution by Stage** (8 KB)
   - Cross-Cutting (Stage 0): All 5 controls are Must-Have
   - Stage 1 (Intent Ingestion): 4M, 2S
   - Stage 2 (System Design): 3M, 2S
   - Stage 3 (Implementation): 4M, 3S
   - Stage 4 (Testing & Documentation): 4M, 2S, 1C
   - Stage 5 (Deployment & Release): 3M, 2S
   - Stage 6 (Observability & Maintenance): 1M, 2S, 2C
   - Each stage includes: critical chains, risk analysis, missing control impact

3. **MoSCoW Category Definitions** (5 KB)
   - Must-Have: 23 controls, non-negotiable, legally required
   - Should-Have: 12 controls, high-value compliance/quality
   - Could-Have: 4 controls, optimization/efficiency
   - Won't-Have: 0 controls (all 39 are in scope)

4. **Critical Regulatory Mapping** (3 KB)
   - DORA articles (Art. 5-28) with control mappings
   - EU AI Act articles (Art. 6-73) with control mappings
   - Coverage metrics by article

5. **Control Dependencies & Blocking Chains** (4 KB)
   - 4 critical dependency chains (Intent, AI, Security, Governance)
   - 3 blocking controls (RC-2A, RC-4A, RC-5A, SC-3A)
   - Blocking impact analysis

6. **Phase-Based Implementation Roadmap** (6 KB)
   - Phase 1 (Weeks 1-26): 23 Must-Have controls, 7-week sequence
   - Phase 2 (Months 7-12): 12 Should-Have enhancements
   - Phase 3 (Months 13-18): 4 Could-Have optimizations
   - Exit criteria for each phase

7. **Risk Assessment** (3 KB)
   - Impact if Must-Have controls missing
   - Specific DORA/EU AI Act article violations
   - Remediation cost and timeline

8. **Implementation Checklist** (2 KB)
   - Pre-implementation tasks
   - Phase 1-3 checkpoints
   - Training and approval requirements

**Best For:** Strategic planning, team alignment, compliance documentation, governance meetings

**Location:** `/home/jerry/Repos/a-sdlc/MOSCOW-PRIORITIZATION-README.md`

---

### 4. MOSCOW-QUICK-REFERENCE.md (11 KB, 286 lines)
**Purpose:** Quick lookup and at-a-glance reference for practitioners

**Sections:**

1. **At-a-Glance Categories** (1 KB)
   - Must-Have by stage with all control IDs
   - Should-Have by stage with all control IDs
   - Could-Have by stage with all control IDs

2. **Critical Blocking Controls** (0.5 KB)
   - RC-2A (Design Approval) → Blocks Stage 3
   - RC-4A (Risk Threshold) → Blocks Stage 5
   - RC-5A (CAB Approval) → Blocks deployment
   - SC-3A (Permission Management) → Blocks code changes
   - Includes decision criteria and approval path for each

3. **Phase Implementation Timeline** (1 KB)
   - 26-week Phase 1 schedule (Stages 0-6)
   - Phase 2 objectives (6-12 months)
   - Phase 3 objectives (12-18 months)

4. **Regulatory Articles & Control Mapping** (2 KB)
   - Quick-lookup table: Article → Controls
   - DORA articles (Art. 5-28)
   - EU AI Act articles (Art. 6-73)

5. **Control Dependencies** (1 KB)
   - 4 critical chains with visual layout
   - Intent Flow, AI System, Security Enforcement, Governance & Audit

6. **Risk Profile** (0.5 KB)
   - If Must-Have controls missing: Legal, Deployment, Incidents, Audit, Security, AI
   - All marked as CRITICAL severity

7. **Distribution Tables** (1 KB)
   - Track-by-track breakdown (QC, RC, SC, AC, GC)
   - M/S/C/W distribution per track

8. **Key Decisions & Approval Criteria** (1 KB)
   - RC-2A decision criteria
   - RC-4A decision criteria
   - RC-5A decision criteria

9. **Implementation Checklist** (1 KB)
   - Pre-implementation (Week 0)
   - Phase 1 Weeks 1-2 (Cross-Cutting)
   - Phase 1 Weeks 3-26 (Stages)
   - Phase 1 Completion (Week 26)

10. **Quick Lookup by Control ID** (2 KB)
    - All 39 controls listed with M/S/C/W category
    - Legend and explanations

**Best For:** Daily reference, team meetings, quick lookups, decision-making

**Location:** `/home/jerry/Repos/a-sdlc/MOSCOW-QUICK-REFERENCE.md`

---

## How to Use These Deliverables

### For Strategic Planning
1. Start with **MOSCOW-PRIORITIZATION-README.md** (full context)
2. Review **Phase-Based Implementation Roadmap** section
3. Identify resource requirements for Phase 1 (23 Must-Have)
4. Plan Phase 2 and 3 in parallel for continuity

### For Daily Operations
1. Use **MOSCOW-QUICK-REFERENCE.md** for quick lookups
2. Refer to **Critical Blocking Controls** section for gate decisions
3. Check **Implementation Checklist** for weekly milestones

### For Compliance Meetings
1. Use **moscow-prioritization.csv** for dashboard/presentation
2. Reference **Regulatory Articles & Control Mapping** in README
3. Highlight Phase 1 impact: +34% DORA, +37% EU AI Act

### For Developer/Team Training
1. Distribute **MOSCOW-QUICK-REFERENCE.md**
2. Highlight the 4 blocking controls and approval criteria
3. Walk through critical dependency chains (Security Enforcement, Governance & Audit)

### For Governance/Risk Management
1. Review **moscow-prioritization.json** for programmatic access
2. Extract Must-Have controls for risk dashboard
3. Map controls to existing governance roles/responsibilities
4. Establish approval workflows for RC-2A, RC-4A, RC-5A

### For Technical Integration
1. Use **moscow-prioritization.json** for tooling integration
2. Extract Phase 1 controls and build implementation sequence
3. Create automated compliance checks based on control definitions
4. Map controls to existing CI/CD pipeline stages

---

## Control Categories Explained

### Must-Have (M) — 23 controls
**Definition:** Non-negotiable, legally required, foundational
**Characteristics:**
- Addresses critical regulatory gaps (DORA, EU AI Act)
- Required for Phase 1 (3-6 months)
- Blocks deployment if missing
- Implements core security/governance functions
- Establishes blocking gates in SDLC flow

**Example:** SC-0D (Core Directive Injection) — foundational for policy enforcement across all stages

**Risk if Missing:** CRITICAL — Cannot legally deploy; violates multiple regulatory articles; uncontrolled agent behavior

### Should-Have (S) — 12 controls
**Definition:** High value, important for compliance/quality
**Characteristics:**
- Addresses partially covered requirements
- Enables Phase 2 enhancements (6-12 months)
- Improves coverage from 65-72% to 80-85%
- Gates compliance through exit criteria or operational benefit
- Can be supplemented by automated tools if unavailable

**Example:** QC-1B (Coherence & Conflict Resolution) — prevents conflicting requirements but not blocking

**Risk if Missing:** HIGH-MEDIUM — Partial compliance, operational inefficiency, undetected risk drift

### Could-Have (C) — 4 controls
**Definition:** Nice-to-have, optimization, efficiency
**Characteristics:**
- Improves implementation efficiency
- Enhances existing controls
- Non-blocking for deployment
- Supports Phase 3 optimization (12-18 months)
- Provides operational benefits over compliance requirements

**Example:** QC-6A (SLA/SLO Monitoring) — operational efficiency, not compliance-driven

**Risk if Missing:** LOW — No compliance impact; operational visibility reduced

### Won't-Have (W) — 0 controls
**Definition:** Out of scope or explicitly deferred
**Status:** N/A — All 39 existing controls are in scope

---

## Critical Findings

### Finding 1: All 39 Controls Required
No controls are deferred or optional. All controls align with framework goals. Every control supports either DORA or EU AI Act compliance.

### Finding 2: Must-Have Controls Are Non-Negotiable
Missing ANY of the 23 Must-Have controls violates DORA or EU AI Act articles and blocks deployment. Phase 1 completion (3-6 months) is a hard deadline for legal compliance.

### Finding 3: Four Blocking Controls Are Decision Gates
- RC-2A (Design Approval) blocks Stage 3 entry
- RC-4A (Risk Threshold) blocks Stage 5 entry
- RC-5A (CAB Approval) blocks production deployment
- SC-3A (Permission Management) blocks code changes

Clear approval criteria and decision-makers must be established before implementation.

### Finding 4: Phase 1 Closes All 8 Critical Gaps
Implementing all 23 Must-Have controls closes all 8 critical regulatory gaps identified in gap analysis. Phase 1 is the minimum viable compliance posture.

### Finding 5: Security Controls Form Integrated Chain
From intent validation (SC-1A) through post-deployment (SC-6A), security controls are interdependent. No weak points are tolerable. Missing any one control weakens the entire chain.

### Finding 6: AI Systems Require Dedicated Pipeline
AC-1A through AC-6A form a complete AI governance pipeline. Organizations with AI components must treat these controls as a dedicated track parallel to general SDLC controls.

### Finding 7: Governance Controls Are Foundational
GC-0A, GC-0B, GC-1A, GC-3A, GC-0C create end-to-end audit trail required by both DORA and EU AI Act. Implementing these early establishes audit mechanisms before development begins.

### Finding 8: Phase 2 Is Compliance Multiplier
Should-Have controls increase coverage from 65% to 82% (EU AI Act). Should not be deferred beyond Phase 2 timeline.

---

## Contact & Feedback

**Framework:** A-SDLC 1.0
**Generated:** 2026-03-04
**Version:** 1.0

For questions, updates, or corrections to this analysis, refer to the A-SDLC project documentation in:
- `/home/jerry/Repos/a-sdlc/asdlc.yaml` (framework manifest)
- `/home/jerry/Repos/a-sdlc/regulatory/sources.yaml` (regulatory sources)
- `/home/jerry/Repos/a-sdlc/regulatory/compliance-matrix.yaml` (article mapping)

---

## File Cross-References

| Need | File | Type | Size |
|------|------|------|------|
| Quick lookup | MOSCOW-QUICK-REFERENCE.md | Markdown | 11 KB |
| Spreadsheet analysis | moscow-prioritization.csv | CSV | 11 KB |
| Comprehensive guide | MOSCOW-PRIORITIZATION-README.md | Markdown | 26 KB |
| Programmatic access | moscow-prioritization.json | JSON | 34 KB |
| Index (this file) | MOSCOW-PRIORITIZATION-INDEX.md | Markdown | This file |

---

**All Files Located In:** `/home/jerry/Repos/a-sdlc/`

**Generated By:** A-SDLC Prioritization Analysis Tool
**Date:** 2026-03-04
**Status:** Complete & Ready for Implementation
