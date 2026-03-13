<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/feature-spec.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: A-SDLC Feature Specification

**File:** `schema/feature-spec.schema.json` · **Type:** `object`

Schema for feature/change specifications produced during Stage 1 (Intent Ingestion). Referenced by control QC-01.

## Required Fields

- `metadata`
- `description`
- `acceptance_criteria`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `metadata` | object |  |
| `description` | object |  |
| `acceptance_criteria` | array |  |
| `technical_requirements` | object |  |
| `api_changes` | object |  |
| `ui_changes` | object |  |
| `testing_requirements` | object |  |
| `rollout` | object |  |
| `risk_classification` | object | Populated by RC-01 (risk classification) and AC-01 (EU AI Act tier). |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/feature-spec.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 14:19 UTC
