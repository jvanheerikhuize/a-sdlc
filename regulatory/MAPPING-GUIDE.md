# Regulatory Mapping Update Guide

**For AI Agents:** Use [MAPPING-RUNBOOK.yaml](MAPPING-RUNBOOK.yaml) — machine-executable workflows with deterministic steps, error handling, and validation rules.

**For Humans:** Use this guide for context and decision-making. The runbook provides the structured execution.

This guide provides a repeatable workflow for maintaining regulatory mappings as controls are added or articles are remapped.

## Quick Reference: Where Regulatory Data Lives

| File | Purpose | Audience |
| --- | --- | --- |
| `controls/[track]/[ID].yaml` | Control definitions with `regulatory_mapping` field | Control owners, developers |
| `compliance-matrix.yaml` | Consolidated control-to-article index (machine-readable) | Validation scripts, dashboards |
| `control-article-index.yaml` | Human-editable source of truth for all mappings | You (for updates) |
| `README.md` | Human-readable article-to-control tables (generated from index) | Auditors, compliance stakeholders |
| `sources.yaml` | Official article texts and obligation summaries | Validators, auditors |

---

## Workflow: Adding or Updating a Control Mapping

### Step 1: Edit the Control YAML

Update the control definition with the `regulatory_mapping` field. Example:

``` yaml
regulatory_mapping:
  - framework: DORA
    article: "9(2)"
    coverage: Strong
    rationale: "SC-07 enforces permission models and access control least-privilege principles."
  - framework: EU AI Act
    article: "15(4)"
    coverage: Strong
    rationale: "SC-07 enforces identity-based access control for AI system resources."
```

**Coverage values:** `Strong` | `Partial` | `Not Mapped`

### Step 2: Update `control-article-index.yaml`

Add or update the entry in this consolidated index:

``` yaml
controls:
  SC-07:
    name: "Permission & Access Control Enforcement"
    mappings:
      - framework: DORA
        article: "9(3)"
        coverage: Strong
        gap_reason: ~  # null = fully covered
      - framework: EU AI Act
        article: "15(4)"
        coverage: Strong
        gap_reason: ~
```

### Step 3: Update `compliance-matrix.yaml`
Add the control to the appropriate section(s):

``` yaml
DORA:
  "9(3)":
    controls:
      - SC-07
    coverage: Strong
```

### Step 4: Update `README.md`
Add or modify the article row in the appropriate chapter table:

```markdown
| **Art. 9(3)** | Least privilege and segregation of duties | SC-07 | **✅ Strong** — SC-07 enforces role-based access control (RBAC) with least-privilege principles and segregation of duties across all environments. |
```

**Format for Partial:** Include "**Not covered (org responsibility):**" section.

### Step 5: Validate and Commit

``` bash
# Run validation (when script is available)
python3 scripts/validate-regulatory.py

# Check consistency
git diff regulatory/

# Commit
git add controls/[track]/[ID].yaml regulatory/
git commit -m "Map [ID] to DORA Art. X and EU AI Act Art. Y"
```

---

## Workflow: Discovering a New Article Mapping

When you discover that an existing control also maps to an article:

1. **Add to control YAML** — Add new entry to `regulatory_mapping` array
2. **Add to control-article-index.yaml** — Add new mapping line
3. **Add to compliance-matrix.yaml** — Add control to article section
4. **Add to README.md** — Add/update article row with new coverage
5. **Update coverage stats** if this is a major new coverage area

---

## Workflow: Explaining Why a Control is "Partial"

For **Partial** mappings, the rationale MUST explain:

1. **What the control covers** — Specific aspect(s) the SDLC enforces
2. **What's NOT covered** — Gap statement explaining organizational responsibility
3. **Boundary statement** — Clear division: "A-SDLC does X; entity does Y"

Example template:
```
**✅ Partial** — [Control] [does what].
**Not covered (org responsibility):** [What entity must do operationally].
A-SDLC [provides X]; entity [handles Y].
```

### Real Example (Art. 16: Backup Policies)
```
**✅ Partial** — RC-07 validates backup/restore procedures work; QC-09 checks
backup integrity. **Not covered (org responsibility):** Backup frequency,
retention policies, and offline storage requirements. A-SDLC validates
procedures work; entity determines operational policy.
```

---

## Workflow: Adding a New Article to a Chapter

If a new article exists in DORA or EU AI Act:

1. **Add article row to README.md** in correct chapter table
2. **Assess coverage** — Does an existing control map? Is it Strong/Partial/Not Mapped?
3. **If no control exists:**
   - If SDLC-relevant → consider creating new control (use plan mode)
   - If org responsibility → mark as `ℹ️ Org-level execution`
   - If regulatory → mark as `ℹ️ Regulatory authority function`
4. **Add to control-article-index.yaml** if relevant
5. **Update coverage stats** in README.md Coverage Summary section

---

## Quick Checklist: Before Committing Regulatory Changes

- [ ] All modified controls have `regulatory_mapping` field
- [ ] `control-article-index.yaml` matches all control YAML mappings
- [ ] `compliance-matrix.yaml` lists all control-article pairs
- [ ] `README.md` article tables reflect all mappings
- [ ] All "Partial" mappings explain "Not covered (org responsibility)"
- [ ] Coverage summary stats updated if adding new mappings
- [ ] No orphaned articles (article mentioned but no control mapped)
- [ ] No duplicate mappings (same control-article pair listed twice)
- [ ] Ran validation script (when available)

---

## Finding Information Quickly

### "Which controls map to DORA Art. 25?"

→ Search `compliance-matrix.yaml` for `"25"` under DORA section

### "What does SC-10 cover?"

→ Read `controls/sc/SC-10.yaml` `regulatory_mapping` field
→ Or search `control-article-index.yaml` for SC-10 entry

### "Which articles don't have control mappings?"

→ Search `README.md` for `ℹ️ Org-level execution` or `ℹ️ Regulatory authority function`

### "Why is this marked Partial?"

→ Read the "Not covered (org responsibility)" paragraph in README.md

---

## Validation Checklist (Manual, until script is available)

1. **Consistency check:** Every control in `controls/[track]/` that has `regulatory_mapping` should appear in `compliance-matrix.yaml`
2. **Article coverage:** Every article listed in `README.md` should have at least one mapping or explicit rationale for no mapping
3. **Bidirectional consistency:** If `compliance-matrix.yaml` lists "SC-07 maps to Art. 9(3)", then `controls/sc/SC-07.yaml` should also list Art. 9(3)
4. **Statistics:** Coverage percentages in README.md Coverage Summary should match actual count of controls with ≥1 mapping

---

## When Adding a NEW Control

1. Create `controls/[track]/[ID].yaml` with full definition including `regulatory_mapping`
2. Add to `controls/registry.yaml`
3. Add to relevant stage YAML (`stages/NN/NN.yaml`)
4. Add to `asdlc.yaml` if cross-cutting
5. **Only then:** Update `control-article-index.yaml`, `compliance-matrix.yaml`, `README.md`
6. Update coverage stats
7. Validate

---

## Notes for Future Automation

When a validation script is written, it should check:

```python
# Pseudo-code
for control in controls_dir:
    for mapping in control.regulatory_mapping:
        # Check mapping exists in compliance_matrix
        assert mapping in compliance_matrix
        # Check mapping exists in README article tables
        assert mapping in readme_article_table
        # For Partial, check "Not covered" explanation exists
        if mapping.coverage == "Partial":
            assert "Not covered" in readme_rationale
```
