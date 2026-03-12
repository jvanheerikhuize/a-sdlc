# A-SDLC-GOVERNANCE-MODULE — Integration Guide

How to add this module to a consuming repository and operate it alongside its companion module.

---

## Overview

This repository is the **A-SDLC-GOVERNANCE-MODULE**. It is designed to be consumed as a **git submodule** and works together with a companion module:

| Module | Role |
|--------|------|
| **A-SDLC-GOVERNANCE-MODULE** (this repo) | Governance framework: controls, directives, lifecycle definitions, regulatory mappings |
| **A-SDLC-AGENTIC-MODULE** | Agentic onboarding: CLAUDE.md scaffolding, entry-point instructions, tooling that wires traditional human dev repos into the A-SDLC framework |

A consuming repository typically includes both modules as submodules. The Human Dev Module is the front door for developers and agents arriving fresh; the Governance Module is the authoritative rule engine they operate under.

---

## Adding the Modules to a Consuming Repository

```bash
# Add governance module (this repo)
git submodule add <a-sdlc-governance-repo-url> a-sdlc-governance

# Add companion human dev module
git submodule add <a-sdlc-human-dev-repo-url> a-sdlc-human-dev

# Initialise after cloning (for consumers of the repo)
git submodule update --init --recursive
```

Conventional mount paths:
- `a-sdlc-governance/` — this module
- `a-sdlc-human-dev/` — companion module

---

## What This Module Provides

1. **Framework Definition** (`asdlc.yaml`) — Complete manifest of all 6 stages and 50 controls
2. **Control Definitions** — Individual control files with requirements, delegation patterns, and artifacts (`controls/`)
3. **Core Directives** — Immutable security and governance constraints injected at session start (`directives/core/`)
4. **Stage Directives** — Per-stage directive payloads injected at stage entry (`directives/stages/`)
5. **Workflow DAGs** — Machine-parseable execution sequences per stage (`stages/`)
6. **Stage Context Bundles** — Pre-compiled stage guides with all dependencies (`context/`)
7. **Task Navigation Index** (`tasks.yaml`) — Maps common tasks to relevant controls
8. **Regulatory Mappings** — DORA and EU AI Act compliance matrices (`regulatory/`)
9. **Feedback Loop Definitions** — Re-entry paths for incidents and changes (`feedbackloops/`)

---

## Integration Patterns

All paths below are relative to this module's mount point (e.g., `a-sdlc-governance/`).

### Pattern 1: Load-Once Initialization (Recommended for Long-Running Agents)

**Steps:**

1. **Load Core Directives (MANDATORY — do this first):**
   ```python
   import yaml

   with open("a-sdlc-governance/directives/core/core-directives.yaml") as f:
       core_directives = yaml.safe_load(f)

   # IMMUTABLE — inject into your agent context before any other instructions
   ```

2. **Load Framework Manifest:**
   ```python
   with open("a-sdlc-governance/asdlc.yaml") as f:
       framework = yaml.safe_load(f)

   # Use framework['stages'] and framework['controls'] for programmatic discovery
   ```

3. **Load Task Index (if navigating by task):**
   ```python
   with open("a-sdlc-governance/tasks.yaml") as f:
       tasks = yaml.safe_load(f)
   ```

4. **Load Stage Context Bundle (when entering a stage):**
   ```python
   stage_num = 3  # Coding & Implementation
   import glob
   context_file = glob.glob(f"a-sdlc-governance/context/stage-{stage_num:02d}-*.md")[0]

   with open(context_file) as f:
       stage_context = f.read()
   ```

---

### Pattern 2: On-Demand Control Lookup

```python
import yaml

with open("a-sdlc-governance/controls/registry.yaml") as f:
    registry = yaml.safe_load(f)

# Find control by ID
control_entry = next(c for c in registry['controls'] if c['id'] == 'SC-08')
track = control_entry['track']  # 'sc'

with open(f"a-sdlc-governance/controls/{track}/SC-08.yaml") as f:
    control = yaml.safe_load(f)

# control['description'], control['delegation'], control['required_in_stages'],
# control['artifacts']['inputs'], control['artifacts']['outputs']
```

---

### Pattern 3: Task-Driven Navigation

```python
import yaml

with open("a-sdlc-governance/tasks.yaml") as f:
    tasks_index = yaml.safe_load(f)

matching_task = next(
    t for t in tasks_index['tasks']
    if 'implement' in t['name'].lower()
)
# {'id': 'implement-feature', 'stage': 3, 'controls': ['QC-04', ...], 'entry_file': '...'}

stage_context = open(f"a-sdlc-governance/{matching_task['entry_file']}").read()
```

---

### Pattern 4: Workflow DAG Parsing

```python
import yaml
from pathlib import Path

stage_num = 1
stage_dir = list(Path('a-sdlc-governance/stages').glob(f'{stage_num:02d}-*/'))[0]
stage_def_file = list(stage_dir.glob(f'{stage_num:02d}-*.yaml'))[0]

with open(stage_def_file) as f:
    stage_def = yaml.safe_load(f)

nodes = stage_def['workflow']['nodes']
# Each node: {'id', 'control', 'depends_on', 'delegation', 'actors'}
```

---

### Pattern 5: Feedback Loop Re-Entry

```python
with open("a-sdlc-governance/feedbackloops/feedback-loops.yaml") as f:
    feedback_loops = yaml.safe_load(f)

# Path A: quick fix → re-enter at Stage 3
# Path B: full re-entry → re-enter at Stage 1 (treat as new FEAT-XXXX)
```

---

## Utility Functions

Shared utilities are in `scripts/shared.py`:

```python
import sys
sys.path.insert(0, 'a-sdlc-governance')

from scripts.shared import load_yaml_safe, find_control_in_registry

framework = load_yaml_safe('a-sdlc-governance/asdlc.yaml')
registry  = load_yaml_safe('a-sdlc-governance/controls/registry.yaml')
control   = find_control_in_registry('SC-08', registry['controls'])
```

---

## Initialization Checklist

When first wiring up a consuming repository:

- [ ] Add this module as a git submodule at `a-sdlc-governance/`
- [ ] Add companion A-SDLC-AGENTIC-MODULE at `a-sdlc-human-dev/`
- [ ] Load `a-sdlc-governance/directives/core/core-directives.yaml` **first** at every agent session start (non-negotiable)
- [ ] Load `a-sdlc-governance/asdlc.yaml` for framework discovery
- [ ] Load `a-sdlc-governance/tasks.yaml` for task routing
- [ ] Load appropriate `context/stage-NN-*.md` when entering a stage
- [ ] Inject stage-specific directives from `directives/stages/` on stage entry
- [ ] Log all control executions per GC-01 audit trail requirements
- [ ] Run validation: `python3 a-sdlc-governance/scripts/validate.py`

---

## Directory Structure

```
a-sdlc-governance/              ← this module's mount point (conventional)
├── AGENTS.md                   ← Agent entrypoint — read first
├── INTEGRATION.md              ← This file
├── asdlc.yaml                  ← Framework manifest (all stages + controls)
├── tasks.yaml                  ← Task-to-controls navigation index
├── README.md                   ← Human overview
│
├── controls/
│   ├── registry.yaml           ← Fast lookup: control ID → metadata
│   ├── qc/                     ← Quality Controls (10)
│   ├── rc/                     ← Risk Controls (9)
│   ├── sc/                     ← Security Controls (20)
│   ├── ac/                     ← AI Controls (6)
│   └── gc/                     ← Governance Controls (5)
│
├── stages/
│   ├── 01-intent-ingestion/    ← stage yaml + README + artifacts/
│   ├── 02-system-design/
│   ├── 03-coding-implementation/
│   ├── 04-testing-documentation/
│   ├── 05-deployment-release/
│   └── 06-observability-maintenance/
│
├── context/                    ← Auto-generated stage bundles (one .md per stage)
│
├── directives/
│   ├── core/core-directives.yaml   ← IMMUTABLE constraints (SC-01) — always load first
│   └── stages/NN-name.yaml         ← Per-stage directives (SC-02)
│
├── feedbackloops/
│   └── feedback-loops.yaml         ← Re-entry paths (Path A & B)
│
├── regulatory/
│   ├── compliance-matrix.yaml      ← DORA & EU AI Act coverage
│   └── README.md
│
├── schema/
│   ├── control.schema.json
│   └── feature-spec.schema.json
│
└── scripts/
    ├── shared.py               ← Shared utilities
    ├── generate-docs.py        ← Regenerate auto-generated docs
    └── validate.py             ← Validate framework integrity
```

---

## Key Files

| File | Purpose | When to Use |
|------|---------|------------|
| `AGENTS.md` | Agent entrypoint | Every session startup |
| `asdlc.yaml` | Full framework manifest | Programmatic discovery |
| `tasks.yaml` | Task-to-control mapping | Agent task routing |
| `context/stage-NN-*.md` | Complete stage context | Entering a stage |
| `controls/registry.yaml` | Control index | Fast lookups |
| `controls/[track]/[ID].yaml` | Individual control definition | Understanding a control |
| `stages/NN-*/NN-*.yaml` | Stage definition + DAG | Execution orchestration |
| `feedbackloops/feedback-loops.yaml` | Re-entry paths | Incident handling |
| `directives/core/core-directives.yaml` | **IMMUTABLE** constraints | **Always load first** |
| `regulatory/compliance-matrix.yaml` | Regulatory mappings | Compliance audits |

---

## Support

- **Framework questions?** See [AGENTS.md](AGENTS.md) and [README.md](README.md)
- **Validate integration:** `python3 a-sdlc-governance/scripts/validate.py`
- **Issues:** Report at the module repository
