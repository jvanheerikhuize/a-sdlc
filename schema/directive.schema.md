<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/directive.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: A-SDLC Directive Bundle

**File:** `schema/directive.schema.json` · **Type:** `object`

Schema for agent behavioural directive bundles: directives/core/core-directives.yaml and directives/stages/NN-name.yaml. Injected by SC-01 (core) and SC-02 (stage).

## Required Fields

- `meta`
- `injection`
- `enforcement`
- `categories`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `meta` | object | Metadata identifying the directive bundle. |
| `injection` | object | Controls how and when the bundle is injected into agent context. |
| `enforcement` | object | Defines what happens when directives are violated or override attempts are made. |
| `categories` | array | Directive categories grouping related behavioural constraints. |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/directive.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 12:43 UTC
