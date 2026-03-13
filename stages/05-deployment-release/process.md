<!-- AUTO-GENERATED FILE — do not edit directly.
     Source: stages/05-deployment-release/stage.yaml
     Regenerate: bash scripts/generate-docs.sh -->

# Stage 5: Deployment & Release — Process

**Stage:** 05-Deployment & Release
**Purpose:** Execute the approved deployment with formal CAB sign-off, verified rollback procedures, and cryptographic artefact integrity checking. RC-06 CAB Approval is a mandatory human gate that cannot be delegated.

## Roles

| Code | Name | Mode | Responsibilities |
|------|------|------|------------------|
| RENG | Release Engineer | Autonomous | Compiles release readiness checklist; prepares CAB submission; validates rollback; runs infrastructure and integrity checks |
| REL | Release Manager | Gated | Reviews and approves release readiness checklist and rollback plan; orchestrates deployment execution |
| RO | Risk Officer | Gated | Makes the formal CAB approval decision for high-risk changes |
| SA | Security Architect | Gated | Reviews infrastructure security baseline deviations; investigates deployment integrity failures |
| OPS | Operations / SRE | Gated | Executes deployment pipeline; monitors smoke tests; manages hypercare window; confirms Stage 6 handover |
| CO | Compliance Officer | Gated | Reviews approval records during regulatory audits |

## Process Steps

### Step 5.1 — Release Readiness Checklist

**Control:** [`QC-09`](../../controls/qc/QC-09.yaml) · **Delegation:** Agent compiles, REL approves

Release readiness checklist

| Actor | Action |
|-------|--------|
| `AGT` | Query audit trail (GC-01) to confirm all prior stage controls were executed and passed |
| `AGT` | Confirm Stage 4 RC-05 result is pass or approved conditional pass |
| `AGT` | Verify documentation is current and release package is complete |
| `AGT` | Flag any gaps in control evidence |
| `REL` | Review completed checklist; approve release package or require resolution of gaps |

**Input:** Audit trail (GC-01) + Stage 4 risk threshold evaluation (RC-05 output)

**Output:** Release readiness checklist (artifacts/outputs/release-readiness-checklist.yaml)


### Step 5.2 — CAB Approval

**Control:** [`RC-06`](../../controls/rc/RC-06.yaml) · **Delegation:** Human required

CAB (Change Advisory Board) approval (human-required gate)

| Actor | Action |
|-------|--------|
| `AGT` | Prepare change approval request with full release readiness package; schedule CAB slot if required |
| `RO` | Review the full evidence package and make the formal approval decision |
| `RO` | Approve: record identity, role, and timestamp; advance to Steps 5.3 and 5.4 |
| `RO` | Reject: document rejection reason; work may return to any required stage |

**Input:** Release readiness checklist (Step 5.1 output) + Stage 1 risk classification

**Output:** Change approval record (artifacts/outputs/change-approval-record.yaml)


### Step 5.3 — Rollback Plan Validation

**Control:** [`RC-07`](../../controls/rc/RC-07.yaml) · **Delegation:** Agent validates, REL approves

Rollback plan validation

| Actor | Action |
|-------|--------|
| `AGT` | Validate rollback plan completeness: triggers, procedure steps, decision authority, time window |
| `AGT` | Execute rollback procedure test in pre-production environment; record execution time |
| `AGT` | Report test results |
| `REL` | Review rollback test results; approve plan or require improvements before deployment |

**Input:** Rollback plan draft + pre-production environment access

**Output:** Rollback plan validation report (artifacts/outputs/rollback-plan.yaml)


### Step 5.4 — Infrastructure Security Baseline

**Control:** [`SC-16`](../../controls/sc/SC-16.yaml) · **Delegation:** Fully automated

Infrastructure security baseline validation

| Actor | Action |
|-------|--------|
| `AGT` | Scan production environment configuration against approved security baseline |
| `AGT` | Check: patching status, access control configurations, network segmentation, IaC compliance, configuration drift |
| `SA` | Review any deviations; resolve before deployment or provide documented risk acceptance |

**Input:** Production environment + approved security baseline configuration

**Output:** Infrastructure security baseline report (artifacts/outputs/infrastructure-security-report.yaml)


### Step 5.4-secrets — Secrets & Key Management Lifecycle

**Control:** [`SC-18`](../../controls/sc/SC-18.yaml) · **Delegation:** Fully automated

Secrets and key management lifecycle validation

| Actor | Action |
|-------|--------|
| `AGT` | Verify all secrets and encryption keys for the deployment are properly vaulted and accessible |
| `AGT` | Validate key rotation schedules and access control policies |
| `SA` | Review vaulting configuration; approve or require remediation |

**Input:** Deployment configuration + secret vault configuration

**Output:** Secrets management validation report (artifacts/outputs/secrets-management-report.yaml)


### Step 5.5 — Deployment Integrity Verification

**Control:** [`SC-17`](../../controls/sc/SC-17.yaml) · **Delegation:** Fully automated

Deployment integrity verification (immediately before deploy)

| Actor | Action |
|-------|--------|
| `AGT` | Compute cryptographic checksums of artefacts staged for production deployment |
| `AGT` | Compare against checksums of artefacts tested in Stage 4 |
| `AGT` | Match: record verification and advance to Step 5.6 |
| `AGT` | Mismatch: block deployment immediately; notify SA; initiate security incident process |

**Input:** Staged deployment artefacts + Stage 4 tested artefact checksums

**Output:** Deployment integrity verification record (artifacts/outputs/deployment-integrity-record.yaml)


### Step 5.6 — Deploy & Handover

**Control:** none (procedural) · **Delegation:** Agent executes pipeline, OPS confirms

Deployment execution and Stage 6 handover

| Actor | Action |
|-------|--------|
| `AGT` | Execute deployment via approved pipeline |
| `OPS` | Execute smoke tests against production |
| `OPS` | Confirm service health and enter hypercare window |
| `OPS` | Activate Stage 6 monitoring profile |
| `OPS` | Confirm Stage 6 handover; record handover timestamp |

**Input:** Verified deployment artefacts (Step 5.5 output)

**Output:** Handover confirmation recorded in deployment integrity record


## Exit Criteria

- QC-09: Release readiness checklist completed — all prior controls evidenced
- RC-06: CAB approval granted by appropriate authority
- RC-07: Rollback plan validated and tested in pre-production
- SC-16: Infrastructure security baseline validated — no unresolved deviations
- SC-17: Deployment integrity verified — artefact checksums match tested build
- SC-18: All secrets/keys validated for proper vaulting, rotation, and access control


## Output Artifacts

- `artifacts/outputs/QC-09-release-readiness-checklist.yaml`
- `artifacts/outputs/RC-06-change-approval-record.yaml`
- `artifacts/outputs/RC-07-rollback-plan.yaml`
- `artifacts/outputs/SC-16-infrastructure-security-report.yaml`
- `artifacts/outputs/SC-17-deployment-integrity-record.yaml`
- `artifacts/outputs/SC-18-secrets-management-report.yaml`


## References

- Stage definition: 
- Controls: See `required_controls` in stage YAML.

---

**Last Updated:** 2026-03-13 14:19 UTC
