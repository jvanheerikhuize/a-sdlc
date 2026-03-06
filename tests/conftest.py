"""Pytest configuration and shared fixtures for A-SDLC tests.

Provides:
  - repo_root: Minimal test repository structure
  - sample_control_registry: Test registry with 5 sample controls
  - sample_stage_yaml: Sample stage YAML structure
  - jinja_env: Configured Jinja2 environment
  - manifest_yaml: Test manifest/catalog.yaml
"""

import tempfile
from pathlib import Path
from typing import Any

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader


@pytest.fixture
def repo_root(tmp_path) -> Path:
    """Create minimal A-SDLC repository structure for testing.

    Creates:
      - asdlc.yaml (minimal manifest)
      - controls/registry.yaml (with 5 sample controls)
      - controls/qc/, controls/sc/, etc. directories
      - stages/01-intent-ingestion/ directory
      - scripts/templates/ directory

    Args:
        tmp_path: Pytest temporary directory fixture.

    Yields:
        Path to test repository root.
    """
    # Create required directories
    (tmp_path / "controls").mkdir()
    (tmp_path / "controls" / "qc").mkdir(parents=True)
    (tmp_path / "controls" / "sc").mkdir(parents=True)
    (tmp_path / "controls" / "rc").mkdir(parents=True)
    (tmp_path / "controls" / "ac").mkdir(parents=True)
    (tmp_path / "controls" / "gc").mkdir(parents=True)
    (tmp_path / "stages" / "01-intent-ingestion").mkdir(parents=True)
    (tmp_path / "scripts/templates").mkdir(parents=True)
    (tmp_path / "regulatory").mkdir(parents=True)
    (tmp_path / "feedbackloops").mkdir(parents=True)
    (tmp_path / "directives" / "core").mkdir(parents=True)
    (tmp_path / "manifest").mkdir(parents=True)

    # Create minimal asdlc.yaml
    asdlc = {
        "framework": {
            "name": "A-SDLC",
            "version": "1.0.0",
            "description": "Test framework",
        },
        "stages": [
            {
                "number": 1,
                "name": "Intent Ingestion",
                "slug": "intent-ingestion",
            }
        ],
    }
    with open(tmp_path / "asdlc.yaml", "w") as f:
        yaml.dump(asdlc, f)

    # Create registry with 5 sample controls
    registry_data = {
        "registry": [
            {"id": "QC-01", "name": "Test Control 1", "file": "controls/qc/QC-01.yaml"},
            {"id": "SC-02", "name": "Test Control 2", "file": "controls/sc/SC-02.yaml"},
            {"id": "RC-04", "name": "Test Control 3", "file": "controls/rc/RC-04.yaml"},
            {"id": "AC-02", "name": "Test Control 4", "file": "controls/ac/AC-02.yaml"},
            {"id": "GC-02", "name": "Test Control 5", "file": "controls/gc/GC-02.yaml"},
        ]
    }
    with open(tmp_path / "controls" / "registry.yaml", "w") as f:
        yaml.dump(registry_data, f)

    # Create sample control files
    for control in registry_data["registry"]:
        control_yaml = {
            "id": control["id"],
            "name": control["name"],
            "description": f"Test control {control['id']}",
            "stage": control["id"].split("-")[1][0],
        }
        control_path = tmp_path / control["file"]
        with open(control_path, "w") as f:
            yaml.dump(control_yaml, f)

    yield tmp_path


@pytest.fixture
def sample_control_registry(repo_root: Path) -> list:
    """Load sample control registry from test repo.

    Args:
        repo_root: Test repository root (fixture).

    Returns:
        List of control dicts from registry.yaml.
    """
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from scripts.shared import load_yaml_safe

    registry_file = repo_root / "controls" / "registry.yaml"
    data = load_yaml_safe(registry_file)
    return data.get("registry", [])


@pytest.fixture
def sample_stage_yaml() -> dict:
    """Create sample stage YAML structure for testing.

    Returns:
        Dict with typical stage structure.
    """
    return {
        "number": 1,
        "name": "Intent Ingestion",
        "slug": "intent-ingestion",
        "description": "Capture and validate feature requirements.",
        "required_controls": ["QC-01", "SC-03"],
        "workflow": {
            "nodes": [
                {"id": "QC-01", "name": "Spec Validation", "type": "quality"},
                {"id": "SC-03", "name": "Security Check", "type": "security"},
            ]
        },
        "exit_criteria": ["All controls passed", "Documentation complete"],
    }


@pytest.fixture
def jinja_env(repo_root: Path) -> Environment:
    """Create Jinja2 environment for template testing.

    Args:
        repo_root: Test repository root (fixture).

    Returns:
        Configured Jinja2 Environment instance.
    """
    env = Environment(
        loader=FileSystemLoader(repo_root / "scripts/templates"),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env


@pytest.fixture
def manifest_yaml(repo_root: Path) -> dict:
    """Create test manifest/catalog.yaml structure.

    Args:
        repo_root: Test repository root (fixture).

    Returns:
        Dict with manifest structure.
    """
    return {
        "framework": {
            "name": "A-SDLC",
            "version": "1.0.0",
        },
        "doc_generation": {
            "templates_dir": "scripts/templates",
            "generator_script": "scripts/generate-docs.py",
            "targets": [
                {
                    "source": "asdlc.yaml",
                    "template": "framework-overview",
                    "output": "README.md",
                    "description": "Root README",
                }
            ],
        },
    }


# Helper functions for creating test data


def create_control_yaml(path: Path, control_id: str, **kwargs) -> dict:
    """Create a sample control YAML file.

    Args:
        path: Path where control file should be created.
        control_id: Control ID (e.g., 'SC-02').
        **kwargs: Additional fields to include in control YAML.

    Returns:
        Dict of written control data.
    """
    control_data = {
        "id": control_id,
        "name": f"Control {control_id}",
        "description": f"Test control {control_id}",
        "stage": control_id.split("-")[1][0],
    }
    control_data.update(kwargs)

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(control_data, f)

    return control_data


def create_stage_yaml(path: Path, stage_num: int, **kwargs) -> dict:
    """Create a sample stage YAML file.

    Args:
        path: Path where stage file should be created.
        stage_num: Stage number (1-6).
        **kwargs: Additional fields to include in stage YAML.

    Returns:
        Dict of written stage data.
    """
    stage_data = {
        "number": stage_num,
        "name": f"Stage {stage_num}",
        "description": f"Test stage {stage_num}",
        "required_controls": [],
    }
    stage_data.update(kwargs)

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(stage_data, f)

    return stage_data


def create_registry_entry(control_id: str, **kwargs) -> dict:
    """Create a registry entry dict.

    Args:
        control_id: Control ID (e.g., 'SC-02').
        **kwargs: Additional fields to include.

    Returns:
        Registry entry dict.
    """
    entry = {
        "id": control_id,
        "name": f"Control {control_id}",
        "file": f"controls/{control_id.split('-')[0].lower()}/{control_id}.yaml",
    }
    entry.update(kwargs)
    return entry
