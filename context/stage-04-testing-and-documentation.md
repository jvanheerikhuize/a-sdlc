# Stage 4 — Testing & Documentation

> **Auto-generated from `stages/04-testing-documentation/04-testing-documentation.yaml`** · Agent context bundle · All controls and workflow in one file

Validate the implementation against all acceptance criteria, security requirements, and documentation standards. RC-4A is the formal go/no-go gate for deployment. No change proceeds to Stage 5 without a passing or conditionally accepted RC-4A result.

---

## Quick Load

Load these files for this stage:

```
- stages/04-testing-documentation/04-testing-documentation.yaml
- directives/stages/04-testing-and-documentation.yaml
```

---

## Workflow — Execution Order

| Step | Title | Control | Actors | Delegation | Depends On |
| ---- | ----- | ------- | ------ | ---------- | ---------- |
| 4.1 | SAST | SC-4A | AGT, AGT, SA | Fully automated | — |
| 4.2 | Functional & Non-Functional Testing | QC-4A | AGT, AGT, AGT, QA | Agent executes, QA reviews | n-sc4a |
| 4.3 | DAST | SC-4B | AGT, AGT, SA | Fully automated | n-sc4a |
| 4.4 | AI Output Validation | QC-4B | AGT, AGT, AGL | Agent executes, AGL reviews | n-sc4a |
| 4.5 | Bias & Fairness Testing | AC-4A | AGT, AGT, AGL | Agent executes, AGL reviews | n-sc4a |
| 4.6 | Documentation Completeness | QC-4C | AGT, AGT, AGT, QA | Agent checks, human approves | n-sc4a |
| 4.2-api | API Security Testing | SC-4C | AGT, SA | Fully automated | n-sc4a |
| 4.7-ai-adversarial | Adversarial AI Robustness Testing | SC-4D | AGT, SA | Fully automated | n-sc4a |
| 4.8 | Risk Threshold Evaluation | RC-4A | AGT, AGT, RO, RO | Agent calculates, RO decides | n-qc4a, n-sc4b, n-qc4b, n-ac4a, n-qc4c, n-sc4c, n-sc4d |

---

## Controls — What Agent and Human Do

| ID | Name | Delegation | Agent Does | Human Does |
| -- | ---- | ---------- | ---------- | ---------- |
| QC-4A | Functional & Non-Functional Testing | agent_executes_human_reviews | Execute full test suite; generate pass/fail report mapped to acceptance criteria. | Review test results; investigate failures; determine if failures block release or require fix. |
| QC-4B | AI Output Validation | agent_executes_human_reviews | Execute AI validation test suite; measure hallucination rate, accuracy, and consistency. | Review AI validation results; determine if accuracy thresholds are acceptable for release. |
| QC-4C | Documentation Completeness | agent_checks_human_approves | Verify all required documentation exists and is current against the implementation; flag gaps. | Review documentation completeness report; approve or require documentation updates. |
| SC-4A | SAST | fully_automated | Execute static analysis scan across full codebase; map findings to CWE; generate findings report. | Review findings; triage; remediate or accept residual risk per severity policy. |
| SC-4B | DAST | fully_automated | Execute runtime security test suite against test environment; generate findings report. | Review findings; remediate or formally accept residual risk per severity policy. |
| SC-4C | API Security Testing | agent_executes_human_reviews | Execute OWASP API Security Top 10 testing using automated tools (Burp Suite, OWASP ZAP API scanner, or equivalent). Perform fuzzing, schema validation testing, authentication boundary testing, and authorisation logic testing. Generate findings report with severity ratings and remediation guidance. | Review findings. Determine which vulnerabilities must be remediated before deployment (blocker), which can be accepted as known risks (exception), and which are false positives. Approve remediation or exception for each finding. |
| AC-4A | Bias & Fairness Testing | agent_executes_human_reviews | Execute bias and fairness test suite across protected characteristic groups; measure disparate impact. | Review bias test results; determine if disparate impact is within acceptable thresholds. |
| SC-4D | Adversarial AI Robustness Testing | agent_executes_human_reviews | Execute adversarial robustness tests: prompt injection fuzzing, input perturbation testing, model extraction attacks, membership inference probes. Generate adversarial examples using techniques (FGSM, PGD, C&W). Measure accuracy degradation. Report findings. | Review adversarial test findings. Determine: is the accuracy degradation acceptable? Are inference endpoints sufficiently hardened? Request design changes (input validation, rate limiting, model hardening) if robustness is insufficient. |
| RC-4A | Risk Threshold Evaluation | agent_calculates_human_decides | Aggregate all Stage 4 results; calculate residual risk score; present recommendation with supporting evidence. | Make the formal go/no-go decision. For conditional pass: provide documented risk acceptance. |
---

## Exit Criteria (Stage 4 Complete When)

- [ ] QC-4A: All acceptance criteria from Stage 1 have passing tests
- [ ] QC-4B: AI output validation passed within defined accuracy thresholds (or not-applicable)
- [ ] QC-4C: Documentation completeness confirmed and approved
- [ ] SC-4A: SAST passed — no critical or high-severity findings unresolved
- [ ] SC-4B: DAST passed — no critical or high-severity findings unresolved
- [ ] SC-4C: API security testing passed — no OWASP API Top 10 violations unresolved
- [ ] AC-4A: Bias & fairness test passed within defined thresholds (or not-applicable)
- [ ] SC-4D: Adversarial robustness testing completed (if applicable for high-risk AI)
- [ ] RC-4A: Go/no-go decision is PASS or CONDITIONAL PASS with formal risk acceptance

---

## Artifact I/O

**Inputs from Prior Stage:**
- ../01-intent-ingestion/artifacts/outputs/QC-1A-feature-spec.yaml
- ../01-intent-ingestion/artifacts/outputs/AC-1A-ai-tier-classification.yaml
- ../03-coding-implementation/artifacts/outputs/QC-3A-pull-request-record.yaml

**Outputs to Next Stage:**
- artifacts/outputs/QC-4A-test-results-report.yaml
- artifacts/outputs/SC-4A-sast-scan-report.yaml
- artifacts/outputs/SC-4B-dast-scan-report.yaml
- artifacts/outputs/QC-4C-documentation-completeness-report.yaml
- artifacts/outputs/QC-4B-ai-output-validation-report.yaml
- artifacts/outputs/AC-4A-bias-fairness-report.yaml
- artifacts/outputs/RC-4A-risk-threshold-evaluation.yaml
- artifacts/outputs/SC-4C-api-security-report.yaml
- artifacts/outputs/SC-4D-adversarial-robustness-report.yaml

---

## Feedback Loop Triggers

Controls in this stage that can trigger re-entry:

- QC-4A → path_a or path_b
- SC-4A → path_a or path_b
- RC-4A → path_a or path_b

For full feedback loop definitions, see [`feedbackloops/feedback-loops.yaml`](../../feedbackloops/feedback-loops.yaml).

---

**Last Updated:** 2026-03-06 07:42 UTC