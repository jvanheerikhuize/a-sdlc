<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/compliance-matrix.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: Regulatory Compliance Matrix Schema

**File:** `schema/compliance-matrix.schema.json` · **Type:** `object`

Validates regulatory/compliance-matrix.yaml — mapping of A-SDLC controls to regulatory framework articles

## Required Fields

- `compliance_matrix`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `compliance_matrix` | object | Compliance mappings by regulatory framework |
| `coverage_summary` | object | Optional: summary of coverage statistics |
| `regulatory_areas` | array | Optional: regulatory areas and their control mappings |

## Shared Definitions (`$defs`)

- `framework_mapping`

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/compliance-matrix.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
