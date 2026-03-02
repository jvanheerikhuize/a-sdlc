# Stage 3: Coding & Implementation

Code is produced by human developers, AI coding agents, or both. This is the **most control-dense stage** of the lifecycle: it enforces quality, controls agent permissions, scans for security issues and leaked secrets, tracks code provenance, and converges everything into a reviewed pull request.

No agent may begin work in this stage without first having received the signed Core Security Directives payload (SC-2B) from Stage 2.

## Key Tasks

- Verify agent trust tier and load permission policy (SC-3A)
- Confirm signed Core Security Directives are loaded (SC-2B — injected in Stage 2)
- Produce code against approved Stage 2 design
- Run continuous code quality checks (QC-3B)
- Log all significant implementation decisions with rationale (RC-3A)
- Scan all code for secrets and credentials in real-time (SC-3C)
- Tag all code with provenance metadata: human, agent, or co-authored (GC-3A)
- Validate agent output for malicious patterns (SC-3B)
- Create pull request with all evidence attached; assign risk-appropriate reviewers
- Resolve all review comments; log approval with reviewer identities and timestamp

## Controls

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| QC-3A | Pull Request Creation & Review | All work converges into a PR with evidence from every other Stage 3 control. Reviewed before merge. | Agent creates, human reviews | DORA: Art. 8(5); DNB: Four-eyes principle |
| QC-3B | Code Quality Standards | Automated linting, complexity thresholds, coding standards, and maintainability metrics. | Fully automated | DORA: Art. 8(4); DNB: Software quality; AI Act: Art. 15(1) |
| RC-3A | Decision Log | Captures implementation decisions — especially agent autonomous choices. Records rationale and alternatives. | Agent logs, human reviews | DORA: Art. 8(6); DNB: Decision audit trail; AI Act: Art. 12(1) |
| SC-3A | Permission Management | Enforces least-privilege on what the agent can access: files, APIs, data, and network resources. | Automated (policy-enforced) | DORA: Art. 9(4)(c); DNB: Logical access management; AI Act: Art. 15(4) |
| SC-3B | Post-Guardrails | Scans agent-generated code for malicious patterns, backdoors, and adversarial constructs. | Fully automated | DORA: Art. 9(2); DNB: Code integrity; AI Act: Art. 15(3) |
| SC-3C | Secrets & Credentials Scanning | Real-time scanning for hardcoded secrets. Blocks commits containing exposed credentials. | Fully automated | DORA: Art. 9(4)(c); DNB: Credential management |
| GC-3A | Code Provenance Tracking | Records human-written vs. agent-generated code. Immutable records for DORA accountability. | Fully automated | DORA: Art. 8(6); DNB: Auditability; AI Act: Art. 12; Art. 17(1)(f) |

Stage definition (required controls + exit criteria): [stage.yaml](stage.yaml)

Individual control definitions by track:
  - [GC-3A](../../controls/gc/GC-3A.yaml)
  - [QC-3A](../../controls/qc/QC-3A.yaml), [QC-3B](../../controls/qc/QC-3B.yaml)
  - [RC-3A](../../controls/rc/RC-3A.yaml)
  - [SC-3A](../../controls/sc/SC-3A.yaml), [SC-3B](../../controls/sc/SC-3B.yaml), [SC-3C](../../controls/sc/SC-3C.yaml)

## Stage Exit Criteria

All of the following must be true before progressing to Stage 4:

- [ ] SC-3A verified: agent operating within defined permission boundary
- [ ] QC-3B passed: all quality gates clear
- [ ] SC-3C passed: no secrets or credentials detected in committed code
- [ ] SC-3B passed: agent output scanned and clear of malicious patterns
- [ ] GC-3A confirmed: all code tagged with provenance metadata
- [ ] RC-3A completed: decision log up to date with all significant decisions
- [ ] QC-3A passed: pull request reviewed and approved by required reviewers
