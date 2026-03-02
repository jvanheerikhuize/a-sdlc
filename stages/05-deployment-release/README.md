# Stage 5: Deployment & Release

Promotion to production. This stage carries the **strongest governance requirements** of the entire lifecycle. It ensures everything prior is genuinely complete, the deployment is trustworthy, and there is a verified way back if something goes wrong.

No deployment may proceed without a formal change approval (RC-5A) and cryptographic verification that the deployed artefact matches what was tested (SC-5B).

## Key Tasks

- Verify Stage 4 exit assessment is pass or approved conditional pass
- Confirm every prior control has been executed via audit trail
- Verify release package matches what was tested
- Define rollback triggers; test rollback procedure in pre-production
- Obtain change approval from appropriate authority
- Validate production environment security baseline
- Verify cryptographic checksums match between test and deploy artefacts
- Deploy, smoke test, enter hypercare window, confirm stability, hand over to Stage 6

## Controls

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| QC-5A | Release Readiness Checklist | Verifies all prior gates passed, approvals obtained, documentation current, release package complete. | Agent compiles, human approves | DORA: Art. 8(5); DNB: Release management |
| RC-5A | CAB Approval | Formal change approval. High-risk: CAB. Medium: line management. Low: pre-approved procedure. | Human required | DORA: Art. 8(1), Art. 5; DNB: Change Advisory Board |
| RC-5B | Rollback Plan Validation | Verified rollback strategy with defined triggers, tested in pre-production, with clear decision authority. | Agent validates, human approves | DORA: Art. 11(6); DNB: Rollback and recovery |
| SC-5A | Infrastructure Security | Validates production environment: patching, access controls, network segmentation, IaC compliance. | Fully automated | DORA: Art. 9(2); DNB: Production security baseline; AI Act: Art. 15(4) |
| SC-5B | Deployment Integrity | Cryptographic verification that tested artefacts are exactly what gets deployed. No tampering. | Fully automated | DORA: Art. 9(2), Art. 28a; DNB: Supply chain controls; AI Act: Art. 15(3) |

Full control definitions: [controls.yaml](controls.yaml)

## Stage Exit Criteria

All of the following must be true before handing over to Stage 6:

- [ ] QC-5A passed: release readiness checklist complete with all prior controls evidenced
- [ ] RC-5A passed: formal change approval obtained from appropriate authority
- [ ] RC-5B passed: rollback plan tested in pre-production and approved
- [ ] SC-5A passed: production environment security baseline validated
- [ ] SC-5B passed: cryptographic integrity verified between test and production artefacts
- [ ] Smoke tests passed post-deployment
- [ ] Hypercare window entered; Stage 6 monitoring activated
