<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/05-deployment-release/05-deployment-release.yaml + controls/ + directives/
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 5: Deployment & Release — Context Bundle

> **Agent load file** — load this at Stage 5 entry for full context.

**Stage:** 05-Deployment & Release
**Purpose:** Execute the approved deployment with formal CAB sign-off, verified rollback procedures, and cryptographic artefact integrity checking. RC-06 CAB Approval is a mandatory human gate that cannot be delegated.

## Files to Load at Stage Entry

- `stages/05-deployment-release/05-deployment-release.yaml` — stage definition and workflow DAG
- `controls/qc/QC-09.yaml` — control definition
- `controls/rc/RC-06.yaml` — control definition *(Human-required gate — cannot be delegated to an agent)*
- `controls/rc/RC-07.yaml` — control definition
- `controls/sc/SC-16.yaml` — control definition
- `controls/sc/SC-17.yaml` — control definition *(Must run immediately before deployment execution)*
- `controls/sc/SC-18.yaml` — control definition *(Verify all secrets and keys are properly vaulted, rotated, and access-controlled)*
- `controls/ac/AC-04.yaml` — control definition *(Applicable when change involves AI models — verify deployed model version matches registry)*

## Workflow Execution Order

| Step | Title | Control | Delegation |
|------|-------|---------|------------|
| 5.1 | Release Readiness Checklist | `QC-09` | Agent compiles, REL approves |
| 5.2 | CAB Approval | `RC-06` | Human required |
| 5.3 | Rollback Plan Validation | `RC-07` | Agent validates, REL approves |
| 5.4 | Infrastructure Security Baseline | `SC-16` | Fully automated |
| 5.4-secrets | Secrets & Key Management Lifecycle | `SC-18` | Fully automated |
| 5.5 | Deployment Integrity Verification | `SC-17` | Fully automated |
| 5.6 | Deploy & Handover | `—` | Agent executes pipeline, OPS confirms |

## Required Controls

| Control | Name | Notes |
|---------|------|-------|
| [`QC-09`](../controls/qc/QC-09.yaml) | Release Readiness Checklist |  |
| [`RC-06`](../controls/rc/RC-06.yaml) | CAB Approval | Human-required gate — cannot be delegated to an agent |
| [`RC-07`](../controls/rc/RC-07.yaml) | Rollback Plan Validation |  |
| [`SC-16`](../controls/sc/SC-16.yaml) | Infrastructure Security |  |
| [`SC-17`](../controls/sc/SC-17.yaml) | Deployment Integrity | Must run immediately before deployment execution |
| [`SC-18`](../controls/sc/SC-18.yaml) | Secrets & Key Management Lifecycle | Verify all secrets and keys are properly vaulted, rotated, and access-controlled |
| [`AC-04`](../controls/ac/AC-04.yaml) | AI Model Governance & Version Control | Applicable when change involves AI models — verify deployed model version matches registry |

## Exit Criteria Checklist

- [ ] QC-09: Release readiness checklist completed — all prior controls evidenced
- [ ] RC-06: CAB approval granted by appropriate authority
- [ ] RC-07: Rollback plan validated and tested in pre-production
- [ ] SC-16: Infrastructure security baseline validated — no unresolved deviations
- [ ] SC-17: Deployment integrity verified — artefact checksums match tested build
- [ ] SC-18: All secrets/keys validated for proper vaulting, rotation, and access control

## Input Artifacts

- `../04-testing-documentation/artifacts/outputs/RC-05-risk-threshold-evaluation.yaml`
- `../03-coding-implementation/artifacts/outputs/QC-04-pull-request-record.yaml`

## Output Artifacts

- `artifacts/outputs/QC-09-release-readiness-checklist.yaml`
- `artifacts/outputs/RC-06-change-approval-record.yaml`
- `artifacts/outputs/RC-07-rollback-plan.yaml`
- `artifacts/outputs/SC-16-infrastructure-security-report.yaml`
- `artifacts/outputs/SC-17-deployment-integrity-record.yaml`
- `artifacts/outputs/SC-18-secrets-management-report.yaml`

## Directives Injected at Stage Entry

*None specified*

## Feedback Loop Triggers

*This stage is not a direct feedback loop trigger source.*

---

**Last Updated:** 2026-03-13 12:43 UTC
