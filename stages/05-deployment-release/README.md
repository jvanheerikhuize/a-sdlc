# Stage 5: Deployment & Release

Promotion to production. This stage carries the **strongest governance requirements** of the entire lifecycle. It ensures everything prior is genuinely complete, the deployment is trustworthy, and there is a verified way back if something goes wrong.

No deployment may proceed without a formal change approval (RC-5A) and cryptographic verification that the deployed artefact matches what was tested (SC-5B).

## Steps

Full step-by-step process with roles and decision points: [process.md](process.md)

| Step | Name | Delegation | Sequencing |
| ---- | ---- | ---------- | ---------- |
| [5.1](process.md#step-51--release-readiness-checklist) | Release Readiness Checklist | Agent compiles, REL approves | Runs first — blocks all other steps if gaps found |
| [5.2](process.md#step-52--cab-approval) | CAB Approval | Human required | After 5.1 |
| [5.3](process.md#step-53--rollback-plan-validation) | Rollback Plan Validation | Agent validates, REL approves | Parallel with 5.4, after 5.2 |
| [5.4](process.md#step-54--infrastructure-security-baseline) | Infrastructure Security Baseline | Fully automated | Parallel with 5.3, after 5.2 |
| [5.5](process.md#step-55--deployment-integrity-verification) | Deployment Integrity Verification | Fully automated | After 5.3 and 5.4 |
| [5.6](process.md#step-56--deploy--handover) | Deploy & Handover | Agent executes, OPS confirms | After 5.5 |

## Controls

Stage definition (required controls + exit criteria): [05-deployment-release.yaml](05-deployment-release.yaml)

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| [QC-5A](../../controls/qc/QC-5A.yaml) | Release Readiness Checklist | Verifies all prior gates passed, approvals obtained, documentation current, release package complete. | Agent compiles, REL approves | DORA: Art. 8(5) |
| [RC-5A](../../controls/rc/RC-5A.yaml) | CAB Approval | Formal change approval. High-risk: CAB. Medium: line management. Low: pre-approved procedure. Cannot be delegated. | Human required | DORA: Art. 8(1), Art. 5 |
| [RC-5B](../../controls/rc/RC-5B.yaml) | Rollback Plan Validation | Verified rollback strategy with defined triggers, tested in pre-production, with clear decision authority. | Agent validates, REL approves | DORA: Art. 11(6) |
| [SC-5A](../../controls/sc/SC-5A.yaml) | Infrastructure Security Baseline | Validates production environment: patching, access controls, network segmentation, IaC compliance. | Fully automated | DORA: Art. 9(2); AI Act: Art. 15(4) |
| [SC-5B](../../controls/sc/SC-5B.yaml) | Deployment Integrity | Cryptographic verification that tested artefacts are exactly what gets deployed. No tampering. | Fully automated | DORA: Art. 9(2), Art. 28a; AI Act: Art. 15(3) |

## Stage Exit Criteria

All of the following must be true before handing over to Stage 6:

- [ ] QC-5A passed: release readiness checklist complete with all prior controls evidenced
- [ ] RC-5A passed: formal change approval obtained from appropriate authority
- [ ] RC-5B passed: rollback plan validated and tested in pre-production
- [ ] SC-5A passed: production environment security baseline validated — no unresolved deviations
- [ ] SC-5B passed: cryptographic integrity verified between tested and deployed artefacts
- [ ] Smoke tests passed post-deployment
- [ ] Stage 6 monitoring activated; hypercare window entered

## Artifacts

- **Process:** [process.md](process.md) — Step-by-step guide with roles, dependencies, and decision points
- **Directives:** [../../directives/stages/05-deployment-release.yaml](../../directives/stages/05-deployment-release.yaml) — SC-2B injection payload (immutable)

**Inputs (from Stages 3 and 4):**

- [risk-threshold-evaluation.yaml](../04-testing-documentation/artifacts/outputs/risk-threshold-evaluation.yaml) — Stage 4 go/no-go decision (RC-4A output)
- [pull-request-record.yaml](../03-coding-implementation/artifacts/outputs/pull-request-record.yaml) — Merged PR with evidence (QC-3A output)

**Outputs:**

- [artifacts/outputs/release-readiness-checklist.yaml](artifacts/outputs/release-readiness-checklist.yaml) — QC-5A output
- [artifacts/outputs/change-approval-record.yaml](artifacts/outputs/change-approval-record.yaml) — RC-5A output
- [artifacts/outputs/rollback-plan.yaml](artifacts/outputs/rollback-plan.yaml) — RC-5B output
- [artifacts/outputs/infrastructure-security-report.yaml](artifacts/outputs/infrastructure-security-report.yaml) — SC-5A output
- [artifacts/outputs/deployment-integrity-record.yaml](artifacts/outputs/deployment-integrity-record.yaml) — SC-5B output
