# Regulatory

This directory contains the regulatory reference material that underpins every A-SDLC control's `regulatory_mapping` field.

## Files

| File | Purpose |
| ---- | ------- |
| [compliance-matrix.yaml](compliance-matrix.yaml) | Consolidated view: which controls satisfy which regulatory requirement areas |
| [sources.yaml](sources.yaml) | Canonical article texts and obligation summaries for DORA and the EU AI Act |
| [gapanalysis/](gapanalysis/) | Gap analysis deliverables: coverage assessment, remediation roadmap, and machine-readable output |
| [moscow/](moscow/) | MoSCoW prioritization framework: 39 controls categorized as Must/Should/Could by regulatory impact |

## Regulatory Frameworks

### DORA — Digital Operational Resilience Act

Regulation (EU) 2022/2554 · Effective 17 January 2025

Applies to financial entities operating in the EU. Key obligations for the A-SDLC:

| DORA Article | Obligation | Primary Controls |
| ------------ | ---------- | ---------------- |
| Art. 8(1–6) | ICT risk management lifecycle | RC-1A, RC-2A, RC-4A, RC-6A |
| Art. 8(5) | Documented procedures for expedited changes | Feedback Loop Path A |
| Art. 9(2) | Prevention and detection of ICT incidents | SC-1A, SC-3B, SC-4A, SC-6A |
| Art. 9(4)(c) | Security policies governing automated agents | SC-0D, SC-2B |
| Art. 10 | Continuous monitoring and response | QC-6A, RC-6A, SC-6B |
| Art. 17–19 | Incident classification, response, and reporting | SC-6A |
| Art. 24–25 | Security testing | SC-4A, SC-4B |

### EU AI Act — Artificial Intelligence Act

Regulation (EU) 2024/1689 · Effective 1 August 2024

Applies to AI systems placed on the EU market. The A-SDLC enforces compliance through the AI control track (AC):

| AI Act Article | Obligation | Primary Controls |
| -------------- | ---------- | ---------------- |
| Art. 6, Annex III | Risk tier classification | AC-1A |
| Art. 9 | Risk management system | AC-1A, RC-4A |
| Art. 10(2)(f), Art. 15(1) | Bias and fairness testing | AC-4A |
| Art. 11, Annex IV | Technical documentation | QC-4C, AC-2A |
| Art. 13 | Transparency and explainability | AC-2A |
| Art. 14 | Human oversight | RC-2A, SC-0D, SC-2B |
| Art. 15 | Accuracy, robustness, security | SC-4A, SC-4B |
| Art. 72–73 | Post-market monitoring and incident reporting | AC-6A, SC-6A |

## How Controls Reference This Material

Each control YAML in `controls/[track]/` carries a `regulatory_mapping` field citing specific articles from the frameworks above. The articles are sourced from [sources.yaml](sources.yaml), and the cross-cutting coverage view is maintained in [compliance-matrix.yaml](compliance-matrix.yaml).
