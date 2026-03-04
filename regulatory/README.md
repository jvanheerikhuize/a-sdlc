# Regulatory

This directory contains the regulatory reference material that underpins every A-SDLC control's `regulatory_mapping` field.

## Files

| File | Purpose |
| ---- | ------- |
| [compliance-matrix.yaml](compliance-matrix.yaml) | Consolidated regulatory mapping: which controls satisfy which DORA and EU AI Act articles; coverage by track and regulatory area |
| [sources.yaml](sources.yaml) | Canonical article texts and obligation summaries for DORA and the EU AI Act; used as source material for all mappings |
| **README.md** (this file) | Overview of regulatory frameworks, coverage summary, control mapping strategy (single-framework vs. dual-framework scoping) |

## Regulatory Frameworks

### DORA — Digital Operational Resilience Act

Regulation (EU) 2022/2554 · Effective 17 January 2025

Applies to financial entities operating in the EU. **All chapters and articles comprehensively mapped below:**

#### DORA Chapter I: General Provisions (Arts. 1–4)

| Article | Title | A-SDLC Control(s) | Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 1** | Subject matter | — | Definitional scope; compliance achieved through adherence to later chapters. |
| **Art. 2** | Scope | — | Scope determination is organizational governance (which entities must comply). A-SDLC applies once scope is determined. |
| **Art. 3** | Definitions | — | Provides terminology used throughout DORA. Not directly controlled by SDLC processes. |
| **Art. 4** | Exemptions and transitional provisions | — | Regulatory exemptions and grandfathering provisions; entity determines applicability. Not SDLC-controlled. |

#### DORA Chapter II: ICT Risk Management (Arts. 5–16)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 5** | Governance and organisation of ICT risk | — | **Org-level responsibility.** Board and senior management establish governance framework, risk appetite, training programs. This is enterprise governance that pre-exists SDLC execution; A-SDLC assumes this framework is in place. RC-2A and RC-5A validate human decision-making authority established by Art. 5 governance. |
| **Art. 6** | ICT risk identification | RC-1A | **✅ Partial** — RC-1A creates risk register at project start (Stage 1), enabling systematic identification of project ICT risks. **Not covered (org responsibility):** Ongoing identification of risks across the organization; enterprise-wide risk inventory beyond development projects. |
| **Art. 7** | Risk management framework documentation | GC-0A, RC-3A, GC-0B | **✅ Strong** — GC-0A maintains immutable audit trail of all risk decisions; GC-0B documents risk assessment history; RC-3A records mitigation decisions. Entire lifecycle documented. |
| **Art. 8** | ICT risk management process | RC-1A, RC-2A, RC-3A, RC-4A, RC-6A | **✅ Strong** — RC-1A identifies risks (Art. 8(2)); RC-2A assesses and prioritizes (Art. 8(3)); RC-3A documents decisions (Art. 8(5)); RC-4A validates risk acceptance (Art. 8(5)); RC-6A monitors ongoing risk evolution (Art. 8(6)). Full lifecycle coverage. |
| **Art. 8(5-6)** | Documentation and continuous monitoring | QC-1A, QC-1B, QC-3A, RC-3A, GC-0A, QC-6A, RC-6A | **✅ Strong** — All controls produce documented evidence; QC-6A and RC-6A enable real-time continuous monitoring throughout stages and post-deployment. |
| **Art. 9(1)** | ICT-related incidents and vulnerabilities | SC-6A, SC-6B, GC-0A | **✅ Strong** — SC-6A detects and logs ICT incidents; SC-6B detects anomalies; GC-0A maintains immutable log with forensic timestamps. |
| **Art. 9(2)** | Prevention and detection of security threats | SC-0D, SC-1A, SC-1B, SC-2A, SC-2B, SC-3A, SC-3B, SC-3D, SC-3E, SC-4A, SC-4B, SC-4C, SC-4D, SC-5A, SC-5B, SC-5C | **✅ Strong** — Comprehensive coverage: SC-0D injects directives; SC-1A/B gate inputs; SC-2A/B validate design; SC-3A/B/C/D/E enforce code/container/supply chain security; SC-4A/B/C/D test security; SC-5A/B/C validate infrastructure/deployment. |
| **Art. 9(3)** | Least privilege and segregation of duties | SC-3A | **✅ Strong** — SC-3A enforces role-based access control (RBAC) with least-privilege principles and segregation of duties across all environments. |
| **Art. 9(4)** | ICT security policies and technical measures | SC-0D, SC-1A, SC-1B, SC-2C, SC-3A, SC-3C, SC-3E, SC-5A, SC-5C, RC-5A | **✅ Strong** — SC-0D injects core security directives; SC-2C validates zero-trust architecture; SC-3C/5C manage credentials; SC-5A validates baseline; SC-3A enforces access; RC-5A gates deployment. |
| **Art. 10** | Detection and monitoring | SC-6A, SC-6B, QC-6A, RC-6A | **✅ Strong** — SC-6A and SC-6B provide real-time incident and anomaly detection; QC-6A monitors SLOs; RC-6A monitors risk metrics. Continuous across all stages. |
| **Art. 11** | Response and recovery procedures | RC-5B, RC-6A, QC-6A | **✅ Strong** — RC-5B validates incident response procedures (rollback, contingency) before release; RC-6A and QC-6A monitor recovery execution post-incident. |
| **Art. 12** | Reporting incidents to competent authorities | GC-0A, SC-6A | **✅ Partial** — GC-0A maintains audit trail with timestamps and evidence; SC-6A classifies incidents. **Not covered (org responsibility):** Actual notification to competent authorities (ECB, EBA), timeline compliance (4 hours), and materiality determination. A-SDLC provides evidence; entity performs regulatory notification. |
| **Art. 13** | Reporting incidents to customers | GC-0A, SC-6A | **✅ Partial** — GC-0A provides audit evidence of incident timelines; SC-6A logs incident classification. **Not covered (org responsibility):** Determining impact materiality to customers and customer notification strategy execution. A-SDLC provides classification and timeline; entity handles communication. |
| **Art. 14** | Mitigation measures and contingency plans | RC-2A, RC-5B | **✅ Strong** — RC-2A develops mitigation strategies and contingency plans during design (Stage 2); RC-5B validates plan feasibility before deployment. |
| **Art. 15** | Continuity and recovery planning | RC-5B, RC-6A, QC-5A | **✅ Strong** — RC-5B validates continuity procedures before release; RC-6A monitors recovery capability; QC-5A gates release only after verification. |
| **Art. 16** | Backup policies and restoration procedures | RC-5B, QC-5A | **✅ Partial** — RC-5B validates backup/restore procedures work; QC-5A checks backup integrity. **Not covered (org responsibility):** Backup frequency, retention policies, and offline storage requirements. A-SDLC validates procedures work; entity determines operational policy. |

#### DORA Chapter III: Incident Management (Arts. 17–23)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 17** | ICT incident management function | GC-0A, SC-6A | **✅ Strong** — GC-0A creates immutable incident log with all metadata; SC-6A detects, escalates, and tracks incidents. Full incident lifecycle managed. |
| **Art. 18** | Classification of incidents | SC-6A | **✅ Partial** — SC-6A automatically classifies incidents by severity and impact (critical, high, medium, low) per severity matrices. **Not covered (org responsibility):** Determination of materiality thresholds (which incidents trigger regulatory reporting per Art. 20-23) and classification policy decisions. A-SDLC provides automated classification; entity applies policy rules. |
| **Art. 19** | Incident reporting to competent authorities | GC-0A, SC-6A | **✅ Strong** — GC-0A maintains timestamp and evidence audit trail; SC-6A triggers automated incident notifications and maintains detailed logging for regulatory submission. |
| **Art. 20** | Classification of significant impact events | — | **Org-level procedure.** DORA Annex defines materiality thresholds (e.g., >€1M loss, >100K customers affected). Classification is entity policy decision, not SDLC-controlled. SC-6A and GC-0A enable the entity to apply these criteria. ℹ️ **Org-level execution** |
| **Art. 21** | Notification to competent authorities | — | **Org-level procedure.** Timelines (4 hours for notification, 15 days for full disclosure) are administrative execution managed by financial entity risk/compliance function. A-SDLC supports through incident logging (GC-0A, SC-6A). ℹ️ **Org-level execution** |
| **Art. 22** | Notification to financial customers | — | **Org-level procedure.** Determination of "likely to materially impact" and customer notification strategy are entity governance decisions. A-SDLC provides evidence trail. ℹ️ **Org-level execution** |
| **Art. 23** | Public disclosure | — | **Org-level procedure.** Public disclosure decisions and timeline are entity responsibility. A-SDLC provides documentation evidence. ℹ️ **Org-level execution** |

#### DORA Chapter IV: Digital Operational Resilience Testing (Arts. 24–27)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 24** | General testing requirements | SC-4A, SC-4B, QC-4A, QC-4B, SC-5A | SC-4A (SAST) and SC-4B (DAST) test code; QC-4A tests functionality; QC-4B tests AI outputs; SC-5A validates infrastructure baseline. ✅ Strong |
| **Art. 25** | Testing of tools, systems, and data | SC-3D, SC-3E, SC-4A, SC-4B, SC-4C, SC-5A, QC-4A | SC-3D scans open-source dependencies (Art. 25(1) explicit requirement); SC-3E scans container/IaC; SC-4A/B/C test application and API security; SC-5A validates infrastructure. ✅ Strong |
| **Art. 26** | Penetration testing | — | **Org-level execution.** Penetration testing is coordinated by financial entity risk/governance function; A-SDLC enables through SC-4A, SC-4B, SC-5A infrastructure readiness. Entity executes test scope and interpretation. ℹ️ **Org-level execution** |
| **Art. 27** | Threat-led penetration testing (TLPT) oversight | — | **Org-level/Regulatory execution.** TLPT is a regulatory-directed assessment coordinated with ECB/EBA. Individual SDLC cannot govern regulatory testing scope. A-SDLC ensures infrastructure and code posture readiness (SC-5A, SC-4A/B). ℹ️ **Org-level execution** |

#### DORA Chapter V: Third-Party Risk (Arts. 28–44)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 28** | ICT third-party risk management | GC-0C, GC-3A, SC-3D, SC-3E, RC-6B | **✅ Strong** — GC-0C tracks code provenance/origin; GC-3A logs third-party code; SC-3D scans dependencies for CVEs; SC-3E scans container/IaC risk; RC-6B monitors provider risk posture. Full supply chain visibility and continuous monitoring. |
| **Art. 29** | ICT concentration risk | — | **Org-level responsibility.** Entity determines which third parties are critical (concentration assessment) and concentration limits. A-SDLC supports through Art. 28 tracking. ℹ️ **Org-level execution** |
| **Art. 30** | Contractual requirements for ICT third parties | — | **Org-level/Procurement responsibility.** Financial entity negotiates SLAs, security clauses, exit terms with vendors. A-SDLC does not control contracting. ℹ️ **Org-level execution** |
| **Art. 31** | Subcontracting arrangements | — | **Org-level/Legal responsibility.** Entity approval of vendor subcontracting chains is governance outside SDLC scope. ℹ️ **Org-level execution** |
| **Art. 32** | Exit strategies and continuity | — | **Org-level responsibility.** Exit planning (data return timelines, continuity arrangements) is vendor management function. RC-5B validates rollback capability for *internal* deployments, not third-party exits. ℹ️ **Org-level execution** |
| **Art. 33** | Right to audit ICT third parties | — | **Org-level responsibility.** Financial entity exercises audit rights in vendor contracts. A-SDLC does not govern third-party audit. ℹ️ **Org-level execution** |
| **Art. 34** | Right of competent authority to audit | — | **Regulatory authority function.** Competent authorities (ECB, EBA, etc.) direct audits of third parties. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 35** | Information-sharing arrangements with third parties | — | **Org-level procedure.** Information-sharing agreements are entity policy. A-SDLC supports through GC-0A audit trail. ℹ️ **Org-level execution** |
| **Art. 36** | Remediation measures (termination, suspension) | — | **Org-level responsibility.** Entity decides whether to suspend/terminate third-party relationships based on incident severity. A-SDLC provides evidence through SC-6A incident logging. ℹ️ **Org-level execution** |
| **Art. 37** | Enhanced due diligence | — | **Org-level responsibility.** Financial entity conducts vendor security assessment (SOC 2 audits, security questionnaires). A-SDLC enforces controls over *use* of third-party services (SC-3D, SC-3E), not vendor selection. ℹ️ **Org-level execution** |
| **Art. 38** | Critical ICT third-party definition | — | **Org-level/Regulatory criteria.** DORA Annex defines criticality thresholds. Entity applies these to determine which third parties are critical. A-SDLC does not determine criticality. ℹ️ **Org-level execution** |
| **Art. 39** | Critical third-party risk management framework | — | **Org-level responsibility.** Entity establishes framework for critical third parties (Art. 32 requires explicit exit plans). A-SDLC ensures code from critical third parties is scanned (SC-3D/E). ℹ️ **Org-level execution** |
| **Art. 40** | Concentration risk for critical third parties | — | **Org-level risk governance.** Entity limits dependency on any single critical third party. A-SDLC supports through supply chain visibility (SC-3D, GC-0C, GC-3A). ℹ️ **Org-level execution** |
| **Art. 41** | Information about critical third parties | — | **Org-level/Regulatory reporting.** Entity discloses critical third-party names to competent authority. Not SDLC-controlled. ℹ️ **Org-level execution** |
| **Art. 42** | Supervisory powers over critical third parties | — | **Regulatory authority function.** Competent authorities (ECB) directly regulate critical ICT third parties (cloud providers, AI service providers). A-SDLC does not control regulatory oversight. ℹ️ **Regulatory authority function** |
| **Art. 43** | Regulatory technical standards (RTS) | — | **Regulatory delegation.** European Commission issues detailed RTS on third-party risk management. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 44** | Implementation timelines | — | **Org-level/Transitional provision.** Entity determines implementation timeline for critical third-party risk measures. Not SDLC-controlled. ℹ️ **Org-level execution** |

#### DORA Chapter VI: Information-Sharing Arrangements (Art. 45)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 45** | Information-sharing arrangements on cyber security incidents | — | **Org-level procedure.** Financial entity participates in DORA information-sharing networks (CSIRTs, sectoral platforms). A-SDLC provides incident evidence (SC-6A, GC-0A); sharing decision is entity governance. ℹ️ **Org-level execution** |

#### DORA Chapter VII: Competent Authorities (Arts. 46–56)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Arts. 46–56** | Competent authority designation, coordination, and powers | — | **Regulatory authority governance.** Articles 46–56 define ECB, EBA, national regulator roles and powers. Authorities supervise financial entities' DORA compliance (including SDLC execution). Not subject to SDLC controls. ℹ️ **Regulatory authority function** |

#### DORA Chapter VIII: Delegated Acts (Arts. 57–60)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Arts. 57–60** | Delegated acts and technical standards | — | **European Commission regulatory delegation.** Articles authorize EC to issue delegated regulations (DAs) and technical standards. Not SDLC-controlled; issued as separate regulations. ℹ️ **Regulatory authority function** |

#### DORA Chapter IX: Transitional and Final Provisions (Arts. 61–64)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 61** | Implementation and reporting timelines | — | **Entity implementation planning.** Entity determines internal timeline for DORA control deployment. Not SDLC-controlled. ℹ️ **Org-level execution** |
| **Art. 62** | Transitional exemptions for critical third parties | — | **Org-level/Regulatory.** Financial entities and ECB determine whether to use exemptions for critical third-party risk measures (Phase 1: up to 2027). Not SDLC-controlled. ℹ️ **Org-level execution** |
| **Art. 63** | Review clause | — | **Regulatory function.** European Commission reviews DORA effectiveness (2027+). Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 64** | Entry into force | — | **Regulatory/Historical.** DORA effective 17 January 2025. Not SDLC-controlled. ℹ️ **Regulatory authority function** |

---

### EU AI Act — Artificial Intelligence Act

Regulation (EU) 2024/1689 · Effective 1 August 2024

Applies to AI system providers and deployers in the EU. **All chapters and articles comprehensively mapped below:**

#### EU AI Act Chapter I: General Provisions (Arts. 1–4)

| Article | Title | A-SDLC Control(s) | Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 1** | Subject matter and objective | — | Establishes scope and objectives of AI Act. Compliance achieved through adherence to later chapters. Not directly SDLC-controlled. |
| **Art. 2** | Scope | — | Determines whether AI systems or providers are in scope (EU market, EU users, EU deployers). Entity makes scope determination; not SDLC-controlled. |
| **Art. 3** | Definitions | — | Defines "AI system," "high-risk," "deployer," "provider," "GPAI," etc. Terminology baseline for compliance. Not directly controlled. |
| **Art. 4** | Amendment of Annex I and Annex III | — | Regulatory procedures for updating prohibited/high-risk AI system definitions. Regulatory authority function, not SDLC-controlled. |

#### EU AI Act Chapter II: Prohibited AI Practices (Art. 5)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 5(1)** | Prohibition of AI practices causing harm | SC-1A, SC-3B, AC-1A | **Strong coverage with implementation responsibility.** SC-1A detects adversarial inputs in intent phase; SC-3B scans for injected code post-implementation; AC-1A flags high-risk AI systems that may violate Art. 5 (automated border control, law enforcement). However, **final determination that an AI system violates Art. 5 is entity responsibility** — A-SDLC enables detection but entity must enforce prohibition. ✅ Strong **+ Org-level enforcement** |

#### EU AI Act Chapter III: High-Risk AI Systems (Arts. 6–49)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 6** | Classification of high-risk AI systems | AC-1A | AC-1A classifies AI systems using Annex III high-risk categories at Stage 1 (Intent Ingestion). ✅ Strong |
| **Art. 7** | High-risk classification obligation | AC-1A | AC-1A documents whether a proposed AI system falls under Annex III high-risk categories. ✅ Strong |
| **Art. 8** | Substantial modification of high-risk AI systems | AC-1A, RC-2A | **✅ Partial** — AC-1A re-classifies the AI system when substantial modification occurs; RC-2A updates risk assessment. **Not covered (org responsibility):** Determination of what constitutes "substantial modification" (Art. 8 Annex defines criteria); documentation of substantial modification rationale. A-SDLC provides gates; entity applies policy. |
| **Art. 9** | Risk management system for high-risk AI systems | AC-1A, RC-1A, RC-2A, RC-4A, AC-6A, QC-1B, RC-3A, GC-0A | **✅ Strong** — RC-1A identifies AI risks (Stage 1); RC-2A develops mitigation (Stage 2); AC-1A classifies risk tier; AC-6A monitors post-market (Stage 6); GC-0A maintains audit evidence. Full lifecycle AI risk management. |
| **Art. 10(1)** | Data governance: training data quality | AC-2A, QC-4B | **✅ Partial** — AC-2A documents training data governance procedures; QC-4B validates data quality metrics. **Not covered (org responsibility):** Definition of quality thresholds, acceptable error rates, and data curation standards specific to use case. A-SDLC validates quality; entity sets quality expectations. |
| **Art. 10(2)** | Data governance: prohibited/bias risks | AC-2A, AC-4A | **✅ Strong** — AC-2A identifies prohibited data categories (special categories, biometric data); AC-4A tests model outputs for bias across demographic groups. Both input and output bias controlled. |
| **Art. 10(3)** | Data governance: data filtering and cleaning | AC-2A, QC-4B | **✅ Partial** — AC-2A documents data preprocessing procedures (filtering, cleaning steps); QC-4B validates that cleaning is effective. **Not covered (org responsibility):** Determination of specific cleaning rules and artifact thresholds (e.g., outlier rejection rules). A-SDLC validates effectiveness; entity defines rules. |
| **Art. 10(4)** | Data governance: feedback loop monitoring | AC-2A, AC-6A | **✅ Strong** — AC-2A establishes feedback loop governance; AC-6A monitors real-world performance degradation and triggers retraining/updates post-market. |
| **Art. 10(5)** | Data governance: fundamental rights impact | AC-2A, SC-1B, AC-1A | **✅ Strong** — AC-2A includes fundamental rights impact assessment (privacy, discrimination); SC-1B classifies sensitive data; AC-1A includes rights impact in high-risk classification. Full coverage. |
| **Art. 11** | Technical documentation of high-risk AI systems | AC-2A, QC-4C, AC-2B | **✅ Strong** — AC-2A documents system design, architecture, model training; QC-4C ensures completeness; AC-2B tracks model versions. Full documentation lifecycle. |
| **Art. 11(Annex IV)** | Detailed technical documentation requirements | AC-2A, QC-4C, AC-2B | **✅ Strong** — Annex IV lists 20+ requirements (model card, SHAP values, confusion matrix, performance metrics); AC-2A collects; QC-4C validates completeness; AC-2B archives versions. |
| **Art. 12** | Record-keeping for high-risk AI systems | GC-0A, GC-0B, GC-0D, RC-3A | **✅ Strong** — GC-0A maintains immutable logs of all AI decisions; GC-0B documents risk assessment history; GC-0D tracks compliance evidence; RC-3A logs risk mitigation decisions. Full lifecycle record-keeping. |
| **Art. 13** | Transparency to deployers | AC-2A | **✅ Partial** — AC-2A documents model limitations, performance thresholds, accuracy metrics in technical documentation. **Not covered (org responsibility):** Format and timing of disclosure to deployers; communication strategy. A-SDLC documents what to disclose; entity handles communication. |
| **Art. 14(1)** | Human oversight: capability requirements | AC-2A, SC-2B, QC-4B | **✅ Partial** — AC-2A documents oversight mechanisms; SC-2B injects guardrails enabling human intervention; QC-4B validates accuracy thresholds. **Not covered (org responsibility):** Definition of which human decisions require override capability; procedures for escalation. A-SDLC enables technical capability; entity defines policies. |
| **Art. 14(2–5)** | Human oversight: specific competencies, intervention procedures | — | **ℹ️ Org-level responsibility.** Entity determines who is competent to override AI decisions, when override is permitted, escalation procedures. A-SDLC documents the technical capability for human oversight (SC-2B); entity operationalizes who makes decisions. |
| **Art. 15(1)** | Accuracy, robustness, cybersecurity: general requirement | QC-4A, QC-4B, AC-4A | **✅ Strong** — QC-4A tests functional correctness; QC-4B tests AI output accuracy against thresholds; AC-4A tests robustness to bias and adversarial inputs. |
| **Art. 15(2)** | Accuracy: performance thresholds and metrics | QC-4B, AC-4A | **✅ Strong** — QC-4B establishes and validates accuracy thresholds (precision, recall, F1, AUC); AC-4A validates across demographic subgroups for fairness. |
| **Art. 15(3)** | Robustness to distribution shifts | AC-4A, QC-4B | **✅ Partial** — AC-4A tests adversarial robustness (adversarial examples, input perturbations); QC-4B validates generalization on test sets. **Not covered (org responsibility):** Real-world distribution shift monitoring and retraining triggers. Stage 6 AC-6A monitors post-market; entity determines retraining thresholds. |
| **Art. 15(4)** | Cybersecurity: infrastructure and supply chain security | SC-1A, SC-3A, SC-3B, SC-3D, SC-3E, SC-5A, SC-5B, SC-5C | **✅ Strong** — SC-1A gates adversarial inputs; SC-3A/B enforce access/code security; SC-3D/E scan dependencies/containers; SC-5A/B/C validate infrastructure/deployment. Full security coverage. |
| **Art. 15(5)** | Adversarial robustness testing | SC-4D, AC-4A | **✅ Strong** — SC-4D performs dedicated adversarial testing (prompt injection, model inversion, FGSM attacks); AC-4A validates resistance. |
| **Art. 16** | Conformity assessment for high-risk AI systems | QC-4C, AC-2A, GC-0D | **✅ Partial** — QC-4C verifies documentation completeness against Annex IV; AC-2A provides evidence of risk management; GC-0D compiles compliance file. **Not covered (org responsibility):** External conformity assessment by Notified Body (if applicable); statement of conformity issuance. A-SDLC prepares evidence; entity may commission external auditor. |
| **Art. 17** | Conformity assessment procedure: internal procedure | QC-4C, AC-2A, RC-4A, GC-0D | **✅ Partial** — QC-4C and AC-2A compile technical evidence; RC-4A conducts risk-based approval gate; GC-0D automates compliance file creation. **Not covered (org responsibility):** Signature authority and legal responsibility for statement of conformity. A-SDLC prepares evidence; entity signs and takes legal responsibility. |
| **Art. 18** | Conformity assessment procedure: third-party assessment | — | **ℹ️ Org-level/Third-party function.** Notified Bodies (independent test labs) perform external conformity assessment for high-risk AI systems. Financial entity may commission external assessment; A-SDLC provides evidence (AC-2A, QC-4C) for auditor review. |
| **Art. 19** | Quality management system | QC-1A, QC-1B, QC-2A, QC-3A, QC-3B, QC-4C, QC-5A, QC-6A | **✅ Strong** — All QC controls implement comprehensive quality management across the entire lifecycle: specification, design, implementation, review, testing, release, monitoring. |
| **Art. 20** | Quality management system: documentation | QC-1A, GC-0A, GC-0B, GC-0D | **✅ Strong** — QC-1A establishes feature specifications; GC-0A logs decisions; GC-0B documents change history; GC-0D automates compliance evidence compilation. |
| **Art. 21** | Quality management system: procedures for addressing non-conformities | RC-4A, QC-3B | **✅ Partial** — RC-4A gates risk acceptance (risk-based decision); QC-3B enforces code quality standards. **Not covered (org responsibility):** Definition of specific non-conformity handling procedures (correction, root cause analysis, prevention). A-SDLC provides gates and quality enforcement; entity details procedures. |
| **Art. 22** | Quality management system: evaluation and updates | QC-6A, RC-6A, AC-6A | **✅ Strong** — QC-6A monitors SLOs continuously; RC-6A monitors risk metrics; AC-6A monitors AI model performance. Continuous evaluation enabled. |
| **Art. 23** | Quality management system: supplier/sub-processor involvement | GC-0C, GC-3A, SC-3D | **✅ Partial** — GC-0C tracks provider/model provenance; GC-3A logs code attribution; SC-3D scans supplier dependencies for vulnerabilities. **Not covered (org responsibility):** Vendor qualification, SLA enforcement, and remediation negotiations. A-SDLC tracks supplier code; entity manages vendor relationships. |
| **Art. 24** | Documentation of compliance measures | GC-0A, GC-0D, QC-4C, AC-2A | **✅ Strong** — GC-0A and GC-0D maintain evidence trail; QC-4C verifies completeness; AC-2A documents all compliance measures. Full documentation trail. |
| **Art. 25** | Post-market surveillance plan | AC-2A, AC-6A, GC-0D | **✅ Partial** — AC-2A documents surveillance approach and metrics; AC-6A executes monitoring; GC-0D compiles evidence. **Not covered (org responsibility):** Determination of monitoring frequency, performance drift thresholds, and retraining triggers. A-SDLC enables monitoring; entity sets operational thresholds. |

#### EU AI Act Chapter IV: Transparency Obligations (Art. 50)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 50(1)** | Transparency for certain AI systems (biometric, emotional recognition, etc.) | AC-2A | **✅ Partial** — AC-2A documents that system uses biometric/emotional recognition in technical documentation. **Not covered (org responsibility):** Actual disclosure to users/data subjects (timing, format, method). A-SDLC documents what to disclose; entity handles user communication. |
| **Art. 50(2)** | Disclosure content | AC-2A | **✅ Partial** — AC-2A documents AI system use, purpose, limitations in technical documentation. **Not covered (org responsibility):** Translation to plain language, accessibility for users, and content delivery format. A-SDLC prepares documentation; entity communicates to users. |
| **Art. 50(3)** | Disclosure format | — | **ℹ️ Org-level responsibility.** How entity discloses (UI notice, terms of service, signage, privacy policy) is operational execution. A-SDLC provides source information. |

#### EU AI Act Chapter V: General-Purpose AI Models (Arts. 51–56)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 51** | Transparency obligations for GPAI providers | AC-1B, AC-2A, AC-2B | **✅ Strong** — AC-1B screens whether a change uses GPAI models; AC-2A documents model provenance, capabilities, and limitations; AC-2B tracks model versions, fine-tuning changes, and usage restrictions. Full transparency obligation coverage. |
| **Art. 52** | GPAI transparency: disclosure of training data summary | AC-2A, AC-2B | **✅ Strong** — AC-2A documents training data characteristics (domains covered, size, quality, bias properties); AC-2B maintains model card with training data summary. |
| **Art. 53** | GPAI transparency: copyright safeguards | AC-2A, AC-2B | **✅ Partial** — AC-2A documents model's handling of copyright data; AC-2B tracks model license and permitted use restrictions (commercial, open-source, proprietary). **Not covered (org responsibility):** Copyright compliance verification at source (verifying GPAI provider's copyright practices); legal review of license terms. A-SDLC documents; entity verifies provider compliance. |
| **Art. 54** | GPAI system security measures | AC-2A, SC-5A, SC-5C | **✅ Partial** — AC-2A documents security requirements for GPAI deployment; SC-5A validates GPAI inference infrastructure security baseline; SC-5C manages GPAI API keys and access controls. **Not covered (org responsibility):** Evaluation of GPAI provider's infrastructure security (third-party audit); monitoring provider's security posture over time. A-SDLC secures deployment; entity monitors provider security. |
| **Art. 55** | Systemic risk assessment for GPAI | AC-1B | **✅ Partial** — AC-1B classifies models as standard GPAI or systemic-risk GPAI (>10²⁵ FLOPs training compute); classification triggers monitoring requirements. **Not covered (org responsibility):** Implementing systemic risk mitigations beyond SDLC (third-party testing by independent auditors, EC mandated requirements). A-SDLC identifies risk tier; entity implements mitigations. |
| **Art. 56** | GPAI governance and post-market surveillance | AC-1B, AC-2A, AC-2B, AC-6A | **✅ Strong** — AC-1B identifies GPAI use cases; AC-2A documents fine-tuning changes and limitations; AC-2B tracks versions and model performance; AC-6A monitors performance drift and triggers updates. Full governance and surveillance. |

#### EU AI Act Chapter VI: Measures in Support of Innovation (Arts. 57–63)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Arts. 57–63** | Regulatory sandbox, innovation support programs, guidance | — | **Org-level/Optional.** Regulatory sandboxes are voluntary programs where participants receive guidance on compliance. Not mandatory for A-SDLC execution; optional for entities seeking regulatory feedback during development. ℹ️ **Org-level execution** |

#### EU AI Act Chapter VII: Governance (Arts. 64–70)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Arts. 64–70** | AI Office, AI Board, Transparency and Information Office | — | **Regulatory authority governance.** Articles 64–70 establish European AI Office and national AI Board structures for regulatory oversight. Regulators, not individual SDLCs, govern these institutions. ℹ️ **Regulatory authority function** |

#### EU AI Act Chapter VIII: Post-Market Monitoring, Information Sharing, Market Surveillance (Arts. 71–80)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 71(1)** | Post-market monitoring by deployers: obligation | AC-6A, SC-6A, QC-6A, RC-6A | **✅ Strong** — AC-6A monitors AI model performance post-deployment; SC-6A detects security incidents; QC-6A monitors SLOs; RC-6A monitors operational risks. Full monitoring obligation. |
| **Art. 71(2)** | Post-market monitoring: collection and analysis of data | AC-6A, QC-6A, RC-6A | **✅ Strong** — AC-6A collects model performance metrics; QC-6A collects availability/SLO metrics; RC-6A collects risk metrics. Continuous data collection enabled. |
| **Art. 71(3)** | Post-market monitoring: procedures and tools | AC-6A, QC-6A | **✅ Partial** — AC-6A and QC-6A provide monitoring tooling, dashboards, and alerting procedures (automated detection). **Not covered (org responsibility):** Response procedures (who investigates alerts, escalation thresholds, retraining decisions). A-SDLC detects anomalies; entity determines investigation and mitigation procedures. |
| **Art. 71(4)** | Post-market monitoring: reporting to provider | — | **ℹ️ Org-level responsibility.** Deployer reports findings to AI system provider via operational channels (support tickets, escalations). A-SDLC enables data collection (AC-6A); deployer operationally reports. |
| **Art. 72(1)** | Post-market monitoring by providers: obligation | AC-6A, GC-0D | **✅ Strong** — AC-6A provides tools for providers to gather deployer feedback on performance degradation and issues; GC-0D compiles evidence. Full provider monitoring enabled. |
| **Art. 72(2)** | Post-market monitoring: specific activities | AC-6A, AC-2B, QC-6A | **✅ Strong** — AC-6A monitors for performance degradation; AC-2B tracks model versions across deployments; QC-6A monitors availability/SLOs. Specific monitoring activities implemented. |
| **Art. 72(3)** | Post-market monitoring: procedures and documentation | AC-2A, AC-6A, GC-0D | **✅ Strong** — AC-2A documents monitoring procedures; AC-6A executes monitoring; GC-0D maintains evidence and compliance trail. Full documentation. |
| **Art. 72(4)** | Post-market monitoring: information sharing with deployers | — | **ℹ️ Org-level responsibility.** Provider shares monitoring findings with deployers (security updates, model patches, performance notifications). A-SDLC enables this through AC-6A findings; provider operationally communicates. |
| **Art. 73(1)** | Serious incident reporting: deployer to provider | AC-6A, SC-6A, GC-0A | **✅ Strong** — AC-6A or SC-6A detects serious incident (major accuracy drop, security breach, bias emergence); GC-0A logs with timestamp; deployer reports to provider. Full detection and logging. |
| **Art. 73(2)** | Serious incident reporting: provider to member state authority | — | **ℹ️ Org-level/Provider responsibility.** Provider reports serious incidents to national AI authority. A-SDLC provides incident evidence (AC-6A, SC-6A, GC-0A); provider operationally reports to authority. |
| **Art. 73(3)** | Serious incident reporting: timeline | GC-0A | **✅ Partial** — GC-0A provides timestamped incident logs (immutable evidence of incident detection time) to enable compliance with Art. 73 reporting timelines. **Not covered (org responsibility):** Determination of "serious incident" materiality threshold; notification timeline execution to authority (Art. 73(2) specifies timing but entity operationally implements). A-SDLC provides timestamps; entity determines materiality and notifies. |
| **Art. 74** | Market surveillance: member state authorities | — | **Regulatory authority function.** Member state authorities conduct market surveillance of AI systems. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 75** | Market surveillance: powers | — | **Regulatory authority function.** Authorities have powers to require information, samples, testing. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 76** | Information sharing: national authorities & European Commission | — | **Regulatory authority function.** Authorities share surveillance findings with EC. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 77** | Information sharing: cross-border | — | **Regulatory authority function.** Authorities coordinate cross-border enforcement. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 78** | Serious incident information platform | — | **Regulatory authority function.** EC maintains platform for incident information sharing. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 79** | Notification procedures | — | **Org-level/Regulatory.** Entity and provider notify authorities per defined procedures. A-SDLC enables evidence (AC-6A, SC-6A); entity operationally notifies. ℹ️ **Org-level execution** |
| **Art. 80** | Protection of confidential information | GC-0A | GC-0A manages audit logging with access controls; deployer/provider protect sensitive information during authority reporting. ✅ Partial |

#### EU AI Act Chapter IX: Codes of Conduct and Guidelines (Arts. 81–83)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 81** | Codes of conduct | — | **Voluntary industry standards.** Providers and deployers may adopt codes of conduct (best practices). Not mandatory; A-SDLC enables compliance to adopted codes through controls (SC, QC, AC). ℹ️ **Org-level execution** |
| **Art. 82** | Guidance from competent authorities | — | **Regulatory guidance.** Authorities issue guidance on AI Act compliance. Not SDLC-controlled; guidance informs how entity deploys A-SDLC controls. ℹ️ **Regulatory authority function** |
| **Art. 83** | EU guidelines | — | **Regulatory guidance.** EC issues guidelines on AI Act interpretation. Not SDLC-controlled. ℹ️ **Regulatory authority function** |

#### EU AI Act Chapter X: Confidentiality and Penalties (Arts. 84–99)

| Article | Title | Primary Controls | Coverage & Rationale |
| ------- | ----- | -------- | --------- |
| **Art. 84** | Confidentiality obligations: protection of information | GC-0A, SC-5C | **✅ Partial** — GC-0A maintains audit trail confidentiality with restricted access logs; SC-5C manages secrets/credentials in provider/deployer interfaces (API keys, authentication tokens). **Not covered (org responsibility):** Classification of what information is confidential; encryption of confidential data at rest; physical/legal security measures. A-SDLC protects credentials and logs; entity enforces broader confidentiality policy. |
| **Art. 85** | Confidentiality obligations: authority proceedings | — | **Org-level/Regulatory.** Confidentiality during authority proceedings is legal/procedural. Not SDLC-controlled. ℹ️ **Org-level execution** |
| **Art. 86** | Confidentiality obligations: reporting entities | — | **Org-level responsibility.** Entity determines what information to keep confidential. A-SDLC supports through GC-0A logging. ℹ️ **Org-level execution** |
| **Art. 87** | Confidentiality: trade secrets protection | — | **Org-level/Legal responsibility.** Entity protects trade secrets (model weights, training data, proprietary architectures). A-SDLC enables through AC-2A documentation controls. ℹ️ **Org-level execution** |
| **Art. 88** | Confidentiality: business information | — | **Org-level/Legal responsibility.** Entity protects confidential business information. A-SDLC enables through GC-0A access controls. ℹ️ **Org-level execution** |
| **Art. 89** | Administrative fines: general provision | — | **Regulatory enforcement.** Authorities impose fines for violations. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 90** | Administrative fines: category 1 (general violations) | — | **Regulatory enforcement.** Up to €30M or 6% of global turnover. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 91** | Administrative fines: category 2 (prohibited practices, high-risk violations) | — | **Regulatory enforcement.** Up to €20M or 4% of global turnover. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 92** | Administrative fines: category 3 (transparency, documentation violations) | — | **Regulatory enforcement.** Up to €10M or 2% of global turnover. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 93** | Determination of fines: criteria | — | **Regulatory authority function.** Authorities assess severity, gravity, intent, economic benefit, obligations violated. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 94** | Right of appeal | — | **Legal/Procedural.** Entities may appeal administrative decisions. Not SDLC-controlled. ℹ️ **Org-level execution** |
| **Art. 95** | Penalties for legal entities | — | **Regulatory enforcement.** Legal entities held liable for violations. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 96** | Penalties for natural persons | — | **Regulatory/Criminal.** Member states may impose penalties on individuals. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 97** | Penalties for repeated violations | — | **Regulatory enforcement.** Enhanced penalties for repeated violations. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 98** | Enforcement powers | — | **Regulatory authority function.** Authorities enforce AI Act provisions. Not SDLC-controlled. ℹ️ **Regulatory authority function** |
| **Art. 99** | Transitional provisions and repeal | — | **Regulatory/Historical.** Timeline for implementation and repeals of prior directives. Not SDLC-controlled. ℹ️ **Regulatory authority function** |

---

### Coverage Interpretation Guide

**✅ Strong:** Explicit control(s) directly verify or enforce this obligation

**✅ Partial:** Control(s) address part of the obligation; remaining aspects handled operationally

**⚠️ Not Mapped:** Obligation exists but falls outside A-SDLC scope

**ℹ️ Org-level execution:** Obligation is non-technical or organizational governance (not lifecycle-controlled); entity determines policy, timeline, or enforcement

**ℹ️ Regulatory authority function:** Obligation is administered by competent authorities (ECB, EBA, national authorities, EC); outside SDLC control

---

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
