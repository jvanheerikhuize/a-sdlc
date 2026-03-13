<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/doc-generation.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: Documentation Generation Configuration Schema

**File:** `schema/doc-generation.schema.json` · **Type:** `object`

Validates manifest/catalog.yaml — documentation generation orchestration

## Required Fields

- `doc_generation`
- `metadata`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `doc_generation` | object |  |
| `controls` | array | Optional: cross-cutting controls referenced in catalog |
| `tracks` | array | Optional: control track definitions |
| `regulatory` | object | Optional: regulatory framework summary |
| `schemas` | object | Optional: schema file references |
| `metadata` | object |  |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/doc-generation.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
