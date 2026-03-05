#!/usr/bin/env python3
"""
A-SDLC Documentation Generator

Generates README.md files from YAML sources using Jinja2 templates.
Ensures YAML is the single source of truth and documentation is always in sync.

Usage:
  python3 scripts/generate-docs.py              # Generate all docs
  python3 scripts/generate-docs.py stage-1      # Generate Stage 1 docs only
  python3 scripts/generate-docs.py --list       # List generation targets
"""

import os
import sys
import yaml
import json
from pathlib import Path
from datetime import datetime

try:
    from jinja2 import Environment, FileSystemLoader, TemplateNotFound
except ImportError:
    print("ERROR: Jinja2 not installed. Install with: pip install jinja2")
    sys.exit(1)


class DocGenerator:
    def __init__(self, repo_root=None):
        """Initialize the documentation generator."""
        self.repo_root = Path(repo_root or os.getcwd())
        self.manifest_file = self.repo_root / "manifest" / "catalog.yaml"
        self.templates_dir = self.repo_root / "docs-templates"

        # Load manifest
        with open(self.manifest_file) as f:
            self.manifest = yaml.safe_load(f)

        # Load framework (single source of truth for shared context)
        # Note: asdlc.yaml has a root 'framework:' key, extract just the inner object
        loaded = self.load_yaml("asdlc.yaml") or {}
        self.framework = loaded.get("framework", {})

        # Setup Jinja2
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def load_yaml(self, file_path):
        """Load a YAML file relative to repo root."""
        full_path = self.repo_root / file_path
        if not full_path.exists():
            print(f"WARNING: File not found: {file_path}")
            return None
        with open(full_path) as f:
            return yaml.safe_load(f)

    def generate_stage_readme(self, stage_file):
        """Generate README.md for a stage."""
        stage_yaml = self.load_yaml(stage_file)
        if not stage_yaml:
            return False

        # Load control registry for lookup
        registry = self.load_yaml("controls/registry.yaml")
        registry_controls = registry.get("registry", []) if registry else []

        # Load control definitions for this stage
        required_controls = []
        for control in stage_yaml.get("required_controls", []):
            control_id = control.get("id")
            # Find control in registry
            for reg_control in registry_controls:
                if reg_control.get("id") == control_id:
                    control_file = reg_control.get("file")
                    control_data = self.load_yaml(control_file) if control_file else None
                    required_controls.append({
                        "id": control_id,
                        "name": reg_control.get("name"),
                        "track": reg_control.get("track"),
                        "delegation": control_data.get("delegation") if control_data else {},
                        "note": control.get("note"),
                        "file": control_file
                    })
                    break

        # Prepare template context
        context = {
            "framework": self.framework,
            "stage": stage_yaml,
            "stage_file": stage_file,
            "required_controls": required_controls,
            "workflow_diagram": self._generate_workflow_diagram(stage_yaml),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("stage-readme.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: stage-readme.jinja2")
            return False

        # Write output (stage_file is like "stages/01-intent-ingestion/01-intent-ingestion.yaml")
        stage_dir = Path(stage_file).parent
        output_file = self.repo_root / stage_dir / "README.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def generate_controls_index(self):
        """Generate controls/README.md from registry."""
        registry = self.load_yaml("controls/registry.yaml")
        if not registry:
            return False

        controls = registry.get("registry", [])

        # Group by track
        controls_by_track = {}
        for track_code in ["QC", "RC", "SC", "AC", "GC"]:
            controls_by_track[track_code] = [c for c in controls if c.get("track") == track_code]

        # Prepare context
        context = {
            "framework": self.framework,
            "total_controls": len(controls),
            "tracks": self.manifest.get("tracks", []),
            "controls_by_track": controls_by_track,
            "all_controls_sorted": sorted(controls, key=lambda c: c.get("id", "")),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("controls-index.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: controls-index.jinja2")
            return False

        # Write output
        output_file = self.repo_root / "controls" / "README.md"
        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def generate_stages_overview(self, source_file):
        """Generate stages/README.md from asdlc.yaml + per-stage YAMLs."""
        loaded = self.load_yaml(source_file) or {}
        fw = loaded.get("framework", {})

        # Load each stage YAML for full detail (stages are at root level, not in framework)
        stages_data = []
        for entry in loaded.get("stages", []):
            stage_yaml = self.load_yaml(entry["stage_file"])
            stages_data.append({
                "entry": entry,
                "yaml": stage_yaml or {}
            })

        # Load feedback loops for summary
        feedback = self.load_yaml("feedbackloops/feedback-loops.yaml") or {}

        # Prepare context: merge framework, roles, and cross_cutting for template
        context = {
            "framework": fw,
            "roles": loaded.get("roles", {}),
            "cross_cutting": loaded.get("cross_cutting", {}),
            "stages_data": stages_data,
            "feedback_loops": feedback.get("feedback_loops", []),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("stages-overview.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: stages-overview.jinja2")
            return False

        # Write output
        output_file = self.repo_root / "stages" / "README.md"
        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def generate_framework_overview(self, source_file):
        """Generate root README.md from asdlc.yaml + controls registry."""
        loaded = self.load_yaml(source_file) or {}
        fw = loaded.get("framework", {})
        stages = loaded.get("stages", [])

        # Load control registry for "All Controls at a Glance" matrix
        registry = self.load_yaml("controls/registry.yaml") or {}
        controls = registry.get("registry", [])

        # Build control matrix: {stage_number: {track: [control_objects]}}
        # stage 0 = cross-cutting
        control_matrix = {}
        for ctrl in controls:
            stage_num = ctrl.get("stage", 0)
            track = ctrl.get("track", "")
            if stage_num not in control_matrix:
                control_matrix[stage_num] = {}
            if track not in control_matrix[stage_num]:
                control_matrix[stage_num][track] = []
            control_matrix[stage_num][track].append({
                "id": ctrl.get("id"),
                "file": ctrl.get("file"),
            })

        # Count totals per track
        track_counts = {}
        for ctrl in controls:
            t = ctrl.get("track", "")
            track_counts[t] = track_counts.get(t, 0) + 1

        # Pre-render control matrix rows as formatted strings to avoid Jinja2 whitespace issues
        matrix_rows = ["| Stage | QC | RC | SC | AC | GC |",
                       "| ----- | -- | -- | -- | -- | -- |"]

        for stage_num in range(0, 7):
            cells = []

            # Stage label
            if stage_num == 0:
                cells.append("Cross-cutting")
            else:
                stage = stages[stage_num - 1]
                cells.append(f"[{stage_num} {stage['name']}](stages/{stage['slug']}/README.md)")

            # Controls per track
            for track in ["QC", "RC", "SC", "AC", "GC"]:
                if stage_num in control_matrix and track in control_matrix[stage_num]:
                    ctrls = control_matrix[stage_num][track]
                    ctrl_links = [f"[{c['id']}](controls/{track.lower()}/{c['id']}.yaml)" for c in ctrls]
                    cells.append(", ".join(ctrl_links))
                else:
                    cells.append("—")

            matrix_rows.append("| " + " | ".join(cells) + " |")

        # Prepare context
        context = {
            "framework": fw,
            "stages": stages,
            "controls": controls,
            "control_matrix_rows": "\n".join(matrix_rows),
            "track_counts": track_counts,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("framework-overview.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: framework-overview.jinja2")
            return False

        # Write output
        output_file = self.repo_root / "README.md"
        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def generate_agents_md(self, source_file):
        """Generate AGENTS.md from asdlc.yaml + registry + feedback loops."""
        loaded = self.load_yaml(source_file) or {}
        fw = loaded.get("framework", {})
        stages = loaded.get("stages", [])
        cross_cutting = loaded.get("cross_cutting", {})

        # Control registry for file path lookup
        registry = self.load_yaml("controls/registry.yaml") or {}
        all_controls = registry.get("registry", [])
        ctrl_by_id = {c.get("id"): c for c in all_controls}

        # Build cc_controls_with_paths for "Always Load" block
        cc_controls_with_paths = []
        for ctrl in cross_cutting.get("controls", []):
            ctrl_id = ctrl.get("id")
            reg_entry = ctrl_by_id.get(ctrl_id, {})
            cc_controls_with_paths.append({
                "id": ctrl_id,
                "name": ctrl.get("name"),
                "file": reg_entry.get("file", ""),
            })

        # Pre-render "Always Load" code block
        always_load_lines = []
        for ctrl in cc_controls_with_paths:
            always_load_lines.append(f"{ctrl['file']}      # {ctrl['name']}")
        fl_def = cross_cutting.get("feedback_loops", {}).get("definition", "")
        always_load_lines.append(f"{fl_def}  # Re-entry paths for incidents and changes")

        # Pre-render Stage-Specific Files table
        table_rows = [
            "| Stage | Stage definition | Controls |",
            "| --- | --- | --- |",
        ]
        for stage in stages:
            num = stage["number"]
            name = stage["name"]
            sf = stage["stage_file"]
            ctrl_list = ", ".join(c["id"] for c in stage.get("controls", []))
            table_rows.append(f"| {num} — {name} | `{sf}` | {ctrl_list} |")

        # Load feedback loops
        feedback = self.load_yaml("feedbackloops/feedback-loops.yaml") or {}

        context = {
            "framework": fw,
            "stages": stages,
            "cross_cutting": cross_cutting,
            "always_load_block": "\n".join(always_load_lines),
            "stage_files_table": "\n".join(table_rows),
            "feedback_loops": feedback.get("feedback_loops", []),
            "total_controls": len(all_controls),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("agents.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: agents.jinja2")
            return False

        # Write output
        output_file = self.repo_root / "AGENTS.md"
        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def generate_feedback_loops_guide(self, source_file):
        """Generate feedbackloops/README.md from feedback-loops.yaml."""
        loaded = self.load_yaml(source_file) or {}
        roles = loaded.get("roles", [])
        steps = loaded.get("steps", [])
        input_artifacts = loaded.get("input_artifacts", {})
        output_artifacts = loaded.get("output_artifacts", [])
        feedback_loops = loaded.get("feedback_loops", [])

        # Pre-render minimum controls table for Path A
        path_a = feedback_loops[0] if feedback_loops else {}
        path_a_min_ctrls = path_a.get("minimum_controls", [])
        path_a_table_rows = [
            "| Control | Stage | Rationale |",
            "| ------- | ----- | --------- |",
        ]
        for ctrl in path_a_min_ctrls:
            ctrl_id = ctrl.get("id", "")
            # Parse stage from control ID (QC-3A → 3, SC-4A → 4, SC-5B → 5, etc.)
            # Format: [TRACK]-[STAGE][LETTER], e.g., QC-3A, SC-4A, SC-5B
            stage = "?"
            if "-" in ctrl_id:
                parts = ctrl_id.split("-")
                if len(parts) > 1 and len(parts[1]) > 0:
                    stage = parts[1][0]  # Get first char after dash (the stage digit)
            rationale = ctrl.get("rationale", "")
            path_a_table_rows.append(f"| {ctrl_id} | {stage} | {rationale} |")

        # Pre-render actor/action tables for each step
        def render_actions_table(actions):
            rows = ["| Actor | Action |", "| ----- | ------ |"]
            for action_item in actions:
                actor = action_item.get("actor", "")
                action = action_item.get("action", "")
                rows.append(f"| {actor} | {action} |")
            return "\n".join(rows)

        fl1_actions = render_actions_table(steps[0].get("actions", [])) if steps else ""
        fl2a_actions = render_actions_table(steps[1].get("actions", [])) if len(steps) > 1 else ""
        fl2b_actions = render_actions_table(steps[2].get("actions", [])) if len(steps) > 2 else ""
        fl3_actions = render_actions_table(steps[3].get("actions", [])) if len(steps) > 3 else ""

        # Prepare context
        context = {
            "roles": roles,
            "steps": steps,
            "feedback_loops": feedback_loops,
            "input_artifacts": input_artifacts,
            "output_artifacts": output_artifacts,
            "path_a": path_a,
            "path_a_minimum_controls_table": "\n".join(path_a_table_rows),
            "fl1_actions_table": fl1_actions,
            "fl2a_actions_table": fl2a_actions,
            "fl2b_actions_table": fl2b_actions,
            "fl3_actions_table": fl3_actions,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("feedback-loops-guide.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: feedback-loops-guide.jinja2")
            return False

        # Write output
        output_file = self.repo_root / "feedbackloops" / "README.md"
        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def generate_stage_context_bundles(self, source_file):
        """Generate context/stage-NN-name.md bundles from stage YAML."""
        stage_yaml = self.load_yaml(source_file) or {}
        if not stage_yaml:
            return False

        # Load control registry for lookup
        registry = self.load_yaml("controls/registry.yaml")
        registry_controls = registry.get("registry", []) if registry else []

        stage_num = stage_yaml.get("number")
        stage_name = stage_yaml.get("name", "")

        # Compute quick load paths
        stage_slug = stage_name.lower().replace(" & ", "-and-").replace(" ", "-").replace("&", "and")
        directive_file = f"directives/stages/{stage_num:02d}-{stage_slug}.yaml"
        quick_load_files = [source_file, directive_file]

        # Pre-render workflow table
        workflow = stage_yaml.get("workflow", {})
        nodes = workflow.get("nodes", [])
        workflow_rows = ["| Step | Title | Control | Actors | Delegation | Depends On |", "| ---- | ----- | ------- | ------ | ---------- | ---------- |"]
        for node in nodes:
            step = node.get("step_number", "?")
            title = node.get("title", "")
            control = node.get("control", "—")
            actors = ", ".join(a.get("role", "?") for a in node.get("actors", []))
            delegation = node.get("delegation", "—")
            depends_on = ", ".join(node.get("depends_on", [])) if node.get("depends_on") else "—"
            workflow_rows.append(f"| {step} | {title} | {control} | {actors} | {delegation} | {depends_on} |")
        workflow_table = "\n".join(workflow_rows)

        # Pre-render controls table
        required_controls = stage_yaml.get("required_controls", [])
        controls_rows = ["| ID | Name | Delegation | Agent Does | Human Does |", "| -- | ---- | ---------- | ---------- | ---------- |"]
        for ctrl_spec in required_controls:
            control_id = ctrl_spec.get("id")
            # Find control in registry
            reg_entry = None
            for reg in registry_controls:
                if reg.get("id") == control_id:
                    reg_entry = reg
                    break

            if reg_entry:
                ctrl_file = reg_entry.get("file")
                ctrl_data = self.load_yaml(ctrl_file) if ctrl_file else {}
                ctrl_name = reg_entry.get("name", control_id)
                delegation_pat = reg_entry.get("delegation", "—")
                delegation_desc = ctrl_data.get("delegation", {}).get("human_display", delegation_pat) if ctrl_data else delegation_pat

                # Extract agent and human actions from the delegation block
                delegation_block = ctrl_data.get("delegation", {}) if ctrl_data else {}
                agent_action = delegation_block.get("agent_role", "—") if isinstance(delegation_block, dict) else "—"
                human_action = delegation_block.get("human_role", "—") if isinstance(delegation_block, dict) else "—"

                controls_rows.append(f"| {control_id} | {ctrl_name} | {delegation_pat} | {agent_action} | {human_action} |")

        controls_table = "\n".join(controls_rows)

        # Pre-render exit criteria as checklist
        exit_criteria = stage_yaml.get("exit_criteria", [])
        exit_checklist_lines = []
        for criterion in exit_criteria:
            exit_checklist_lines.append(f"- [ ] {criterion}")
        exit_criteria_checklist = "\n".join(exit_checklist_lines) if exit_checklist_lines else "No exit criteria defined"

        # Pre-render input artifacts
        input_artifacts_list = stage_yaml.get("artifacts", {}).get("inputs", [])
        input_artifacts_lines = []
        for artifact in input_artifacts_list:
            input_artifacts_lines.append(f"- {artifact}")
        input_artifacts = "\n".join(input_artifacts_lines) if input_artifacts_lines else "None"

        # Pre-render output artifacts
        output_artifacts_list = stage_yaml.get("artifacts", {}).get("outputs", [])
        output_artifacts_lines = []
        for artifact in output_artifacts_list:
            output_artifacts_lines.append(f"- {artifact}")
        output_artifacts = "\n".join(output_artifacts_lines) if output_artifacts_list else "None"

        # Pre-render feedback loop triggers
        feedback_triggers_lines = []
        for ctrl_spec in required_controls:
            control_id = ctrl_spec.get("id")
            # Check registry for feedback_loops field
            for reg in registry_controls:
                if reg.get("id") == control_id:
                    triggers = reg.get("feedback_loops", [])
                    if triggers:
                        triggers_str = " or ".join(f"Path {t}" if t in ["a", "b"] else t for t in triggers)
                        feedback_triggers_lines.append(f"- {control_id} → {triggers_str}")
                    break

        feedback_triggers = "\n".join(feedback_triggers_lines) if feedback_triggers_lines else "None"

        # Prepare template context
        context = {
            "stage": stage_yaml,
            "stage_file": source_file,
            "quick_load_files": "\n".join(f"- {f}" for f in quick_load_files),
            "workflow_table": workflow_table,
            "controls_table": controls_table,
            "exit_criteria_checklist": exit_criteria_checklist,
            "input_artifacts": input_artifacts,
            "output_artifacts": output_artifacts,
            "feedback_triggers": feedback_triggers,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("stage-context-bundle.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: stage-context-bundle.jinja2")
            return False

        # Determine output file path
        output_file = self.repo_root / "context" / f"stage-{stage_num:02d}-{stage_slug}.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def _generate_workflow_diagram(self, stage_yaml):
        """Convert workflow DAG to markdown diagram."""
        workflow = stage_yaml.get("workflow", {})
        if not workflow.get("nodes"):
            return "(No workflow DAG defined)"

        nodes = workflow.get("nodes", [])
        lines = ["```mermaid", "graph LR"]

        # Add nodes
        for node in nodes:
            node_id = node.get("id")
            control = node.get("control", "handover")
            desc = node.get("description", "").split("\n")[0][:40]
            lines.append(f'  {node_id}["{control}: {desc}"]')

        # Add edges
        for node in nodes:
            node_id = node.get("id")
            for dep in node.get("depends_on", []):
                lines.append(f"  {dep} --> {node_id}")

        lines.append("```")
        return "\n".join(lines)

    def generate_regulatory_index(self):
        """Generate regulatory/README.md from compliance-matrix.yaml and sources.yaml."""
        matrix = self.load_yaml("regulatory/compliance-matrix.yaml") or {}
        sources = self.load_yaml("regulatory/sources.yaml") or {}

        if not matrix or not sources:
            return False

        compliance = matrix.get("compliance_matrix", {})
        coverage_summary = matrix.get("coverage_summary", {})
        regulatory_areas = matrix.get("regulatory_areas", [])

        # Pre-render coverage by track table
        track_coverage = coverage_summary.get("coverage_by_track", {})
        track_rows = [
            "| Track | Total | DORA Mapped | DORA % | EU AI Act Mapped | EU AI Act % |",
            "|-------|-------|---|---|---|---|",
        ]
        for track_code in ["QC", "RC", "SC", "AC", "GC"]:
            track_info = track_coverage.get(track_code, {})
            total = track_info.get("total", 0)
            dora_mapped = track_info.get("dora_mapped", 0)
            dora_pct = track_info.get("percentage", "0%")
            eu_ai_mapped = track_info.get("eu_ai_act_mapped", 0)
            eu_ai_pct = track_info.get("percentage", "0%")
            track_rows.append(f"| {track_code} | {total} | {dora_mapped} | {dora_pct} | {eu_ai_mapped} | {eu_ai_pct} |")
        coverage_by_track_table = "\n".join(track_rows)

        # Pre-render regulatory areas table
        areas_rows = [
            "| Area | DORA Articles | EU AI Act | A-SDLC Controls | Status |",
            "|------|---|---|---|---|",
        ]
        for area in regulatory_areas:
            area_name = area.get("area", "—")
            dora_arts = ", ".join(area.get("dora_articles", []))[:40]
            eu_arts = ", ".join(area.get("eu_ai_act_articles", []))[:40]
            ctrls = ", ".join([c.split(" ")[0] for c in area.get("controls", [])])[:40]
            status = area.get("status", "—")
            areas_rows.append(f"| {area_name} | {dora_arts} | {eu_arts} | {ctrls} | {status} |")
        regulatory_areas_table = "\n".join(areas_rows)

        # Pre-render DORA article mappings
        dora_articles = compliance.get("dora", {}).get("articles", [])
        dora_rows = [
            "| Article | Title | A-SDLC Controls | Coverage & Rationale |",
            "|---------|-------|---|---|",
        ]
        for article in dora_articles:
            article_id = article.get("article", "—")
            title = article.get("title", "")
            controls = ", ".join(article.get("controls", []))
            coverage = article.get("coverage", "—")
            dora_rows.append(f"| {article_id} | {title} | {controls} | {coverage} |")
        dora_article_table = "\n".join(dora_rows)

        # Pre-render EU AI Act article/annex mappings
        eu_articles = compliance.get("eu_ai_act", {}).get("articles", [])
        eu_annexes = compliance.get("eu_ai_act", {}).get("annexes", [])
        eu_all = eu_articles + eu_annexes
        eu_rows = [
            "| Article / Annex | Title | A-SDLC Controls | Coverage & Rationale |",
            "|---|---|---|---|",
        ]
        for item in eu_all:
            article_id = item.get("article") or item.get("annex") or "—"
            title = item.get("title", "")
            controls = ", ".join(item.get("controls", []))
            coverage = item.get("coverage", "—")
            eu_rows.append(f"| {article_id} | {title} | {controls} | {coverage} |")
        eu_article_table = "\n".join(eu_rows)

        # Prepare template context
        context = {
            "coverage_by_track_rows": coverage_by_track_table,
            "regulatory_areas_rows": regulatory_areas_table,
            "dora_article_rows": dora_article_table,
            "eu_ai_act_rows": eu_article_table,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        }

        # Render template
        try:
            template = self.jinja_env.get_template("regulatory-index.jinja2")
            content = template.render(context)
        except TemplateNotFound:
            print(f"ERROR: Template not found: regulatory-index.jinja2")
            return False

        # Write output
        output_file = self.repo_root / "regulatory" / "README.md"
        with open(output_file, "w") as f:
            f.write(content)

        print(f"✓ Generated: {output_file}")
        return True

    def generate_all(self):
        """Generate all documentation targets."""
        targets = self.manifest.get("doc_generation", {}).get("targets", [])

        print(f"\n=== A-SDLC Documentation Generator ===\n")
        print(f"Generating {len(targets)} documentation targets...\n")

        count = 0
        for target in targets:
            source = target.get("source")
            output = target.get("output")
            template = target.get("template")

            if template == "stage-readme":
                if self.generate_stage_readme(source):
                    count += 1
            elif template == "controls-index":
                if self.generate_controls_index():
                    count += 1
            elif template == "stages-overview":
                if self.generate_stages_overview(source):
                    count += 1
            elif template == "framework-overview":
                if self.generate_framework_overview(source):
                    count += 1
            elif template == "agents":
                if self.generate_agents_md(source):
                    count += 1
            elif template == "feedback-loops-guide":
                if self.generate_feedback_loops_guide(source):
                    count += 1
            elif template == "stage-context-bundle":
                if self.generate_stage_context_bundles(source):
                    count += 1
            elif template == "regulatory-index":
                # TODO: compliance-matrix.yaml has YAML syntax errors (mixed scalars + list).
                # Temporarily skip until data is fixed.
                # if self.generate_regulatory_index():
                #     count += 1
                print(f"⏸ Skipped (data validation needed): {output} ({template})")
            else:
                print(f"⚠ Skipping (unsupported template): {output} ({template})")

        print(f"\n✓ Generated {count}/{len(targets)} documentation files\n")
        return count == len(targets)

    def list_targets(self):
        """List all generation targets."""
        targets = self.manifest.get("doc_generation", {}).get("targets", [])

        print(f"\nA-SDLC Documentation Generation Targets:\n")
        for i, target in enumerate(targets, 1):
            source = target.get("source")
            output = target.get("output")
            desc = target.get("description", "")
            template = target.get("template")

            print(f"{i:2}. [{template}]")
            print(f"    From:   {source}")
            print(f"    To:     {output}")
            print(f"    About:  {desc}\n")


def main():
    """Main entry point."""
    generator = DocGenerator()

    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == "--list":
            generator.list_targets()
        elif arg == "--help":
            print(__doc__)
        else:
            print(f"Unknown argument: {arg}")
            print(__doc__)
            sys.exit(1)
    else:
        success = generator.generate_all()
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
