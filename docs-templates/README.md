# Documentation Templates & Generation

This directory contains the Jinja2 templates used to auto-generate all README.md files from YAML sources.

## Philosophy

**YAML is the single source of truth.** README.md files are generated outputs and should never be hand-edited. This ensures:

- Documentation is always in sync with the actual framework
- No duplicate information to maintain
- Agents can use YAML directly without parsing markdown
- Humans can read generated markdown for clarity

## Workflow

```
┌─────────────────────┐
│  Edit YAML sources  │
│ (controls/, stages/)│
└──────────┬──────────┘
           │
           ↓
┌──────────────────────────────┐
│ python3 scripts/generate-docs.py │
└──────────┬───────────────────┘
           │
           ↓
┌──────────────────────────────┐
│  README.md files generated   │
│  (never hand-edited)         │
└──────────────────────────────┘
```

## Available Templates

### `stage-readme.jinja2`

Generates `stages/NN-name/README.md` from a stage YAML file.

**Input:** `stages/NN-name/NN-name.yaml`
**Output:** `stages/NN-name/README.md`
**Variables:**
- `stage` — The entire stage YAML object
- `stage_file` — Path to the source YAML file
- `required_controls` — List of controls for this stage with metadata
- `workflow_diagram` — Mermaid diagram of control execution order
- `last_updated` — Timestamp

**Sections generated:**
- Overview (stage number, name, control count)
- Execution workflow (DAG and parallelism)
- Required controls (table with links)
- Entry/exit gates
- Input/output artifacts
- Directives injected

### `controls-index.jinja2`

Generates `controls/README.md` from the control registry.

**Input:** `controls/registry.yaml`
**Output:** `controls/README.md`
**Variables:**
- `total_controls` — Count of all controls
- `tracks` — List of control tracks
- `controls_by_track` — Controls grouped by track
- `all_controls_sorted` — Flat list sorted by ID
- `last_updated` — Timestamp

**Sections generated:**
- Track overview (table)
- Controls by track (one table per track)
- Control ID format explanation
- Flat index for fast lookup
- Schema validation reference

### `framework-overview.jinja2`

Generates `README.md` from `asdlc.yaml`.

**Input:** `asdlc.yaml`
**Output:** `README.md`

(To be implemented)

### `regulatory-index.jinja2`

Generates `regulatory/README.md` from `regulatory/` files.

**Input:** `regulatory/sources.yaml` + `regulatory/compliance-matrix.yaml`
**Output:** `regulatory/README.md`

(To be implemented)

### `feedback-loops-guide.jinja2`

Generates `feedbackloops/README.md` from `feedbackloops/feedback-loops.yaml`.

**Input:** `feedbackloops/feedback-loops.yaml`
**Output:** `feedbackloops/README.md`

(To be implemented)

## Running the Generator

### Generate all documentation

```bash
python3 scripts/generate-docs.py
```

Output:
```
=== A-SDLC Documentation Generator ===

Generating 10 documentation targets...

✓ Generated: stages/01-intent-ingestion/README.md
✓ Generated: stages/02-system-design/README.md
...
✓ Generated 10/10 documentation files
```

### List all generation targets

```bash
python3 scripts/generate-docs.py --list
```

Output:
```
A-SDLC Documentation Generation Targets:

 1. [framework-overview]
    From:   asdlc.yaml
    To:     README.md
    About:  Framework overview and control summary

 2. [stage-readme]
    From:   stages/01-intent-ingestion/01-intent-ingestion.yaml
    To:     stages/01-intent-ingestion/README.md
    About:  Stage 1 overview, workflow, and controls
...
```

## Adding a New Template

1. Create a new `.jinja2` file in this directory:
   ```bash
   touch docs-templates/my-template.jinja2
   ```

2. Add a target to `manifest/catalog.yaml` in the `doc_generation.targets` list:
   ```yaml
   - source: path/to/source.yaml
     template: my-template
     output: path/to/output.md
     description: "What this generates"
   ```

3. Implement the template using Jinja2 syntax
   - Access YAML data via variables
   - Use `{% for %}` loops, `{% if %}` conditionals
   - See existing templates for examples

4. Update `scripts/generate-docs.py` to handle your template type in the `generate_all()` method

5. Run the generator:
   ```bash
   python3 scripts/generate-docs.py
   ```

## Template Variables

All templates have access to:

- `last_updated` — Current timestamp (ISO 8601 format)
- Context-specific variables (see template sections above)

To access variables in a template:

```jinja2
{{ variable }}                     {# Outputs a variable #}
{% for item in list %}
  {{ item.name }}
{% endfor %}                       {# Iterate over lists #}
{% if condition %}
  ...
{% endif %}                        {# Conditionals #}
{{ text | upper }}                 {# Filters #}
```

## Jinja2 Filters Available

- `upper` — Convert to uppercase
- `lower` — Convert to lowercase
- `length` — Get list/string length
- `join` — Join list items into a string
- `sort` — Sort a list
- `reverse` — Reverse a list

See [Jinja2 documentation](https://jinja.palletsprojects.com/templates/) for more.

## Generated File Headers

All generated README.md files begin with:

```markdown
> ⚠️ **AUTO-GENERATED FILE**
>
> This file is generated from [`path/to/source.yaml`](source.yaml).
> Do NOT edit this file directly. Edit the YAML source and run:
>
> ```bash
> python3 scripts/generate-docs.py
> ```
```

This warns humans not to hand-edit the file and provides clear instructions for updating it.

## Troubleshooting

### Template not found
```
ERROR: Template not found: my-template.jinja2
```

**Fix:** Check the template filename matches the `template` field in `manifest/catalog.yaml` (without the `.jinja2` extension).

### Missing required variables
```
jinja2.exceptions.UndefinedError: 'foo' is undefined
```

**Fix:** The template tries to use a variable that wasn't passed. Check the `generate_*` method in `scripts/generate-docs.py` to ensure all required variables are included in the context dictionary.

### YAML parse error
```
yaml.YAMLError: mapping values are not allowed here
```

**Fix:** Check the source YAML file for syntax errors. Common issues:
- Missing colons after keys
- Incorrect indentation
- Unquoted strings with special characters

### Output file not created
Check that the output directory exists:

```bash
mkdir -p path/to/output/dir
```

Then re-run the generator.

## Integration with CI/CD

Optionally add a pre-commit hook to regenerate docs when YAML files change:

```bash
# .git/hooks/pre-commit (or use a tool like husky)
#!/bin/bash
python3 scripts/generate-docs.py
git add stages/*/README.md controls/README.md
```

This ensures documentation is always up-to-date before committing.

---

**Last Updated:** 2026-03-05
