<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/framework.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: A-SDLC Framework Schema

**File:** `schema/framework.schema.json` · **Type:** `object`

Validates asdlc.yaml — the root framework manifest defining stages, controls, and governance

## Required Fields

- `framework`
- `roles`
- `cross_cutting`
- `stages`
- `supporting_files`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `framework` | object |  |
| `roles` | object | Actor roles in the framework |
| `cross_cutting` | object |  |
| `stages` | array | The six stages of the A-SDLC |
| `supporting_files` | object | References to supporting configuration files |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/framework.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 14:19 UTC
