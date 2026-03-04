# A-SDLC Framework Gap Analysis
## Comprehensive Regulatory Compliance Assessment Against DORA and EU AI Act

**Analysis Date:** 2026-03-04
**Scope:** DORA (Regulation EU 2022/2554) and EU AI Act (Regulation EU 2024/1689)
**Total Controls Analyzed:** 39
**Total Regulatory Requirements Analyzed:** 25 articles/annexes

---

## Executive Summary

The A-SDLC framework demonstrates foundational regulatory compliance coverage but faces **significant gaps** in key areas of both DORA and EU AI Act requirements:

| Framework | Coverage % | Status | Risk Level |
|-----------|-----------|--------|-----------|
| **DORA** | 38% | Partial | HIGH |
| **EU AI Act** | 28% | Limited | CRITICAL |
| **Combined** | 33% | Partial | HIGH |

### Key Findings

- **DORA:** 9 of 11 articles have some level of control coverage; 2 critical articles (Art. 9, 11) have zero controls
- **EU AI Act:** 8 of 14 articles have some level of control coverage; 6 critical articles have zero controls
- **Feedback Loops:** Adequately address expedited remediation but lack explicit regulatory incident reporting workflows

---

## DORA Analysis: Digital Operational Resilience Act

### Coverage Breakdown

| Category | Count | Articles |
|----------|-------|----------|
| Well Covered (90%) | 1 | Art. 10 |
| Partially Covered (66%) | 2 | Art. 8, Art. 24 |
| Poorly Covered (33%) | 6 | Art. 5, 17, 18, 19, 25, 28 |
| Not Covered (0%) | 2 | **Art. 9, Art. 11** |

### CRITICAL GAPS

#### 1. Art. 9: Protection and Prevention (NOT COVERED - CRITICAL)

**Requirement:** Financial entities must continuously monitor ICT systems, deploy appropriate security tools, establish security policies, implement access controls, deploy strong authentication, implement change management, and maintain patch policies.

**Current State:** While individual security controls exist (SC-1A through SC-6B), they are **not explicitly mapped** to Art. 9 in the regulatory mapping.

**Gap Details:**
- No documented comprehensive security policy control
- No explicit authentication and access control policy framework
- No patch and update management program control
- No network segmentation and isolation procedure control
- No data protection (at rest, in transit, in use) control

**Impact:** Leaves a fundamental DORA obligation unaddressed despite having relevant technical controls.

**Recommendation:**
1. Explicitly map existing SC-series controls to Art. 9 in their regulatory_mapping
2. Consider creating SC-9A: "ICT Security Policy and Prevention Framework" to consolidate Art. 9 requirements
3. Add controls for patch management and network segmentation

#### 2. Art. 11: Response and Recovery (NOT COVERED - CRITICAL)

**Requirement:** Financial entities must implement comprehensive ICT business continuity policy, limit damage through recovery procedures, test plans annually, maintain crisis management function, and keep accessible records of disruptions.

**Current State:** RC-5B (Rollback Plan Validation) addresses only narrow rollback validation; no business continuity controls exist.

**Gap Details:**
- No ICT business continuity policy control
- No crisis management function control
- No business impact analysis (BIA) control
- No RTO/RPO definition and monitoring control
- No business continuity testing and exercises control
- No critical function identification control

**Impact:** DORA Art. 11 is a core operational resilience requirement; its absence creates regulatory compliance risk.

**Recommendation:**
1. Create RC-7A: "ICT Business Continuity Policy and Planning"
2. Create RC-7B: "Business Impact Analysis and RTO/RPO Definition"
3. Create RC-7C: "Business Continuity Testing and Exercises"
4. Map to stages 1, 4, and 6

---

### HIGH-PRIORITY GAPS

#### 3. Art. 5: Governance and Organisation (POORLY COVERED - 33%)

**Requirement:** Management body must maintain governance framework, define ICT risk policies, approve strategy and risk tolerance levels, oversee business continuity plans, and establish reporting channels.

**Current Coverage:** RC-5A (CAB Approval) addresses formal governance approval only.

**Gap Details:**
- No management body training and competency control
- No ICT risk appetite and tolerance level definition control
- No risk tolerance monitoring and adjustment control
- No board-level reporting cadence control

**Recommendation:** Enhance RC-5A or create new governance controls for management body accountability.

#### 4. Art. 17: ICT-related Incident Management Process (POORLY COVERED - 33%)

**Requirement:** Financial entities must define and implement ICT incident management process including documentation, root cause analysis, consistent monitoring, and follow-up.

**Current Coverage:** SC-6A (Incident Scanning & Detection) provides detection and classification only.

**Gap Details:**
- No root cause analysis procedures control
- No corrective action tracking control
- No post-incident review process control
- No incident escalation criteria control

**Recommendation:** Enhance SC-6A or create SC-6C: "Incident Root Cause Analysis and Corrective Action".

#### 5. Art. 18 & 19: Incident Classification and Reporting (POORLY COVERED - 33% each)

**Requirement:** Art. 18 requires classification per DORA taxonomy (6 impact criteria). Art. 19 requires reporting to authorities with specific timelines: 4h initial, 72h intermediate, 1 month final.

**Current Coverage:** SC-6A detects incidents but lacks:
- Documented DORA classification taxonomy implementation
- Client impact assessment procedures
- Geographical spread analysis
- Data integrity impact measurement
- **Regulatory reporting workflow with timeline automation**

**Impact:** Art. 19 reporting timelines are legally mandated; absence of controls creates compliance violation risk.

**Recommendation:** Create SC-7A: "Incident Reporting and Regulatory Notification" with explicit timeline tracking.

#### 6. Art. 25: Testing of ICT Tools and Systems (POORLY COVERED - 33%)

**Requirement:** Testing must include vulnerability assessments, open source analysis, network security assessments, gap analyses, physical security reviews, source code reviews, scenario tests, compatibility testing, and penetration testing.

**Current Coverage:** SC-4B (DAST) covers dynamic testing only.

**Missing:**
- Open source component analysis (SBOM)
- Network security assessment
- Physical security testing
- Scenario-based testing framework
- Penetration testing roadmap

#### 7. Art. 28: ICT Third-Party Risk Management (POORLY COVERED - 33%)

**Requirement:** Financial entities must manage third-party ICT risk, maintain vendor registers, conduct due diligence, ensure contractual compliance, and develop exit strategies.

**Current Coverage:** GC-0C (Agent Provenance Registry) tracks agents but does not address vendor management.

**Missing:**
- Third-party vendor register
- Pre-contract due diligence procedures
- Concentration risk assessment
- Contract termination procedures
- Exit strategy validation

---

## EU AI Act Analysis: Artificial Intelligence Act

### Coverage Breakdown

| Category | Count | Articles/Annexes |
|----------|-------|------------------|
| Well Covered (90%) | 1 | Art. 12 |
| Partially Covered (66%) | 2 | Art. 9, Art. 73 |
| Poorly Covered (33%) | 5 | Art. 6, 13, 14, 72, Annex III |
| Not Covered (0%) | 6 | **Art. 10, 11, 15, 17, 26, Annex IV** |

### CRITICAL GAPS

#### 1. Art. 10: Data and Data Governance (NOT COVERED - CRITICAL)

**Requirement:** High-risk AI systems must use training, validation, and testing data meeting quality criteria. Governance must address: data collection, preparation, annotation, labeling, cleaning, enrichment, bias examination, and data gap identification.

**Current State:** AC-4A (Bias & Fairness Testing) addresses only bias detection; no broader data governance control exists.

**Gap Details:**
- No data governance framework control
- No data quality criteria and standards control
- No data collection process documentation control
- No data preparation operations control (annotation, labeling, cleaning)
- No systematic bias detection methodology
- No data gap analysis and remediation control
- No data retention and deletion policies control

**Impact:** Data governance is foundational to AI Act compliance; this gap affects all high-risk AI systems.

**Recommendation:** Create AC-3A: "Data Governance and Quality Management" covering all EU AI Act Art. 10 requirements.

#### 2. Art. 11: Technical Documentation (NOT COVERED - CRITICAL)

**Requirement:** Technical documentation must be prepared before market placement with minimum elements per Annex IV, including system description, development process, monitoring, risk management, lifecycle changes, harmonised standards, and EU declaration of conformity.

**Current State:** QC-4C (Documentation Completeness) is generic; does not reference AI Act requirements or Annex IV elements.

**Gap Details:**
- No Annex IV element checklist implementation
- No AI system general description documentation control
- No development process documentation control
- No risk management system documentation control
- No change management documentation control
- No harmonised standards application documentation
- No EU declaration of conformity preparation control

**Impact:** Annex IV compliance is legally required before market placement; absence creates deployment blocker.

**Recommendation:** Enhance QC-4C or create new AC-5B: "AI Act Technical Documentation and Annex IV Compliance".

#### 3. Art. 15: Accuracy, Robustness and Cybersecurity (NOT COVERED - CRITICAL)

**Requirement:** High-risk AI systems must achieve appropriate levels of accuracy, robustness, and cybersecurity; be resilient against unauthorized alterations; protect against data poisoning, model poisoning, adversarial examples, and other attacks.

**Current State:** AC-4A (Bias & Fairness Testing) addresses fairness only; does not address accuracy metrics or adversarial resilience.

**Gap Details:**
- No accuracy metric definition and documentation control
- No robustness testing framework control
- No cybersecurity assessment for AI-specific vulnerabilities
- No adversarial attack simulation and testing control
- No data poisoning defense mechanism control
- No model poisoning detection and mitigation control
- No fail-safe and backup plan documentation

**Impact:** Core AI Act requirement for safe, reliable AI systems; essential for high-risk classifications.

**Recommendation:** Create AC-5A: "AI Model Accuracy, Robustness, and Adversarial Resilience Testing" covering all Art. 15 requirements.

#### 4. Art. 17: Quality Management System (NOT COVERED - CRITICAL)

**Requirement:** Providers must implement a documented quality management system with 13 specific elements: strategy, design control, development procedures, testing procedures, technical specifications, data management, risk management, post-market monitoring, incident reporting, communication protocols, record-keeping, resource management, and accountability framework.

**Current State:** Multiple controls address individual elements, but **no unified QMS control exists**; requirements scattered across QC, RC, AC, GC tracks.

**Gap Details:**
- No consolidated QMS strategy documentation
- No design control procedures
- No quality control and assurance procedures documentation
- No technical specifications and standards documentation
- No unified data management system documentation
- No resource management and supply chain security procedures
- No management accountability framework
- No QMS audit and review process

**Impact:** Art. 17 QMS is foundational for high-risk AI compliance; scattered controls create gaps in unified oversight.

**Recommendation:** Create new GC-4A: "Quality Management System for High-Risk AI Systems" consolidating Art. 17(1) elements, or enhance existing controls with explicit cross-referencing.

#### 5. Art. 26: Obligations of Deployers (NOT COVERED - CRITICAL)

**Requirement:** Deployers must use AI systems per instructions, assign competent oversight personnel, ensure input data quality, monitor system operation, report issues, and immediately notify authorities of serious incidents.

**Current State:** GC-0C (Agent Provenance Registry) tracks agent actions but does not address deployer obligations.

**Gap Details:**
- No deployer compliance procedures control
- No oversight personnel assignment and training control
- No input data quality assurance control
- No input data representativeness validation control
- No performance monitoring procedures control
- No issue and incident reporting to provider control
- No authority notification procedures control
- No suspension and use termination procedures

**Impact:** Deployers are responsible parties under AI Act; absent controls leave deployer organizations exposed.

**Recommendation:** Create new GC-5A: "Deployer Obligations and Input Data Quality Management".

#### 6. Annex IV: Technical Documentation Elements (NOT COVERED - CRITICAL)

**Requirement:** Specifies minimum technical documentation elements for high-risk AI systems including general description, detailed components, development process, monitoring, risk management, lifecycle changes, standards, and EU declaration of conformity.

**Current State:** Covered only partially by generic QC-4C; not AI Act specific.

**Gap Details:** (See Art. 11 above)

**Recommendation:** See Art. 11 recommendation.

---

### HIGH-PRIORITY GAPS

#### 7. Art. 6: Classification Rules (POORLY COVERED - 33%)

**Requirement:** AI systems classified as high-risk if they are safety components under Union harmonisation legislation or fall within Annex III categories (biometrics, critical infrastructure, employment, essential services, law enforcement, migration, justice).

**Current Coverage:** AC-1A (AI Risk Tier Classification) provides only basic risk tier, not Annex III category mapping.

**Missing:**
- Annex III category identification and mapping
- Product harmonisation legislation assessment
- Safety component determination
- Risk tier escalation criteria

#### 8. Art. 13: Transparency and Information Provision (POORLY COVERED - 33%)

**Requirement:** AI systems must be accompanied by instructions for use with complete information about system characteristics, capabilities, limitations, accuracy, robustness, cybersecurity, potential risks, and human oversight measures.

**Current Coverage:** AC-2A (AI Component Design Review) provides design review but not instructions for use documentation.

**Missing:**
- Instructions for use documentation
- Accuracy metrics declaration
- Limitation documentation
- Human oversight measure documentation
- Deployer communication process

#### 9. Art. 14: Human Oversight (POORLY COVERED - 33%)

**Requirement:** High-risk AI systems must be designed with human-machine interfaces enabling effective human oversight, with oversight assigned to competent, trained natural persons with authority and support.

**Current Coverage:** AC-2A and SC-2B address design and directive injection but not human oversight role definition or competency requirements.

**Missing:**
- Human oversight role definition
- Competency and training requirements
- Authority and accountability framework
- Human-machine interface usability
- Intervention capability design

#### 10. Art. 72: Post-Market Monitoring (POORLY COVERED - 33%)

**Requirement:** Providers must actively collect and analyze data on AI system performance and compliance throughout lifetime; post-market monitoring plan must be proportionate and included in technical documentation.

**Current Coverage:** AC-6A (AI Post-Market Surveillance) provides monitoring but not comprehensive plan documentation.

**Missing:**
- Post-market monitoring plan documentation
- Performance metric definition and collection
- Data collection methodology
- Compliance trend analysis
- Root cause investigation process

#### 11. Art. 73: Reporting of Serious Incidents (PARTIALLY COVERED - 66%)

**Requirement:** Providers must report serious AI incidents to authorities within 15 days (10 days if death involved, 2 days for widespread infringements).

**Current Coverage:** AC-6A and SC-6A detect incidents but lack explicit AI-specific reporting workflow.

**Missing:**
- Serious incident definition for AI systems
- Regulatory reporting workflow for AI incidents
- Timeline compliance automation (15/10/2 days)

---

## Cross-Framework Findings

### Critical Cross-Framework Gap: Incident Reporting and Regulatory Timelines

Both DORA and EU AI Act impose strict **legally mandated reporting timelines** that create significant compliance risk:

| Framework | Timeline | Requirement | Current Control |
|-----------|----------|-------------|-----------------|
| **DORA Art. 19** | 4h initial, 72h intermediate, 1 month final | Major ICT incidents to competent authorities | SC-6A (insufficient) |
| **EU AI Act Art. 73** | 15 days normal, 10 days if death, 2 days widespread | Serious AI incidents to authorities | AC-6A (insufficient) |

**Gap:** No control explicitly manages regulatory reporting workflows with automated timeline tracking.

**Recommendation:** Create SC-7A: "Incident Reporting and Regulatory Notification" with:
- Incident classification triggering regulatory reporting
- Automated timeline tracking (4h, 72h, 1m for DORA; 15/10/2 days for AI Act)
- Authority notification workflow
- Client notification procedures
- Escalation authority assignment

---

## Feedback Loops Analysis

### Regulatory Alignment

**Strengths:**
- Path A includes critical security controls (SC-3B, SC-3C, SC-5B) for expedited remediation
- Path B ensures full lifecycle compliance by re-entering at Stage 1
- Both paths include GC-3A (code provenance) ensuring accountability

**Weaknesses:**
- **No explicit regulatory incident classification** (DORA Art. 18)
- **No regulatory reporting trigger** in feedback loop decision tree
- **Gap in medium-risk handling** between Path A (low-risk only) and Path B (all risks)
- **No third-party impact assessment** for Art. 28 (third-party risk) incidents
- **Missing escalation authority** assignment in feedback loops

### Recommendations for Feedback Loop Enhancement

1. **Add regulatory incident classification** trigger to feedback loop decision tree
2. **Create feedback trigger** for DORA Art. 19 and AI Act Art. 73 reporting timelines
3. **Add escalation authority** field (Risk Officer, Security Architect, Compliance Officer)
4. **Create medium-risk path** for issues exceeding Path A eligibility but not requiring full re-entry
5. **Add third-party impact assessment** for incidents involving vendors/agents

---

## Control Track Coverage Assessment

### SC (Security Controls) - 45% Coverage
**Strengths:** Comprehensive testing and incident detection controls
**Gaps:**
- Art. 9 (comprehensive protection policy)
- Art. 11 (recovery procedures)
- Art. 19 (regulatory reporting workflows)

### QC (Quality Controls) - 35% Coverage
**Strengths:** Requirements validation, design validation, testing
**Gaps:**
- Art. 11 (business continuity)
- AIACT Art. 10 (data governance)
- AIACT Art. 11 (technical documentation)

### RC (Risk Controls) - 32% Coverage
**Strengths:** Risk classification and threshold evaluation
**Gaps:**
- Art. 5 (governance framework)
- Art. 11 (recovery and business continuity)
- AIACT Art. 17 (quality management system)

### AC (AI Controls) - 42% Coverage
**Strengths:** AI risk classification, bias testing, post-market monitoring
**Gaps:**
- AIACT Art. 10 (data governance)
- AIACT Art. 15 (accuracy/robustness)
- AIACT Art. 26 (deployer obligations)

### GC (Governance Controls) - 38% Coverage
**Strengths:** Audit trails, traceability, provenance tracking
**Gaps:**
- DORA Art. 5 (management body accountability)
- AIACT Art. 17 (comprehensive quality management system)

---

## Remediation Roadmap

### Phase 1: CRITICAL - Immediate Action (3-6 months)

**DORA:**
1. SC-9A: "ICT Security Policy and Prevention Framework"
   - Consolidate and map Art. 9 requirements
   - Include authentication, access control, patch management, network segmentation

2. RC-7A: "ICT Business Continuity Policy and Planning"
   - Address Art. 11 fundamental gap

3. SC-7A: "Incident Reporting and Regulatory Notification"
   - Implement Art. 19 reporting timelines (4h/72h/1 month)
   - Add authority notification workflow

**EU AI Act:**
1. AC-3A: "Data Governance and Quality Management"
   - Implement Art. 10 data governance framework
   - Include data quality criteria, bias assessment, data preparation

2. AC-5A: "AI Model Accuracy, Robustness, and Adversarial Resilience Testing"
   - Implement Art. 15 accuracy and robustness requirements
   - Include adversarial attack simulation

3. Enhance QC-4C or create AC-5B: "AI Act Technical Documentation"
   - Implement Annex IV requirements explicitly

**Cross-Framework:**
1. Update feedback-loops.yaml to include regulatory incident reporting triggers

### Phase 2: HIGH-PRIORITY - Implementation (6-12 months)

1. Enhance Art. 5 governance controls with management body accountability
2. Enhance Art. 17/18 incident management with root cause analysis
3. Enhance Art. 25 testing controls with open source and physical security testing
4. Enhance Art. 28 third-party controls with vendor management and exit strategy
5. Create AC-4A enhancement for deployer obligations (AIACT Art. 26)

### Phase 3: OPTIMIZATION - Integration (12-18 months)

1. Create GC-4A: "Unified Quality Management System for High-Risk AI" (AIACT Art. 17)
2. Implement regulatory timeline automation across incident reporting
3. Create cross-functional controls for third-party coordination (Art. 28)
4. Add regulatory reporting artifacts to all relevant control outputs

---

## Summary Table: All Gaps by Severity

### CRITICAL Gaps (NOT COVERED - Immediate Action Required)

| Framework | Article | Title | Impact | Control Needed |
|-----------|---------|-------|--------|-----------------|
| DORA | Art. 9 | Protection and prevention | Core security obligation | SC-9A |
| DORA | Art. 11 | Response and recovery | Business continuity absent | RC-7A, RC-7B, RC-7C |
| DORA | Art. 19 | Incident reporting timelines | Legal compliance risk | SC-7A |
| AIACT | Art. 10 | Data governance | Foundation for AI compliance | AC-3A |
| AIACT | Art. 11 | Technical documentation | Pre-market requirement | AC-5B |
| AIACT | Art. 15 | Accuracy/robustness | AI safety requirement | AC-5A |
| AIACT | Art. 17 | Quality management system | Unified oversight missing | GC-4A |
| AIACT | Art. 26 | Deployer obligations | Deployer responsibility | GC-5A |

### HIGH-PRIORITY Gaps (POORLY COVERED - 3-6 month remediation)

| Framework | Article | Title | Current Control | Enhancement |
|-----------|---------|-------|-----------------|-----------------|
| DORA | Art. 5 | Governance | RC-5A only | Enhance with management body accountability |
| DORA | Art. 17 | Incident management | SC-6A only | Create SC-6C for root cause analysis |
| DORA | Art. 18 | Incident classification | SC-6A only | Enhance with DORA taxonomy automation |
| DORA | Art. 25 | Testing | SC-4B only | Add open source, network, physical security testing |
| DORA | Art. 28 | Third-party risk | GC-0C only | Enhance with vendor management, exit strategy |
| AIACT | Art. 6 | Classification | AC-1A only | Map Annex III categories explicitly |
| AIACT | Art. 13 | Transparency | AC-2A only | Add instructions for use documentation |
| AIACT | Art. 14 | Human oversight | AC-2A + SC-2B | Add role definition, competency requirements |
| AIACT | Art. 72 | Post-market monitoring | AC-6A only | Enhance with monitoring plan documentation |
| AIACT | Art. 73 | Incident reporting | AC-6A + SC-6A | Add 15/10/2-day timeline automation |

---

## Conclusion

The A-SDLC framework provides a **solid foundational control structure** for software development lifecycle governance, with particular strength in:

- Security testing controls (SC-4A, SC-4B)
- Code quality and provenance tracking (QC-3B, GC-3A)
- Risk classification and threshold evaluation (RC-1A, RC-4A)
- AI bias and fairness testing (AC-4A)
- Incident detection and logging (SC-6A, SC-6B)

However, **significant regulatory compliance gaps** exist that require immediate remediation:

### Critical Gaps Summary:
- **2 DORA articles** (Art. 9, 11) with zero control coverage
- **6 EU AI Act articles** (Art. 10, 11, 15, 17, 26, Annex IV) with zero control coverage
- **No incident reporting workflow** for DORA/AI Act regulatory timelines
- **No data governance framework** for AI systems
- **No unified quality management system** for AI Act compliance
- **No business continuity controls** for operational resilience

### Regulatory Risk Assessment:
- **DORA Compliance:** 38% coverage = MODERATE-HIGH RISK (non-compliance on critical articles)
- **EU AI Act Compliance:** 28% coverage = HIGH RISK (multiple critical gaps)
- **Combined Risk:** Organizations using A-SDLC for regulated activities face potential compliance violations

### Recommended Action:
**Implement Phase 1 critical gap controls within 3-6 months** to address DORA Art. 9, 11, 19 and AI Act Art. 10, 11, 15, 17, 26 before deploying systems in regulated environments. Prioritize incident reporting (SC-7A) as it addresses legally mandated timelines in both frameworks.

---

## Appendix: Detailed Gap Analysis JSON

See `gap-analysis-output.json` for machine-readable gap analysis with:
- Article-by-article coverage assessment
- Control-to-requirement mapping
- Coverage percentages
- Specific gap descriptions
- Remediation recommendations
