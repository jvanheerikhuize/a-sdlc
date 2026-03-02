# Stage 1: Intent Ingestion — Process

## Roles

| Role | Short | Stage 1 responsibilities |
| ---- | ----- | ------------------------- |
| Requester | REQ | Submits the change request |
| Agent | AGT | Automated processing and drafting |
| Product Owner | PO | Approves specification; resolves conflicts |
| Risk Officer | RO | Validates risk classification |
| Security Architect | SA | Reviews blocked or flagged requests |
| AI Governance Lead | AGL | Confirms EU AI Act tier (if AI component involved) |
| Compliance Officer | CO | Reviews audit records during audits |

## Input Artifacts

| Artifact | Provided by | Template |
| -------- | ----------- | -------- |
| Change Request | REQ | [artifacts/inputs/change-request.yaml](artifacts/inputs/change-request.yaml) |

---

## Step Sequence

Steps 3, 4, and 5 are independent of each other and run in parallel after Step 2 completes.

```text
[1: SC-1A Screen] → [2: QC-1A Draft spec] → ┬─ [3: QC-1B Conflict analysis]  ────────────┐
                                              ├─ [4: RC-1A risk classification] ─────────┤ → [6: QC-1A PO sign-off] → [7: GC-1A Audit]
                                              └─ [5: AC-1A AI tier] (if AI component) ──────┘
```

---

## Step 1 — Screen Incoming Request

**Control:** [SC-1A](../../controls/sc/SC-1A.yaml) · **Delegation:** Fully automated · **Runs before all other steps**

| Actor | Action |
| ----- | ------ |
| AGT | Scan raw change request for prompt injection patterns, adversarial framing, and manipulation attempts |
| AGT | **Pass:** forward to Step 2. **Block:** log attempt; notify SA |
| SA | Review blocked request; contact requester for resubmission |

| | |
|---|---|
| **Input** | Change Request (`CR-XXXX`) |
| **Output** | Screened request (pass) or blocked log entry |
| **On failure** | SA reviews flagged request; requester must resubmit a clean change request |

---

## Step 2 — Draft Feature Specification

**Control:** [QC-1A](../../controls/qc/QC-1A.yaml) (agent phase) · **Delegation:** Agent drafts → human approves at Step 6 · **Runs after:** Step 1

| Actor | Action |
| ----- | ------ |
| AGT | Parse screened change request; populate `FEAT-XXXX` specification template |
| AGT | Identify any gaps in acceptance criteria or non-functional requirements |
| AGT | Flag gaps inline in the draft for Product Owner review |

| | |
|---|---|
| **Input** | Screened change request |
| **Output** | Draft feature specification (`artifacts/outputs/feature-spec.yaml`) |
| **Note** | Product Owner approval is at Step 6; this step only produces the draft |

---

## Steps 3, 4, 5 — Run in parallel after Step 2

---

## Step 3 — Conflict Analysis

**Control:** [QC-1B](../../controls/qc/QC-1B.yaml) · **Delegation:** Agent analyses, human resolves · **Runs after:** Step 2

| Actor | Action |
| ----- | ------ |
| AGT | Cross-reference all requirements; detect contradictions, competing priorities, and logical inconsistencies |
| AGT | Produce conflict map: each conflict rated `blocking`, `significant`, or `minor`, with resolution options |
| PO | Review conflict map; make binding decisions on all `blocking` conflicts |
| PO | Accept or document `significant` and `minor` conflicts with rationale |

| | |
|---|---|
| **Input** | Draft feature specification |
| **Output** | Conflict resolution record (`artifacts/outputs/conflict-resolution-record.yaml`) |
| **On failure** | Unresolved `blocking` conflicts halt Stage 1. PO must resolve before proceeding |

---

## Step 4 — Risk Classification

**Control:** [RC-1A](../../controls/rc/RC-1A.yaml) · **Delegation:** Agent classifies, human validates · **Runs after:** Step 2 · **Parallel with:** Steps 3 and 5

| Actor | Action |
| ----- | ------ |
| AGT | Apply risk classification criteria across 6 dimensions (see [Risk Classification Methodology](../../controls/rc/RISK-CLASSIFICATION-METHODOLOGY.md)) |
| AGT | Propose tier (`low` / `medium` / `high` / `critical`) and governance intensity |
| RO | Review proposed tier and rationale; validate or override with documented justification |

| | |
|---|---|
| **Input** | Draft feature specification |
| **Output** | Risk classification record (`artifacts/outputs/risk-classification.yaml`) |
| **On failure** | Escalate to Risk Officer for manual assessment; classification must resolve before Step 6 |

---

## Step 5 — AI Tier Classification *(conditional)*

**Control:** [AC-1A](../../controls/ac/AC-1A.yaml) · **Delegation:** Agent proposes, human confirms · **Runs after:** Step 2 · **Parallel with:** Steps 3 and 4

**Condition:** Only applicable when the change introduces, modifies, or interacts with AI components. If not applicable, document as `not_applicable` and skip human confirmation.

| Actor | Action |
| ----- | ------ |
| AGT | Analyse specification for AI component involvement |
| AGT | Propose EU AI Act risk tier with rationale referencing Art. 6 and Annex III |
| AGL | Review proposed tier and rationale; confirm or override with documented justification |

| | |
|---|---|
| **Input** | Draft feature specification |
| **Output** | AI tier classification (`artifacts/outputs/ai-tier-classification.yaml`) |
| **On uncertainty** | Default to highest applicable tier pending AGL resolution |

---

## Step 6 — Product Owner Sign-off

**Control:** [QC-1A](../../controls/qc/QC-1A.yaml) (approval phase) · **Delegation:** Human required · **Runs after:** Steps 3, 4, and 5 all complete

| Actor | Action |
| ----- | ------ |
| PO | Review final specification, conflict resolutions, risk tier, and AI tier (if applicable) |
| PO | **Approve:** mark specification `status: approved`; Stage 1 may exit |
| PO | **Reject:** return to Step 2 with documented gaps; requester addresses them |

| | |
|---|---|
| **Input** | Draft spec + conflict resolution record + risk classification + AI tier classification |
| **Output** | Approved feature specification |
| **On rejection** | Return to Step 2; document reason; requester and agent address gaps |

---

## Step 7 — Traceability Log

**Control:** [GC-1A](../../controls/gc/GC-1A.yaml) · **Delegation:** Fully automated · **Runs after:** Step 6 (approval)

| Actor | Action |
| ----- | ------ |
| AGT | Write immutable audit record: original request hash, all transformations, all human decisions, approved spec reference |

| | |
|---|---|
| **Input** | All Stage 1 events and outputs |
| **Output** | Intent audit record (`artifacts/outputs/intent-audit-record.yaml`) |
| **On failure** | Stage 1 completion is blocked until logging is restored |

---

## Output Artifacts

| Artifact | Produced at | Control | Template |
| -------- | ----------- | ------- | -------- |
| Feature Specification | Step 2 / Step 6 | QC-1A | [artifacts/outputs/feature-spec.yaml](artifacts/outputs/feature-spec.yaml) |
| Conflict Resolution Record | Step 3 | QC-1B | [artifacts/outputs/conflict-resolution-record.yaml](artifacts/outputs/conflict-resolution-record.yaml) |
| Risk Classification | Step 4 | RC-1A | [artifacts/outputs/risk-classification.yaml](artifacts/outputs/risk-classification.yaml) |
| AI Tier Classification | Step 5 | AC-1A | [artifacts/outputs/ai-tier-classification.yaml](artifacts/outputs/ai-tier-classification.yaml) |
| Intent Audit Record | Step 7 | GC-1A | [artifacts/outputs/intent-audit-record.yaml](artifacts/outputs/intent-audit-record.yaml) |
