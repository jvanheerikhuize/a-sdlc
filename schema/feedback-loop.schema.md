<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/feedback-loop.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: Feedback Loop Workflow Schema

**File:** `schema/feedback-loop.schema.json` · **Type:** `object`

Validates feedbackloops/feedback-loops.yaml — feedback path definitions and workflow steps

## Required Fields

- `process`
- `roles`
- `input_artifacts`
- `steps`
- `feedback_loops`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `process` | string | Reference to feedback loop process documentation |
| `roles` | array | Actor roles involved in feedback loops |
| `input_artifacts` | object | Input artifacts required by feedback loops, keyed by stage name |
| `steps` | array | Feedback loop execution steps |
| `output_artifacts` | array | Artifacts produced by feedback loops |
| `artifacts` | object | Artifact file references |
| `autofix_templates_dir` | string | Directory containing autofix templates |
| `feedback_loops` | array | Feedback loop path definitions |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/feedback-loop.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
