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
