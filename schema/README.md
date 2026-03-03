# Schema

JSON Schema definitions (Draft 2020-12) for all structured YAML files in the repository. Used by the validation script (`scripts/validate.py`) and by any toolchain that needs to validate framework YAML before processing it.

## Files

| Schema | Validates | Used by |
| ------ | --------- | ------- |
| [control.schema.json](control.schema.json) | `controls/[track]/[ID].yaml` | All 39 control definitions |
| [stage.schema.json](stage.schema.json) | `stages/NN-name/NN-name.yaml` | All 6 stage definition files |
| [directive.schema.json](directive.schema.json) | `directives/core/core-directives.yaml` · `directives/stages/NN-name.yaml` | SC-0D and SC-2B injection payloads |
| [feature-spec.schema.json](feature-spec.schema.json) | `stages/01-intent-ingestion/artifacts/outputs/feature-spec.yaml` | Stage 1 QC-1A output artefact |

## Key Constraints

**control.schema.json**
- `id` must match pattern `[Track]-[Stage][Letter]` and must equal the filename (without `.yaml`)
- `required_in_stages` is an array — controls can appear in multiple stages
- `regulatory_mapping` must include at least one of `dora`, `dnb`, or `eu_ai_act`

**stage.schema.json**
- `required_controls` lists control IDs by reference — full definitions stay in `controls/`
- `exit_criteria` is a list of human-readable gate conditions
- `artifacts.inputs` and `artifacts.outputs` are file paths relative to the stage directory

**directive.schema.json**
- Covers both the core directive bundle and all six per-stage directive bundles
- Enforces `meta`, `injection`, `enforcement`, and `categories` sections

**feature-spec.schema.json**
- Enforces `metadata`, `description`, and `acceptance_criteria` as required top-level fields
- Referenced by control QC-1A; output is the input artefact for all downstream stages

## Running Validation

```bash
pip install -r scripts/requirements.txt
python3 scripts/validate.py
```

See [scripts/README.md](../scripts/README.md) for full usage.
