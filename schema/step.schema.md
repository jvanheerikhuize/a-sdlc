<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/step.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: A-SDLC Step Definition

**File:** `schema/step.schema.json` · **Type:** `object`

Schema for individual step files at stages/NN-name/steps/step-N-N.yaml. Steps are the atomic units of work within a stage — they trigger a control (optional), consume input artifacts, and produce output artifacts. Steps are executed by roles.

## Required Fields

- `id`
- `title`
- `stage`
- `delegation`
- `depends_on`
- `actors`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Step identifier matching the step number (e.g., '1.1', '1.5b', '3.2-sc3c', '4.7-ai-adversarial'). Must match the filename stem after 'step-' with dots replaced by hyphens. |
| `title` | string | Human-readable step title. |
| `stage` | integer | Stage number this step belongs to. |
| `control` | string | null | Control ID triggered by this step. Null for procedural/handover steps. |
| `description` | string | null | Brief description of what happens in this step. |
| `delegation` | string | Human-readable delegation pattern describing who does what (e.g., 'Fully automated', 'Agent drafts → human approves'). |
| `depends_on` | array | Step IDs this step depends on. Empty array means this step has no prerequisites within the stage. |
| `condition` | string | null | Conditionality text. Null or absent if the step is unconditional. |
| `frequency` | string | Execution frequency. Defaults to per_change. Stage 6 steps often use 'continuous'. |
| `actors` | array | Ordered list of role-action pairs defining who does what in this step. |
| `inputs` | array | Input descriptions or artifact references consumed by this step. |
| `outputs` | array | Output descriptions or artifact references produced by this step. |
| `on_failure` | string | null | What happens if this step fails or is blocked. |
| `on_uncertainty` | string | null | What happens if the step result is uncertain or ambiguous. |
| `on_changes_requested` | string | null | What happens if changes are requested during a review step. |
| `note` | string | null | Additional note or clarification for this step. |
| `tables` | array | Supplementary reference tables (e.g., approval authority by risk tier). |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/step.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 14:19 UTC
