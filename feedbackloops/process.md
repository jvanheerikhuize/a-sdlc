<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: feedbackloops/feedback-loops.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Feedback Loops — Process

**Module:** A-SDLC Feedback Loops
**Purpose:** Define the re-entry paths by which issues detected in Stage 4 (Testing & Documentation) or Stage 6 (Observability & Maintenance) flow back into the lifecycle. Every activation requires a formal path classification decision before re-entry begins.

## Regulatory Basis

| Regulation | Article | Obligation |
|------------|---------|------------|
| DORA | Art. 17(3) | Incident response and recovery must follow defined procedures. |
| DORA | Art. 8(1) | ICT risk management framework must cover all changes. No exception for urgency. |
| DORA | Art. 8(5) | Even expedited changes must follow documented procedures. |

## Roles

| Code | Name | Responsibilities |
|------|------|------------------|
| AGT | Agent | Detects Stage 4 or Stage 6 trigger; prepares activation record; re-executes minimum controls on Path A |
| OPS | Operations / SRE | First responder to Stage 6 alerts; co-classifies path; monitors Path A execution |
| QA | QA Lead | First responder to Stage 4 failures; co-classifies path; confirms root cause from test output |
| SA | Security Architect | Validates path classification for SC-12, SC-13, SC-19, and SC-20 triggers; confirms root cause before Path A is approved |
| RO | Risk Officer | Makes the formal path selection and classification decisions; provides signed approval for any Path B selection |
| CO | Compliance Officer | Reviews activation record; confirms DORA Art. 8 reporting obligations are documented |

## Process Steps

### Step FL.1 — Path Classification

**Delegation:** Human required — blocks re-entry until formal decision recorded

Classify feedback trigger and select re-entry path

| Actor | Action |
|-------|--------|
| `AGT` | Retrieve trigger: source stage (4 or 6), originating control, alert/finding ID, issue description |
| `OPS / QA` | Assess issue scope, urgency, affected components; provide initial path recommendation |
| `SA` | For SC-12, SC-13, SC-19, SC-20 triggers: confirm root cause is understood |
| `RO` | Make formal path selection decision: Path A or Path B |
| `RO` | Record identity, role, timestamp, rationale, selected path in activation record |

**Input:** Stage 4 or Stage 6 trigger record

**Output:** Signed path selection (Path A or Path B) recorded in activation record


### Step FL.2A — Path A: Quick Fix

**Delegation:** Agent executes, OPS/QA monitors

> **Conditional:** Only runs if Path A is selected in FL.1

Execute minimum control set for expedited re-entry at Stage 3

| Actor | Action |
|-------|--------|
| `AGT` | For Stage 6 triggers: retrieve matched pre-approved autofix template; verify exact signature match |
| `AGT` | Execute minimum controls in sequence: Stage 3 group → Stage 4 group → Stage 5 check |
| `AGT` | For Stage 4 triggers: re-execute specific Stage 4 control(s) that raised the issue |
| `AGT` | At any deviation: stop immediately; escalate to OPS/QA; upgrade to Path B |
| `OPS / QA` | Monitor execution continuously; validate no out-of-scope actions taken |

**Input:** Stage 4 failing control output OR matched Stage 6 autofix template + trigger record

**Output:** All minimum controls passed; change deployed via SC-17; activation record updated


### Step FL.2B — Path B: Full Re-entry

**Delegation:** Full lifecycle — all stages

> **Conditional:** Runs if Path B selected in FL.1 OR if FL.2A deviates

Re-enter full lifecycle from Stage 1

| Actor | Action |
|-------|--------|
| `OPS / QA` | Initiate Stage 1 re-entry; create new FEAT-XXXX change request referencing Stage 4 or Stage 6 trigger |
| `All actors` | Execute full lifecycle: Stages 1 → 2 → 3 → 4 → 5 → Stage 6 monitoring re-activation |

**Input:** Path B selection from FL.1 (or deviation upgrade from FL.2A)

**Output:** New FEAT-XXXX proceeding through full lifecycle; Stage 4/6 trigger linked in feature specification


### Step FL.3 — Activation Record & Handover

**Delegation:** Agent creates, CO reviews

> **Conditional:** Runs at completion of both Path A and Path B journeys

Document feedback loop completion and link to audit trail

| Actor | Action |
|-------|--------|
| `AGT` | Complete feedback-loop activation record: trigger source, control ID, path selected, approvals, re-entry ID, outcome |
| `AGT` | Link activation record to GC-01 audit trail and resulting change's Stage 3 or Stage 1 evidence package |
| `CO` | Review activation record; confirm DORA Art. 8 documentation obligations met |
| `CO` | For SC-19-triggered loops: confirm DORA Art. 19 reporting timelines not impacted |

**Input:** Path A/B completion outcomes

**Output:** Activation record (artifacts/outputs/feedback-loop-activation-record.yaml)

**Retention:** 7 years (DORA Art. 8(6))


## Path A Eligibility

### Stage 6 Triggers (ALL must be met)

- Issue matches a pre-approved autofix template exactly (no partial matches).
- Risk classification is low.
- No new architectural changes are required.
- Root cause is confirmed (SA sign-off required for SC-19 and SC-20 triggers).

### Stage 4 Triggers (ALL must be met)

- Root cause is unambiguous from the failing control output.
- Risk classification is low.
- No new architectural changes are required.
- Fix is isolated to code only — no schema, API, or contract changes.

## Path A: Minimum Controls

- **QC-04: Pull Request Creation & Review** — All code changes must be reviewed before merge.
- **QC-05: Code Quality Standards** — Automated quality checks apply to all fixes.
- **SC-08: Post-Guardrails** — Agent-generated fix must be scanned for malicious patterns.
- **SC-09: Secrets & Credentials Scanning** — Fix must not introduce exposed credentials.
- **GC-03: Agent Provenance Registry** — Fix output must be attributed to the agent or developer that produced it.
- **QC-06: Functional & Non-Functional Testing** — Fix must be tested before deployment.
- **SC-12: SAST** — Static security analysis is mandatory even for expedited paths.
- **RC-05: Risk Threshold Evaluation** — Residual risk must be assessed before deployment.
- **SC-17: Deployment Integrity** — Cryptographic verification that tested artefact matches deployed artefact.

## Autofix Templates

Pre-approved autofix templates for Path A (Stage 6 triggers) are stored in `feedbackloops/autofix-templates/`. Each template defines the exact issue signature, fix scope, and minimum control set. Path A eligibility requires an exact template match — no partial matches are permitted.

## References

- Feedback loop definitions: `feedback-loops.yaml`
- Autofix templates: `autofix-templates/`
- Activation record template: `artifacts/outputs/feedback-loop-activation-record.yaml`

---

**Last Updated:** 2026-03-13 12:43 UTC
