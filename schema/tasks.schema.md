<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/tasks.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: Task Navigation Schema

**File:** `schema/tasks.schema.json` · **Type:** `object`

Validates tasks.yaml — task-to-control mapping for agent navigation

## Required Fields

- `version`
- `description`
- `tasks`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `version` | string | Semantic version (e.g., 1.0.0) |
| `description` | string | Purpose of this task navigation index |
| `tasks` | array | Array of task definitions |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/tasks.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
