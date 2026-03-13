<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/03-coding-implementation/stage.yaml + controls/ + directives/
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 3: Coding & Implementation — Context Bundle

> **Agent load file** — load this at Stage 3 entry for full context.

**Stage:** 03-Coding & Implementation
**Purpose:** Implement the approved design under continuous automated quality and security controls. All implementation — human, agent, or co-authored — converges into a reviewed and approved pull request before Stage 4 begins.

## Files to Load at Stage Entry

- `stages/03-coding-implementation/stage.yaml` — stage definition (steps in: `stages/03-coding-implementation/steps/`)
- `controls/qc/QC-05.yaml` — control definition *(Runs continuously on every commit)*
- `controls/sc/SC-07.yaml` — control definition *(Enforced throughout the implementation session)*
- `controls/sc/SC-08.yaml` — control definition *(Runs on all agent-generated code before PR creation)*
- `controls/sc/SC-09.yaml` — control definition *(Runs on every commit)*
- `controls/sc/SC-10.yaml` — control definition *(Scans all third-party dependencies for known vulnerabilities)*
- `controls/sc/SC-11.yaml` — control definition *(Scans all container images and IaC manifests for security misconfigurations)*
- `controls/rc/RC-04.yaml` — control definition *(Logged throughout; reviewed by Tech Lead)*
- `controls/gc/GC-03.yaml` — control definition *(All code tagged at point of generation)*
- `controls/qc/QC-04.yaml` — control definition *(Final gate — aggregates all other Stage 3 evidence)*

## Workflow Execution Order

| Step | Title | Control | Delegation |
|------|-------|---------|------------|
| 3.1 | Verify Prerequisites & Load Permissions | `SC-07` | Fully automated |
| 3.2 | Implementation Loop | `QC-05` | Agent implements, DEV authors |
| 3.2-sc3c | Secrets Scanning | `SC-09` | Fully automated |
| 3.2-sc3d | Software Composition Analysis | `SC-10` | Fully automated |
| 3.2-sc3e | Container & IaC Security Scanning | `SC-11` | Fully automated |
| 3.2-rc3a | Decision Logging | `RC-04` | Agent logs, DEV reviews |
| 3.2-gc3a | Agent Provenance Registry | `GC-03` | Fully automated |
| 3.3 | Agent Output Scan | `SC-08` | Fully automated |
| 3.4 | Pull Request Creation | `QC-04` | Agent creates, humans review |

## Required Controls

| Control | Name | Notes |
|---------|------|-------|
| [`QC-05`](../controls/qc/QC-05.yaml) | Code Quality Standards | Runs continuously on every commit |
| [`SC-07`](../controls/sc/SC-07.yaml) | Permission Management | Enforced throughout the implementation session |
| [`SC-08`](../controls/sc/SC-08.yaml) | Post-Guardrails | Runs on all agent-generated code before PR creation |
| [`SC-09`](../controls/sc/SC-09.yaml) | Secrets & Credentials Scanning | Runs on every commit |
| [`SC-10`](../controls/sc/SC-10.yaml) | Software Composition Analysis & SBOM Generation | Scans all third-party dependencies for known vulnerabilities |
| [`SC-11`](../controls/sc/SC-11.yaml) | Container & IaC Security Scanning | Scans all container images and IaC manifests for security misconfigurations |
| [`RC-04`](../controls/rc/RC-04.yaml) | Decision Log | Logged throughout; reviewed by Tech Lead |
| [`GC-03`](../controls/gc/GC-03.yaml) | Agent Provenance Registry | All code tagged at point of generation |
| [`QC-04`](../controls/qc/QC-04.yaml) | Pull Request Creation & Review | Final gate — aggregates all other Stage 3 evidence |

## Exit Criteria Checklist

- [ ] QC-05: All commits passed quality gates (no threshold violations)
- [ ] SC-07: Permission enforcement log shows no out-of-boundary access
- [ ] SC-08: Post-guardrail scan passed — no malicious patterns detected
- [ ] SC-09: Secrets scan passed on all commits — no credentials found
- [ ] SC-10: SCA scan passed — no critical/high vulnerabilities in dependencies without documented exception
- [ ] SC-11: Container/IaC scan passed — no critical security misconfigurations
- [ ] RC-04: Decision log complete and reviewed
- [ ] GC-03: Code provenance tags applied to all contributions
- [ ] QC-04: Pull request approved by required reviewers per risk tier

## Input Artifacts

- `../02-system-design/artifacts/outputs/QC-03-design-document.yaml`
- `../02-system-design/artifacts/outputs/SC-02-directive-injection-confirmation.yaml`

## Output Artifacts

- `artifacts/outputs/QC-04-pull-request-record.yaml`
- `artifacts/outputs/QC-05-quality-gate-report.yaml`
- `artifacts/outputs/SC-07-permission-enforcement-log.yaml`
- `artifacts/outputs/SC-08-post-guardrail-scan.yaml`
- `artifacts/outputs/SC-09-secrets-scan-report.yaml`
- `artifacts/outputs/RC-04-decision-log.yaml`
- `artifacts/outputs/SC-10-sca-report.yaml`
- `artifacts/outputs/SC-11-container-iac-security-report.yaml`
- `artifacts/outputs/GC-03-code-provenance-record.yaml`

## Directives Injected at Stage Entry

*None specified*

## Feedback Loop Triggers

*This stage is not a direct feedback loop trigger source.*

---

**Last Updated:** 2026-03-13 14:19 UTC
