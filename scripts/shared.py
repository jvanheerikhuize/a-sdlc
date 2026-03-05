"""Shared utilities for A-SDLC scripts (validate.py, generate-docs.py).

This module provides common functionality used across multiple scripts:
  - YAML and JSON loading with error handling
  - Registry lookup helpers
  - Markdown table builders
  - Template rendering wrappers
  - Control ID extraction
  - Path utilities

All functions handle edge cases gracefully (missing files, parse errors, etc.)
and include type hints for IDE support.
"""

import json
import re
from pathlib import Path
from typing import Any, Optional

import yaml
from jinja2 import Environment, TemplateNotFound


def load_yaml_safe(path: Path) -> dict:
    """Load YAML file with comprehensive error handling.

    Args:
        path: Path to YAML file.

    Returns:
        Parsed YAML dict, or empty dict if file not found.

    Raises:
        yaml.YAMLError: If YAML syntax is invalid.
        IOError: If file cannot be read.
    """
    try:
        if not path.exists():
            return {}
        with open(path) as f:
            data = yaml.safe_load(f)
            return data if data else {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"YAML parsing failed in {path}: {e}") from e
    except IOError as e:
        raise IOError(f"Cannot read file {path}: {e}") from e


def load_json_safe(path: Path) -> dict:
    """Load JSON file with error handling.

    Args:
        path: Path to JSON file.

    Returns:
        Parsed JSON dict, or empty dict if file not found.

    Raises:
        json.JSONDecodeError: If JSON is invalid.
        IOError: If file cannot be read.
    """
    try:
        if not path.exists():
            return {}
        with open(path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"JSON parsing failed in {path}: {e.msg}", e.doc, e.pos) from e
    except IOError as e:
        raise IOError(f"Cannot read file {path}: {e}") from e


def extract_control_id_from_string(text: str) -> Optional[str]:
    """Extract control ID from text using regex pattern.

    Control ID format: [TRACK]-[STAGE][LETTER]
    Examples: SC-2B, QC-1A, RC-5B

    Args:
        text: Text to search for control ID.

    Returns:
        Control ID string (e.g., 'SC-2B'), or None if not found.
    """
    pattern = r'([A-Z]{2})-(\d[A-Z])'
    match = re.search(pattern, text)
    return match.group(0) if match else None


def find_control_in_registry(control_id: str, registry: list) -> Optional[dict]:
    """Find control by ID in registry list.

    Args:
        control_id: Control ID to search for (e.g., 'SC-2B').
        registry: List of control dicts from registry.yaml.

    Returns:
        Control dict if found, None otherwise.
    """
    for ctrl in registry:
        if ctrl.get("id") == control_id:
            return ctrl
    return None


def build_markdown_table(headers: list, rows: list) -> str:
    """Build a markdown table from headers and row dicts.

    Args:
        headers: List of header strings (column names).
        rows: List of dicts, one per row. Each dict should have keys matching headers.

    Returns:
        Markdown table as multi-line string.

    Example:
        >>> headers = ["Name", "Status"]
        >>> rows = [{"Name": "SC-2B", "Status": "Active"}]
        >>> print(build_markdown_table(headers, rows))
        | Name | Status |
        |------|--------|
        | SC-2B | Active |
    """
    if not headers:
        return ""

    # Build header row
    header_row = "| " + " | ".join(str(h) for h in headers) + " |"

    # Build separator row
    sep_row = "| " + " | ".join("-" * max(3, len(str(h))) for h in headers) + " |"

    # Build data rows
    data_rows = []
    for row_dict in rows:
        row_values = [str(row_dict.get(h, "—")) for h in headers]
        data_rows.append("| " + " | ".join(row_values) + " |")

    # Combine all rows
    all_rows = [header_row, sep_row] + data_rows
    return "\n".join(all_rows)


def render_template_safe(env: Environment, template_name: str, context: dict) -> Optional[str]:
    """Render Jinja2 template with error handling.

    Args:
        env: Jinja2 Environment instance.
        template_name: Name of template file (e.g., 'stage-readme.jinja2').
        context: Dict of variables to pass to template.

    Returns:
        Rendered template string, or None if template not found.

    Raises:
        Exception: For template rendering errors other than TemplateNotFound.
    """
    try:
        template = env.get_template(template_name)
        return template.render(context)
    except TemplateNotFound:
        return None


def get_repo_root() -> Path:
    """Find repository root directory.

    Searches upward from current directory for a directory containing:
      - asdlc.yaml (framework manifest)
      - controls/ directory
      - stages/ directory

    Returns:
        Path to repository root.

    Raises:
        RuntimeError: If repository root cannot be found.
    """
    current = Path.cwd()
    max_depth = 10  # Prevent infinite loops

    for _ in range(max_depth):
        if (current / "asdlc.yaml").exists() and (current / "controls").is_dir():
            return current
        if current.parent == current:  # Reached filesystem root
            break
        current = current.parent

    raise RuntimeError("Cannot find A-SDLC repository root (asdlc.yaml not found)")


def rel_path(path: Path, from_root: Path) -> str:
    """Get relative path from repository root for display.

    Args:
        path: Full path to file.
        from_root: Repository root path.

    Returns:
        Relative path as string (e.g., 'controls/sc/SC-2B.yaml').
    """
    try:
        return str(path.relative_to(from_root))
    except ValueError:
        # Path is not relative to from_root
        return str(path)
