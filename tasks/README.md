<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: tasks.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Task Navigation Index

**Version:** 1.0
**Tasks:** 29 tasks across 6 stages + cross-cutting

Agent task index — maps common tasks to stages, controls, and entry files

## How to Use

1. Identify the task you need to perform (e.g., *"write code"*, *"run SAST"*)
2. Find the matching task ID in the quick-reference table below
3. Load the **Entry file** — it provides workflow, controls, actors, and exit criteria
4. For any specific control listed, load: `controls/[track]/[CONTROL-ID].yaml`

## Quick Reference

| Stage | Task ID | Name | Entry File |
|-------|---------|------|------------|
| Cross-cutting | `execute-path-a-quick-fix` | Execute Path A quick-fix flow | `feedbackloops/feedback-loops.yaml` |
| Cross-cutting | `execute-path-b-full-reentry` | Execute Path B full re-entry flow | `feedbackloops/feedback-loops.yaml` |
| Cross-cutting | `feedback-loop-classification` | Classify incident for feedback loop re-entry | `feedbackloops/feedback-loops.yaml` |
| Stage 1 | `classify-ai-risk` | Classify AI risk level for a new system | `controls/ac/AC-01.yaml` |
| Stage 1 | `ingest-feature-request` | Ingest a new feature request | `context/stage-01-intent-ingestion.md` |
| Stage 1 | `validate-feature-intent` | Validate and refine feature intent | `controls/qc/QC-01.yaml` |
| Stage 2 | `create-system-design` | Create system design and architecture | `context/stage-02-system-design.md` |
| Stage 2 | `design-review` | Hold design review with stakeholders | `controls/rc/RC-03.yaml` |
| Stage 2 | `threat-model` | Run threat modelling | `controls/sc/SC-05.yaml` |
| Stage 3 | `log-code-provenance` | Log code provenance and authorship | `controls/gc/GC-03.yaml` |
| Stage 3 | `review-pull-request` | Review a pull request | `controls/qc/QC-04.yaml` |
| Stage 3 | `scan-for-exposed-credentials` | Scan for exposed credentials or secrets | `controls/sc/SC-09.yaml` |
| Stage 3 | `scan-for-malicious-code` | Scan agent-generated code for malicious patterns | `controls/sc/SC-08.yaml` |
| Stage 3 | `validate-agent-permissions` | Validate agent permission boundaries | `controls/sc/SC-07.yaml` |
| Stage 3 | `write-code` | Write or generate code | `context/stage-03-coding-and-implementation.md` |
| Stage 4 | `evaluate-risk-threshold` | Evaluate risk threshold before deployment | `controls/rc/RC-05.yaml` |
| Stage 4 | `run-api-security-testing` | Run API-specific security testing | `controls/sc/SC-14.yaml` |
| Stage 4 | `run-dast` | Run dynamic security analysis (DAST) | `controls/sc/SC-13.yaml` |
| Stage 4 | `run-sast` | Run static security analysis (SAST) | `controls/sc/SC-12.yaml` |
| Stage 4 | `run-tests` | Run automated tests | `controls/qc/QC-06.yaml` |
| Stage 4 | `validate-ai-testing` | Validate AI component testing | `controls/ac/AC-05.yaml` |
| Stage 4 | `write-documentation` | Write technical and operational documentation | `controls/qc/QC-08.yaml` |
| Stage 5 | `deploy-to-production` | Deploy to production | `context/stage-05-deployment-and-release.md` |
| Stage 5 | `prepare-rollback-plan` | Prepare and test rollback plan | `controls/rc/RC-07.yaml` |
| Stage 5 | `verify-deployment-integrity` | Verify deployed artefact integrity | `controls/sc/SC-17.yaml` |
| Stage 6 | `conduct-ai-post-market-surveillance` | Conduct AI post-market surveillance | `controls/ac/AC-06.yaml` |
| Stage 6 | `detect-model-anomaly` | Detect AI model anomaly or drift | `controls/ac/AC-06.yaml` |
| Stage 6 | `detect-security-incident` | Detect and triage security incident | `feedbackloops/feedback-loops.yaml` |
| Stage 6 | `monitor-production` | Monitor production health and SLOs | `context/stage-06-observability-and-maintenance.md` |


## Stage 1: Intent Ingestion

### `ingest-feature-request` — Ingest a new feature request

Capture, disambiguate, and structure a new business requirement into a feature specification

| Field | Value |
|-------|-------|
| **Controls** | `QC-01, QC-02, RC-01, SC-03, SC-04, AC-01, AC-02, GC-05` |
| **Entry file** | `context/stage-01-intent-ingestion.md` |

### `classify-ai-risk` — Classify AI risk level for a new system

Determine risk tier under EU AI Act; impacts testing, controls, and documentation

| Field | Value |
|-------|-------|
| **Controls** | `AC-01, AC-02` |
| **Entry file** | `controls/ac/AC-01.yaml` |

### `validate-feature-intent` — Validate and refine feature intent

Confirm that business requirements are unambiguous and architecturally feasible

| Field | Value |
|-------|-------|
| **Controls** | `QC-01, QC-02` |
| **Entry file** | `controls/qc/QC-01.yaml` |


## Stage 2: System Design

### `create-system-design` — Create system design and architecture

Translate validated intent into architecture, data flows, and technical specifications

| Field | Value |
|-------|-------|
| **Controls** | `QC-03, RC-02, RC-03, SC-05, SC-06, AC-03, AC-04` |
| **Entry file** | `context/stage-02-system-design.md` |

### `threat-model` — Run threat modelling

Identify potential security threats and design mitigations before coding begins

| Field | Value |
|-------|-------|
| **Controls** | `SC-05` |
| **Entry file** | `controls/sc/SC-05.yaml` |

### `design-review` — Hold design review with stakeholders

Validate architecture and risk profile before proceeding to implementation

| Field | Value |
|-------|-------|
| **Controls** | `RC-03` |
| **Entry file** | `controls/rc/RC-03.yaml` |


## Stage 3: Coding & Implementation

### `write-code` — Write or generate code

Produce code by human developers, AI agents, or both. Enforce quality and security scanning

| Field | Value |
|-------|-------|
| **Controls** | `SC-07, QC-05, SC-09, SC-10, SC-11, RC-04, GC-03, SC-08, QC-04` |
| **Entry file** | `context/stage-03-coding-and-implementation.md` |

### `review-pull-request` — Review a pull request

Human code review of changes before merge; check quality gates and security scan results

| Field | Value |
|-------|-------|
| **Controls** | `QC-04` |
| **Entry file** | `controls/qc/QC-04.yaml` |

### `scan-for-malicious-code` — Scan agent-generated code for malicious patterns

Automated scan to prevent injection, backdoors, and policy violations in AI-generated code

| Field | Value |
|-------|-------|
| **Controls** | `SC-08` |
| **Entry file** | `controls/sc/SC-08.yaml` |

### `scan-for-exposed-credentials` — Scan for exposed credentials or secrets

Detect hardcoded API keys, passwords, and other sensitive data before commit

| Field | Value |
|-------|-------|
| **Controls** | `SC-09` |
| **Entry file** | `controls/sc/SC-09.yaml` |

### `validate-agent-permissions` — Validate agent permission boundaries

Ensure agent has not exceeded scoped permissions during code generation

| Field | Value |
|-------|-------|
| **Controls** | `SC-07` |
| **Entry file** | `controls/sc/SC-07.yaml` |

### `log-code-provenance` — Log code provenance and authorship

Track whether code was human-written, AI-generated, or hybrid; maintain attribution

| Field | Value |
|-------|-------|
| **Controls** | `GC-03` |
| **Entry file** | `controls/gc/GC-03.yaml` |


## Stage 4: Testing & Documentation

### `run-tests` — Run automated tests

Execute unit, integration, and end-to-end tests; validate coverage

| Field | Value |
|-------|-------|
| **Controls** | `QC-06, QC-07` |
| **Entry file** | `controls/qc/QC-06.yaml` |

### `run-sast` — Run static security analysis (SAST)

Scan code for common vulnerabilities, policy violations, and insecure patterns

| Field | Value |
|-------|-------|
| **Controls** | `SC-12` |
| **Entry file** | `controls/sc/SC-12.yaml` |

### `run-dast` — Run dynamic security analysis (DAST)

Test running application for runtime vulnerabilities, API issues, and data flow problems

| Field | Value |
|-------|-------|
| **Controls** | `SC-13` |
| **Entry file** | `controls/sc/SC-13.yaml` |

### `run-api-security-testing` — Run API-specific security testing

Test API endpoints for injection, authentication bypass, and data exposure

| Field | Value |
|-------|-------|
| **Controls** | `SC-14` |
| **Entry file** | `controls/sc/SC-14.yaml` |

### `evaluate-risk-threshold` — Evaluate risk threshold before deployment

Assess residual risk against organizational tolerance; gate progression to Stage 5

| Field | Value |
|-------|-------|
| **Controls** | `RC-05` |
| **Entry file** | `controls/rc/RC-05.yaml` |

### `write-documentation` — Write technical and operational documentation

Create README, API docs, runbooks, and operational guides

| Field | Value |
|-------|-------|
| **Controls** | `QC-08, AC-05` |
| **Entry file** | `controls/qc/QC-08.yaml` |

### `validate-ai-testing` — Validate AI component testing

Run bias tests, adversarial tests, and data validation for AI-based systems

| Field | Value |
|-------|-------|
| **Controls** | `AC-05` |
| **Entry file** | `controls/ac/AC-05.yaml` |


## Stage 5: Deployment & Release

### `deploy-to-production` — Deploy to production

Promote tested artefact to production with governance, rollback readiness, and monitoring setup

| Field | Value |
|-------|-------|
| **Controls** | `QC-09, RC-06, RC-07, SC-16, SC-17, SC-18` |
| **Entry file** | `context/stage-05-deployment-and-release.md` |

### `verify-deployment-integrity` — Verify deployed artefact integrity

Cryptographic verification that the deployed code matches the tested version

| Field | Value |
|-------|-------|
| **Controls** | `SC-17` |
| **Entry file** | `controls/sc/SC-17.yaml` |

### `prepare-rollback-plan` — Prepare and test rollback plan

Document and execute dry-run of rollback procedure before go-live

| Field | Value |
|-------|-------|
| **Controls** | `RC-07` |
| **Entry file** | `controls/rc/RC-07.yaml` |


## Stage 6: Observability & Maintenance

### `monitor-production` — Monitor production health and SLOs

Observe system health, error rates, latency, and SLO compliance in real time

| Field | Value |
|-------|-------|
| **Controls** | `QC-10, RC-08, SC-19, SC-20, AC-06` |
| **Entry file** | `context/stage-06-observability-and-maintenance.md` |

### `detect-security-incident` — Detect and triage security incident

Identify potential security compromise, data breach, or attack

| Field | Value |
|-------|-------|
| **Controls** | `SC-19, SC-20` |
| **Entry file** | `feedbackloops/feedback-loops.yaml` |
| **Note** | Classify as Path A (quick fix) or Path B (full re-entry) via Step FL.1 |

### `detect-model-anomaly` — Detect AI model anomaly or drift

Identify unexpected AI model behavior, performance degradation, or bias drift

| Field | Value |
|-------|-------|
| **Controls** | `SC-20, AC-06` |
| **Entry file** | `controls/ac/AC-06.yaml` |

### `conduct-ai-post-market-surveillance` — Conduct AI post-market surveillance

Monitor AI system for regulatory compliance, bias, and out-of-distribution behavior

| Field | Value |
|-------|-------|
| **Controls** | `AC-06` |
| **Entry file** | `controls/ac/AC-06.yaml` |


## Cross-Cutting Tasks

### `feedback-loop-classification` — Classify incident for feedback loop re-entry

Determine if a Stage 4 or Stage 6 issue requires Path A (quick fix) or Path B (full re-entry)

| Field | Value |
|-------|-------|
| **Controls** | `none` |
| **Entry file** | `feedbackloops/feedback-loops.yaml` |
| **Note** | Execute Step FL.1 to classify and get RO approval before proceeding to Path A or Path B |

### `execute-path-a-quick-fix` — Execute Path A quick-fix flow

Re-execute minimum control set for easy, obvious, low-risk issues at Stage 3

| Field | Value |
|-------|-------|
| **Controls** | `QC-04, QC-05, SC-08, SC-09, GC-03, QC-06, SC-12, RC-05, SC-17` |
| **Entry file** | `feedbackloops/feedback-loops.yaml` |
| **Note** | Follow Steps FL.1 → FL.2A. If any deviation, upgrade to Path B immediately |

### `execute-path-b-full-reentry` — Execute Path B full re-entry flow

Re-enter at Stage 1 and process through full lifecycle (Stages 1→6) for complex issues

| Field | Value |
|-------|-------|
| **Controls** | `none` |
| **Entry file** | `feedbackloops/feedback-loops.yaml` |
| **Note** | Follow Steps FL.1 → FL.2B. Creates new FEAT-XXXX and runs all controls |


---

**Last Updated:** 2026-03-13 12:43 UTC
