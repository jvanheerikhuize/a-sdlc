# A-SDLC Scripts

Utility scripts for validating and generating documentation for the A-SDLC framework.

## Overview

| Script | Purpose | When to Use |
|--------|---------|------------|
| **validate.sh** | Framework self-audit | Before committing YAML changes |
| **generate-docs.sh** | Auto-generate documentation | After updating YAML sources |
| **generate-diagram.sh** | Generate HTML/SVG diagram | After updating stages or controls |

## Quick Start

### Requirements

- `bash` (≥4.0)
- `jq` — JSON processor (`apt install jq` / `brew install jq`)
- `python3` with `PyYAML` — used only as a YAML→JSON converter (`pip install pyyaml`)

No Jinja2, no jsonschema, no other Python dependencies.

### Running validate.sh

```bash
# Full audit (cross-reference checks)
bash scripts/validate.sh

# Skip cross-reference checks
bash scripts/validate.sh --no-xref

# Suppress passing checks — show failures and warnings only
bash scripts/validate.sh --quiet

# Note: --no-schema is accepted but is a no-op (JSON schema validation
# is not supported in the bash version)
```

**Exit codes:**
- `0` — passed (with or without warnings)
- `1` — failures present
- `2` — dependency error (missing jq or pyyaml)

### Running generate-docs.sh

```bash
# Generate all documentation targets
bash scripts/generate-docs.sh

# List what will be generated
bash scripts/generate-docs.sh --list
```

### Running generate-diagram.sh

```bash
# Generate docs/diagram.html
bash scripts/generate-diagram.sh

# Custom output path
bash scripts/generate-diagram.sh -o path/to/output.html
```

---

## validate.sh — Framework Self-Audit

### What It Checks

| Check | Verifies | Key Validations |
|-------|----------|-----------------|
| **1/7 Control files** | Individual control YAMLs | ID matches filename; ID pattern `[Track]-[NN]` |
| **2/7 Registry** | `controls/registry.yaml` | All controls present; no duplicate IDs; all file/directive paths resolve |
| **3/7 Stage files** | Stage YAMLs in `stages/NN-*/` | `process.md` exists; required controls in registry; artifact paths exist |
| **4/7 Directives** | `directives/core/` and `directives/stages/` | All directive files present |
| **5/7 Dependencies** | Control cross-references | All `dependencies` IDs exist in registry; no circular dependency chains |
| **6/7 Feedback loops** | `feedbackloops/feedback-loops.yaml` | `process.md` and `README.md` present; control IDs in registry |
| **7/7 Stage structure** | Directory layout | Each stage has `README.md`, `process.md`, `artifacts/outputs/` |

> **Note:** JSON Schema validation is not included in this bash version.

---

## generate-docs.sh — Documentation Generator

Templates are embedded directly in the script as bash functions (no separate template files).
Each generator reads YAML sources via `python3` (YAML→JSON) + `jq`, then writes markdown output.

### Generation Targets

| # | Generator | Source | Output |
|---|-----------|--------|--------|
| 1 | `gen_framework_overview` | `asdlc.yaml` | `README.md` |
| 2 | `gen_agents_md` | `asdlc.yaml` | `AGENTS.md` |
| 3–8 | `gen_stage_readme` | `stages/NN-*/NN-*.yaml` | `stages/NN-*/README.md` |
| 9 | `gen_stages_overview` | `asdlc.yaml` | `stages/README.md` |
| 10 | `gen_controls_index` | `controls/registry.yaml` | `controls/README.md` |
| 11 | `gen_regulatory_index` | `regulatory/compliance-matrix.yaml` | `regulatory/README.md` |
| 12 | `gen_feedback_loops_guide` | `feedbackloops/feedback-loops.yaml` | `feedbackloops/README.md` |
| 13 | `gen_directives_index` | `directives/` | `directives/README.md` |
| 14 | `gen_roles_index` | `roles/registry.yaml` | `roles/README.md` |

---

## File Manifest

```
scripts/
├── README.md              ← This file
├── validate.sh            ← Framework validator
├── generate-docs.sh       ← Documentation generator (templates embedded)
├── generate-diagram.sh    ← HTML/SVG diagram generator
└── templates/
    └── README.md          ← Template authoring guide (reference only)
```
