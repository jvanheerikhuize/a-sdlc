# Stage 4: Testing & Documentation

The verification gate where everything from Stage 3 is rigorously examined. Answers two questions: **"does it work correctly?"** and **"is it safe to release?"**

This stage culminates in a risk threshold evaluation (RC-4A) that produces one of three outcomes: pass, conditional pass (with human risk acceptance), or fail (return to Stage 3).

## Steps

Full step-by-step process with roles and decision points: [process.md](process.md)

| Step | Name | Delegation | Sequencing |
| ---- | ---- | ---------- | ---------- |
| [4.1](process.md#step-41--sast) | SAST | Fully automated | Runs first on merged code |
| [4.2](process.md#step-42--functional--non-functional-testing) | Functional & Non-Functional Testing | Agent executes, QA reviews | Parallel with 4.3, 4.4, 4.5, 4.6 |
| [4.3](process.md#step-43--dast) | DAST | Fully automated | Parallel with 4.2, 4.4, 4.5, 4.6 |
| [4.4](process.md#step-44--ai-output-validation-conditional) | AI Output Validation *(conditional)* | Agent executes, AGL reviews | Parallel with 4.2, 4.3, 4.5, 4.6 |
| [4.5](process.md#step-45--bias--fairness-testing-conditional) | Bias & Fairness Testing *(conditional)* | Agent executes, AGL reviews | Parallel with 4.2, 4.3, 4.4, 4.6 |
| [4.6](process.md#step-46--documentation-completeness) | Documentation Completeness | Agent checks, human approves | Parallel with 4.2, 4.3, 4.4, 4.5 |
| [4.7](process.md#step-47--risk-threshold-evaluation) | Risk Threshold Evaluation | Agent calculates, RO decides | After 4.1–4.6 all complete |

## Controls

Stage definition (required controls + exit criteria): [04-testing-documentation.yaml](04-testing-documentation.yaml)

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| [SC-4A](../../controls/sc/SC-4A.yaml) | SAST | Static security analysis of full codebase for CWE-mapped vulnerabilities. Heightened scrutiny on agent-generated code. | Fully automated | DORA: Art. 24; DNB: Security testing; AI Act: Art. 15(2) |
| [QC-4A](../../controls/qc/QC-4A.yaml) | Functional & Non-Functional Testing | Full test suite against Stage 1 acceptance criteria: functional, performance, load, accessibility, regression. | Agent executes, QA reviews | DORA: Art. 8(4); DNB: OTAP; AI Act: Art. 15(1) |
| [SC-4B](../../controls/sc/SC-4B.yaml) | DAST | Runtime security testing: injection attacks, auth flaws, session management, TLS configuration, OWASP Top 10. | Fully automated | DORA: Art. 24, Art. 25; DNB: Penetration testing; AI Act: Art. 15(3) |
| [QC-4B](../../controls/qc/QC-4B.yaml) | AI Output Validation *(conditional)* | For AI components: hallucination detection, accuracy benchmarking, output consistency, and boundary testing. | Agent executes, AGL reviews | AI Act: Art. 15(1); Art. 9(7) |
| [AC-4A](../../controls/ac/AC-4A.yaml) | Bias & Fairness Testing *(conditional)* | For AI components: tests for discriminatory outcomes across protected characteristics. | Agent executes, AGL reviews | AI Act: Art. 10(2)(f); Art. 10(5); Art. 15(1) |
| [QC-4C](../../controls/qc/QC-4C.yaml) | Documentation Completeness | Verifies runbooks, API docs, ADRs, and decision logs are present and current. | Agent checks, human approves | DORA: Art. 8(6); DNB: Documentation standards; AI Act: Art. 11, Annex IV |
| [RC-4A](../../controls/rc/RC-4A.yaml) | Risk Threshold Evaluation | Aggregates all Stage 4 results. Determines whether residual risk is within appetite. Formal go/no-go decision. | Agent calculates, RO decides | DORA: Art. 8(1); DNB: Risk acceptance; AI Act: Art. 9(2)(a) |

## Stage Exit Criteria

All of the following must be true before progressing to Stage 5:

- [ ] SC-4A passed: no critical or high CWE-mapped vulnerabilities unresolved
- [ ] QC-4A passed: all functional and NFR tests passing against Stage 1 acceptance criteria
- [ ] SC-4B passed: no critical or high runtime security findings unresolved
- [ ] QC-4B passed (if AI component): no hallucination or accuracy threshold breaches
- [ ] AC-4A passed (if AI component): no discriminatory outcomes exceeding defined thresholds
- [ ] QC-4C passed: all documentation complete and current
- [ ] RC-4A completed: go/no-go decision is pass or approved conditional pass

## Artifacts

- **Process:** [process.md](process.md) — Step-by-step guide with roles, dependencies, and decision points
- **Directives:** [../../directives/stages/04-testing-documentation.yaml](../../directives/stages/04-testing-documentation.yaml) — SC-2B injection payload (immutable)

**Inputs (from Stages 1 and 3):**

- [feature-spec.yaml](../01-intent-ingestion/artifacts/outputs/feature-spec.yaml) — Acceptance criteria test basis (QC-1A output)
- [ai-tier-classification.yaml](../01-intent-ingestion/artifacts/outputs/ai-tier-classification.yaml) — AI risk tier (AC-1A output, if applicable)
- [pull-request-record.yaml](../03-coding-implementation/artifacts/outputs/pull-request-record.yaml) — Merged PR (QC-3A output)

**Outputs:**

- [artifacts/outputs/sast-scan-report.yaml](artifacts/outputs/sast-scan-report.yaml) — SC-4A output
- [artifacts/outputs/test-results-report.yaml](artifacts/outputs/test-results-report.yaml) — QC-4A output
- [artifacts/outputs/dast-scan-report.yaml](artifacts/outputs/dast-scan-report.yaml) — SC-4B output
- [artifacts/outputs/ai-output-validation-report.yaml](artifacts/outputs/ai-output-validation-report.yaml) — QC-4B output (if AI component)
- [artifacts/outputs/bias-fairness-report.yaml](artifacts/outputs/bias-fairness-report.yaml) — AC-4A output (if AI component)
- [artifacts/outputs/documentation-completeness-report.yaml](artifacts/outputs/documentation-completeness-report.yaml) — QC-4C output
- [artifacts/outputs/risk-threshold-evaluation.yaml](artifacts/outputs/risk-threshold-evaluation.yaml) — RC-4A output
