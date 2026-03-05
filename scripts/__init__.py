"""A-SDLC utility scripts for validation and documentation generation.

Shared utilities for both scripts:
  - load_yaml_safe, load_json_safe: Safe file loading with error handling
  - find_control_in_registry: Registry lookup helper
  - build_markdown_table: Markdown table builder
  - render_template_safe: Template rendering wrapper
  - extract_control_id_from_string: Control ID extraction
  - get_repo_root, rel_path: Path utilities
"""

from .shared import (
    build_markdown_table,
    extract_control_id_from_string,
    find_control_in_registry,
    get_repo_root,
    load_json_safe,
    load_yaml_safe,
    rel_path,
    render_template_safe,
)

__all__ = [
    "load_yaml_safe",
    "load_json_safe",
    "extract_control_id_from_string",
    "find_control_in_registry",
    "build_markdown_table",
    "render_template_safe",
    "get_repo_root",
    "rel_path",
]
