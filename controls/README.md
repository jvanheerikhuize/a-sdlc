# Controls

This directory contains all 51 A-SDLC control definitions, organised by track.

## Tracks

| Directory | Code | Name | Controls | Owner team |
| --------- | ---- | ---- | -------- | ---------- |
| [qc/](qc/) | `QC` | Quality Controls | 10 | Engineering / Product |
| [rc/](rc/) | `RC` | Risk Controls | 9 | Risk Management |
| [sc/](sc/) | `SC` | Security Controls | 20 | Security |
| [ac/](ac/) | `AC` | AI Controls | 6 | AI Governance |
| [gc/](gc/) | `GC` | Governance Controls | 6 | Governance & Compliance |

## Fast Lookup

[registry.yaml](registry.yaml) — flat index of all 51 controls with ID, name, stage, track, delegation pattern, and file path. Use this for programmatic lookup or quick reference without reading individual control files.

## Control ID Format

`[Track]-[Stage][Letter]` — e.g. `SC-2B`, `QC-3A`, `GC-0A`

- Stage `0` = cross-cutting (always active)
- Stages `1`–`6` = lifecycle stage where the control is primarily executed

## Cross-Cutting Controls

Six controls are always active regardless of stage:

| ID | Name | Payload |
| -- | ---- | ------- |
| [SC-0D](sc/SC-0D.yaml) | Core Directive Injection | [directives/core/core-directives.yaml](../directives/core/core-directives.yaml) |
| [SC-2B](sc/SC-2B.yaml) | Stage Directive Injection | [directives/stages/](../directives/stages/) |
| [GC-0A](gc/GC-0A.yaml) | Audit Trail & Compliance Reporting | — |
| [GC-0B](gc/GC-0B.yaml) | End-to-End Traceability | — |
| [GC-0C](gc/GC-0C.yaml) | Agent Provenance Registry | — |
| [GC-0D](gc/GC-0D.yaml) | Compliance Evidence Automation | — |

## Control File Structure

Each control YAML conforms to [../schema/control.schema.json](../schema/control.schema.json):

```text
id                   # Unique ID (must match filename)
name                 # Short title
description          # What this control enforces and why
required_in_stages   # List of stages + mandatory flag
track                # code + name
delegation           # pattern + agent_role + human_role
owner                # team + role + contact
regulatory_mapping   # dora / eu_ai_act articles
inputs               # Artifacts consumed
outputs              # Artifacts produced (type, description, retention)
failure_behaviour    # action + escalation_target
automation           # frequency
dependencies         # Other control IDs that must run first
feedback_loops       # Which feedback loop paths use this control
metadata             # version, last_updated, status
```

## Editing Guidelines

- **Control owners** edit only their `controls/[track]/` files.
- **Stage owners** edit only `stages/NN-name/NN-name.yaml` to add or remove control references.
- After any change, run `python3 scripts/validate.py` to verify schema compliance and cross-reference integrity.
