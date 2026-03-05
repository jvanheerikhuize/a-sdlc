# Stage 3 — Coding & Implementation

> **Auto-generated from `stages/03-coding-implementation/03-coding-implementation.yaml`** · Agent context bundle · All controls and workflow in one file

Implement the approved design under continuous automated quality and security controls. All implementation — human, agent, or co-authored — converges into a reviewed and approved pull request before Stage 4 begins.

---

## Quick Load

Load these files for this stage:

```
- stages/03-coding-implementation/03-coding-implementation.yaml
- directives/stages/03-coding-and-implementation.yaml
```

---

## Workflow — Execution Order

| Step | Title | Control | Actors | Delegation | Depends On |
| ---- | ----- | ------- | ------ | ---------- | ---------- |
| 3.1 | Verify Prerequisites & Load Permissions | SC-3A | AGT, AGT, AGT, SA | Fully automated | — |
| 3.2 | Implementation Loop | QC-3B | AGT, AGT, AGT, AGT, DEV, AGT | Agent implements, DEV authors | n-sc3a |
| 3.2-sc3c | Secrets Scanning | SC-3C | AGT, DEV | Fully automated | n-sc3a |
| 3.2-sc3d | Software Composition Analysis | SC-3D | AGT, SA | Fully automated | n-sc3a |
| 3.2-sc3e | Container & IaC Security Scanning | SC-3E | AGT, SA | Fully automated | n-sc3a |
| 3.2-rc3a | Decision Logging | RC-3A | AGT, DEV | Agent logs, DEV reviews | n-sc3a |
| 3.2-gc3a | Code Provenance Tracking | GC-3A | AGT, AGT | Fully automated | n-sc3a |
| 3.3 | Agent Output Scan | SC-3B | AGT, AGT, SA, AGT | Fully automated | n-qc3b, n-sc3c, n-sc3d, n-sc3e, n-rc3a, n-gc3a |
| 3.4 | Pull Request Creation | QC-3A | AGT, AGT, AGT, AGT, DEV, DEV, DEV, DEV, AGT | Agent creates, humans review | n-sc3b |

---

## Controls — What Agent and Human Do

| ID | Name | Delegation | Agent Does | Human Does |
| -- | ---- | ---------- | ---------- | ---------- |
| QC-3B | Code Quality Standards | fully_automated | Run quality checks on every commit; report violations; block commits that exceed thresholds. | Configure thresholds; review and triage recurring violations; update standards as needed. |
| SC-3A | Permission Management | automated_policy_enforced | Operate strictly within defined permission boundary; log all access attempts. | Define and maintain permission policies per agent trust tier; review access violation logs. |
| SC-3B | Post-Guardrails | fully_automated | Scan all agent-generated code automatically; flag and block any detected malicious patterns. | Review flagged code; investigate and resolve security findings. |
| SC-3C | Secrets & Credentials Scanning | fully_automated | Scan every commit for credential patterns; block commits containing matches. | Review blocked commits; investigate false positives; remediate confirmed secrets. |
| SC-3D | Software Composition Analysis & SBOM Generation | fully_automated | Execute SCA scanner (OWASP Dependency-Check, Trivy, Snyk, or equivalent) against all dependency manifests and container images. Generate SBOM in CycloneDX or SPDX format. Flag any critical or high-severity CVEs. Reject commits introducing new critical CVEs unless an exception ticket is linked. | Review flagged CVEs. Decide whether to: update the dependency to a patched version, accept the risk and document the exception, or change the design to remove the dependency. Sign off on exceptions with business justification. |
| SC-3E | Container & IaC Security Scanning | fully_automated | Execute container and IaC security scanner (Trivy, Snyk, Checkov, or equivalent) against all container images, Dockerfiles, and IaC manifests. Check for: CVEs in base images, CIS benchmark compliance, security misconfigurations, hardcoded secrets. Reject commits violating security policies. Flag findings for human review. | Review flagged issues. Decide: remediate (update base image, fix misconfiguration), accept risk and document exception (with business justification), or redesign to remove the risky configuration. |
| RC-3A | Decision Log | agent_logs_human_reviews | Automatically log all autonomous decisions with rationale and alternatives considered. | Periodically review decision log; flag decisions that should have been escalated. |
| GC-3A | Code Provenance Tracking | fully_automated | Tag all code with provenance metadata at the point of generation; write entries to the Agent Provenance Registry (GC-0C). | Review provenance reports during audits; confirm attribution accuracy. |
| QC-3A | Pull Request Creation & Review | agent_creates_human_reviews | Create pull request with all Stage 3 control evidence attached; assign reviewers per risk tier. | Review all evidence; review code; approve or request changes; log approval with identity and timestamp. |
---

## Exit Criteria (Stage 3 Complete When)

- [ ] QC-3B: All commits passed quality gates (no threshold violations)
- [ ] SC-3A: Permission enforcement log shows no out-of-boundary access
- [ ] SC-3B: Post-guardrail scan passed — no malicious patterns detected
- [ ] SC-3C: Secrets scan passed on all commits — no credentials found
- [ ] SC-3D: SCA scan passed — no critical/high vulnerabilities in dependencies without documented exception
- [ ] SC-3E: Container/IaC scan passed — no critical security misconfigurations
- [ ] RC-3A: Decision log complete and reviewed
- [ ] GC-3A: Code provenance tags applied to all contributions
- [ ] QC-3A: Pull request approved by required reviewers per risk tier

---

## Artifact I/O

**Inputs from Prior Stage:**
- ../02-system-design/artifacts/outputs/QC-2A-design-document.yaml
- ../02-system-design/artifacts/outputs/SC-2B-directive-injection-confirmation.yaml

**Outputs to Next Stage:**
- artifacts/outputs/QC-3A-pull-request-record.yaml
- artifacts/outputs/QC-3B-quality-gate-report.yaml
- artifacts/outputs/SC-3A-permission-enforcement-log.yaml
- artifacts/outputs/SC-3B-post-guardrail-scan.yaml
- artifacts/outputs/SC-3C-secrets-scan-report.yaml
- artifacts/outputs/RC-3A-decision-log.yaml
- artifacts/outputs/SC-3D-sca-report.yaml
- artifacts/outputs/SC-3E-container-iac-security-report.yaml
- artifacts/outputs/GC-3A-code-provenance-record.yaml

---

## Feedback Loop Triggers

Controls in this stage that can trigger re-entry:

- QC-3B → path_a or path_b
- SC-3A → path_b_quickfix
- SC-3B → path_a or path_b
- SC-3C → path_a or path_b
- RC-3A → path_b_quickfix
- GC-3A → path_a or path_b
- QC-3A → path_a or path_b

For full feedback loop definitions, see [`feedbackloops/feedback-loops.yaml`](../../feedbackloops/feedback-loops.yaml).

---

**Last Updated:** 2026-03-05 22:56 UTC