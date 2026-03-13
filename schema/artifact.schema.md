<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/artifact.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: Artifact Output Template Schema

**File:** `schema/artifact.schema.json` · **Type:** `object`

Validates stages/*/artifacts/outputs/*.yaml — all artifact output templates produced during the A-SDLC

## Required Fields

None specified
## Shared Definitions (`$defs`)

- `artifact_envelope`
- `classification_record`
- `feature_spec`
- `lifecycle_record`
- `scan_report`

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/artifact.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
