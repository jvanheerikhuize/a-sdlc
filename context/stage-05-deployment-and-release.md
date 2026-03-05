# Stage 5 — Deployment & Release

> **Auto-generated from `stages/05-deployment-release/05-deployment-release.yaml`** · Agent context bundle · All controls and workflow in one file

Execute the approved deployment with formal CAB sign-off, verified rollback procedures, and cryptographic artefact integrity checking. RC-5A CAB Approval is a mandatory human gate that cannot be delegated.

---

## Quick Load

Load these files for this stage:

```
- stages/05-deployment-release/05-deployment-release.yaml
- directives/stages/05-deployment-and-release.yaml
```

---

## Workflow — Execution Order

| Step | Title | Control | Actors | Delegation | Depends On |
| ---- | ----- | ------- | ------ | ---------- | ---------- |
| 5.1 | Release Readiness Checklist | QC-5A | AGT, AGT, AGT, AGT, REL | Agent compiles, REL approves | — |
| 5.2 | CAB Approval | RC-5A | AGT, RO, RO, RO | Human required | n-qc5a |
| 5.3 | Rollback Plan Validation | RC-5B | AGT, AGT, AGT, REL | Agent validates, REL approves | n-rc5a |
| 5.4 | Infrastructure Security Baseline | SC-5A | AGT, AGT, SA | Fully automated | n-rc5a |
| 5.4-secrets | Secrets & Key Management Lifecycle | SC-5C | AGT, AGT, SA | Fully automated | n-rc5a |
| 5.5 | Deployment Integrity Verification | SC-5B | AGT, AGT, AGT, AGT | Fully automated | n-rc5b, n-sc5a, n-sc5c |
| 5.6 | Deploy & Handover | None | AGT, OPS, OPS, OPS, OPS | Agent executes pipeline, OPS confirms | n-sc5b |

---

## Controls — What Agent and Human Do

| ID | Name | Delegation | Agent Does | Human Does |
| -- | ---- | ---------- | ---------- | ---------- |
| QC-5A | Release Readiness Checklist | agent_compiles_human_approves | Compile release readiness checklist by querying audit trail for all control pass evidences; flag any gaps. | Review checklist; approve release package or require resolution of flagged gaps. |
| RC-5A | CAB Approval | human_required | Prepare change approval request with full evidence package; schedule CAB slot if required. | Make the formal approval decision. This control cannot be delegated to an agent under any circumstances. |
| RC-5B | Rollback Plan Validation | agent_validates_human_approves | Validate rollback plan completeness; execute rollback test in pre-production; report results. | Review rollback test results; approve plan or require improvements before deployment. |
| SC-5A | Infrastructure Security | fully_automated | Scan production environment configuration against approved security baseline; report any deviations. | Review deviations; resolve before deployment or provide documented risk acceptance. |
| SC-5B | Deployment Integrity | fully_automated | Compute and compare cryptographic checksums of test and deployment artefacts; block deployment if any mismatch. | Investigate any detected integrity failures before deployment can proceed. |
| SC-5C | Secrets & Key Management Lifecycle | agent_checks_human_approves | Before deployment: validate all required secrets against a vault system. Check: is each secret stored in approved vault (Vault, AWS Secrets Manager, Azure Key Vault)? Does it have a defined rotation schedule? Has it been rotated within policy limits? Are ACLs configured to allow only necessary services? Is audit logging enabled? Verify deployment process uses runtime secret injection, not config files. Report any violations. | Review agent validation report. For any failed validation: decide to remediate (rotate secret, update deployment process), accept risk (document exception), or delay deployment. Approve deployment only if all secrets pass validation. |
| AC-2B | AI Model Governance & Version Control | agent_creates_human_reviews | Create model registry entry for each AI model. Populate: model ID, version, provider, training data description, performance metrics, bias test results, known limitations. For model updates: propose new version with change rationale. Track model dependency in deployment configuration. | Review model registry entry. Validate training data provenance and licensing. Approve model version for use. For model updates: approve change or request rollback. Monitor for performance degradation. |
---

## Exit Criteria (Stage 5 Complete When)

- [ ] QC-5A: Release readiness checklist completed — all prior controls evidenced
- [ ] RC-5A: CAB approval granted by appropriate authority
- [ ] RC-5B: Rollback plan validated and tested in pre-production
- [ ] SC-5A: Infrastructure security baseline validated — no unresolved deviations
- [ ] SC-5B: Deployment integrity verified — artefact checksums match tested build
- [ ] SC-5C: All secrets/keys validated for proper vaulting, rotation, and access control

---

## Artifact I/O

**Inputs from Prior Stage:**
- ../04-testing-documentation/artifacts/outputs/RC-4A-risk-threshold-evaluation.yaml
- ../03-coding-implementation/artifacts/outputs/QC-3A-pull-request-record.yaml

**Outputs to Next Stage:**
- artifacts/outputs/QC-5A-release-readiness-checklist.yaml
- artifacts/outputs/RC-5A-change-approval-record.yaml
- artifacts/outputs/RC-5B-rollback-plan.yaml
- artifacts/outputs/SC-5A-infrastructure-security-report.yaml
- artifacts/outputs/SC-5B-deployment-integrity-record.yaml
- artifacts/outputs/SC-5C-secrets-management-report.yaml

---

## Feedback Loop Triggers

Controls in this stage that can trigger re-entry:

- RC-5A → path_b_quickfix
- SC-5B → path_a or path_b

For full feedback loop definitions, see [`feedbackloops/feedback-loops.yaml`](../../feedbackloops/feedback-loops.yaml).

---

**Last Updated:** 2026-03-05 22:56 UTC