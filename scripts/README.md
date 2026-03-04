# Scripts

Tooling for validating and auditing the A-SDLC framework repository.

## validate.py

Self-audit script. Validates all YAML files against their JSON schemas and runs cross-reference integrity checks across the entire repository.

### Installation

```bash
pip install -r scripts/requirements.txt
```

Requirements: `pyyaml>=6.0`, `jsonschema>=4.18.0`

### Usage

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

Exit codes: `0` = passed (with or without warnings) · `1` = failures present · `2` = dependency error

### What It Checks

| Section | Checks |
| ------- | ------ |
| **1/7 Control files** | Schema compliance; `id` field matches filename; ID pattern `[Track]-[Stage][Letter]` |
| **2/7 Registry** | All 51 controls present; no duplicate IDs; all `file` and `directive_payload` paths resolve |
| **3/7 Stage files** | Schema compliance; `process.md` exists; all `required_controls` IDs in registry; all artifact paths exist |
| **4/7 Directive files** | Schema compliance for core and all six stage directive bundles |
| **5/7 Control dependencies** | All `dependencies` IDs exist in registry; no circular dependency chains |
| **6/7 Feedback loops** | `process.md` and `README.md` present; all control IDs in `minimum_controls` exist in registry |
| **7/7 Stage structure** | Each stage has `README.md`, `process.md`, and an `artifacts/outputs/` directory |

### When to Run

Run `validate.py` before committing any change to:
- A control YAML in `controls/[track]/`
- A stage definition YAML in `stages/NN-name/`
- A directive YAML in `directives/`
- `controls/registry.yaml`
- `feedbackloops/feedback-loops.yaml`
