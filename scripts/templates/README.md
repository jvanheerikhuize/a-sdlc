# Documentation Generator

This directory is part of the `scripts/` tooling for A-SDLC documentation generation.

> **Note:** There are no template files here. The generator uses inline bash functions — see [`scripts/generate-docs.sh`](../generate-docs.sh).

## Philosophy

**YAML is the single source of truth.** README.md files are generated outputs — never hand-edit them. This ensures:

- Documentation stays in sync with the actual framework
- No duplicate information to maintain
- Agents can use YAML directly; humans read generated markdown for clarity

## Architecture

The generator is a self-contained bash script using `jq` for data extraction. Python is used only as a YAML→JSON converter (no Python templating engine).

```
┌─────────────────────┐
│  Edit YAML sources  │
│ (controls/, stages/)│
└──────────┬──────────┘
           │
           ↓
┌─────────────────────────────┐
│  bash scripts/generate-docs.sh  │
│  (reads YAML via python3+jq)    │
└──────────┬──────────────────┘
           │
           ↓
┌──────────────────────────────┐
│  README.md files generated   │
│  (never hand-edited)         │
└──────────────────────────────┘
```

**Requirements:**
- `jq` (JSON processor)
- `python3` with `PyYAML` (YAML→JSON conversion only)

## Usage

```bash
# Generate all 14 documentation targets
bash scripts/generate-docs.sh

# List all generation targets with source/output paths
bash scripts/generate-docs.sh --list

# Show help
bash scripts/generate-docs.sh --help
```

Example output:
```
=== A-SDLC Documentation Generator ===

Generating documentation targets...

✓ Generated: README.md
✓ Generated: AGENTS.md
✓ Generated: stages/01-intent-ingestion/README.md
...
Generated 14 documentation files
```

## Generation Targets

Targets are defined in [`manifest/catalog.yaml`](../../manifest/catalog.yaml) and implemented as bash functions in `generate-docs.sh`.

| # | Function | Output | Source |
|---|----------|--------|--------|
| 1 | `gen_framework_overview()` | `README.md` | `asdlc.yaml` |
| 2 | `gen_agents_md()` | `AGENTS.md` | `asdlc.yaml` + control files |
| 3–8 | `gen_stage_readme()` | `stages/NN-name/README.md` (×6) | `stages/NN-name/NN-name.yaml` |
| 9 | `gen_stages_overview()` | `stages/README.md` | `asdlc.yaml` |
| 10 | `gen_controls_index()` | `controls/README.md` | `controls/registry.yaml` |
| 11 | `gen_regulatory_index()` | `regulatory/README.md` | `regulatory/sources.yaml` + `compliance-matrix.yaml` |
| 12 | `gen_feedback_loops_guide()` | `feedbackloops/README.md` | `feedbackloops/feedback-loops.yaml` |
| 13 | `gen_directives_index()` | `directives/README.md` | `directives/` directory |
| 14 | `gen_roles_index()` | `roles/README.md` | `roles/registry.yaml` + role YAML files |

## How the Generator Works

Each function follows the same pattern:

1. Load the relevant YAML source(s) into JSON via `yaml_to_json()`
2. Extract fields using `jq` queries
3. Build markdown content using bash heredocs and string concatenation
4. Write the output file

```bash
# YAML→JSON conversion (Python used only here)
yaml_to_json() {
  python3 -c "import yaml,json,sys; print(json.dumps(yaml.safe_load(sys.stdin) or {}))" < "$file"
}

# Example jq extraction
fw_name="$(echo "$asdlc_json" | jq -r '.framework.name')"

# Example table row generation
while IFS=$'\t' read -r number slug name desc; do
  stage_rows+="| [Stage ${number}](stages/${slug}/README.md) | ${name} | ${desc} |"$'\n'
done < <(echo "$asdlc_json" | jq -r '.stages[] | [(.number|tostring), .slug, .name, .description] | @tsv')
```

## Adding a New Generation Target

1. Add an entry to `manifest/catalog.yaml` under `doc_generation.targets`:
   ```yaml
   - source: path/to/source.yaml
     template: my-target-name
     output: path/to/output.md
     description: "What this generates"
   ```

2. Implement a new bash function in `scripts/generate-docs.sh`:
   ```bash
   gen_my_target() {
     local out="$REPO/path/to/output.md"
     local src_json
     src_json="$(yaml_to_json "$REPO/path/to/source.yaml")"

     # Extract fields with jq
     local field
     field="$(echo "$src_json" | jq -r '.some.field')"

     # Write output
     cat > "$out" << EOF
   <!-- AUTO-GENERATED — edit source YAML, not this file -->
   # My Target

   ${field}
   EOF
     ok "$out"
   }
   ```

3. Call the new function inside `generate_all()` in `generate-docs.sh`.

4. Run and verify:
   ```bash
   bash scripts/generate-docs.sh
   ```

## Generated File Headers

All generated files begin with an auto-generated warning comment so humans and agents know not to edit them directly:

```markdown
<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: path/to/source.yaml
     Regenerate: bash scripts/generate-docs.sh -->
```

## Troubleshooting

**`jq: command not found`**
Install jq: `sudo apt install jq` or `brew install jq`

**`ModuleNotFoundError: No module named 'yaml'`**
Install PyYAML: `pip3 install pyyaml`

**Output file not updated**
Ensure the source YAML is valid. Run `bash scripts/validate.sh` to check for structural issues before regenerating.

**`ERROR: Could not find asdlc.yaml`**
Run the script from within the repository tree. The script walks up from `scripts/` to find the repo root via `asdlc.yaml`.

## CI/CD Integration

Add a pre-commit hook to keep docs in sync when YAML sources change:

```bash
# .git/hooks/pre-commit
#!/bin/bash
bash scripts/generate-docs.sh
git add README.md AGENTS.md stages/*/README.md controls/README.md \
        regulatory/README.md feedbackloops/README.md \
        directives/README.md roles/README.md stages/README.md
```

---

**Last Updated:** 2026-03-13
