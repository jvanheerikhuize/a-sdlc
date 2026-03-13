<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/01-intent-ingestion/01-intent-ingestion.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 1: Intent Ingestion — Process

**Stage:** 01-Intent Ingestion
**Purpose:** Capture, validate, and enrich an incoming change request into a structured, approved feature specification. All downstream stages depend on this specification as their source of truth. No design work begins until Stage 1 is complete.

## Roles

| Code | Name | Mode | Responsibilities |
|------|------|------|------------------|
| REQ | Requester | Gated | Submits the change request |
| IA | Intake Analyst | Autonomous | Screens, parses, drafts, classifies, and logs |
| PO | Product Owner | Gated | Approves specification; makes binding conflict decisions |
| RO | Risk Officer | Gated | Validates risk classification; may override agent-proposed tier |
| SA | Security Architect | Gated | Reviews blocked or flagged requests; contacts requester |
| AGL | AI Governance Lead | Gated | Confirms EU AI Act tier (if AI component involved) |
| CO | Compliance Officer | Gated | Reviews audit records during regulatory audits |

## Process Steps

### Step 1.1 — Screen Incoming Request

**Control:** [`SC-03`](../../controls/sc/SC-03.yaml) · **Delegation:** Fully automated

Screen incoming request for adversarial patterns

| Actor | Action |
|-------|--------|
| `AGT` | Scan raw change request for prompt injection patterns, adversarial framing, and manipulation attempts |
| `AGT` | Pass: forward to Step 1.2. Block: log attempt; notify SA |
| `SA` | Review blocked request; contact requester for resubmission |

**Input:** Change Request (CR-XXXX)

**Output:** Screened request (pass) or blocked log entry


### Step 1.2 — Draft Feature Specification

**Control:** [`QC-01`](../../controls/qc/QC-01.yaml) · **Delegation:** Agent drafts → human approves

Draft and validate feature specification

| Actor | Action |
|-------|--------|
| `AGT` | Parse screened change request; populate FEAT-XXXX specification template |
| `AGT` | Identify any gaps in acceptance criteria or non-functional requirements |
| `AGT` | Flag gaps inline in the draft for Product Owner review |

**Input:** Screened change request

**Output:** Draft feature specification (artifacts/outputs/feature-spec.yaml)


### Step 1.3 — Conflict Analysis

**Control:** [`QC-02`](../../controls/qc/QC-02.yaml) · **Delegation:** Agent analyses, human resolves

Identify and resolve conflicts in specification

| Actor | Action |
|-------|--------|
| `AGT` | Cross-reference all requirements; detect contradictions, competing priorities, and logical inconsistencies |
| `AGT` | Produce conflict map: each conflict rated blocking, significant, or minor, with resolution options |
| `PO` | Review conflict map; make binding decisions on all blocking conflicts |
| `PO` | Accept or document significant and minor conflicts with rationale |

**Input:** Draft feature specification

**Output:** Conflict resolution record (artifacts/outputs/conflict-resolution-record.yaml)


### Step 1.4 — Risk Classification

**Control:** [`RC-01`](../../controls/rc/RC-01.yaml) · **Delegation:** Agent classifies, human validates

Classify risk tier

| Actor | Action |
|-------|--------|
| `AGT` | Apply risk classification criteria across 6 dimensions |
| `AGT` | Propose tier (low / medium / high / critical) and governance intensity |
| `RO` | Review proposed tier and rationale; validate or override with documented justification |

**Input:** Draft feature specification

**Output:** Risk classification record (artifacts/outputs/risk-classification.yaml)


### Step 1.5 — AI Tier Classification (conditional)

**Control:** [`AC-01`](../../controls/ac/AC-01.yaml) · **Delegation:** Agent proposes, human confirms

> **Conditional:** Only applicable when the change introduces, modifies, or interacts with AI components. If not applicable, document as not_applicable and skip human confirmation.

Classify AI Act risk tier (conditional on ai_component)

| Actor | Action |
|-------|--------|
| `AGT` | Analyse specification for AI component involvement |
| `AGT` | Propose EU AI Act risk tier with rationale referencing Art. 6 and Annex III |
| `AGL` | Review proposed tier and rationale; confirm or override with documented justification |

**Input:** Draft feature specification

**Output:** AI tier classification (artifacts/outputs/ai-tier-classification.yaml)


### Step 1.5b — Data Classification Screening

**Control:** [`SC-04`](../../controls/sc/SC-04.yaml) · **Delegation:** Agent classifies, SA reviews

> **Conditional:** Only applicable when the change processes personal data or involves profiling. If not applicable, document as not_applicable.

Data classification screening (conditional on processes_personal_data)

| Actor | Action |
|-------|--------|
| `AGT` | Identify all personal data elements and processing activities |
| `AGT` | Classify each element per GDPR categories; flag any high-risk processing |
| `SA` | Review classification; confirm compliance with data handling policy |

**Input:** Draft feature specification

**Output:** Data classification record (artifacts/outputs/data-classification-record.yaml)


### Step 1.6 — Product Owner Sign-off

**Control:** [`GC-05`](../../controls/gc/GC-05.yaml) · **Delegation:** Human required

Write intent audit trail entry

| Actor | Action |
|-------|--------|
| `PO` | Review final specification, conflict resolutions, risk tier, and AI tier (if applicable) |
| `PO` | Approve: mark specification status: approved; Stage 1 may exit |
| `PO` | Reject: return to Step 1.2 with documented gaps; requester addresses them |

**Input:** Draft spec + conflict resolution record + risk classification + AI tier classification

**Output:** Approved feature specification


## Exit Criteria

- SC-03: Pre-guardrails passed — no injection patterns detected in incoming request
- SC-04: Data classification assigned (if applicable to change)
- QC-01: Feature specification approved by Product Owner
- QC-02: All blocking conflicts resolved; non-blocking conflicts documented
- RC-01: Risk classification tier assigned and logged
- AC-01: AI Act risk tier confirmed (or not-applicable documented)
- AC-02: GPAI obligation screening completed (if applicable)
- GC-05: Intent audit record written to immutable log


## Output Artifacts

- `artifacts/outputs/QC-01-feature-spec.yaml`
- `artifacts/outputs/QC-02-conflict-resolution-record.yaml`
- `artifacts/outputs/RC-01-risk-classification.yaml`
- `artifacts/outputs/AC-01-ai-tier-classification.yaml`
- `artifacts/outputs/SC-04-data-classification-record.yaml`
- `artifacts/outputs/GC-05-intent-audit-record.yaml`


## References

- Stage definition: `01-intent-ingestion.yaml`
- Controls: See `required_controls` in stage YAML.

---

**Last Updated:** 2026-03-13 12:43 UTC
