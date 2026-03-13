<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/04-testing-documentation/stage.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 4: Testing & Documentation — Process

**Stage:** 04-Testing & Documentation
**Purpose:** Validate the implementation against all acceptance criteria, security requirements, and documentation standards. RC-05 is the formal go/no-go gate for deployment. No change proceeds to Stage 5 without a passing or conditionally accepted RC-05 result.

## Roles

| Code | Name | Mode | Responsibilities |
|------|------|------|------------------|
| TENG | Test Engineer | Autonomous | Executes test suites; runs scans; checks documentation completeness; calculates risk threshold; presents evidence |
| QA | QA Engineer | Gated | Reviews functional and NFR test results; investigates failures; approves documentation completeness |
| SA | Security Architect | Gated | Reviews SAST and DAST findings; triages CWE-mapped vulnerabilities; approves risk acceptance for security findings |
| AGL | AI Governance Lead | Gated | Reviews AI output validation and bias test results; approves AI-specific risk acceptance |
| RO | Risk Officer | Gated | Makes the formal go/no-go decision at RC-05; provides documented risk acceptance for conditional pass |
| CO | Compliance Officer | Gated | Reviews documentation artefacts and test evidence during regulatory audits |

## Process Steps

### Step 4.1 — SAST

**Control:** [`SC-12`](../../controls/sc/SC-12.yaml) · **Delegation:** Fully automated

SAST (static application security testing)

| Actor | Action |
|-------|--------|
| `AGT` | Execute static analysis scan across the full codebase; apply heightened scrutiny to agent-generated code |
| `AGT` | Map all findings to CWE categories; assign severity ratings |
| `SA` | Review findings; triage critical and high findings; remediate or document risk acceptance |

**Input:** Merged source code from Stage 3

**Output:** SAST scan report (artifacts/outputs/sast-scan-report.yaml)


### Step 4.2 — Functional & Non-Functional Testing

**Control:** [`QC-06`](../../controls/qc/QC-06.yaml) · **Delegation:** Agent executes, QA reviews

Functional and non-functional testing

| Actor | Action |
|-------|--------|
| `AGT` | Execute functional tests mapped to every Stage 1 acceptance criterion |
| `AGT` | Execute regression, negative, boundary, performance, load, stress, accessibility, and resilience tests |
| `AGT` | Produce pass/fail report with each result traced to its originating acceptance criterion |
| `QA` | Review test results; investigate failures; determine if failures block release or require Stage 3 return |

**Input:** Merged code + Stage 1 feature specification (acceptance criteria)

**Output:** Test results report (artifacts/outputs/test-results-report.yaml)


### Step 4.3 — DAST

**Control:** [`SC-13`](../../controls/sc/SC-13.yaml) · **Delegation:** Fully automated

DAST (dynamic application security testing)

| Actor | Action |
|-------|--------|
| `AGT` | Execute runtime security test suite against deployed test environment |
| `AGT` | Test injection attacks, authentication flaws, session management, TLS, OWASP Top 10 categories |
| `SA` | Review findings; remediate or formally accept residual risk per severity policy |

**Input:** Application deployed to test environment

**Output:** DAST scan report (artifacts/outputs/dast-scan-report.yaml)


### Step 4.4 — AI Output Validation

**Control:** [`QC-07`](../../controls/qc/QC-07.yaml) · **Delegation:** Agent executes, AGL reviews

> **Conditional:** Only applicable when the change involves an AI component. If not applicable, document as not_applicable.

AI output validation (conditional on ai_component)

| Actor | Action |
|-------|--------|
| `AGT` | Execute hallucination detection tests; measure accuracy against defined thresholds |
| `AGT` | Run output consistency tests across equivalent inputs; execute boundary condition tests |
| `AGL` | Review AI validation results; determine whether accuracy thresholds are acceptable for release |

**Input:** AI component deployed to test environment + AI tier classification from Stage 1

**Output:** AI output validation report (artifacts/outputs/ai-output-validation-report.yaml)


### Step 4.5 — Bias & Fairness Testing

**Control:** [`AC-05`](../../controls/ac/AC-05.yaml) · **Delegation:** Agent executes, AGL reviews

> **Conditional:** Only applicable when the change involves an AI component. If not applicable, document as not_applicable.

Bias and fairness testing (conditional on ai_component)

| Actor | Action |
|-------|--------|
| `AGT` | Execute bias test suite across protected characteristic groups (age, gender, ethnicity, disability) |
| `AGT` | Measure disparate impact for each group; compare against defined thresholds |
| `AGL` | Review bias test results; determine if disparate impact is within acceptable thresholds |

**Input:** AI component deployed to test environment

**Output:** Bias & fairness report (artifacts/outputs/bias-fairness-report.yaml)


### Step 4.6 — Documentation Completeness

**Control:** [`QC-08`](../../controls/qc/QC-08.yaml) · **Delegation:** Agent checks, human approves

Documentation completeness

| Actor | Action |
|-------|--------|
| `AGT` | Verify all required documentation exists and is current: runbooks, API docs, ADRs, Stage 3 decision log |
| `AGT` | For AI components: verify AI Act technical documentation (Annex IV) is complete |
| `AGT` | Flag any gaps or outdated documentation |
| `QA` | Review documentation completeness report; approve or require documentation updates |

**Input:** All documentation artefacts from the change

**Output:** Documentation completeness report (artifacts/outputs/documentation-completeness-report.yaml)


### Step 4.2-api — API Security Testing

**Control:** [`SC-14`](../../controls/sc/SC-14.yaml) · **Delegation:** Fully automated

API security testing (OWASP API Top 10)

| Actor | Action |
|-------|--------|
| `AGT` | Execute OWASP API Security Top 10 test suite against all exposed APIs |
| `SA` | Review findings; remediate critical issues or provide risk acceptance |

**Input:** Deployed APIs

**Output:** API security test report (artifacts/outputs/api-security-report.yaml)


### Step 4.7-ai-adversarial — Adversarial AI Robustness Testing

**Control:** [`SC-15`](../../controls/sc/SC-15.yaml) · **Delegation:** Fully automated

> **Conditional:** Only applicable for high-risk or security-critical AI deployments. If not applicable, document as not_applicable.

Adversarial AI robustness testing (conditional on high-risk AI)

| Actor | Action |
|-------|--------|
| `AGT` | Generate adversarial test inputs to probe AI model robustness |
| `SA` | Review results; assess susceptibility to adversarial attack |

**Input:** AI model + adversarial test suite

**Output:** Adversarial robustness report (artifacts/outputs/adversarial-robustness-report.yaml)


### Step 4.8 — Risk Threshold Evaluation

**Control:** [`RC-05`](../../controls/rc/RC-05.yaml) · **Delegation:** Agent calculates, RO decides

Risk threshold evaluation and go/no-go gate

| Actor | Action |
|-------|--------|
| `AGT` | Aggregate all Stage 4 control results; calculate residual risk score |
| `AGT` | Present recommendation with supporting evidence from each control |
| `RO` | Review aggregated results; make formal go/no-go decision |
| `RO` | For conditional pass: provide documented risk acceptance signed with identity and timestamp |

**Input:** All Stage 4 control outputs (steps 4.1-4.7)

**Output:** Risk threshold evaluation (artifacts/outputs/risk-threshold-evaluation.yaml)


## Exit Criteria

- QC-06: All acceptance criteria from Stage 1 have passing tests
- QC-07: AI output validation passed within defined accuracy thresholds (or not-applicable)
- QC-08: Documentation completeness confirmed and approved
- SC-12: SAST passed — no critical or high-severity findings unresolved
- SC-13: DAST passed — no critical or high-severity findings unresolved
- SC-14: API security testing passed — no OWASP API Top 10 violations unresolved
- AC-05: Bias & fairness test passed within defined thresholds (or not-applicable)
- SC-15: Adversarial robustness testing completed (if applicable for high-risk AI)
- RC-05: Go/no-go decision is PASS or CONDITIONAL PASS with formal risk acceptance


## Output Artifacts

- `artifacts/outputs/QC-06-test-results-report.yaml`
- `artifacts/outputs/SC-12-sast-scan-report.yaml`
- `artifacts/outputs/SC-13-dast-scan-report.yaml`
- `artifacts/outputs/QC-08-documentation-completeness-report.yaml`
- `artifacts/outputs/QC-07-ai-output-validation-report.yaml`
- `artifacts/outputs/AC-05-bias-fairness-report.yaml`
- `artifacts/outputs/RC-05-risk-threshold-evaluation.yaml`
- `artifacts/outputs/SC-14-api-security-report.yaml`
- `artifacts/outputs/SC-15-adversarial-robustness-report.yaml`


## References

- Stage definition: 
- Controls: See `required_controls` in stage YAML.

---

**Last Updated:** 2026-03-13 14:19 UTC
