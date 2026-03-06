#!/usr/bin/env python3
"""
Control ID Migration Script

Migrates control IDs from old format [Track]-[Stage][Letter] to new format [Track]-[NN].
Reads mapping from migration/id-mapping.yaml.

Usage:
  python3 scripts/migrate-control-ids.py --dry-run    # Preview changes
  python3 scripts/migrate-control-ids.py --execute     # Apply changes
"""

import os
import re
import sys
import yaml
from pathlib import Path


def load_mapping(repo_root):
    """Load the ID mapping from migration/id-mapping.yaml."""
    mapping_file = repo_root / "migration" / "id-mapping.yaml"
    with open(mapping_file) as f:
        data = yaml.safe_load(f)
    return data.get("mappings", [])


def build_replacement_map(mappings):
    """Build old->new mapping dict, sorted by old ID length descending to avoid partial matches."""
    replacements = {}
    for m in mappings:
        replacements[m["old"]] = m["new"]
    # Sort by length descending so longer IDs are replaced first
    return dict(sorted(replacements.items(), key=lambda x: len(x[0]), reverse=True))


def replace_ids_in_content(content, replacements):
    """Replace all old control IDs with new ones in text content.

    Uses word-boundary-aware replacement to avoid partial matches.
    """
    new_content = content
    for old_id, new_id in replacements.items():
        # Use word boundary regex to avoid partial matches
        # Match old_id when surrounded by non-alphanumeric chars or start/end of string
        pattern = re.compile(r'(?<![A-Za-z0-9-])' + re.escape(old_id) + r'(?![A-Za-z0-9])')
        new_content = pattern.sub(new_id, new_content)
    return new_content


def find_files_to_process(repo_root):
    """Find all files that may contain control IDs."""
    extensions = {".yaml", ".yml", ".json", ".md", ".py", ".jinja2"}
    skip_dirs = {".git", "__pycache__", "node_modules", ".claude", "migration", "initialcontext"}

    files = []
    for root, dirs, filenames in os.walk(repo_root):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for filename in filenames:
            filepath = Path(root) / filename
            if filepath.suffix in extensions:
                files.append(filepath)
    return sorted(files)


def find_files_to_rename(repo_root, replacements):
    """Find control YAML files and artifact files that need renaming."""
    renames = []

    # Control YAML files: controls/[track]/OLD.yaml -> controls/[track]/NEW.yaml
    controls_dir = repo_root / "controls"
    for track_dir in controls_dir.iterdir():
        if track_dir.is_dir() and track_dir.name in ("qc", "rc", "sc", "ac", "gc"):
            for yaml_file in track_dir.glob("*.yaml"):
                stem = yaml_file.stem  # e.g., "SC-01"
                if stem in replacements:
                    new_name = replacements[stem] + ".yaml"
                    renames.append((yaml_file, yaml_file.parent / new_name))

    # Artifact output files: stages/*/artifacts/outputs/OLD-description.yaml
    stages_dir = repo_root / "stages"
    for stage_dir in stages_dir.iterdir():
        if stage_dir.is_dir():
            outputs_dir = stage_dir / "artifacts" / "outputs"
            if outputs_dir.exists():
                for yaml_file in outputs_dir.glob("*.yaml"):
                    filename = yaml_file.name
                    for old_id, new_id in replacements.items():
                        if filename.startswith(old_id):
                            new_filename = filename.replace(old_id, new_id, 1)
                            renames.append((yaml_file, yaml_file.parent / new_filename))
                            break

    return renames


def dry_run(repo_root, replacements):
    """Preview all changes without modifying files."""
    print("\n=== DRY RUN: Control ID Migration ===\n")

    # 1. File content replacements
    files = find_files_to_process(repo_root)
    content_changes = 0
    files_changed = 0

    for filepath in files:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except (UnicodeDecodeError, PermissionError):
            continue

        new_content = replace_ids_in_content(content, replacements)
        if new_content != content:
            files_changed += 1
            # Count individual replacements
            for old_id in replacements:
                pattern = re.compile(r'(?<![A-Za-z0-9-])' + re.escape(old_id) + r'(?![A-Za-z0-9])')
                count = len(pattern.findall(content))
                if count > 0:
                    rel_path = filepath.relative_to(repo_root)
                    print(f"  {rel_path}: {old_id} -> {replacements[old_id]} ({count}x)")
                    content_changes += count

    print(f"\n  Content changes: {content_changes} replacements across {files_changed} files\n")

    # 2. File renames
    renames = find_files_to_rename(repo_root, replacements)
    print(f"  File renames: {len(renames)}")
    for old_path, new_path in renames:
        rel_old = old_path.relative_to(repo_root)
        rel_new = new_path.relative_to(repo_root)
        print(f"    {rel_old} -> {rel_new}")

    print(f"\n=== Summary: {content_changes} replacements, {files_changed} files modified, {len(renames)} files renamed ===\n")


def execute(repo_root, replacements):
    """Apply all changes."""
    print("\n=== EXECUTING: Control ID Migration ===\n")

    # 1. Replace content in all files first (before renaming)
    files = find_files_to_process(repo_root)
    content_changes = 0
    files_changed = 0

    for filepath in files:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except (UnicodeDecodeError, PermissionError):
            continue

        new_content = replace_ids_in_content(content, replacements)
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            files_changed += 1
            rel_path = filepath.relative_to(repo_root)
            print(f"  Updated: {rel_path}")
            content_changes += 1

    print(f"\n  Content: {files_changed} files updated\n")

    # 2. Rename files
    renames = find_files_to_rename(repo_root, replacements)
    renamed_count = 0
    for old_path, new_path in renames:
        if old_path.exists():
            old_path.rename(new_path)
            rel_old = old_path.relative_to(repo_root)
            rel_new = new_path.relative_to(repo_root)
            print(f"  Renamed: {rel_old} -> {rel_new}")
            renamed_count += 1

    print(f"\n  Renames: {renamed_count} files renamed")
    print(f"\n=== Migration complete: {files_changed} files updated, {renamed_count} files renamed ===\n")


def main():
    repo_root = Path(__file__).parent.parent

    if len(sys.argv) < 2 or sys.argv[1] not in ("--dry-run", "--execute"):
        print(__doc__)
        sys.exit(1)

    mappings = load_mapping(repo_root)
    replacements = build_replacement_map(mappings)

    print(f"Loaded {len(replacements)} ID mappings")

    if sys.argv[1] == "--dry-run":
        dry_run(repo_root, replacements)
    elif sys.argv[1] == "--execute":
        execute(repo_root, replacements)


if __name__ == "__main__":
    main()
