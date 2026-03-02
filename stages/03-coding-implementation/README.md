# Stage 3: Coding & Implementation

Code is produced by human developers, AI coding agents, or both. This is the **most control-dense stage** of the lifecycle: it enforces quality, controls agent permissions, scans for security issues and leaked secrets, tracks code provenance, and converges everything into a reviewed pull request.

No agent may begin work in this stage without first having received the signed Stage 3 directive bundle (SC-2B) from Stage 2.

## Steps

Full step-by-step process with roles and decision points: [process.md](process.md)

| Step | Name | Delegation | Sequencing |
| ---- | ---- | ---------- | ---------- |
| [3.1](process.md#step-31--verify-prerequisites--load-permissions) | Verify Prerequisites & Load Permissions | Fully automated | Runs first — blocks all other steps if failed |
| [3.2](process.md#step-32--implementation-loop) | Implementation Loop | Agent implements, human authors | After 3.1 — continuous until complete |
| [3.3](process.md#step-33--agent-output-scan) | Agent Output Scan | Fully automated | After 3.2 |
| [3.4](process.md#step-34--create-pull-request) | Create Pull Request | Agent creates | After 3.3 |
| [3.5](process.md#step-35--review--approve) | Review & Approve | Human required | After 3.4 |

## Controls

Stage definition (required controls + exit criteria): [03-coding-implementation.yaml](03-coding-implementation.yaml)

| ID | Name | What It Does | Who Decides | Regulatory Mapping |
| -- | ---- | ------------ | ----------- | ------------------ |
| [SC-3A](../../controls/sc/SC-3A.yaml) | Permission Management | Enforces least-privilege on what the agent can access: files, APIs, data, and network resources. | Automated (policy-enforced) | DORA: Art. 9(4)(c); DNB: Logical access management; AI Act: Art. 15(4) |
| [QC-3B](../../controls/qc/QC-3B.yaml) | Code Quality Standards | Automated linting, complexity thresholds, coding standards, and maintainability metrics. Runs on every commit. | Fully automated | DORA: Art. 8(4); DNB: Software quality; AI Act: Art. 15(1) |
| [SC-3C](../../controls/sc/SC-3C.yaml) | Secrets & Credentials Scanning | Real-time scanning for hardcoded secrets. Blocks commits containing exposed credentials. | Fully automated | DORA: Art. 9(4)(c); DNB: Credential management |
| [RC-3A](../../controls/rc/RC-3A.yaml) | Decision Log | Captures implementation decisions — especially agent autonomous choices. Records rationale and alternatives. | Agent logs, human reviews | DORA: Art. 8(6); DNB: Decision audit trail; AI Act: Art. 12(1) |
| [GC-3A](../../controls/gc/GC-3A.yaml) | Code Provenance Tracking | Records human-written vs. agent-generated code. Immutable records for DORA accountability. | Fully automated | DORA: Art. 8(6); DNB: Auditability; AI Act: Art. 12; Art. 17(1)(f) |
| [SC-3B](../../controls/sc/SC-3B.yaml) | Post-Guardrails | Scans agent-generated code for malicious patterns, backdoors, and adversarial constructs. | Fully automated | DORA: Art. 9(2); DNB: Code integrity; AI Act: Art. 15(3) |
| [QC-3A](../../controls/qc/QC-3A.yaml) | Pull Request Creation & Review | All work converges into a PR with evidence from every other Stage 3 control. Reviewed before merge. | Agent creates, human reviews | DORA: Art. 8(5); DNB: Four-eyes principle |

## Stage Exit Criteria

All of the following must be true before progressing to Stage 4:

- [ ] SC-3A verified: agent operating within defined permission boundary
- [ ] QC-3B passed: all commits passed quality gates (no threshold violations)
- [ ] SC-3C passed: no secrets or credentials detected in committed code
- [ ] RC-3A completed: decision log up to date and reviewed by Tech Lead
- [ ] GC-3A confirmed: all code tagged with provenance metadata
- [ ] SC-3B passed: agent output scanned and clear of malicious patterns
- [ ] QC-3A passed: pull request reviewed and approved by required reviewers per risk tier

## Artifacts

- **Process:** [process.md](process.md) — Step-by-step guide with roles, dependencies, and decision points
- **Directives:** [../../directives/stages/03-coding-implementation.yaml](../../directives/stages/03-coding-implementation.yaml) — SC-2B injection payload (immutable)

**Inputs (from Stage 2):**

- [design-document.yaml](../02-system-design/artifacts/outputs/design-document.yaml) — Approved system design (QC-2A output)
- [directive-injection-confirmation.yaml](../02-system-design/artifacts/outputs/directive-injection-confirmation.yaml) — SC-2B confirmation (prerequisite)

**Outputs:**

- [artifacts/outputs/permission-enforcement-log.yaml](artifacts/outputs/permission-enforcement-log.yaml) — SC-3A output
- [artifacts/outputs/quality-gate-report.yaml](artifacts/outputs/quality-gate-report.yaml) — QC-3B output
- [artifacts/outputs/decision-log.yaml](artifacts/outputs/decision-log.yaml) — RC-3A output
- [artifacts/outputs/post-guardrail-scan.yaml](artifacts/outputs/post-guardrail-scan.yaml) — SC-3B output
- [artifacts/outputs/secrets-scan-report.yaml](artifacts/outputs/secrets-scan-report.yaml) — SC-3C output
- [artifacts/outputs/pull-request-record.yaml](artifacts/outputs/pull-request-record.yaml) — QC-3A output
