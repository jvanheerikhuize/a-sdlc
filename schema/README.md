# Schema

JSON Schema definitions (Draft 2020-12) for all structured YAML files in the A-SDLC repository. These schemas are used by the validation script (`scripts/validate.py`) and by any toolchain that needs to validate framework YAML before processing.

## Full Schema Coverage

All 152 YAML files in the repository are now validated by one of 13 schemas:

| # | Schema | Validates | Purpose | Files |
|---|--------|-----------|---------|-------|
| **Core Schemas (Already existed)** | | | | |
| 1 | [control.schema.json](control.schema.json) | `controls/[track]/[ID].yaml` | Individual control definitions | 51 controls |
| 2 | [stage.schema.json](stage.schema.json) | `stages/NN-name/NN-name.yaml` | Stage workflow & execution | 6 stages |
| 3 | [directive.schema.json](directive.schema.json) | `directives/**/[name].yaml` | Security directives (SC-0D, SC-2B) | 7 directives |
| 4 | [feature-spec.schema.json](feature-spec.schema.json) | `stages/01-*/artifacts/outputs/FEAT-*.yaml` | Feature specifications | 47+ artifacts |
| **Infrastructure Schemas (NEW)** | | | | |
| 5 | [common.schema.json](common.schema.json) | $defs in all schemas | Shared reusable definitions | All schemas |
| 6 | [framework.schema.json](framework.schema.json) | `asdlc.yaml` | Root framework manifest | 1 file |
| 7 | [registry.schema.json](registry.schema.json) | `controls/registry.yaml` | Master control index | 1 file (51 entries) |
| 8 | [tasks.schema.json](tasks.schema.json) | `tasks.yaml` | Task navigation index | 1 file |
| 9 | [doc-generation.schema.json](doc-generation.schema.json) | `manifest/catalog.yaml` | Documentation generation config | 1 file |
| **Regulatory Schemas (NEW)** | | | | |
| 10 | [compliance-matrix.schema.json](compliance-matrix.schema.json) | `regulatory/compliance-matrix.yaml` | DORA/EU AI Act control mappings | 1 file |
| 11 | [regulatory-sources.schema.json](regulatory-sources.schema.json) | `regulatory/sources.yaml` | Regulatory framework reference texts | 1 file |
| **Workflow & Artifact Schemas (NEW)** | | | | |
| 12 | [feedback-loop.schema.json](feedback-loop.schema.json) | `feedbackloops/feedback-loops.yaml` | Feedback path workflows | 1 file |
| 13 | [artifact.schema.json](artifact.schema.json) | All artifact output templates | 4 artifact categories (spec, classification, lifecycle, scan) | 46 files |

**Schema Coverage:** 100% of 152 YAML files

---

## Shared Definitions (common.schema.json)

All new schemas use `$ref` to reference shared definitions from `common.schema.json`:

| Definition | Type | Values |
|---|---|---|
| `control_id` | pattern | `^(QC\|RC\|SC\|AC\|GC)-[0-6][A-Z]$` |
| `track_code` | enum | QC, RC, SC, AC, GC |
| `stage_number` | integer | 0–6 (0=cross-cutting) |
| `stage_name` | enum | 7 stage names |
| `role_code` | enum | 12 role codes |
| `delegation_pattern` | enum | 16 delegation patterns |
| `automation_frequency` | enum | 9 frequency values |
| `severity` | enum | critical, high, medium, low |
| `risk_tier` | enum | low, medium, high, critical |
| `iso_date` | pattern | `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `artifact_envelope` | object | Common header for all artifact templates |
| `feedback_path_id` | enum | path_a, path_b |
| `feedback_step_id` | pattern | FL.1, FL.2A, FL.2B, FL.3 |

---

## Schema Descriptions

### Core Schemas (Existing)

#### 1. **control.schema.json** — Control Definition Schema

**Validates:** All 51 control YAML files in `controls/[track]/`

**Key Constraints:**
- `id` must match pattern `[Track]-[Stage][Letter]` and equal filename without `.yaml`
- `required_in_stages` is an array — supports multi-stage controls (e.g., SC-0D in all 6 stages)
- `track` must be one of: QC, RC, SC, AC, GC
- `delegation` specifies how the control is split between agent and human
- `regulatory_mapping` documents DORA and/or EU AI Act coverage
- `moscow_score` indicates prioritization: must, should, could, wont
- `dependencies[]` lists other control IDs that must be satisfied first

**Required Fields:**
```yaml
id: SC-2B                    # Control ID
name: string                 # Human-readable name
description: string          # What this control does
required_in_stages: []       # Stages where required
track: QC|RC|SC|AC|GC        # Control track
delegation: string           # Delegation pattern
moscow_score: must|should|could|wont  # Priority
```

---

#### 2. **stage.schema.json** — Stage Workflow Schema

**Validates:** All 6 stage YAML files in `stages/NN-name/`

**Key Constraints:**
- `number` must be 1–6
- `required_controls[]` lists control IDs that must be executed in this stage
- `workflow.nodes[]` defines the DAG of execution steps
- `workflow.parallelism` specifies concurrency constraints
- `exit_criteria[]` are human-readable gates before stage exit

**Required Fields:**
```yaml
number: 1-6                  # Stage number
name: string                 # Stage name (must match enum)
description: string          # Stage purpose
required_controls: []        # Control IDs required
exit_criteria: []            # Gate conditions
workflow:                    # Execution DAG
  nodes: []
  parallelism: { max_concurrent, groups }
roles: []                    # Actor roles in this stage
```

---

#### 3. **directive.schema.json** — Directive Injection Schema

**Validates:** Core (`directives/core/`) and per-stage directives (`directives/stages/`)

**Key Constraints:**
- `meta.scope` is either `global` (SC-0D) or `stage` (SC-2B)
- `meta.classification` is always `immutable` — directives cannot be overridden
- `injection.trigger` is either `session_start` (SC-0D) or `stage_entry` (SC-2B)
- `categories[]` group related security directives

**Required Fields:**
```yaml
meta:
  id: SC-0D|SC-2B            # Directive ID
  scope: global|stage         # Scope of application
  classification: immutable   # Cannot override
injection:
  trigger: session_start|stage_entry
  stage_number?: 1-6          # For SC-2B
enforcement:
  overridable: false          # Security directives always enforced
categories:                   # Grouped directives
  - id: string
    name: string
    directives: []
```

---

#### 4. **feature-spec.schema.json** — Feature Specification Schema

**Validates:** Feature specification artifacts in Stage 1 (QC-1A output)

**Key Constraints:**
- `metadata.id` must match pattern `FEAT-[0-9]{4}`
- `metadata.version` must be semantic (e.g., 1.0.0)
- `acceptance_criteria[]` uses BDD format (given/when/then)
- `technical_requirements` includes constraints, performance, security
- `risk_classification` ties to RC-1A and AC-1A controls

**Required Fields:**
```yaml
metadata:
  id: FEAT-XXXX              # Feature ID
  title: string
  version: semver            # e.g., 1.0.0
description:
  summary: string
  problem_statement: string
  proposed_solution: string
acceptance_criteria:         # BDD-style
  - id: AC-XXX
    given: string
    when: string
    then: string
```

---

### Infrastructure Schemas (New)

#### 5. **common.schema.json** — Shared Definitions

**Purpose:** Eliminate duplication across all schemas using JSON Schema `$defs` and `$ref`

Contains reusable patterns used by 10+ other schemas:
- Control ID pattern (referenced in framework, registry, tasks, regulatory schemas)
- Track/stage/role enums (referenced in multiple schemas)
- Artifact envelope (common header for all output templates)
- Frequency/delegation enums (referenced in control and stage schemas)

---

#### 6. **framework.schema.json** — Framework Manifest Schema

**Validates:** `asdlc.yaml` — the root framework definition

**Top-level required:** `framework`, `roles`, `cross_cutting`, `stages`, `supporting_files`

**Key Fields:**
```yaml
framework:
  name: "Agentic Software Development Life Cycle"
  abbreviation: "A-SDLC"
  version: "1.0"
  status: approved
  tagline: string
  narrative:
    what_is_it: string
    properties: []
    value_propositions: [{ benefit, target, mechanism }]
  regulatory_scope: [DORA, EU AI Act]
  control_tracks: [{ code, name, description }]
  delegation_patterns: [{ pattern, description }]
roles:                        # Actor role definitions
  REQ: { name, description }
  AGT: { name, description }
  # ... etc
cross_cutting:
  description: string
  feedback_loops: { definition, process, readme, artifacts_dir }
  directives: { core, stages }
  controls: [{ id, name, track }]
stages:                       # All 6 stages
  - number: 1
    name: Intent Ingestion
    slug: 01-intent-ingestion
    directory: stages/01-intent-ingestion
    stage_file: stages/.../01-intent-ingestion.yaml
    readme: stages/.../README.md
    description: string
    controls: [{ id, name, track }]
supporting_files:
  schema: { ... }
  registry: string
  regulatory: string
```

---

#### 7. **registry.schema.json** — Control Registry Schema

**Validates:** `controls/registry.yaml` — the master index of all 51 controls

**Top-level required:** `registry` (array, exactly 51 entries)

**Each registry entry:**
```yaml
id: QC-1A                        # Control ID
name: Specification Validation   # Control name
stage: 1                         # Stage number
stage_name: Intent Ingestion     # Stage name
track: QC                        # Track code
delegation: agent_drafts_human_approves  # Delegation pattern
file: controls/qc/QC-1A.yaml    # YAML file path
owner_team: Product / Delivery   # Responsible team
directive_payload?: string       # Optional: SC-0D only
note?: string                    # Optional: additional notes
```

---

#### 8. **tasks.schema.json** — Task Navigation Schema

**Validates:** `tasks.yaml` — task-to-control mapping for agent navigation

**Top-level required:** `version`, `description`, `tasks`

**Each task:**
```yaml
id: ingest-feature-request       # Task ID (lowercase-hyphenated)
name: Ingest a new feature request  # Human-readable name
stage: 1                         # Stage number (0=cross-cutting)
description: string              # What this task accomplishes
controls:                        # Control IDs required for this task
  - QC-1A
  - RC-1A
entry_file: context/stage-01-intent-ingestion.md  # Context document
note?: string                    # Optional: special instructions
```

---

#### 9. **doc-generation.schema.json** — Documentation Generation Configuration

**Validates:** `manifest/catalog.yaml` — documentation generation orchestration

**Key Fields:**
```yaml
doc_generation:
  templates_dir: scripts/templates/
  generator_script: scripts/generate-docs.py
  targets:                       # Documentation generation targets
    - source: asdlc.yaml
      template: framework-overview  # Template name (enum)
      output: README.md
      description: "Root README describing the framework"
controls: []                      # Cross-cutting controls (optional)
tracks: []                        # Track definitions (optional)
regulatory: {}                    # Regulatory framework summary (optional)
schemas: {}                       # Schema file references (optional)
metadata:
  created: YYYY-MM-DD
  last_updated: YYYY-MM-DD
  status: approved
  maintainer: Architecture Team
  review_cycle_months: 12
```

**Template enum values:**
- `framework-overview` → README.md
- `agents` → AGENTS.md
- `stage-readme` → stages/NN-*/README.md
- `stages-overview` → stages/README.md
- `controls-index` → controls/README.md
- `regulatory-index` → regulatory/README.md
- `feedback-loops-guide` → feedbackloops/README.md
- `stage-context-bundle` → context/stage-NN-*.md

---

### Regulatory Schemas (New)

#### 10. **compliance-matrix.schema.json** — Regulatory Compliance Mapping

**Validates:** `regulatory/compliance-matrix.yaml` — control-to-article mappings

**Top-level required:** `compliance_matrix`

**Structure:**
```yaml
compliance_matrix:
  dora:
    framework_name: "Digital Operational Resilience Act"
    effective_date: 2025-01-17
    scope: "Financial entities and ICT service providers"
    articles:
      - article: "Art. 8"
        title: "Identification of ICT risk"
        scope: string
        controls: [RC-1A, GC-0B]  # Mapped controls
        coverage: "Strong - ..."  # Pattern: (Strong|Partial) + description
  eu_ai_act:
    # ... similar structure
coverage_summary:                # Optional
  total_controls: 51
  coverage_by_track: { ... }
regulatory_areas: [ ... ]        # Optional: regulatory areas mapping
```

---

#### 11. **regulatory-sources.schema.json** — Regulatory Framework Sources

**Validates:** `regulatory/sources.yaml` — authoritative texts and obligations

**Top-level:** `dora` and/or `eu_ai_act` (at least one required)

**Structure per framework:**
```yaml
dora:
  name: "Digital Operational Resilience Act"
  regulation: "Regulation (EU) 2022/2554"
  celex: "32022R2554"
  oj_reference: "OJ L 333, 27.12.2022, p. 1–79"
  date_adopted: 2022-12-14
  date_published: 2022-12-27
  effective_date: 2025-01-17
  scope: string
  official_url: https://...
  reference_site: https://...
  wikipedia: https://...
  structure:
    chapters:
      - number: "I"              # Roman numeral or integer
        title: "General provisions (Arts. 1–4)"
  articles:
    - id: "Art. 5"               # Article identifier
      title: "Governance and organisation"
      paragraph_summary:
        "1": string              # Paragraph 1 content
        "2": string              # Paragraph 2 content
        # ...
      controls_mapped: [QC-1A]   # Controls addressing this article
  annexes:                        # Optional: regulation annexes
    - id: "Annex I"
      title: string
      description: string
      controls_mapped: []
```

---

### Workflow & Artifact Schemas (New)

#### 12. **feedback-loop.schema.json** — Feedback Loop Workflows

**Validates:** `feedbackloops/feedback-loops.yaml` — feedback path definitions

**Top-level required:** `process`, `roles`, `input_artifacts`, `steps`, `feedback_loops`

**Key Structures:**
- `roles[]` — feedback loop actors (AGT, OPS, QA, SA, RO, CO)
- `input_artifacts` — keyed by stage (stage4, stage6)
- `steps[]` — execution steps (FL.1, FL.2A, FL.2B, FL.3)
- `feedback_loops[]` — path definitions (path_a: quick fix → Stage 3, path_b: full re-entry → Stage 1)

**Example feedback loop entry:**
```yaml
id: path_a
name: "Path A — Quick Fix → Stage 3"
re_entry_stage: 3
re_entry_stage_name: "Coding & Implementation"
description: string
trigger_sources:
  - stage: 6
    name: "Observability & Maintenance"
    source_controls: [QC-6A, RC-6A]
    description: string
minimum_controls:              # Path A: array; Path B: object
  - id: QC-3A
    name: "Pull Request Creation & Review"
    rationale: string
regulatory_mapping:
  dora:
    - article: "Art. 8(5)"
      obligation: string
```

---

#### 13. **artifact.schema.json** — Artifact Output Templates

**Validates:** All 46 artifact template files in `stages/*/artifacts/outputs/`

**Polymorphic schema using `oneOf` for 4 artifact categories:**

| Category | Key Fields | Example File |
|----------|-----------|--------------|
| **Classification Record** | `feat_id`, `stage`, `control`, `tier`, `rationale`, `criteria`, `classification` | `RC-1A-risk-classification.yaml` |
| **Lifecycle Record** | `feat_id`, `stage`, `control`, `immutable`, `pull_request`, `decision` | `QC-3A-pull-request-record.yaml` |
| **Scan Report** | `feat_id`, `stage`, `control`, `findings[]`, `summary` | `SC-3B-post-guardrail-scan.yaml` |
| **Feature Spec** | Delegates to `feature-spec.schema.json` | `QC-1A-feature-spec.yaml` |

**Shared artifact envelope (all templates):**
```yaml
feat_id: FEAT-XXXX             # Feature ID (FEAT-0001 format)
stage: 1-6                     # Stage number
control: QC-1A                 # Producing control
immutable?: true               # Optional: prevent edits after creation
<timestamp>?: YYYY-MM-DD       # Optional: creation/scan timestamp
```

---

## Running Validation

### Validate All YAML Files

```bash
python3 scripts/validate.py
```

Expected output (10 checks):
```
✓ 1/10 Control files ... 51 controls found
✓ 2/10 Registry ... 51 controls registered
✓ 3/10 Stage files ... 6 stages validated
✓ 4/10 Directive files ... 7 directives validated
✓ 5/10 Control dependencies ... no cycles detected
✓ 6/10 Feedback loops ... workflows validated
✓ 7/10 Stage structure ... directories and files correct
✓ 8/10 Infrastructure files ... asdlc.yaml, registry.yaml, tasks.yaml, catalog.yaml
✓ 9/10 Regulatory files ... compliance-matrix.yaml, sources.yaml
✓ 10/10 Artifact templates ... 46 output templates validated
✓ All checks passed (0 failures, 0 warnings)
```

### Validate Specific File

```bash
# Validate a single control against control.schema.json
python3 -c "from jsonschema import validate; import yaml, json
control = yaml.safe_load(open('controls/qc/QC-1A.yaml'))
schema = json.load(open('schema/control.schema.json'))
validate(control, schema)
print('✓ Valid')"
```

---

## Schema Development Notes

### Adding a New Schema

1. Define the schema in `schema/new-schema.json`
2. Use `$ref` to reference shared definitions from `common.schema.json`:
   ```json
   { "$ref": "https://asdlc/schema/common.schema.json#/$defs/control_id" }
   ```
3. Add validation logic to `scripts/validate.py`
4. Update this README.md with the schema description
5. Run `python3 scripts/validate.py` to verify

### Updating common.schema.json

When adding shared definitions:
1. Add the definition to the `$defs` object in `common.schema.json`
2. Update the existing schemas to use `$ref` instead of inline definitions
3. Reduces duplication and improves maintainability

---

## See Also

- [scripts/validate.py](../scripts/validate.py) — Validation driver (10 checks)
- [scripts/README.md](../scripts/README.md) — Scripts documentation
- [asdlc.yaml](../asdlc.yaml) — Framework manifest (source of truth)
