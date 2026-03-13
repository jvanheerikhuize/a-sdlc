<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/registry.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: Control Registry Schema

**File:** `schema/registry.schema.json` · **Type:** `object`

Validates controls/registry.yaml — the master index of all 50 A-SDLC controls

## Required Fields

- `registry`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `registry` | array | Array of all 50 controls in the framework |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/registry.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
