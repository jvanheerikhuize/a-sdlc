# Feedback Loops — Process

## Roles

Canonical role definitions: [../stages/roles.yaml](../stages/roles.yaml)

| Role | Short | Feedback loop responsibilities |
| ---- | ----- | ------------------------------ |
| Agent | AGT | Detects Stage 4 or Stage 6 trigger; prepares activation record; re-executes minimum controls on Path A |
| Operations / SRE | OPS | First responder to Stage 6 alerts; co-classifies path; monitors Path A execution |
| QA Lead | QA | First responder to Stage 4 failures; co-classifies path; confirms root cause from test output |
| Security Architect | SA | Validates path classification for SC-4A, SC-4B, SC-6A, and SC-6B triggers; confirms root cause before Path A is approved |
| Risk Officer | RO | Makes the formal path selection and classification decisions; provides signed approval for any Path B selection |
| Compliance Officer | CO | Reviews activation record; confirms DORA Art. 8 reporting obligations are documented |

## Input Artifacts

| Artifact | Source |
| -------- | ------ |
| SAST scan report | SC-4A (Step 4.1) |
| Test results report | QC-4A (Step 4.2) |
| DAST scan report | SC-4B (Step 4.3) |
| Risk threshold evaluation | RC-4A (Step 4.7) |
| SLO monitoring record | QC-6A (Step 6.2) |
| Risk & health monitoring record | RC-6A (Step 6.3) |
| Incident detection record | SC-6A (Step 6.4) |
| Anomaly detection record | SC-6B (Step 6.5) |
| AI post-market surveillance report | AC-6A (Step 6.6) |

---

## Step Sequence

Steps FL.1 and FL.3 run for every activation. FL.2A or FL.2B is selected based on the path classification in FL.1.

```mermaid
flowchart LR
    S1["Step FL.1\nPath Classification\n(human required)"]
    S2A["Step FL.2A\nPath A · Quick Fix\n(minimum control set)"]
    S2B["Step FL.2B\nPath B · Full Re-entry\n(Stage 1 — full lifecycle)"]
    S3["Step FL.3\nActivation Record\n& Handover"]

    S1 -->|"Path A eligible"| S2A
    S1 -->|"Path B required"| S2B
    S2A -->|"all controls pass"| S3
    S2A -->|"deviation → upgrade"| S2B
    S2B --> S3
```

---

## Step FL.1 — Path Classification

**Delegation:** Human required · **Runs first — blocks re-entry until path is formally approved**

| Actor | Action |
| ----- | ------ |
| AGT | Retrieve the trigger: source stage (4 or 6), originating control, alert or finding ID, issue description |
| OPS / QA | Assess issue scope, urgency, and affected components; provide initial path recommendation |
| SA | For SC-4A, SC-4B, SC-6A, or SC-6B triggers: confirm root cause is understood before any path is approved |
| RO | Make the formal path selection decision: Path A or Path B |
| RO | Record identity, role, timestamp, rationale, and selected path in the activation record |

**Path A eligibility — when triggered from Stage 6 (ALL conditions must be true):**

| Condition | Check |
| --------- | ----- |
| Issue matches a pre-approved autofix template exactly (no partial matches) | AGT verifies against template registry |
| Risk classification of the issue is `low` | RO confirms |
| No new architectural changes are required | OPS confirms |
| Root cause is understood (for security-triggered issues: SA confirms) | SA / OPS confirms |

**Path A eligibility — when triggered from Stage 4 (ALL conditions must be true):**

| Condition | Check |
| --------- | ----- |
| Root cause is unambiguous from the failing control output | QA / SA confirms |
| Risk classification is `low` | RO confirms |
| No new architectural changes are required | QA confirms |
| Fix is isolated to code only — no schema, API, or contract changes | QA confirms |

If any condition is not met, Path B is mandatory. Do not attempt a partial Path A.

| | |
| --- | --- |
| **Input** | Stage 4 or Stage 6 trigger record |
| **Output** | Signed path selection (Path A or Path B) recorded in the activation record |
| **On ambiguity** | Default to Path B — never assume Path A eligibility under uncertainty |

---

## Step FL.2A — Path A: Quick Fix

**Delegation:** Agent executes minimum control set, OPS/QA monitors · **Runs after FL.1 — Path A selected**

| Actor | Action |
| ----- | ------ |
| AGT | For Stage 6 triggers: retrieve the matched pre-approved autofix template; verify exact signature match |
| AGT | Execute minimum controls in sequence: Stage 3 group, then Stage 4 group, then Stage 5 check |
| AGT | For Stage 4 triggers: additionally re-execute the specific Stage 4 control(s) that raised the issue |
| AGT | At any deviation from expected scope during execution: stop immediately; escalate to OPS/QA; upgrade to Path B |
| OPS / QA | Monitor execution continuously; validate no out-of-scope actions are taken |

**Minimum control set (in execution order):**

| Control | Stage | Rationale |
| ------- | ----- | --------- |
| QC-3A | 3 | All code changes must be reviewed before merge |
| QC-3B | 3 | Automated quality checks apply to all fixes |
| SC-3B | 3 | Agent-generated fix must be scanned for malicious patterns |
| SC-3C | 3 | Fix must not introduce exposed credentials |
| GC-3A | 3 | Fix output must be attributed to the agent or developer that produced it |
| QC-4A | 4 | Fix must be tested before deployment |
| SC-4A | 4 | Static security analysis is mandatory even on expedited paths |
| RC-4A | 4 | Residual risk must be assessed before deployment |
| SC-5B | 5 | Cryptographic verification that tested artefact matches deployed artefact |

| | |
| --- | --- |
| **Input** | Stage 4 failing control output or matched Stage 6 autofix template + trigger record |
| **Output** | All minimum controls passed; change deployed via SC-5B; activation record updated |
| **On deviation** | Immediately upgrade to Path B — do not attempt to continue with modifications |

---

## Step FL.2B — Path B: Full Re-entry

**Delegation:** Full lifecycle from Stage 1 · **Runs after FL.1 (Path B selected) or upgrade from FL.2A**

| Actor | Action |
| ----- | ------ |
| OPS / QA | Initiate Stage 1 re-entry; create a new FEAT-XXXX change request referencing the Stage 4 or Stage 6 trigger |
| All actors | Execute the full lifecycle: Stages 1 → 2 → 3 → 4 → 5 → Stage 6 monitoring re-activation |

| | |
| --- | --- |
| **Input** | Path B selection from FL.1 (or deviation upgrade from FL.2A) |
| **Output** | New FEAT-XXXX proceeding through full lifecycle; Stage 4/6 trigger linked in feature specification |
| **Linkage** | The trigger record ID must appear in the FEAT-XXXX feature specification's `dependencies` field |
| **On ambiguity** | Default to Path B — the full lifecycle is always the safe choice |

---

## Step FL.3 — Activation Record & Handover

**Delegation:** Agent creates, CO reviews · **Runs at completion of every path**

| Actor | Action |
| ----- | ------ |
| AGT | Complete the feedback-loop activation record: trigger source (Stage 4 or 6), control ID, path selected, approvals, re-entry ID, outcome |
| AGT | Link activation record to the GC-0A audit trail and to the resulting change's Stage 3 or Stage 1 evidence package |
| CO | Review activation record; confirm DORA Art. 8 documentation obligations are met |
| CO | For SC-6A-triggered loops: confirm DORA Art. 19 reporting timelines are not impacted by the re-entry |

| | |
| --- | --- |
| **Output** | Activation record (`artifacts/outputs/feedback-loop-activation-record.yaml`) |
| **Retention** | 7 years (DORA Art. 8(6)) |

---

## Output Artifacts

| Artifact | Produced at | Template |
| -------- | ----------- | -------- |
| Feedback Loop Activation Record | Step FL.3 | [artifacts/outputs/feedback-loop-activation-record.yaml](artifacts/outputs/feedback-loop-activation-record.yaml) |
