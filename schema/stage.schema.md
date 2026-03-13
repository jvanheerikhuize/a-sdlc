<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/stage.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: A-SDLC Stage Definition

**File:** `schema/stage.schema.json` · **Type:** `object`

Schema for per-stage definition files (stages/NN-name/NN-name.yaml). Lists required controls, exit criteria, and artifact paths for one lifecycle stage.

## Required Fields

- `number`
- `name`
- `description`
- `required_controls`
- `exit_criteria`
- `workflow`
- `roles`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `number` | integer | Lifecycle stage number (1–6). |
| `name` | string | Canonical stage name. |
| `description` | string | Purpose of the stage. Answers: what work happens here and why? |
| `required_controls` | array | Control IDs that must execute within this stage. |
| `exit_criteria` | array | Conditions that must be true before the stage is considered complete. |
| `next_stage` | integer | null | Stage number that follows this one. Null for Stage 6 (no bounded exit). |
| `workflow` | object | Execution DAG: nodes (control execution steps) and parallelism metadata. |
| `roles` | array | Stage-specific role definitions with responsibilities. |
| `feedback_loop_summary` | array | Feedback loop triggers and re-entry stages (Stage 6 only). |
| `artifacts` | object | Paths to input and output artifact templates, relative to the stage directory. |
| `directives` | array | Paths to directive YAML files injected at this stage's entry (SC-02 payloads). |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/stage.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
