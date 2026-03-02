# Stage 4: Testing & Documentation

The verification gate where everything from Stage 3 is rigorously examined. Answers two questions: **"does it work correctly?"** and **"is it safe to release?"**

This stage culminates in a risk threshold evaluation (RC-4A) that produces one of three outcomes: pass, conditional pass (with human risk acceptance), or fail (return to Stage 3).

## Key Tasks

- Map every acceptance criterion from Stage 1 to at least one test case
- Execute functional, regression, negative, and boundary test suites
- Execute non-functional tests: performance, load, stress, accessibility, resilience
- For AI components: run hallucination detection, accuracy, and consistency tests
- For AI components: execute bias and fairness testing across protected groups
- Run full SAST and DAST scans including heightened scrutiny of agent-generated code
- Verify all documentation is complete, current, and matches actual implementation
- Aggregate all results into risk threshold evaluation: pass, conditional pass, or fail
- For conditional pass: obtain risk acceptance from appropriate authority

## Controls

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| QC-4A | Functional & Non-Functional Testing | Full test suite against Stage 1 acceptance criteria: functional, performance, load, accessibility, regression. | Agent executes, human reviews | DORA: Art. 8(4); DNB: OTAP; AI Act: Art. 15(1) |
| QC-4B | AI Output Validation | For AI systems: hallucination detection, accuracy benchmarking, consistency, and boundary testing. | Agent executes, human reviews | AI Act: Art. 15(1); Art. 9(7) |
| QC-4C | Documentation Completeness | Verifies runbooks, API docs, ADRs, and decision logs are present and current. | Agent checks, human approves | DORA: Art. 8(6); DNB: Documentation standards; AI Act: Art. 11, Annex IV |
| RC-4A | Risk Threshold Evaluation | Aggregates all Stage 4 results. Determines whether residual risk is within appetite. Go/no-go decision. | Agent calculates, human decides | DORA: Art. 8(1); DNB: Risk acceptance; AI Act: Art. 9(2)(a) |
| SC-4A | SAST | Static security analysis of full codebase for vulnerabilities mapped to CWE categories. | Fully automated | DORA: Art. 24; DNB: Security testing; AI Act: Art. 15(2) |
| SC-4B | DAST | Runtime security testing: injection attacks, auth flaws, session management, TLS configuration. | Fully automated | DORA: Art. 24, Art. 25; DNB: Penetration testing; AI Act: Art. 15(3) |
| AC-4A | Bias & Fairness Testing | For AI systems: tests for discriminatory outcomes across protected characteristics. | Agent executes, human reviews | AI Act: Art. 10(2)(f); Art. 10(5); Art. 15(1) |

Stage definition (required controls + exit criteria): [stage.yaml](stage.yaml)

Individual control definitions by track:
  - [AC-4A](../../controls/ac/AC-4A.yaml)
  - [QC-4A](../../controls/qc/QC-4A.yaml), [QC-4B](../../controls/qc/QC-4B.yaml), [QC-4C](../../controls/qc/QC-4C.yaml)
  - [RC-4A](../../controls/rc/RC-4A.yaml)
  - [SC-4A](../../controls/sc/SC-4A.yaml), [SC-4B](../../controls/sc/SC-4B.yaml)

## Stage Exit Criteria

All of the following must be true before progressing to Stage 5:

- [ ] QC-4A passed: all functional and NFR tests passing against Stage 1 criteria
- [ ] QC-4B passed (if AI component): no hallucination or accuracy threshold breaches
- [ ] QC-4C passed: all documentation complete and current
- [ ] SC-4A passed: no critical or high CWE-mapped vulnerabilities outstanding
- [ ] SC-4B passed: no critical runtime security findings outstanding
- [ ] AC-4A passed (if AI component): no discriminatory outcomes detected
- [ ] RC-4A completed: risk threshold evaluation result is pass or approved conditional pass
