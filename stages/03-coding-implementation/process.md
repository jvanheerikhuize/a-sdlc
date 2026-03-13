<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/03-coding-implementation/stage.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 3: Coding & Implementation — Process

**Stage:** 03-Coding & Implementation
**Purpose:** Implement the approved design under continuous automated quality and security controls. All implementation — human, agent, or co-authored — converges into a reviewed and approved pull request before Stage 4 begins.

## Roles

| Code | Name | Mode | Responsibilities |
|------|------|------|------------------|
| IMPL | Implementation Engineer | Autonomous | Writes code; logs decisions (RC-04); tags provenance (GC-03); scans output (SC-08); creates pull request (QC-04) |
| DEV | Developer | Gated | Authors human-written code; reviews pull request; approves; escalation reviewer for high/critical risk tiers |
| SA | Security Architect | Gated | Defines and maintains agent permission policy (SC-07); reviews violation logs; escalation target for SC-08 and SC-09 findings |
| CO | Compliance Officer | Gated | Reviews code provenance records and audit artefacts during regulatory audits |

## Process Steps

### Step 3.1 — Verify Prerequisites & Load Permissions

**Control:** [`SC-07`](../../controls/sc/SC-07.yaml) · **Delegation:** Fully automated

Verify prerequisites and load permissions

| Actor | Action |
|-------|--------|
| `AGT` | Verify that SC-02 directive injection confirmation exists and covers Stage 3 directives |
| `AGT` | Load agent trust tier and permission policy from SC-07 |
| `AGT` | Confirm that directives/stages/03-coding-implementation.yaml has been acknowledged |
| `SA` | Confirms permission policy is up to date for the agent trust tier |

**Input:** Directive injection confirmation (Stage 2 SC-02 output)

**Output:** Permission enforcement log started (artifacts/outputs/permission-enforcement-log.yaml)


### Step 3.2 — Implementation Loop

**Control:** [`QC-05`](../../controls/qc/QC-05.yaml) · **Delegation:** Agent implements, DEV authors

Code quality standards (per-commit)

| Actor | Action |
|-------|--------|
| `AGT` | Implement code against the approved Stage 2 design document |
| `AGT` | Tag all agent-generated code with provenance metadata at point of generation (GC-03 Agent Provenance Registry) |
| `AGT` | Commit; QC-05 runs quality gates and SC-09 scans for secrets automatically |
| `AGT` | Log all significant autonomous decisions to the decision log (RC-04): rationale, alternatives considered |
| `DEV` | Review and triage any QC-05 violations or SC-09 blocked commits; resolve before re-committing |
| `AGT` | Repeat until all design requirements are implemented |

**Input:** Approved design document

**Output:** Quality gate report (artifacts/outputs/quality-gate-report.yaml) · Secrets scan report (artifacts/outputs/secrets-scan-report.yaml) · Decision log (artifacts/outputs/decision-log.yaml)


### Step 3.2-sc3c — Secrets Scanning

**Control:** [`SC-09`](../../controls/sc/SC-09.yaml) · **Delegation:** Fully automated

Secrets and credentials scanning (per-commit)

| Actor | Action |
|-------|--------|
| `AGT` | Scan every commit for exposed secrets, API keys, and credentials |
| `DEV` | On secret detection: remove secret, rotate the credential, and re-commit |

**Input:** Code commits

**Output:** Secrets scan report (artifacts/outputs/secrets-scan-report.yaml)


### Step 3.2-sc3d — Software Composition Analysis

**Control:** [`SC-10`](../../controls/sc/SC-10.yaml) · **Delegation:** Fully automated

Software Composition Analysis and SBOM generation

| Actor | Action |
|-------|--------|
| `AGT` | Generate SBOM; scan all third-party dependencies for known CVEs |
| `SA` | Review critical/high findings; document risk acceptance if needed |

**Input:** Dependency manifests (package.json, requirements.txt, etc.)

**Output:** SCA report with SBOM (artifacts/outputs/sca-report.yaml)


### Step 3.2-sc3e — Container & IaC Security Scanning

**Control:** [`SC-11`](../../controls/sc/SC-11.yaml) · **Delegation:** Fully automated

Container and IaC security scanning

| Actor | Action |
|-------|--------|
| `AGT` | Scan all container images and IaC manifests (Terraform, CloudFormation, etc.) for misconfigurations |
| `SA` | Triage findings; remediate or document risk acceptance |

**Input:** Container images and IaC manifests

**Output:** Container and IaC security report (artifacts/outputs/container-iac-security-report.yaml)


### Step 3.2-rc3a — Decision Logging

**Control:** [`RC-04`](../../controls/rc/RC-04.yaml) · **Delegation:** Agent logs, DEV reviews

Decision log (logged throughout)

| Actor | Action |
|-------|--------|
| `AGT` | Log all significant autonomous decisions: rationale, alternatives considered, decision owner |
| `DEV` | Review decision log; flag any gaps or unexplained decisions |

**Input:** Implementation activities

**Output:** Decision log (artifacts/outputs/decision-log.yaml)


### Step 3.2-gc3a — Agent Provenance Registry

**Control:** [`GC-03`](../../controls/gc/GC-03.yaml) · **Delegation:** Fully automated

Code provenance tracking (per-commit)

| Actor | Action |
|-------|--------|
| `AGT` | Tag all agent-generated code with provenance metadata (author, model, date, commitment) at point of generation |
| `AGT` | Register tags in GC-03 provenance registry |

**Input:** Generated code

**Output:** Provenance registry entries


### Step 3.3 — Agent Output Scan

**Control:** [`SC-08`](../../controls/sc/SC-08.yaml) · **Delegation:** Fully automated

Post-guardrails scan on agent-generated code

| Actor | Action |
|-------|--------|
| `AGT` | Trigger SC-08 scan across all agent-generated code in the branch |
| `AGT` | Report findings: file, line, category, severity |
| `SA` | Review any flagged findings; determine resolution |
| `AGT` | Block PR creation if any critical or high findings remain unresolved |

**Input:** All agent-generated code on the branch

**Output:** Post-guardrail scan result (artifacts/outputs/post-guardrail-scan.yaml)


### Step 3.4 — Pull Request Creation

**Control:** [`QC-04`](../../controls/qc/QC-04.yaml) · **Delegation:** Agent creates, humans review

Pull request creation and review (final gate)

| Actor | Action |
|-------|--------|
| `AGT` | Assemble evidence package: all Stage 3 control outputs |
| `AGT` | Create pull request from feature branch to target branch |
| `AGT` | Attach all evidence artefacts to the PR |
| `AGT` | Assign reviewers per risk tier from Stage 1 RC-01 |
| `DEV` | Review code changes against the approved design document |
| `DEV` | Review all Stage 3 evidence artefacts (quality gate report, decision log, scan results) |
| `DEV` | Request changes or approve; all requested changes must be resolved before re-review |
| `DEV` | Approve: record identity and timestamp; PR is eligible for merge |
| `AGT` | Update pull request record with approval details |

**Input:** All Stage 3 control outputs + approved design document

**Output:** Pull request record (artifacts/outputs/pull-request-record.yaml) — status: approved


## Exit Criteria

- QC-05: All commits passed quality gates (no threshold violations)
- SC-07: Permission enforcement log shows no out-of-boundary access
- SC-08: Post-guardrail scan passed — no malicious patterns detected
- SC-09: Secrets scan passed on all commits — no credentials found
- SC-10: SCA scan passed — no critical/high vulnerabilities in dependencies without documented exception
- SC-11: Container/IaC scan passed — no critical security misconfigurations
- RC-04: Decision log complete and reviewed
- GC-03: Code provenance tags applied to all contributions
- QC-04: Pull request approved by required reviewers per risk tier


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


## References

- Stage definition: 
- Controls: See `required_controls` in stage YAML.

---

**Last Updated:** 2026-03-13 14:19 UTC
