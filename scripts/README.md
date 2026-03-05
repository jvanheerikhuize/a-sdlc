# A-SDLC Scripts

Utility scripts for validating and generating documentation for the A-SDLC framework.

## Overview

| Script | Purpose | When to Use |
|--------|---------|------------|
| **validate.py** | Framework self-audit | Before committing YAML changes |
| **generate-docs.py** | Auto-generate documentation | After updating YAML sources |

## Quick Start

### Installation

```bash
cd scripts
pip install -r requirements.txt
```

**Requirements:**
- Python 3.6+
- PyYAML ≥6.0
- Jinja2 ≥3.0
- jsonschema ≥4.18.0

### Running validate.py

```bash
# Full audit (schema validation + cross-reference checks)
python3 scripts/validate.py

# Skip schema validation — run cross-reference checks only
python3 scripts/validate.py --no-schema

# Skip cross-reference checks — run schema validation only
python3 scripts/validate.py --no-xref

# Suppress passing checks — show failures and warnings only
python3 scripts/validate.py --quiet
```

**Exit codes:**
- `0` — passed (with or without warnings)
- `1` — failures present
- `2` — dependency error (missing pyyaml/jsonschema)

### Running generate-docs.py

```bash
# Generate all documentation targets
python3 scripts/generate-docs.py

# List what will be generated
python3 scripts/generate-docs.py --list

# View generation specification
cat manifest/catalog.yaml
```

## validate.py — Framework Self-Audit

### What It Checks

The validator performs **7 comprehensive checks** across the entire framework:

| Check | Verifies | Key Validations |
|-------|----------|-----------------|
| **1/7 Control files** | Individual control YAMLs | Schema compliance; ID matches filename; ID pattern `[Track]-[Stage][Letter]` |
| **2/7 Registry** | `controls/registry.yaml` | All 51 controls present; no duplicate IDs; all file/directive paths resolve |
| **3/7 Stage files** | Stage YAMLs in `stages/NN-*/` | Schema compliance; `process.md` exists; required controls in registry; artifact paths exist |
| **4/7 Directives** | `directives/core/` and `directives/stages/` | Schema compliance for core and all 6 stage directive bundles |
| **5/7 Dependencies** | Control cross-references | All `dependencies` IDs exist in registry; no circular dependency chains |
| **6/7 Feedback loops** | `feedbackloops/feedback-loops.yaml` | `process.md` and `README.md` present; all control IDs exist in registry |
| **7/7 Stage structure** | Directory layout | Each stage has `README.md`, `process.md`, and `artifacts/outputs/` |

### When to Run

Run `validate.py` before committing any change to:
- A control YAML in `controls/[track]/`
- A stage definition YAML in `stages/NN-name/`
- A directive YAML in `directives/`
- `controls/registry.yaml`
- `feedbackloops/feedback-loops.yaml`

### Output Interpretation

**Passing output:**
```
✓ 1/7 Control files ... 51 controls found
✓ 2/7 Registry ... all controls registered
...
✓ All checks passed (0 failures, 0 warnings)
```

**With warnings:**
```
⚠ Stage 01 artifact_in not yet in git
✓ All checks passed (0 failures, 2 warnings)
```

**With failures:**
```
✗ Registry: Duplicate control ID found: SC-2B (appears in controls/sc/SC-2B.yaml and controls/sc/SC-2B-alt.yaml)
✗ Control file: controls/sc/SC-5D.yaml references missing control QC-9Z in dependencies
✗ 2 failures found (exit code 1)
```

## generate-docs.py — Documentation Generator

### Architecture

The documentation system follows **YAML-as-single-source-of-truth** principle:

```
Edit YAML sources
    ↓
Run: python3 scripts/generate-docs.py
    ↓
Generator loads manifest/catalog.yaml
    ↓
For each target:
  - Load source YAML
  - Render Jinja2 template
  - Write output README.md
    ↓
Generated docs are updated
(never hand-edit these)
```

### Generation Targets

Current targets in `manifest/catalog.yaml`:

| # | Template | Source | Output | Status |
|---|----------|--------|--------|--------|
| 1 | controls-index | controls/registry.yaml | controls/README.md | ✓ Ready |
| 2-7 | stage-readme | stages/NN-*/NN-*.yaml | stages/NN-*/README.md | ✓ Ready |
| 8 | framework-overview | asdlc.yaml | README.md | ✓ Ready |
| 9 | stages-overview | asdlc.yaml | stages/README.md | ✓ Ready |
| 10 | agents | asdlc.yaml + tasks.yaml | AGENTS.md | ✓ Ready |
| 11 | stage-context-bundle | stages/NN-*/NN-*.yaml | context/stage-NN.md | ✓ Ready |
| 12 | feedback-loops-guide | feedbackloops/feedback-loops.yaml | feedbackloops/README.md | ✓ Ready |
| 13 | regulatory-index | regulatory/compliance-matrix.yaml | regulatory/README.md | ✓ Ready |

**All 18/18 targets generate successfully.**

### How to Update Documentation

**Scenario: Update a stage's documentation**

1. Edit the stage YAML:
   ```bash
   vim stages/01-intent-ingestion/01-intent-ingestion.yaml
   ```

2. Modify the `description`, `workflow`, `required_controls`, or `exit_criteria` fields

3. Regenerate:
   ```bash
   python3 scripts/generate-docs.py
   ```

4. The stage README is now updated:
   ```bash
   cat stages/01-intent-ingestion/README.md
   ```

**Scenario: Update the controls registry**

1. Edit `controls/registry.yaml`

2. Regenerate:
   ```bash
   python3 scripts/generate-docs.py
   ```

3. `controls/README.md` is now updated

**Scenario: Add a new template**

1. Create new Jinja2 template:
   ```bash
   vim scripts/templates/my-template.jinja2
   ```

2. Add generation target to `manifest/catalog.yaml`:
   ```yaml
   - source: path/to/source.yaml
     template: my-template
     output: path/to/output.md
     description: "What this generates"
   ```

3. Implement handler in `scripts/generate-docs.py`

4. Run generator:
   ```bash
   python3 scripts/generate-docs.py
   ```

For detailed template authoring, see: [`scripts/templates/README.md`](../scripts/templates/README.md)

## Architecture

### Shared Utilities

Both scripts use common utilities from `scripts/shared.py`:

- **YAML Loading:** `load_yaml_safe()` — safe YAML parsing with error handling
- **Registry Lookup:** `find_control_in_registry()` — efficient control lookup
- **Table Building:** `build_markdown_table()` — consistent markdown tables
- **Template Rendering:** `render_template_safe()` — graceful template error handling
- **Path Utilities:** `get_repo_root()`, `rel_path()` — robust path operations
- **Control ID Extraction:** `extract_control_id_from_string()` — regex-based ID finding

### Dependency Graph

```
scripts/shared.py
    ├── generate-docs.py (uses all 8 functions)
    ├── validate.py (uses 4-5 functions)
    └── tests/conftest.py (provides fixtures)
         └── tests/test_*.py (unit & integration tests)
```

## Workflow Integration

### Git Pre-Commit Hook

Add this pre-commit hook to auto-regenerate docs:

```bash
#!/bin/bash
# .git/hooks/pre-commit
python3 scripts/generate-docs.py
git add stages/*/README.md controls/README.md regulatory/README.md feedbackloops/README.md
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

### CI/CD Pipeline (GitHub Actions)

```yaml
- name: Validate framework
  run: python3 scripts/validate.py

- name: Generate documentation
  run: python3 scripts/generate-docs.py

- name: Verify docs are in sync
  run: |
    git diff --exit-code controls/README.md stages/*/README.md || \
    (echo "Generated docs are out of sync with YAML sources" && exit 1)
```

## Testing

### Running Tests

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run with coverage
python3 -m pytest tests/ --cov=scripts --cov-report=term-missing

# Run specific test file
python3 -m pytest tests/test_shared.py -v

# Run specific test class
python3 -m pytest tests/test_shared.py::TestLoadYamlSafe -v
```

### Test Structure

```
tests/
├── conftest.py              ← Pytest configuration, fixtures, factories
├── test_shared.py           ← Unit tests for scripts/shared.py (40+ tests)
├── test_validate.py         ← Integration tests for validate.py (25+ tests)
└── test_generate_docs.py    ← Integration tests for generate-docs.py (28+ tests)
```

### Coverage Goals

- `scripts/shared.py`: 100% coverage (8 functions, all paths tested)
- `scripts/validate.py`: >85% coverage
- `scripts/generate-docs.py`: >85% coverage

## Troubleshooting

### validate.py Issues

**Error: "pyyaml not installed"**
```bash
pip install -r scripts/requirements.txt
```

**Error: "jsonschema not installed"**
```bash
pip install jsonschema>=4.18.0
```

**Error: "Control file controls/sc/SC-2B.yaml not found"**
- Check file path is correct
- Ensure registry.yaml references correct file path
- Verify file exists: `ls -la controls/sc/SC-2B.yaml`

**Circular dependency detected**
- Examine control's `dependencies` field
- Check for cycles: A→B→C→A
- Remove or modify one edge to break cycle

### generate-docs.py Issues

**Error: "Template not found: my-template.jinja2"**
- Check template filename in `scripts/templates/` directory
- Verify template name matches `template` field in `manifest/catalog.yaml`
- Ensure `.jinja2` extension is correct

**Error: "YAML parsing failed in controls/registry.yaml"**
- Check registry.yaml YAML syntax
- Look for indentation errors
- Verify colons after keys
- Use YAML validator: `python3 -m yaml < controls/registry.yaml`

**Error: "Cannot read file controls/registry.yaml"**
- Verify file exists: `ls -la controls/registry.yaml`
- Check file permissions: `chmod 644 controls/registry.yaml`
- Ensure path is absolute or relative to repo root

**Generated docs have stale data**
- Verify source YAML files are updated
- Check manifest/catalog.yaml has correct source paths
- Re-run generator: `python3 scripts/generate-docs.py`
- Commit generated files: `git add *.md stages/*/README.md`

### General Troubleshooting

**"Cannot find A-SDLC repository root"**
- Run scripts from within repository directory
- Verify `asdlc.yaml` exists in repo root
- Run: `cd /path/to/a-sdlc && python3 scripts/validate.py`

**"No module named 'yaml'"**
- Install dependencies: `pip install -r scripts/requirements.txt`
- Verify installation: `python3 -c "import yaml; print(yaml.__version__)"`

**"No module named 'jsonschema'"**
- Install: `pip install jsonschema>=4.18.0`
- Verify: `python3 -c "import jsonschema; print(jsonschema.__version__)"`

## Best Practices

1. **Always validate before committing** — Run `validate.py` to catch errors early
2. **Regenerate docs after YAML changes** — Keep documentation in sync with sources
3. **Never hand-edit generated files** — All changes should be to YAML sources
4. **Use meaningful YAML structures** — Follow existing patterns (see `controls/*/` for examples)
5. **Test templates locally** — Run generator on small YAML subsets before applying globally
6. **Commit both YAML and generated files** — Ensures other developers see current state

## File Manifest

```
scripts/
├── README.md                    ← This file
├── requirements.txt             ← Python dependencies
├── __init__.py                  ← Package initialization
├── shared.py                    ← Shared utilities (8 functions, 180 lines)
├── generate-docs.py             ← Documentation generator (820 lines)
└── validate.py                  ← Framework validator (500 lines)

tests/
├── __init__.py                  ← Test package marker
├── conftest.py                  ← Pytest configuration & fixtures (230 lines)
├── test_shared.py               ← Unit tests for shared.py (40+ tests, 410 lines)
├── test_validate.py             ← Integration tests for validate.py (25+ tests, TBD)
└── test_generate_docs.py        ← Integration tests for generate-docs.py (28+ tests, TBD)
```

## See Also

- **[DOCUMENTATION-GENERATION.md](../DOCUMENTATION-GENERATION.md)** — Detailed doc generation architecture
- **[scripts/templates/README.md](../scripts/templates/README.md)** — Template authoring guide
- **[asdlc.yaml](../asdlc.yaml)** — Framework manifest (source of truth)
- **[manifest/catalog.yaml](../manifest/catalog.yaml)** — Doc generation orchestration spec

---

**Last Updated:** 2026-03-05
