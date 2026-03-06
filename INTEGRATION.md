# A-SDLC Framework Integration Guide

How to integrate and use the Agentic SDLC framework from another agentic repository.

---

## Overview

The A-SDLC repository provides:

1. **Framework Definition** (`asdlc.yaml`) — Complete manifest of all 6 stages and 51 controls
2. **Workflow DAGs** — Machine-parseable execution sequences for agent orchestration
3. **Control Definitions** — Individual control implementations with requirements and artifacts
4. **Stage Context Bundles** — Pre-compiled stage guides with all dependencies
5. **Task Navigation Index** (`tasks.yaml`) — Maps common tasks to relevant controls
6. **Directives** — Immutable security & governance constraints
7. **Regulatory Mappings** — DORA and EU AI Act compliance matrices

---

## Integration Patterns

### Pattern 1: Load-Once Initialization (Recommended for Long-Running Agents)

Use this when your agent starts a session and needs full framework context.

**Steps:**

1. **Clone or mount the repository:**
   ```bash
   git clone https://github.com/jvanheerikhuize/a-sdlc.git
   # or add as a git submodule:
   git submodule add https://github.com/jvanheerikhuize/a-sdlc.git a-sdlc
   ```

2. **Load Core Directives (MANDATORY):**
   ```python
   import yaml

   with open("a-sdlc/directives/core/core-directives.yaml") as f:
       core_directives = yaml.safe_load(f)

   # These directives are IMMUTABLE — inject them into your agent context
   # They take absolute precedence over user instructions
   ```

3. **Load Framework Manifest:**
   ```python
   with open("a-sdlc/asdlc.yaml") as f:
       framework = yaml.safe_load(f)

   # Use framework['stages'] and framework['controls'] for programmatic discovery
   ```

4. **Load Task Index (if navigating by task):**
   ```python
   with open("a-sdlc/tasks.yaml") as f:
       tasks = yaml.safe_load(f)

   # Map: task name → stage → controls → entry_file
   # Example: "implement-feature" → Stage 3 → [QC-3A, QC-3B, ...] → context/stage-03.md
   ```

5. **Load Stage Context Bundle (when entering a stage):**
   ```python
   stage_num = 3  # Coding & Implementation
   context_file = f"a-sdlc/context/stage-{stage_num:02d}-*.md"

   with open(context_file) as f:
       stage_context = f.read()

   # This single file contains:
   # - Workflow DAG for the stage
   # - All required controls with their definitions
   # - Artifacts (inputs/outputs)
   # - Exit criteria
   # - Parallelism rules
   ```

---

### Pattern 2: On-Demand Control Lookup

Use this when you need a specific control definition without loading the full framework.

**Steps:**

1. **Look up control in registry:**
   ```python
   import yaml

   with open("a-sdlc/controls/registry.yaml") as f:
       registry = yaml.safe_load(f)

   # Find control by ID
   control_entry = next(
       c for c in registry['controls']
       if c['id'] == 'SC-3B'
   )
   # Result: {'id': 'SC-3B', 'name': '...', 'track': 'sc', 'stages': [...]}
   ```

2. **Load control definition:**
   ```python
   track = control_entry['track']  # 'sc'
   control_id = control_entry['id']  # 'SC-3B'

   control_path = f"a-sdlc/controls/{track}/{control_id}.yaml"
   with open(control_path) as f:
       control = yaml.safe_load(f)

   # Access:
   # control['description'] - what this control does
   # control['delegation'] - automation level (fully_automated, human_required, etc.)
   # control['required_in_stages'] - [1, 2, 3, ...] which stages this runs in
   # control['artifacts']['inputs'] - required inputs
   # control['artifacts']['outputs'] - produced outputs
   ```

---

### Pattern 3: Task-Driven Navigation

Use this when an agent receives a task description and needs to discover relevant controls.

**Steps:**

1. **Load task index:**
   ```python
   import yaml

   with open("a-sdlc/tasks.yaml") as f:
       tasks_index = yaml.safe_load(f)
   ```

2. **Find matching task:**
   ```python
   user_task = "implement a new REST API endpoint"

   matching_task = next(
       t for t in tasks_index['tasks']
       if t['name'].lower() in user_task.lower()
   )
   # Result:
   # {
   #   'id': 'implement-feature',
   #   'name': 'Implement a feature',
   #   'stage': 3,
   #   'controls': ['QC-3A', 'QC-3B', 'SC-3B', 'SC-3C', ...],
   #   'entry_file': 'context/stage-03-coding-and-implementation.md'
   # }
   ```

3. **Load entry file and control definitions:**
   ```python
   entry_file = matching_task['entry_file']
   stage_context = open(f"a-sdlc/{entry_file}").read()

   # Load all relevant controls
   controls = {}
   for control_id in matching_task['controls']:
       track = control_id.split('-')[0].lower()
       path = f"a-sdlc/controls/{track}/{control_id}.yaml"
       with open(path) as f:
           controls[control_id] = yaml.safe_load(f)
   ```

---

### Pattern 4: Workflow DAG Parsing for Execution Orchestration

Use this when your agent orchestrator needs to understand stage sequencing and parallelism.

**Steps:**

1. **Load stage DAG:**
   ```python
   import yaml

   stage_num = 1
   with open(f"a-sdlc/stages/{stage_num:02d}-*/{{stage_num:02d}-*.yaml") as f:
       stage_def = yaml.safe_load(f)

   workflow = stage_def.get('workflow', {})
   nodes = workflow.get('nodes', [])
   parallelism = workflow.get('parallelism', {})
   ```

2. **Parse dependencies:**
   ```python
   # Build execution graph
   dependency_graph = {}
   for node in nodes:
       node_id = node['id']
       depends_on = node.get('depends_on', [])
       condition = node.get('condition', None)

       dependency_graph[node_id] = {
           'control': node.get('control'),
           'depends_on': depends_on,
           'condition': condition,
           'delegation': node.get('delegation'),
           'actors': node.get('actors', [])
       }
   ```

3. **Topological sort for sequential execution:**
   ```python
   from collections import deque

   def get_execution_order(graph):
       """Returns nodes in execution order respecting dependencies."""
       in_degree = {n: len(graph[n].get('depends_on', [])) for n in graph}
       queue = deque([n for n in graph if in_degree[n] == 0])
       order = []

       while queue:
           node = queue.popleft()
           order.append(node)

           # Find all nodes that depend on this one
           for other_node in graph:
               if node in graph[other_node].get('depends_on', []):
                   in_degree[other_node] -= 1
                   if in_degree[other_node] == 0:
                       queue.append(other_node)

       return order if len(order) == len(graph) else None  # None = cycle detected
   ```

4. **Identify parallel groups:**
   ```python
   parallel_groups = parallelism.get('groups', [])
   # Example: [['n-qc1b', 'n-rc1a', 'n-ac1a']]
   # These 3 nodes can run concurrently after their dependencies resolve
   ```

---

### Pattern 5: Feedback Loop Re-Entry

Use this when your agent detects a Stage 4 test failure or Stage 6 production issue.

**Steps:**

1. **Load feedback loop definition:**
   ```python
   with open("a-sdlc/feedbackloops/feedback-loops.yaml") as f:
       feedback_loops = yaml.safe_load(f)

   workflow = feedback_loops.get('workflow', {})
   nodes = workflow.get('nodes', [])
   decision_gates = workflow.get('parallelism', {}).get('decision_gates', [])
   ```

2. **Execute FL.1 (Path Classification):**
   ```python
   # Get the human decision (Path A or Path B)
   trigger_record = {
       'source_stage': 4,  # or 6
       'control_id': 'SC-4A',
       'alert_id': 'ALT-2024-00123',
       'description': 'SAST found SQL injection in query builder'
   }

   # This is a human decision — your agent surfaces options, RO decides
   path_decision = get_path_classification(trigger_record)  # Returns 'path_a' or 'path_b'
   ```

3. **Execute Path A (Quick Fix) or Path B (Full Re-entry):**
   ```python
   if path_decision == 'path_a':
       # Re-execute minimum controls: QC-3A, QC-3B, SC-3B, SC-3C, GC-3A, QC-4A, SC-4A, RC-4A, SC-5B
       # Runs at Stage 3 (Coding) level
       execute_path_a(trigger_record)

   elif path_decision == 'path_b':
       # Full lifecycle re-entry from Stage 1
       # Treat as new FEAT-XXXX, link to trigger in feature spec
       execute_path_b(trigger_record)
   ```

4. **Complete FL.3 (Activation Record):**
   ```python
   activation_record = {
       'trigger_id': trigger_record['alert_id'],
       'path_selected': path_decision,
       'timestamp': datetime.now().isoformat(),
       'approvals': [...],
       're_entry_id': f"FEAT-{uuid4()}",
       'outcome': 'success' or 'escalated'
   }

   # Save for audit trail
   with open("artifacts/outputs/feedback-loop-activation-record.yaml", 'w') as f:
       yaml.dump(activation_record, f)
   ```

---

## Utility Functions (Python)

The repository provides shared utilities in `scripts/shared.py`. Import and use:

```python
from a_sdlc.scripts.shared import (
    load_yaml_safe,
    find_control_in_registry,
    extract_control_id_from_string,
    build_markdown_table
)

# Load with error handling
framework = load_yaml_safe('a-sdlc/asdlc.yaml')

# Registry lookup
registry = load_yaml_safe('a-sdlc/controls/registry.yaml')
control = find_control_in_registry('SC-3B', registry['controls'])

# Extract control IDs from freetext
text = "We must implement QC-1A and RC-1A before proceeding"
control_ids = extract_control_id_from_string(text)  # ['QC-1A', 'RC-1A']
```

---

## Directory Structure Reference

```
a-sdlc/
├── AGENTS.md                          ← Start here
├── INTEGRATION.md                     ← This file
├── asdlc.yaml                         ← Framework manifest (all stages + controls)
├── tasks.yaml                         ← Task-to-controls navigation index
├── README.md                          ← Human overview
│
├── controls/
│   ├── registry.yaml                  ← Fast lookup: control ID → metadata
│   ├── qc/                            ← Quality Controls (10)
│   ├── rc/                            ← Risk Controls (9)
│   ├── sc/                            ← Security Controls (20)
│   ├── ac/                            ← AI Controls (6)
│   └── gc/                            ← Governance Controls (6)
│
├── stages/
│   ├── 01-intent-ingestion/
│   │   ├── 01-intent-ingestion.yaml   ← Stage definition + workflow DAG
│   │   ├── README.md                  ← Auto-generated docs
│   │   └── artifacts/
│   ├── 02-system-design/
│   ├── 03-coding-implementation/
│   ├── 04-testing-documentation/
│   ├── 05-deployment-release/
│   └── 06-observability-maintenance/
│
├── context/                           ← Auto-generated stage bundles
│   ├── stage-01-intent-ingestion.md
│   ├── stage-02-system-design.md
│   └── ... (one per stage)
│
├── feedbackloops/
│   ├── feedback-loops.yaml            ← Re-entry paths (Path A & B) + DAGs
│   └── autofix-templates/
│
├── directives/
│   ├── core/
│   │   └── core-directives.yaml       ← IMMUTABLE security constraints (SC-0D)
│   └── stages/
│       └── NN-name.yaml               ← Stage-specific directives (SC-2B)
│
├── regulatory/
│   ├── compliance-matrix.yaml         ← DORA & EU AI Act coverage
│   └── README.md                      ← Regulatory narrative
│
├── schema/
│   ├── control.schema.json            ← JSON Schema for control definitions
│   ├── feature-spec.schema.json       ← JSON Schema for FEAT-XXXX specs
│   └── ...
│
├── scripts/
│   ├── shared.py                      ← Shared utility functions
│   ├── generate-docs.py               ← Auto-generate documentation
│   ├── validate.py                    ← Validate framework integrity
│   └── requirements.txt               ← Python dependencies
│
├── manifest/
│   └── catalog.yaml                   ← Documentation generation orchestration
│
└── tests/
    ├── test_shared.py                 ← Unit tests for utilities
    ├── test_validate.py               ← Tests for validation
    └── test_generate_docs.py          ← Tests for doc generation
```

---

## Key Files to Know

| File | Purpose | When to Use |
|------|---------|------------|
| `AGENTS.md` | Agent entrypoint | Session startup |
| `asdlc.yaml` | Full framework manifest | Programmatic discovery |
| `tasks.yaml` | Task-to-control mapping | Agent task routing |
| `context/stage-NN-*.md` | Complete stage context | Entering a stage |
| `controls/registry.yaml` | Control index | Fast lookups |
| `controls/[track]/[ID].yaml` | Individual control def | Understanding a control |
| `stages/NN-*/NN-*.yaml` | Stage definition + DAG | Execution orchestration |
| `feedbackloops/feedback-loops.yaml` | Re-entry paths | Incident handling |
| `directives/core/core-directives.yaml` | **IMMUTABLE** constraints | **ALWAYS load first** |
| `regulatory/compliance-matrix.yaml` | Regulatory mappings | Compliance audits |

---

## Initialization Checklist

When integrating into your agentic repository:

- [ ] Clone or add `a-sdlc` as submodule
- [ ] Load `directives/core/core-directives.yaml` **first** (non-negotiable)
- [ ] Load `asdlc.yaml` for framework discovery
- [ ] Load `tasks.yaml` for task routing
- [ ] Load appropriate `context/stage-NN.md` when entering a stage
- [ ] Verify YAML parsing against schemas in `schema/`
- [ ] Run validation: `python3 a-sdlc/scripts/validate.py`
- [ ] Inject stage-specific directives when entering a new stage
- [ ] Log all control executions to `GC-0A` audit trail

---

## Example: Multi-Stage Orchestration

```python
import yaml
from pathlib import Path
from a_sdlc.scripts.shared import load_yaml_safe, find_control_in_registry

# Initialize framework
framework = load_yaml_safe('a-sdlc/asdlc.yaml')
registry = load_yaml_safe('a-sdlc/controls/registry.yaml')
tasks_index = load_yaml_safe('a-sdlc/tasks.yaml')

# Route task to stage
user_task = "create a new REST API endpoint"
matching_task = next(
    t for t in tasks_index['tasks']
    if 'implement' in t['name'].lower()
)

stage_num = matching_task['stage']

# Load stage context
stage_file = list(Path('a-sdlc/stages').glob(f'{stage_num:02d}-*/')) [0]
stage_def = load_yaml_safe(stage_file / f'{stage_num:02d}-*.yaml')
context = (stage_file.parent / f'context/stage-{stage_num:02d}-*.md').read_text()

# Parse workflow DAG
workflow = stage_def['workflow']
nodes = workflow['nodes']
execution_order = topological_sort(nodes)

# Execute each node
for node_id in execution_order:
    node = next(n for n in nodes if n['id'] == node_id)
    control_id = node['control']

    # Load control definition
    control_registry_entry = find_control_in_registry(control_id, registry['controls'])
    track = control_registry_entry['track']
    control_def = load_yaml_safe(f'a-sdlc/controls/{track}/{control_id}.yaml')

    # Execute based on delegation pattern
    if control_def['delegation'] == 'fully_automated':
        execute_control_automatically(control_def)
    elif control_def['delegation'] == 'agent_drafts_human_approves':
        draft = agent_drafts(control_def)
        approval = wait_for_human_approval(draft)
        if approval:
            proceed_to_next_node()
```

---

## Support

- **Questions about the framework?** See [AGENTS.md](AGENTS.md) and [README.md](README.md)
- **Need to validate your integration?** Run `python3 scripts/validate.py`
- **Issues or bugs?** Report at https://github.com/jvanheerikhuize/a-sdlc/issues
