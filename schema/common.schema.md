<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/common.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: A-SDLC Common Schema Definitions

**File:** `schema/common.schema.json` · **Type:** `object`

Shared definitions used across all A-SDLC schemas to eliminate duplication

## Required Fields

None specified
## Shared Definitions (`$defs`)

- `artifact_envelope`
- `automation_frequency`
- `control_id`
- `delegation_pattern`
- `feedback_path_id`
- `feedback_step_id`
- `iso_date`
- `risk_tier`
- `role_code`
- `severity`
- `stage_name`
- `stage_number`
- `track_code`

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/common.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
