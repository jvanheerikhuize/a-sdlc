# Feedback Loops

When Stage 4 (Testing & Documentation) or Stage 6 (Observability & Maintenance) detects an issue requiring a code change, work re-enters the lifecycle through one of two defined paths. These paths ensure no change bypasses governance controls — even under urgency.

Full process with roles, steps, and decision points: [process.md](process.md)

Full path definitions and minimum control sets: [feedback-loops.yaml](feedback-loops.yaml)

---

## Steps

| Step | Name | Delegation | When |
| ---- | ---- | ---------- | ---- |
| [FL.1](process.md#step-fl1--path-classification) | Path Classification | Human required | Every activation |
| [FL.2A](process.md#step-fl2a--path-a-quick-fix) | Path A — Quick Fix | Agent executes, OPS monitors | Path A selected |
| [FL.2B](process.md#step-fl2b--path-b-full-re-entry) | Path B — Full Re-entry | Full lifecycle from Stage 1 | Path B selected or FL.2A deviation |
| [FL.3](process.md#step-fl3--activation-record--handover) | Activation Record & Handover | Agent creates, CO reviews | Every activation |

---

## Path A — Quick Fix → Stage 3

**Re-entry point:** Stage 3 (Coding & Implementation)

For easy, obvious, low-risk issues with a clear root cause. Re-enters directly at Stage 3 with a minimum control set. If any eligibility condition is not met, Path B is mandatory — no exceptions.

**Eligibility — when triggered from Stage 6:**

- Issue matches a pre-approved autofix template exactly (no partial matches)
- Risk classification is low
- No new architectural changes are required
- Root cause is confirmed (SA sign-off required for SC-6A and SC-6B triggers)

**Eligibility — when triggered from Stage 4:**

- Root cause is unambiguous from the failing control output
- Risk classification is low
- No new architectural changes are required
- Fix is isolated to code only — no schema, API, or contract changes

**Minimum controls required:**

| Control | Stage | Rationale |
| ------- | ----- | --------- |
| QC-3A | 3 | All code changes must be reviewed before merge |
| QC-3B | 3 | Automated quality checks apply to all fixes |
| SC-3B | 3 | Agent-generated fix must be scanned for malicious patterns |
| SC-3C | 3 | Fix must not introduce exposed credentials |
| GC-3A | 3 | Fix output must be attributed to the agent or developer that produced it |
| QC-4A | 4 | Fix must be tested before deployment |
| SC-4A | 4 | Static security analysis is mandatory even for expedited paths |
| RC-4A | 4 | Residual risk must be assessed before deployment |
| SC-5B | 5 | Cryptographic verification that tested artefact matches deployed artefact |

> When triggered from Stage 4, also re-execute the specific Stage 4 control(s) that raised the issue.

**Regulatory basis:** DORA Art. 8(5), Art. 17(3)

---

## Path B — Full Re-entry → Stage 1

**Re-entry point:** Stage 1 (Intent Ingestion)

For any issue not meeting Path A eligibility: complex bugs, new functionality requirements, architectural changes, or cases where root cause is unclear. No controls are skipped. The change is treated as a new feature request and goes through all six stages in sequence.

**Regulatory basis:** DORA Art. 8(1)

---

## Decision Tree

```mermaid
flowchart TD
    START(["Issue detected\n(Stage 4 or Stage 6)"])
    Q1{"Easy, obvious, low-risk?\nRoot cause clear?\nNo architectural changes?"}
    PA["Path A — Quick Fix\nRe-enter at Stage 3\nMinimum control set"]
    Q2{"Deviation from expected\nscope during execution?"}
    DONE([Activation record complete])
    PB["Path B — Full Re-entry\nRe-enter at Stage 1\nFull lifecycle — all controls"]

    START --> Q1
    Q1 -- Yes --> PA
    Q1 -- No --> PB
    PA --> Q2
    Q2 -- No --> DONE
    Q2 -- "Yes — upgrade immediately" --> PB
    PB --> DONE
```

---

## Artifacts

**Inputs (from Stage 4):**

- [../stages/04-testing-documentation/artifacts/outputs/sast-scan-report.yaml](../stages/04-testing-documentation/artifacts/outputs/sast-scan-report.yaml) — SC-4A trigger source
- [../stages/04-testing-documentation/artifacts/outputs/test-results-report.yaml](../stages/04-testing-documentation/artifacts/outputs/test-results-report.yaml) — QC-4A trigger source
- [../stages/04-testing-documentation/artifacts/outputs/dast-scan-report.yaml](../stages/04-testing-documentation/artifacts/outputs/dast-scan-report.yaml) — SC-4B trigger source
- [../stages/04-testing-documentation/artifacts/outputs/risk-threshold-evaluation.yaml](../stages/04-testing-documentation/artifacts/outputs/risk-threshold-evaluation.yaml) — RC-4A trigger source

**Inputs (from Stage 6):**

- [../stages/06-observability-maintenance/artifacts/outputs/slo-monitoring-record.yaml](../stages/06-observability-maintenance/artifacts/outputs/slo-monitoring-record.yaml) — QC-6A trigger source
- [../stages/06-observability-maintenance/artifacts/outputs/risk-health-monitoring-record.yaml](../stages/06-observability-maintenance/artifacts/outputs/risk-health-monitoring-record.yaml) — RC-6A trigger source
- [../stages/06-observability-maintenance/artifacts/outputs/incident-detection-record.yaml](../stages/06-observability-maintenance/artifacts/outputs/incident-detection-record.yaml) — SC-6A trigger source
- [../stages/06-observability-maintenance/artifacts/outputs/anomaly-detection-record.yaml](../stages/06-observability-maintenance/artifacts/outputs/anomaly-detection-record.yaml) — SC-6B trigger source
- [../stages/06-observability-maintenance/artifacts/outputs/ai-surveillance-report.yaml](../stages/06-observability-maintenance/artifacts/outputs/ai-surveillance-report.yaml) — AC-6A trigger source

**Outputs:**

- [artifacts/outputs/feedback-loop-activation-record.yaml](artifacts/outputs/feedback-loop-activation-record.yaml) — FL.3 output; one record per activation
- [artifacts/outputs/autofix-template.yaml](artifacts/outputs/autofix-template.yaml) — Template for defining pre-approved Stage 6 Path A patterns
