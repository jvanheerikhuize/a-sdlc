"""Unit tests for scripts/shared.py utilities.

Tests all 8 shared utility functions with various inputs and edge cases.
"""

import json
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader

from scripts.shared import (
    build_markdown_table,
    extract_control_id_from_string,
    find_control_in_registry,
    get_repo_root,
    load_json_safe,
    load_yaml_safe,
    rel_path,
    render_template_safe,
)


class TestLoadYamlSafe:
    """Tests for load_yaml_safe() function."""

    def test_load_valid_yaml(self, repo_root: Path):
        """Test loading valid YAML file."""
        yaml_file = repo_root / "asdlc.yaml"
        data = load_yaml_safe(yaml_file)
        assert isinstance(data, dict)
        assert "framework" in data

    def test_load_missing_file_returns_empty_dict(self, repo_root: Path):
        """Test that missing file returns empty dict (not error)."""
        missing_file = repo_root / "nonexistent.yaml"
        data = load_yaml_safe(missing_file)
        assert data == {}

    def test_load_malformed_yaml_raises_error(self, tmp_path: Path):
        """Test that malformed YAML raises yaml.YAMLError."""
        bad_yaml = tmp_path / "bad.yaml"
        bad_yaml.write_text("key: value\n  bad indentation:")
        with pytest.raises(yaml.YAMLError):
            load_yaml_safe(bad_yaml)

    def test_load_registry_yaml(self, repo_root: Path):
        """Test loading registry YAML with multiple entries."""
        registry_file = repo_root / "controls" / "registry.yaml"
        data = load_yaml_safe(registry_file)
        assert "registry" in data
        assert len(data["registry"]) == 5
        assert data["registry"][0]["id"] == "QC-1A"


class TestLoadJsonSafe:
    """Tests for load_json_safe() function."""

    def test_load_valid_json(self, tmp_path: Path):
        """Test loading valid JSON file."""
        json_file = tmp_path / "test.json"
        test_data = {"key": "value", "number": 42}
        json_file.write_text(json.dumps(test_data))

        data = load_json_safe(json_file)
        assert data == test_data

    def test_load_missing_json_returns_empty_dict(self, tmp_path: Path):
        """Test that missing JSON file returns empty dict."""
        missing_file = tmp_path / "nonexistent.json"
        data = load_json_safe(missing_file)
        assert data == {}

    def test_load_malformed_json_raises_error(self, tmp_path: Path):
        """Test that malformed JSON raises JSONDecodeError."""
        bad_json = tmp_path / "bad.json"
        bad_json.write_text('{"invalid": json}')
        with pytest.raises(json.JSONDecodeError):
            load_json_safe(bad_json)


class TestExtractControlIdFromString:
    """Tests for extract_control_id_from_string() function."""

    def test_extract_valid_control_id(self):
        """Test extracting valid control ID from text."""
        text = "Please implement SC-2B security control"
        control_id = extract_control_id_from_string(text)
        assert control_id == "SC-2B"

    def test_extract_multiple_ids_returns_first(self):
        """Test that function returns first match when multiple IDs present."""
        text = "Controls SC-2B and QC-1A are required"
        control_id = extract_control_id_from_string(text)
        assert control_id == "SC-2B"

    def test_extract_invalid_id_returns_none(self):
        """Test that function returns None for invalid ID."""
        text = "This text has no control ID"
        control_id = extract_control_id_from_string(text)
        assert control_id is None

    def test_extract_all_valid_track_codes(self):
        """Test extraction for all track codes."""
        test_cases = [
            ("Control QC-1A", "QC-1A"),
            ("Control SC-3B", "SC-3B"),
            ("Control RC-2A", "RC-2A"),
            ("Control AC-4C", "AC-4C"),
            ("Control GC-5D", "GC-5D"),
        ]
        for text, expected in test_cases:
            result = extract_control_id_from_string(text)
            assert result == expected


class TestFindControlInRegistry:
    """Tests for find_control_in_registry() function."""

    def test_find_existing_control(self, sample_control_registry: list):
        """Test finding control that exists in registry."""
        control = find_control_in_registry("QC-1A", sample_control_registry)
        assert control is not None
        assert control["id"] == "QC-1A"
        assert control["name"] == "Test Control 1"

    def test_find_missing_control_returns_none(self, sample_control_registry: list):
        """Test that missing control returns None."""
        control = find_control_in_registry("ZZ-9Z", sample_control_registry)
        assert control is None

    def test_find_all_sample_controls(self, sample_control_registry: list):
        """Test finding all sample controls in registry."""
        for control_id in ["QC-1A", "SC-2B", "RC-3A", "AC-1B", "GC-2A"]:
            control = find_control_in_registry(control_id, sample_control_registry)
            assert control is not None
            assert control["id"] == control_id

    def test_find_in_empty_registry(self):
        """Test finding control in empty registry."""
        control = find_control_in_registry("SC-2B", [])
        assert control is None


class TestBuildMarkdownTable:
    """Tests for build_markdown_table() function."""

    def test_simple_table(self):
        """Test building simple 2-column table."""
        headers = ["ID", "Name"]
        rows = [
            {"ID": "SC-2B", "Name": "Security Control"},
            {"ID": "QC-1A", "Name": "Quality Control"},
        ]
        result = build_markdown_table(headers, rows)

        assert "| ID | Name |" in result
        assert "| SC-2B | Security Control |" in result
        assert "| QC-1A | Quality Control |" in result

    def test_table_with_special_chars(self):
        """Test table with special markdown characters."""
        headers = ["Field", "Value"]
        rows = [
            {"Field": "Pipe", "Value": "| symbol |"},
            {"Field": "Bracket", "Value": "[link]"},
        ]
        result = build_markdown_table(headers, rows)

        assert "| Pipe | symbol |" in result
        assert "| Bracket | [link] |" in result

    def test_empty_rows_list(self):
        """Test table with headers but no rows."""
        headers = ["Column 1", "Column 2"]
        rows = []
        result = build_markdown_table(headers, rows)

        assert "| Column 1 | Column 2 |" in result
        # Should have header and separator, but no data rows
        lines = result.strip().split("\n")
        assert len(lines) == 2  # header + separator

    def test_missing_fields_use_dash(self):
        """Test that missing fields in row dict are replaced with '—'."""
        headers = ["ID", "Name", "Status"]
        rows = [
            {"ID": "SC-2B"},  # Missing Name and Status
        ]
        result = build_markdown_table(headers, rows)

        assert "| SC-2B | — | — |" in result

    def test_multiple_columns(self):
        """Test table with many columns."""
        headers = ["A", "B", "C", "D", "E"]
        rows = [{"A": "1", "B": "2", "C": "3", "D": "4", "E": "5"}]
        result = build_markdown_table(headers, rows)

        assert "| 1 | 2 | 3 | 4 | 5 |" in result


class TestRenderTemplateSafe:
    """Tests for render_template_safe() function."""

    def test_render_with_nonexistent_template(self, jinja_env: Environment):
        """Test that nonexistent template returns None (not error)."""
        result = render_template_safe(jinja_env, "nonexistent.jinja2", {})
        assert result is None

    def test_render_simple_template(self, tmp_path: Path):
        """Test rendering simple template with variables."""
        template_dir = tmp_path / "templates"
        template_dir.mkdir()

        template_file = template_dir / "test.jinja2"
        template_file.write_text("Hello {{ name }}!")

        env = Environment(loader=FileSystemLoader(template_dir))
        result = render_template_safe(env, "test.jinja2", {"name": "World"})

        assert result == "Hello World!"

    def test_render_with_loops(self, tmp_path: Path):
        """Test rendering template with for loop."""
        template_dir = tmp_path / "templates"
        template_dir.mkdir()

        template_file = template_dir / "list.jinja2"
        template_file.write_text("Items:\n{% for item in items %}  - {{ item }}\n{% endfor %}")

        env = Environment(loader=FileSystemLoader(template_dir))
        result = render_template_safe(env, "list.jinja2", {"items": ["a", "b", "c"]})

        assert "Items:" in result
        assert "- a" in result
        assert "- b" in result
        assert "- c" in result


class TestGetRepoRoot:
    """Tests for get_repo_root() function."""

    def test_find_repo_root_in_current_dir(self, repo_root: Path, monkeypatch):
        """Test finding repo root when in repo directory."""
        monkeypatch.chdir(repo_root)
        root = get_repo_root()
        assert root == repo_root
        assert (root / "asdlc.yaml").exists()

    def test_find_repo_root_in_subdirectory(self, repo_root: Path, monkeypatch):
        """Test finding repo root from subdirectory."""
        subdir = repo_root / "controls" / "sc"
        subdir.mkdir(parents=True, exist_ok=True)
        monkeypatch.chdir(subdir)
        root = get_repo_root()
        assert root == repo_root

    def test_repo_root_not_found_raises_error(self, tmp_path: Path, monkeypatch):
        """Test that error is raised when repo root not found."""
        # Create temp dir without asdlc.yaml
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        monkeypatch.chdir(empty_dir)

        with pytest.raises(RuntimeError, match="Cannot find A-SDLC repository root"):
            get_repo_root()


class TestRelPath:
    """Tests for rel_path() function."""

    def test_relative_path_conversion(self, repo_root: Path):
        """Test converting absolute path to relative."""
        abs_path = repo_root / "controls" / "sc" / "SC-2B.yaml"
        result = rel_path(abs_path, repo_root)
        assert result == "controls/sc/SC-2B.yaml"

    def test_path_not_relative_returns_str(self, repo_root: Path):
        """Test that path not under root returns full path string."""
        other_path = Path("/tmp/some/other/file.yaml")
        result = rel_path(other_path, repo_root)
        assert "/tmp/some/other/file.yaml" in result

    def test_relative_path_with_dots(self, repo_root: Path):
        """Test relative path conversion with directory traversal."""
        file_path = repo_root / "a" / "b" / "c" / "file.txt"
        result = rel_path(file_path, repo_root)
        assert result == "a/b/c/file.txt"
