<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: schema/control.schema.json
     Regenerate: bash scripts/generate-docs.sh -->

# Schema: A-SDLC Control Definition

**File:** `schema/control.schema.json` · **Type:** `object`

Schema for Agentic SDLC control definitions. Regulatory scope: DORA · EU AI Act.

## Required Fields

- `id`
- `name`
- `description`
- `required_in_stages`
- `track`
- `delegation`
- `moscow_score`

## Properties

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique control identifier. Format: [Track]-[Stage][Letter]. Track: QC|RC|SC|AC|GC. Stage: 0=cross-cutting, 1-6=lifecycle stage. |
| `name` | string | Short, descriptive control title using action-oriented nouns. |
| `description` | string | Functional description starting with a verb. Answers: if this control didn't exist, what would go wrong? |
| `required_in_stages` | array | Stages in which this control is required. Supports controls active in multiple stages. |
| `track` | object |  |
| `delegation` | object |  |
| `owner` | object | Ownership metadata for this control. |
| `regulatory_mapping` | object | Optional: Regulatory framework mappings. Will be populated during regulatory context rebuild phase. |
| `inputs` | array | Artefacts or data this control consumes. |
| `outputs` | array | What this control produces, including audit evidence. |
| `failure_behaviour` | object |  |
| `automation` | object |  |
| `dependencies` | array | Controls that must pass before this one can execute. |
| `feedback_loops` | array | Feedback loop re-entry paths that include this control. |
| `directive_payload` | string | Path to the directive payload file injected by this control. Used by SC-01 for the core directive bundle. |
| `moscow_score` | string | MoSCoW prioritization category: Must have (critical), Should have (important), Could have (nice-to-have), Won't have (out of scope). |
| `metadata` | object |  |

## Validation

Validate a file against this schema:

```bash
python3 -c "
import json, jsonschema, yaml, sys
schema = json.load(open('schema/control.schema.json'))
data   = yaml.safe_load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print('valid')
" your-file.yaml
```

---

**Last Updated:** 2026-03-13 14:19 UTC
