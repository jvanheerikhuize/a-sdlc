<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/02-system-design/02-system-design.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 2: System Design — Process

**Stage:** 02-System Design
**Purpose:** Translate the approved specification into a complete, approved system design. Security directives are injected before coding begins. No implementation may start without RC-02 (design approval) and SC-02 directive injection confirmation.

## Roles

| Code | Name | Mode | Responsibilities |
|------|------|------|------------------|
| ARCH | Solution Architect | Autonomous | Drafts system design; generates threat model; injects directives |
| LAD | Lead Architect | Gated | Validates and approves design completeness and standards compliance |
| SA | Security Architect | Gated | Validates STRIDE threat model; signs and publishes directive payload |
| RO | Risk Officer | Gated | Makes formal design approval decision; determines sign-off authority by risk tier |
| AGL | AI Governance Lead | Gated | Reviews and approves AI component design (if AI component involved) |
| CO | Compliance Officer | Gated | Reviews design records during regulatory audits |

## Process Steps

### Step 2.1 — Draft System Design

**Control:** [`QC-03`](../../controls/qc/QC-03.yaml) · **Delegation:** Agent drafts

Draft system design

| Actor | Action |
|-------|--------|
| `AGT` | Parse approved feature specification; translate requirements into architecture |
| `AGT` | Produce component diagram, integration map, data flow diagram, and technology decisions |
| `AGT` | Map every requirement to a specific architectural component; flag any unmapped requirements |
| `AGT` | Validate design coverage against organisational patterns; flag gaps and standards deviations |

**Input:** Approved feature specification (FEAT-XXXX)

**Output:** Draft design document (artifacts/outputs/design-document.yaml)


### Step 2.2 — Design Validation

**Control:** [`QC-03`](../../controls/qc/QC-03.yaml) · **Delegation:** Agent validates, LAD approves

Validate design completeness and standards

| Actor | Action |
|-------|--------|
| `LAD` | Review draft design; verify all requirements are mapped to architectural components |
| `LAD` | Confirm design follows organisational architectural patterns and technology standards |
| `LAD` | Approve: advance to Step 2.5 package. Reject: return to Step 2.1 with documented gaps |

**Input:** Draft design document

**Output:** Approved design document (artifacts/outputs/design-document.yaml — status: approved)


### Step 2.3 — STRIDE Threat Modelling

**Control:** [`SC-05`](../../controls/sc/SC-05.yaml) · **Delegation:** Agent generates, SA validates

Generate and validate STRIDE threat model

| Actor | Action |
|-------|--------|
| `AGT` | Identify all trust boundaries in the design |
| `AGT` | Generate STRIDE threat analysis across each trust boundary; propose mitigations for each threat |
| `SA` | Review threat model for completeness; validate proposed mitigations |
| `SA` | Accept: advance to Step 2.5 package. Reject: require design revision to address unmitigated threats |

**Input:** Draft design document

**Output:** STRIDE threat model (artifacts/outputs/stride-threat-model.yaml)


### Step 2.4 — AI Component Design Review

**Control:** [`AC-03`](../../controls/ac/AC-03.yaml) · **Delegation:** Agent assists, AGL approves

> **Conditional:** Only applicable when the change introduces, modifies, or interacts with AI components. If not applicable, document as not_applicable and skip human confirmation.

AI component design review (conditional on ai_component)

| Actor | Action |
|-------|--------|
| `AGT` | Analyse design for AI component involvement |
| `AGT` | Validate model selection, data pipeline design, explainability mechanisms, and human oversight provisions against AI Act requirements |
| `AGL` | Review AI design validation; confirm or require revisions |

**Input:** Draft design document + AI tier classification from Stage 1

**Output:** AI component design review (artifacts/outputs/ai-component-design-review.yaml)


### Step 2.3b — Privacy Impact Assessment

**Control:** [`RC-03`](../../controls/rc/RC-03.yaml) · **Delegation:** Agent generates, LAD reviews

> **Conditional:** Only applicable when the change processes personal data, involves profiling, or high-risk AI processing. If not applicable, document as not_applicable.

Privacy Impact Assessment (conditional on processes_personal_data)

| Actor | Action |
|-------|--------|
| `AGT` | Identify all personal data processing activities in the design |
| `AGT` | Assess privacy risks across: lawfulness, necessity, minimization, retention, recipient access |
| `LAD` | Review PIA; confirm privacy safeguards are adequate |

**Input:** Draft design document

**Output:** Privacy Impact Assessment (artifacts/outputs/privacy-impact-assessment.yaml)


### Step 2.3c — Zero-Trust Architecture Validation

**Control:** [`SC-06`](../../controls/sc/SC-06.yaml) · **Delegation:** Fully automated

Zero-trust architecture validation

| Actor | Action |
|-------|--------|
| `AGT` | Validate design against zero-trust principles; verify all network segments require authentication |
| `AGT` | Check encryption of all data in motion and at rest; verify principle of least privilege |
| `SA` | Review validation results; approve or require mitigations |

**Input:** Draft design document

**Output:** Zero-trust validation report (artifacts/outputs/zero-trust-validation.yaml)


### Step 2.5 — Design Approval

**Control:** [`RC-02`](../../controls/rc/RC-02.yaml) · **Delegation:** Human required

Design approval (human-required gate)

| Actor | Action |
|-------|--------|
| `AGT` | Assemble approval package: design document, threat model, AI review (if applicable), risk tier |
| `RO` | Review approval package; make formal approval decision |
| `RO` | Approve: record decision with identity and timestamp; advance to Step 2.6 |
| `RO` | Reject: return to Step 2.1 with documented reasons; no coding may begin |

**Input:** Approved design doc + STRIDE threat model + AI review + Stage 1 risk classification

**Output:** Design approval decision (artifacts/outputs/design-approval-decision.yaml)


### Step 2.6 — AI Model Governance and Version Control

**Control:** [`AC-04`](../../controls/ac/AC-04.yaml) · **Delegation:** Agent registers, AGL approves

> **Conditional:** Only applicable when the change introduces or modifies use of a GPAI or foundation model. If not applicable, document as not_applicable.

AI model governance and version control (conditional on ai_component)

| Actor | Action |
|-------|--------|
| `AGT` | Register all models in the model registry with versioning metadata |
| `AGT` | Record model lineage, data sources, training dates, and performance baselines |
| `AGL` | Approve model registry entries and version pinning |

**Input:** Approved design document + AI component design review

**Output:** AI model governance record (artifacts/outputs/ai-model-governance-record.yaml)


### Step 2.7 — Stage Directive Injection

**Control:** [`SC-02`](../../controls/sc/SC-02.yaml) · **Delegation:** Fully automated

Stage directive injection confirmation

| Actor | Action |
|-------|--------|
| `AGT` | Receive signed Stage 2 and Stage 3 directive payloads; load into agent context |
| `AGT` | Acknowledge receipt of both payloads with confirmation |

**Input:** directives/stages/02-system-design.yaml · directives/stages/03-coding-implementation.yaml

**Output:** Directive injection confirmation (artifacts/outputs/directive-injection-confirmation.yaml)


## Exit Criteria

- QC-03: Design validated and approved by Lead Architect
- RC-02: Design approval granted and logged
- RC-03: Privacy Impact Assessment completed (if applicable)
- SC-05: STRIDE threat model validated and all critical threats mitigated
- SC-06: Zero-trust architecture principles validated
- SC-02: Stage 2 and Stage 3 directive bundles injected and acknowledged by agent
- AC-03: AI component design review approved (or not-applicable documented)
- AC-04: AI model registry entry created with version pinning (if applicable)


## Output Artifacts

- `artifacts/outputs/QC-03-design-document.yaml`
- `artifacts/outputs/SC-05-stride-threat-model.yaml`
- `artifacts/outputs/RC-02-design-approval-decision.yaml`
- `artifacts/outputs/SC-02-directive-injection-confirmation.yaml`
- `artifacts/outputs/AC-03-ai-component-design-review.yaml`
- `artifacts/outputs/RC-03-privacy-impact-assessment.yaml`
- `artifacts/outputs/SC-06-zero-trust-validation.yaml`
- `artifacts/outputs/AC-04-ai-model-governance-record.yaml`


## References

- Stage definition: `02-system-design.yaml`
- Controls: See `required_controls` in stage YAML.

---

**Last Updated:** 2026-03-13 12:43 UTC
