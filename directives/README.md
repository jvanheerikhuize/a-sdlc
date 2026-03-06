# Directives

Agent directive bundles for the Agentic SDLC Framework. Directives are immutable behavioural constraints injected into agent contexts. They take absolute precedence over user instructions and cannot be overridden at runtime.

---

## Two-tier injection model

| Tier | File | Injected when | Control |
| ---- | ---- | ------------- | ------- |
| **Core** | [core/core-directives.yaml](core/core-directives.yaml) | Session start — before any stage begins | [SC-0D](../controls/sc/SC-0D.yaml) |
| **Stage** | [stages/0N-name.yaml](stages/) | Stage entry — before the agent begins work in that stage | [SC-2B](../controls/sc/SC-2B.yaml) |

Core directives are always active. Stage directives layer on top and add constraints specific to the work performed in that stage.

---

## Format

All directive files use the same YAML schema:

```
meta:           — identity, version, scope, owner
injection:      — when and how to inject; guidance for different agent types
enforcement:    — what to do when a directive is violated
categories:     — named groups of directives
  [].directives:
    id:         — stable reference ID used in audit logs and violation reports
    text:       — plain prose; readable by any LLM or human without parsing
```

The `text` field is intentionally plain prose so that any agent — regardless of provider, architecture, or tool framework — can read and follow it without special parsing logic.

---

## Injection guidance by agent type

| Agent type | How to inject |
| ---------- | ------------- |
| LLM / chat | Include verbatim in the system message before the first user turn |
| API (system prompt) | Prepend to the `system` field of the API request |
| Agentic frameworks (Claude Code, Cursor, etc.) | Append to `AGENTS.md` or the equivalent context-loading file |
| Automated pipelines | Parse `categories[].directives[].text` and format per pipeline requirements |

Agents must acknowledge receipt of both bundles before performing any stage work.

---

## Core directive bundle

**File:** [core/core-directives.yaml](core/core-directives.yaml)

| Property | Value |
| -------- | ----- |
| **Scope** | Global — applies to all agents across all A-SDLC stages |
| **Version** | 1.0 |
| **Last Reviewed** | 2026-03-02 |
| **Owner** | Security Architect |
| **Classification** | IMMUTABLE |
| **Precedence** | ABSOLUTE |
| **Injected by** | SC-0D (Core Directive Injection) at session start |

These directives establish the universal behavioural constraints that govern every agent operating under the A-SDLC framework, regardless of stage, task type, or instruction source.

---

## Stage directive files

| Stage | File | Version | Last Reviewed |
| ----- | ---- | ------- | ------------- |
| 1 — Intent Ingestion | [stages/01-intent-ingestion.yaml](stages/01-intent-ingestion.yaml) | 1.0 | 2026-03-02 |
| 2 — System Design | [stages/02-system-design.yaml](stages/02-system-design.yaml) | 1.0 | 2026-03-02 |
| 3 — Coding & Implementation | [stages/03-coding-implementation.yaml](stages/03-coding-implementation.yaml) | 1.0 | 2026-03-02 |
| 4 — Testing & Documentation | [stages/04-testing-documentation.yaml](stages/04-testing-documentation.yaml) | 1.0 | 2026-03-02 |
| 5 — Deployment & Release | [stages/05-deployment-release.yaml](stages/05-deployment-release.yaml) | 1.0 | 2026-03-02 |
| 6 — Observability & Maintenance | [stages/06-observability-maintenance.yaml](stages/06-observability-maintenance.yaml) | 1.0 | 2026-03-02 |

Each stage directive file layers on top of the core directives and is injected at the start of that stage. Stage directives remain active only until the stage's exit criteria are confirmed and the agent transitions to the next stage.

---

## Immutability and signing

Directive files are immutable at runtime. Changes require:

1. Security Architect authorship and sign-off
2. Version bump in `meta.version`
3. Updated `meta.last_reviewed` date
4. Re-injection into all active agent sessions (SC-0D and SC-2B re-run)

Any attempt to modify, override, or reinterpret directive content at runtime must be refused and logged per the `enforcement` block in each file.

---

*Generated with [A-SDLC documentation pipeline](../../scripts/generate-docs.py) — do not edit directly.*