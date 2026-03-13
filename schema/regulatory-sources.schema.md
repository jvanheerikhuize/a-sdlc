<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/regulatory-sources.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: Regulatory Framework Sources Schema

**File:** `schema/regulatory-sources.schema.json` · **Type:** `object`

At least one regulatory framework (dora or eu_ai_act) must be present

## Required Fields

None specified
## Properties

| Field | Type | Description |
|-------|------|-------------|
| `dora` | object |  |
| `eu_ai_act` | object |  |

## Shared Definitions (`$defs`)

- `regulatory_framework`

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/regulatory-sources.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 14:19 UTC
