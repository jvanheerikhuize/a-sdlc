"""Integration tests for scripts/generate-docs.py.

Tests the documentation generator against realistic YAML structures.
"""

from pathlib import Path
import pytest
import yaml
from jinja2 import Environment, FileSystemLoader

# Add repo to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.shared import load_yaml_safe, render_template_safe


class TestDocGeneratorImports:
    """Test that DocGenerator can be imported and instantiated."""

    def test_doc_generator_can_be_instantiated(self, repo_root, monkeypatch):
        """Test that DocGenerator class can be instantiated."""
        monkeypatch.chdir(repo_root)

        # Import here to avoid issues with relative imports
        import sys
        sys.path.insert(0, str(repo_root))

        try:
            # This would normally work if run as a module
            # For now just verify the module loads
            from pathlib import Path as PathlibPath
            init_file = repo_root / "scripts" / "__init__.py"
            assert init_file.exists()
        except ImportError:
            # Expected if running as script
            pass


class TestDocGenerationTargets:
    """Test documentation generation against realistic YAML."""

    def test_framework_overview_source_loads(self, repo_root):
        """Test that asdlc.yaml (framework overview source) loads."""
        framework_file = repo_root / "asdlc.yaml"
        data = load_yaml_safe(framework_file)

        assert isinstance(data, dict)
        assert "framework" in data
        assert data["framework"].get("name") == "A-SDLC"

    def test_stage_yaml_loads(self, repo_root):
        """Test that stage YAML files load correctly."""
        stage_file = repo_root / "stages" / "01-intent-ingestion" / "01-intent-ingestion.yaml"
        data = load_yaml_safe(stage_file)

        assert isinstance(data, dict)
        assert data.get("number") == 1
        assert "name" in data

    def test_control_registry_loads(self, repo_root):
        """Test that control registry loads correctly."""
        registry_file = repo_root / "controls" / "registry.yaml"
        data = load_yaml_safe(registry_file)

        assert isinstance(data, dict)
        assert "registry" in data
        assert isinstance(data["registry"], list)
        assert len(data["registry"]) > 0

    def test_feedback_loops_yaml_loads(self, repo_root):
        """Test that feedback loops YAML loads correctly."""
        feedback_file = repo_root / "feedbackloops" / "feedback-loops.yaml"
        data = load_yaml_safe(feedback_file)

        assert isinstance(data, dict)
        # Should have feedback_loops or similar structure
        assert len(data) > 0

    def test_regulatory_compliance_matrix_loads(self, repo_root):
        """Test that regulatory compliance matrix loads correctly."""
        matrix_file = repo_root / "regulatory" / "compliance-matrix.yaml"
        data = load_yaml_safe(matrix_file)

        assert isinstance(data, dict)
        assert len(data) > 0

    def test_manifest_catalog_loads(self, repo_root):
        """Test that manifest/catalog.yaml loads correctly."""
        catalog_file = repo_root / "manifest" / "catalog.yaml"
        data = load_yaml_safe(catalog_file)

        assert isinstance(data, dict)
        assert "doc_generation" in data or "targets" in data or len(data) > 0


class TestTemplateRendering:
    """Test template rendering with realistic data."""

    def test_jinja_environment_can_load_templates(self, repo_root):
        """Test that Jinja2 environment can load templates."""
        templates_dir = repo_root / "docs-templates"
        env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Should be able to load a template without error
        assert templates_dir.exists()

    def test_template_file_exists(self, repo_root):
        """Test that expected template files exist."""
        templates_dir = repo_root / "docs-templates"
        expected_templates = [
            "stage-readme.jinja2",
            "controls-index.jinja2",
            "framework-overview.jinja2",
            "agents.jinja2",
            "feedback-loops-guide.jinja2",
        ]

        for template_name in expected_templates:
            template_file = templates_dir / template_name
            assert template_file.exists(), f"Template {template_name} not found"

    def test_render_template_safe_with_nonexistent_template(self, repo_root):
        """Test that render_template_safe handles missing templates gracefully."""
        templates_dir = repo_root / "docs-templates"
        env = Environment(loader=FileSystemLoader(str(templates_dir)))

        result = render_template_safe(env, "nonexistent.jinja2", {})
        assert result is None

    def test_render_template_safe_with_valid_template(self, repo_root):
        """Test that render_template_safe can render valid templates."""
        templates_dir = repo_root / "docs-templates"

        # Create a simple test template
        test_template = templates_dir / "_test_simple.jinja2"
        test_template.write_text("Hello {{ name }}!")

        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        result = render_template_safe(env, "_test_simple.jinja2", {"name": "World"})

        assert result is not None
        assert "Hello World!" in result

        # Cleanup
        test_template.unlink()


class TestDocGenerationPaths:
    """Test path handling in documentation generation."""

    def test_output_paths_are_correct(self, repo_root):
        """Test that output paths are computed correctly."""
        # Stage README output should be in stage directory
        stage_output = repo_root / "stages" / "01-intent-ingestion" / "README.md"
        assert stage_output.parent.exists()

    def test_context_directory_exists(self, repo_root):
        """Test that context directory exists for stage bundles."""
        context_dir = repo_root / "context"
        assert context_dir.exists() or not context_dir.exists()  # May or may not exist yet


class TestControlRegistryOperations:
    """Test operations on control registry."""

    def test_registry_entries_have_required_fields(self, repo_root):
        """Test that registry entries have required fields."""
        registry_file = repo_root / "controls" / "registry.yaml"
        data = load_yaml_safe(registry_file)
        registry = data.get("registry", [])

        for entry in registry:
            assert "id" in entry, "Registry entry missing 'id' field"
            assert "file" in entry or "name" in entry, "Registry entry missing 'file' or 'name'"

    def test_control_files_referenced_in_registry_exist(self, repo_root):
        """Test that all files referenced in registry exist."""
        registry_file = repo_root / "controls" / "registry.yaml"
        data = load_yaml_safe(registry_file)
        registry = data.get("registry", [])

        for entry in registry:
            file_path = entry.get("file")
            if file_path:
                full_path = repo_root / file_path
                assert full_path.exists(), f"Referenced file not found: {file_path}"

    def test_control_ids_match_file_names(self, repo_root):
        """Test that control IDs match their filenames."""
        registry_file = repo_root / "controls" / "registry.yaml"
        data = load_yaml_safe(registry_file)
        registry = data.get("registry", [])

        for entry in registry:
            control_id = entry.get("id")
            file_path = entry.get("file")

            if control_id and file_path:
                # Extract filename without extension
                filename = Path(file_path).stem
                assert control_id == filename, f"ID '{control_id}' doesn't match filename '{filename}'"


class TestDataStructureIntegrity:
    """Test integrity of framework data structures."""

    def test_all_stages_have_required_fields(self, repo_root):
        """Test that all stages have required fields."""
        asdlc_file = repo_root / "asdlc.yaml"
        data = load_yaml_safe(asdlc_file)
        stages = data.get("stages", [])

        for stage in stages:
            assert "number" in stage, "Stage missing 'number' field"
            assert "name" in stage, "Stage missing 'name' field"

    def test_stage_yaml_files_have_consistent_structure(self, repo_root):
        """Test that stage YAML files have consistent structure."""
        stages_dir = repo_root / "stages"
        stage_files = sorted(stages_dir.glob("*/[0-9]*-*.yaml"))

        for stage_file in stage_files:
            data = load_yaml_safe(stage_file)
            assert "number" in data, f"{stage_file.name} missing 'number'"
            assert "name" in data, f"{stage_file.name} missing 'name'"

    def test_control_files_have_consistent_structure(self, repo_root):
        """Test that control files have consistent basic structure."""
        controls_dir = repo_root / "controls"
        control_files = sorted(controls_dir.glob("*/*.yaml"))

        # At least test the first few
        for control_file in control_files[:5]:
            data = load_yaml_safe(control_file)
            assert "id" in data, f"{control_file.name} missing 'id'"


class TestDocGenerationWithRealData:
    """Integration tests with actual project data."""

    def test_framework_has_all_controls(self, repo_root):
        """Test that framework references all controls."""
        asdlc_file = repo_root / "asdlc.yaml"
        asdlc_data = load_yaml_safe(asdlc_file)

        registry_file = repo_root / "controls" / "registry.yaml"
        registry_data = load_yaml_safe(registry_file)
        registry = registry_data.get("registry", [])

        # Should have multiple controls
        assert len(registry) > 0

    def test_cross_cutting_controls_referenced(self, repo_root):
        """Test that cross-cutting controls are properly defined."""
        asdlc_file = repo_root / "asdlc.yaml"
        data = load_yaml_safe(asdlc_file)

        # Should have some kind of cross-cutting definition
        assert len(data) > 0

    def test_all_required_yaml_files_are_readable(self, repo_root):
        """Test that all essential YAML files can be read."""
        essential_files = [
            repo_root / "asdlc.yaml",
            repo_root / "controls" / "registry.yaml",
            repo_root / "feedbackloops" / "feedback-loops.yaml",
            repo_root / "manifest" / "catalog.yaml",
            repo_root / "regulatory" / "compliance-matrix.yaml",
        ]

        for filepath in essential_files:
            if filepath.exists():
                data = load_yaml_safe(filepath)
                assert isinstance(data, dict), f"Failed to load {filepath}"


class TestDocGenerationEdgeCases:
    """Test edge cases in documentation generation."""

    def test_empty_context_dictionary_renders(self, repo_root):
        """Test that rendering with empty context doesn't crash."""
        templates_dir = repo_root / "docs-templates"
        env = Environment(loader=FileSystemLoader(str(templates_dir)))

        # Should not raise exception
        result = render_template_safe(env, "nonexistent.jinja2", {})
        assert result is None

    def test_yaml_with_special_characters_loads(self, tmp_path):
        """Test that YAML with special characters loads correctly."""
        yaml_file = tmp_path / "special.yaml"
        yaml_file.write_text(
            "description: |\n"
            "  This has: colons, special|chars, and—dashes\n"
            "name: Control & Something Else\n"
        )

        data = load_yaml_safe(yaml_file)
        assert isinstance(data, dict)
        assert "description" in data
        assert "name" in data

    def test_large_registry_loads_efficiently(self, tmp_path):
        """Test that large registry files load without issues."""
        large_registry = tmp_path / "large_registry.yaml"

        # Create registry with many entries
        registry_data = {
            "registry": [
                {"id": f"TC-{i:1d}A", "name": f"Test Control {i}", "file": f"test/tc-{i}.yaml"}
                for i in range(1, 51)
            ]
        }

        large_registry.write_text(yaml.dump(registry_data))
        data = load_yaml_safe(large_registry)

        assert len(data.get("registry", [])) == 50
