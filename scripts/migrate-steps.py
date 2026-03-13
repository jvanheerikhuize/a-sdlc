#!/usr/bin/env python3
"""
migrate-steps.py — Restructures A-SDLC stage definitions.

Extracts workflow.nodes from stage YAMLs into individual step files
in stages/NN-name/steps/, creates slim stage.yaml files (without
workflow block), and updates asdlc.yaml stage_file references.

Usage:
    python3 scripts/migrate-steps.py [--dry-run]
"""

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
STAGES_DIR = ROOT / "stages"
DRY_RUN = "--dry-run" in sys.argv

WRITTEN = []
SKIPPED = []


def write_file(path, content):
    if DRY_RUN:
        SKIPPED.append(str(path.relative_to(ROOT)))
        print(f"  [dry-run] {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    WRITTEN.append(str(path.relative_to(ROOT)))
    print(f"  ✓  {path.relative_to(ROOT)}")


def step_filename(step_id):
    """'1.5b' → 'step-1-5b.yaml',  '3.2-sc3c' → 'step-3-2-sc3c.yaml'"""
    return "step-" + str(step_id).replace(".", "-") + ".yaml"


def split_artifacts(text):
    """Split ' · ' separated descriptions into a list."""
    if not text:
        return []
    return [x.strip() for x in str(text).split(" · ") if x.strip()]


class OrderedDumper(yaml.Dumper):
    """YAML dumper that preserves key order and formats strings cleanly."""
    pass


def _str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


OrderedDumper.add_representer(str, _str_representer)


def dump(data):
    return yaml.dump(
        data,
        Dumper=OrderedDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2,
        width=120,
    )


def process_stage(stage_dir):
    # Find source YAML (not stage.yaml)
    candidates = sorted(
        f for f in stage_dir.iterdir()
        if f.suffix == ".yaml" and f.name != "stage.yaml"
    )
    if not candidates:
        print(f"  skip {stage_dir.name}: no source YAML")
        return

    source = candidates[0]
    print(f"\n{'─'*60}")
    print(f"  Stage dir : {stage_dir.name}")
    print(f"  Source    : {source.name}")
    print(f"{'─'*60}")

    data = yaml.safe_load(source.read_text())
    nodes = data.get("workflow", {}).get("nodes", [])
    if not nodes:
        print("  No workflow.nodes — skipping step extraction")
        return

    # Build node_id → step_number map for depends_on translation
    id_map = {n["id"]: str(n["step_number"]) for n in nodes}

    steps_dir = stage_dir / "steps"

    # ── Write individual step files ──────────────────────────────────────────
    for node in nodes:
        step_id = str(node["step_number"])
        depends_on = [id_map.get(d, d) for d in node.get("depends_on", [])]

        step = {
            "id": step_id,
            "title": node.get("title"),
            "stage": data["number"],
            "control": node.get("control"),
            "description": node.get("description"),
            "delegation": node.get("delegation"),
            "depends_on": depends_on,
        }

        if node.get("condition") is not None:
            step["condition"] = node["condition"]
        if "frequency" in node:
            step["frequency"] = node["frequency"]

        step["actors"] = node.get("actors", [])
        step["inputs"] = split_artifacts(node.get("input") or "")
        step["outputs"] = split_artifacts(node.get("output") or "")

        for opt in ["on_failure", "on_uncertainty", "on_changes_requested", "note", "tables"]:
            if node.get(opt) is not None:
                step[opt] = node[opt]

        fname = step_filename(step_id)
        header = (
            f"# Step {step_id}: {node.get('title', '')}\n"
            f"# Stage {data['number']} — {data['name']}\n"
            f"# Control: {node.get('control') or 'none'}\n\n"
        )
        write_file(steps_dir / fname, header + dump(step))

    # ── Build slim parallelism (node IDs → step IDs) ─────────────────────────
    wf_par = data.get("workflow", {}).get("parallelism", {})
    if wf_par:
        parallelism = {
            "max_concurrent": wf_par.get("max_concurrent"),
            "groups": [
                [id_map.get(n, n) for n in grp]
                for grp in wf_par.get("groups", [])
            ],
        }
    else:
        parallelism = None

    # ── Build escalation_paths (Stage 6 only, node IDs → step IDs) ───────────
    wf_esc = data.get("workflow", {}).get("escalation_paths", [])
    escalation_paths = []
    for ep in wf_esc:
        escalation_paths.append({
            "source_step": id_map.get(ep.get("source_control"), ep.get("source_control")),
            "condition": ep.get("condition"),
            "target_path": ep.get("target_path"),
        })

    # ── Write slim stage.yaml ─────────────────────────────────────────────────
    stage_slim = {
        "number": data["number"],
        "name": data["name"],
        "description": data["description"],
        "roles": data.get("roles", []),
        "steps_dir": "steps/",
        "steps": [str(n["step_number"]) for n in nodes],
    }
    if parallelism:
        stage_slim["parallelism"] = parallelism
    if escalation_paths:
        stage_slim["escalation_paths"] = escalation_paths

    stage_slim["required_controls"] = data.get("required_controls", [])
    stage_slim["exit_criteria"] = data.get("exit_criteria", [])
    stage_slim["next_stage"] = data.get("next_stage")
    stage_slim["artifacts"] = data.get("artifacts", {})

    if "directives" in data:
        stage_slim["directives"] = data["directives"]
    if "feedback_loop_summary" in data:
        stage_slim["feedback_loop_summary"] = data["feedback_loop_summary"]

    stage_header = (
        "# ============================================================\n"
        f"# Stage {data['number']}: {data['name']}\n"
        f"# Steps: stages/{stage_dir.name}/steps/\n"
        "# Controls: controls/[track]/[ID].yaml\n"
        "# ============================================================\n\n"
    )
    write_file(stage_dir / "stage.yaml", stage_header + dump(stage_slim))


def update_asdlc_yaml():
    """Update asdlc.yaml: fix stage_file paths, remove stages[].controls."""
    asdlc_path = ROOT / "asdlc.yaml"
    data = yaml.safe_load(asdlc_path.read_text())

    changed = False
    for stage in data.get("stages", []):
        slug = stage.get("slug", "")
        new_sf = f"stages/{slug}/stage.yaml"
        if stage.get("stage_file") != new_sf:
            stage["stage_file"] = new_sf
            changed = True
        if "controls" in stage:
            del stage["controls"]
            changed = True
        # Remove artifacts_dir (redundant - artifacts are inside stage dir)
        # Keep it for now for backward compatibility

    if not changed:
        print("\n  asdlc.yaml — already up to date, no changes needed")
        return

    header = (
        "# ============================================================\n"
        "# A-SDLC Framework Manifest\n"
        "# ============================================================\n"
        "# Lightweight index of stages, controls, and supporting files.\n"
        "# Stages:   stages/NN-name/stage.yaml\n"
        "# Steps:    stages/NN-name/steps/step-N-N.yaml\n"
        "# Controls: controls/[track]/[ID].yaml\n"
        "# Registry: controls/registry.yaml\n"
        "# Schema:   schema/framework.schema.json\n"
        "# ============================================================\n\n"
    )
    write_file(asdlc_path, header + dump(data))


def main():
    print("=" * 60)
    print("  A-SDLC Step Migration")
    print(f"  Mode: {'DRY-RUN' if DRY_RUN else 'WRITE'}")
    print("=" * 60)

    for stage_name in sorted(d.name for d in STAGES_DIR.iterdir() if d.is_dir()):
        if stage_name[0].isdigit():
            process_stage(STAGES_DIR / stage_name)

    print()
    update_asdlc_yaml()

    print()
    print("=" * 60)
    if DRY_RUN:
        print(f"  Would write {len(SKIPPED)} files. Re-run without --dry-run.")
    else:
        print(f"  ✓ Wrote {len(WRITTEN)} files.")
        print()
        print("  Next steps:")
        print("  1. Delete old stage YAML files (stages/*/0*.yaml)")
        print("  2. Run: bash scripts/validate.sh")
        print("  3. Run: bash scripts/generate-docs.sh")
    print("=" * 60)


if __name__ == "__main__":
    main()
