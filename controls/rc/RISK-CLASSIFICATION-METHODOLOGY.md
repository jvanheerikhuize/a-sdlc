# Risk Classification Methodology

The risk classification methodology is applied by control [RC-1A](RC-1A.yaml) during Stage 1 (Intent Ingestion). It assesses the non-functional risk exposure of a proposed change before any design or coding begins. The resulting tier determines governance intensity for all subsequent stages.

---

## Tiers and Governance Intensity

| Tier | Governance Intensity | Meaning |
| ---- | -------------------- | ------- |
| `low` | Standard | Routine change; standard controls apply |
| `medium` | Enhanced | Elevated oversight at key stage gates |
| `high` | Full | Heightened scrutiny; dedicated review sessions required |
| `critical` | Full + escalated authority | Worst-case exposure; VP/CISO-level sign-off required for RC-2A in Stage 2 |

---

## Assessment Dimensions

The tier is assessed across **six independent dimensions**. Each dimension is rated separately. The final risk tier is the **highest rating across all dimensions** (worst-case wins).

The Risk Officer may apply documented discretion to lower a proposed tier if there is strong contextual justification — but must record the rationale explicitly.

### 1. Availability Impact

Does this change affect service availability?

| Rating | Criteria |
| ------ | -------- |
| `low` | No impact on serving components; applies to non-production or auxiliary systems only |
| `medium` | Potential degraded performance (e.g. p99 latency increase); no outage expected |
| `high` | Partial service disruption possible; service may degrade but remain operational |
| `critical` | Full or near-full service outage possible during or after the change |

### 2. Data Scope

What data does this change create, read, modify, or delete?

| Rating | Criteria |
| ------ | -------- |
| `low` | Public or non-sensitive internal data only; no regulatory classification |
| `medium` | Internal operational data; not subject to regulatory data classification |
| `high` | Personal data (PII, health, biometric), payment data (PCI-DSS), or DORA-regulated operational data |
| `critical` | Core financial transaction data, supervisory reporting data, or data subject to cross-border regulatory requirements |

### 3. System Criticality

Which systems are affected by this change?

| Rating | Criteria |
| ------ | -------- |
| `low` | Non-critical auxiliary or development system; not used in production flows |
| `medium` | Supporting production system; not on the critical path for core operations |
| `high` | Business-critical system that supports key operational processes |
| `critical` | Core infrastructure, payment processing, regulatory reporting systems, or systems with cross-organisational dependencies |

### 4. User Impact Scope

Who and how many users are affected if this change causes an incident?

| Rating | Criteria |
| ------ | -------- |
| `low` | Internal users only; fewer than 50 affected |
| `medium` | Internal users; 50–500 affected |
| `high` | External users affected, or more than 500 internal users |
| `critical` | All external customers affected, or regulatory/compliance exposure triggered |

### 5. Reversibility

How quickly and safely can this change be undone if problems are detected?

| Rating | Criteria |
| ------ | -------- |
| `low` | Instant automated rollback available (e.g. feature flag toggle, blue/green switch) |
| `medium` | Rollback possible within hours; requires manual steps or coordination |
| `high` | Rollback requires days or complex cross-team coordination |
| `critical` | Change is difficult or impossible to reverse (e.g. data migrations, external integrations, published contracts) |

### 6. Change Blast Radius

How many systems, teams, or third parties are affected by this change?

| Rating | Criteria |
| ------ | -------- |
| `low` | Single isolated component; single team owns everything in scope |
| `medium` | Multiple components within one domain; single team or closely related teams |
| `high` | Cross-domain or cross-team; requires coordination between multiple squads or business units |
| `critical` | Organisation-wide impact, or involves third-party ICT service providers subject to DORA Art. 28 oversight |

---

## Governance Intensity: What Changes at Each Tier

| Control / Stage | Standard (`low`) | Enhanced (`medium`) | Full (`high` / `critical`) |
| --------------- | ---------------- | ------------------- | -------------------------- |
| RC-2A Design Approval | Tech Lead | Architecture Board | CTO / VP Engineering |
| RC-5A CAB Approval | Standard CAB | Priority CAB | Emergency CAB + CISO |
| QC-4A Testing | Standard test suite | Extended regression | Full regression + performance |
| SC-4A / SC-4B | Automated scan | Scan + manual review | Scan + manual review + penetration test |
| QC-4C Documentation | Standard docs | Enhanced runbook | Full operational playbook |

---

## Worked Examples

### Example A — UI cosmetic update
- Availability impact: `low` (no backend changes)
- Data scope: `low` (no data touched)
- System criticality: `low` (frontend only)
- User impact: `low` (internal users only)
- Reversibility: `low` (instant rollback via deployment)
- Blast radius: `low` (single component, single team)
- **risk tier: `low` — Standard governance**

### Example B — New payment processing endpoint
- Availability impact: `high` (new endpoint on critical path)
- Data scope: `critical` (payment data, PCI-DSS scope)
- System criticality: `critical` (core payment system)
- User impact: `critical` (all external customers)
- Reversibility: `medium` (can disable endpoint)
- Blast radius: `high` (payment, risk, compliance teams)
- **risk tier: `critical` — Full governance + escalated authority**

### Example C — New internal reporting dashboard
- Availability impact: `low` (read-only, separate system)
- Data scope: `medium` (internal operational data)
- System criticality: `medium` (supporting system)
- User impact: `low` (internal finance team, <50 users)
- Reversibility: `low` (can be disabled instantly)
- Blast radius: `medium` (data platform + finance teams)
- **risk tier: `medium` — Enhanced governance**

---

## Regulatory Basis

| Framework | Requirement |
| --------- | ----------- |
| DORA Art. 8(1) | Proportionate ICT risk management must be applied to all changes |
| DORA Art. 8(4) | Risk classification must consider availability, integrity, and continuity |
| DNB | Risk-based approach to change governance; tier determines approval authority |
| EU AI Act Art. 9(2) | Risk management must be applied proportionately throughout the AI system lifecycle |
