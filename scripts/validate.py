#!/usr/bin/env python3
"""
A-SDLC Framework Self-Audit
============================
Validates all YAML files against their JSON schemas and runs cross-reference
integrity checks across the repository.

Usage:
  python3 scripts/validate.py              # full audit
  python3 scripts/validate.py --no-schema  # skip schema validation
  python3 scripts/validate.py --no-xref   # skip cross-reference checks
  python3 scripts/validate.py --quiet     # only show failures and warnings

Requirements:
  pip install -r scripts/requirements.txt
  (pyyaml + jsonschema)
"""

import sys
import os
import json
import re
import argparse
from pathlib import Path

# Add repo root to path for imports
_repo_root = Path(__file__).parent.parent
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

# ── dependency check ──────────────────────────────────────────────────────────

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed.")
    print("       Run: pip install -r scripts/requirements.txt")
    sys.exit(2)

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

try:
    from scripts.shared import (
        load_yaml_safe,
        load_json_safe,
        rel_path,
        extract_control_id_from_string,
    )
except ImportError:
    # Fallback for module imports
    from .shared import (
        load_yaml_safe,
        load_json_safe,
        rel_path,
        extract_control_id_from_string,
    )

# ── paths ─────────────────────────────────────────────────────────────────────

REPO = Path(__file__).parent.parent.resolve()
SCHEMA_DIR    = REPO / "schema"
CONTROLS_DIR  = REPO / "controls"
STAGES_DIR    = REPO / "stages"
DIRECTIVES_DIR = REPO / "directives"
REGISTRY_FILE  = CONTROLS_DIR / "registry.yaml"
FEEDBACK_FILE  = REPO / "feedbackloops" / "feedback-loops.yaml"
FEEDBACK_DIR   = REPO / "feedbackloops"

CONTROL_ID_RE = re.compile(r"^(QC|RC|SC|AC|GC)-[0-6][A-Z]$")

# ── result tracking ───────────────────────────────────────────────────────────

class Checker:
    def __init__(self, quiet=False):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.quiet = quiet
        self._section = ""

    def section(self, title):
        self._section = title
        print(f"\n{'─' * 60}")
        print(f"  {title}")
        print(f"{'─' * 60}")

    def ok(self, msg):
        self.passed += 1
        if not self.quiet:
            print(f"  \u2713  {msg}")

    def fail(self, msg):
        self.failed += 1
        print(f"  \u2717  {msg}")

    def warn(self, msg):
        self.warnings += 1
        print(f"  \u26a0  {msg}")

    @property
    def all_passed(self):
        return self.failed == 0

# ── helpers ───────────────────────────────────────────────────────────────────

def load_yaml(path: Path) -> dict:
    """Load YAML file using shared utility.

    Args:
        path: Path to YAML file.

    Returns:
        Parsed YAML as dict, or empty dict if not found.
    """
    return load_yaml_safe(Path(path)) or {}

def load_json(path: Path) -> dict:
    """Load JSON file using shared utility.

    Args:
        path: Path to JSON file.

    Returns:
        Parsed JSON as dict, or empty dict if not found.
    """
    return load_json_safe(Path(path)) or {}

def rel(path: Path) -> str:
    """Return path relative to REPO root for display.

    Args:
        path: Path to convert.

    Returns:
        Relative path string.
    """
    return rel_path(Path(path), REPO)

def validate_schema(data: dict, schema: dict, path: Path, checker) -> None:
    """Validate data against a JSON Schema. Reports pass/fail.

    Args:
        data: Data to validate.
        schema: JSON Schema to validate against.
        path: Path to file (for error messages).
        checker: Checker instance for result tracking.
    """
    if not HAS_JSONSCHEMA:
        checker.warn(f"jsonschema not installed — skipping: {rel(path)}")
        return
    try:
        validator = jsonschema.Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            for e in errors:
                loc = " > ".join(str(p) for p in e.path) or "(root)"
                checker.fail(f"{rel(path)}\n       [{loc}] {e.message}")
        else:
            checker.ok(f"{rel(path)}")
    except jsonschema.SchemaError as e:
        checker.fail(f"SCHEMA ERROR in {rel(path)}: {e.message}")

# ── section 1: control files ──────────────────────────────────────────────────

def check_control_files(checker) -> list:
    """Check control files for schema compliance and ID alignment.

    Args:
        checker: Checker instance for result tracking.

    Returns:
        List of found control IDs.
    """
    checker.section("1/7  Control files — schema + filename alignment")
    schema = load_json(SCHEMA_DIR / "control.schema.json")

    control_files = sorted(CONTROLS_DIR.glob("*/*.yaml"))
    if not control_files:
        checker.fail("No control files found in controls/*/")
        return []

    found_ids = []
    for path in control_files:
        data = load_yaml(path)
        if not isinstance(data, dict):
            checker.fail(f"{rel(path)} — not a YAML mapping")
            continue

        cid = data.get("id", "")

        # Filename must match id field
        if cid != path.stem:
            checker.fail(f"{rel(path)} — id '{cid}' does not match filename '{path.stem}'")
        else:
            checker.ok(f"{rel(path)} — id matches filename")

        # id must match pattern
        if not CONTROL_ID_RE.match(cid):
            checker.fail(f"{rel(path)} — id '{cid}' does not match pattern [Track]-[Stage][Letter]")

        # Schema validation
        validate_schema(data, schema, path, checker)

        found_ids.append(cid)

    checker.ok(f"Found {len(found_ids)} control files")
    return found_ids

# ── section 2: registry ───────────────────────────────────────────────────────

def check_registry(checker, found_control_ids: list) -> list:
    checker.section("2/7  Registry — completeness + file existence")

    if not REGISTRY_FILE.exists():
        checker.fail(f"controls/registry.yaml not found")
        return []

    data = load_yaml(REGISTRY_FILE)
    entries = data.get("registry", [])

    registry_ids = []
    seen = set()

    for entry in entries:
        eid = entry.get("id", "")

        # Duplicate IDs
        if eid in seen:
            checker.fail(f"Duplicate ID in registry: {eid}")
        seen.add(eid)
        registry_ids.append(eid)

        # Control file exists
        file_path = REPO / entry.get("file", "")
        if file_path.exists():
            checker.ok(f"{eid}: control file exists")
        else:
            checker.fail(f"{eid}: control file not found — {entry.get('file')}")

        # Single directive_payload (optional)
        dp = entry.get("directive_payload")
        if dp:
            dp_path = REPO / dp
            if dp_path.exists():
                checker.ok(f"{eid}: directive_payload exists")
            else:
                checker.fail(f"{eid}: directive_payload not found — {dp}")

        # Array directive_payloads (optional)
        for dp in entry.get("directive_payloads", []):
            dp_path = REPO / dp
            if dp_path.exists():
                checker.ok(f"{eid}: directive_payload exists — {dp}")
            else:
                checker.fail(f"{eid}: directive_payload not found — {dp}")

    # Every control file → in registry
    for cid in found_control_ids:
        if cid not in registry_ids:
            checker.fail(f"Control {cid} found in controls/ but missing from registry")
        else:
            checker.ok(f"Control {cid} present in registry")

    # Every registry entry → control file exists
    for rid in registry_ids:
        if rid not in found_control_ids:
            checker.fail(f"Registry entry {rid} has no matching file in controls/")

    checker.ok(f"Registry: {len(registry_ids)} entries")
    return registry_ids

# ── section 3: stage files ────────────────────────────────────────────────────

def check_stage_files(checker, registry_ids: list) -> None:
    checker.section("3/7  Stage files — schema + control + artifact references")
    schema = load_json(SCHEMA_DIR / "stage.schema.json")

    # Stage YAML files named like 01-intent-ingestion.yaml
    stage_files = sorted(f for f in STAGES_DIR.glob("*/0?-*.yaml")
                         if re.match(r"0[1-6]-", f.name))

    if not stage_files:
        checker.fail("No stage YAML files found in stages/*/")
        return

    for path in stage_files:
        data = load_yaml(path)
        stage_dir = path.parent

        # Schema validation
        validate_schema(data, schema, path, checker)

        # process.md exists
        proc = stage_dir / data.get("process", "process.md")
        if proc.exists():
            checker.ok(f"{rel(path)}: process.md exists")
        else:
            checker.fail(f"{rel(path)}: process.md not found — {rel(proc)}")

        # required_controls IDs exist in registry
        for ctrl in data.get("required_controls", []):
            cid = ctrl["id"] if isinstance(ctrl, dict) else ctrl
            if cid in registry_ids:
                checker.ok(f"{rel(path)}: required control {cid} in registry")
            else:
                checker.fail(f"{rel(path)}: required control {cid} not found in registry")

        # Artifact paths — resolve relative to the stage directory
        artifacts = data.get("artifacts", {})
        for section in ("inputs", "outputs"):
            for apath in artifacts.get(section, []):
                full = (stage_dir / apath).resolve()
                if full.exists():
                    checker.ok(f"{rel(path)}: artifact {section} exists — {apath}")
                else:
                    checker.warn(f"{rel(path)}: artifact template not found — {apath}")

        # Directive paths — relative to REPO root
        for dpath in data.get("directives", []):
            full = REPO / dpath
            if full.exists():
                checker.ok(f"{rel(path)}: directive exists — {dpath}")
            else:
                checker.fail(f"{rel(path)}: directive not found — {dpath}")

    checker.ok(f"Checked {len(stage_files)} stage files")

# ── section 4: directive files ────────────────────────────────────────────────

def check_directive_files(checker) -> None:
    checker.section("4/7  Directive files — schema validation")
    schema = load_json(SCHEMA_DIR / "directive.schema.json")

    directive_files = sorted(
        list(DIRECTIVES_DIR.glob("core/*.yaml")) +
        list(DIRECTIVES_DIR.glob("stages/*.yaml"))
    )

    if not directive_files:
        checker.fail("No directive files found in directives/")
        return

    for path in directive_files:
        data = load_yaml(path)
        validate_schema(data, schema, path, checker)

    checker.ok(f"Checked {len(directive_files)} directive files")

# ── section 5: control dependencies ──────────────────────────────────────────

def check_control_dependencies(checker, registry_ids: list) -> None:
    checker.section("5/7  Control dependency chains")

    for path in sorted(CONTROLS_DIR.glob("*/*.yaml")):
        data = load_yaml(path)
        cid = data.get("id", path.stem)
        deps = data.get("dependencies", []) or []

        for dep in deps:
            if dep in registry_ids:
                checker.ok(f"{cid} → dependency {dep} exists")
            else:
                checker.fail(f"{cid} → dependency {dep} not found in registry")

    # Cycle detection (DFS)
    graph = {}
    for path in CONTROLS_DIR.glob("*/*.yaml"):
        data = load_yaml(path)
        cid = data.get("id", path.stem)
        graph[cid] = data.get("dependencies", []) or []

    def has_cycle(node, visited, stack):
        visited.add(node)
        stack.add(node)
        for dep in graph.get(node, []):
            if dep not in visited:
                if has_cycle(dep, visited, stack):
                    return True
            elif dep in stack:
                return True
        stack.discard(node)
        return False

    visited = set()
    for node in list(graph):
        if node not in visited:
            if has_cycle(node, visited, set()):
                checker.fail(f"Circular dependency detected involving {node}")

    checker.ok("No circular dependencies detected")

# ── section 6: feedback loops ─────────────────────────────────────────────────

def check_feedback_loops(checker, registry_ids: list) -> None:
    checker.section("6/7  Feedback loops — structure + control reference validation")

    if not FEEDBACK_FILE.exists():
        checker.fail(f"Feedback loops file not found: {rel(FEEDBACK_FILE)}")
        return

    # Structural files
    for required_file in ("process.md", "README.md"):
        p = FEEDBACK_DIR / required_file
        if p.exists():
            checker.ok(f"feedbackloops/{required_file} present")
        else:
            checker.fail(f"feedbackloops/{required_file} missing")

    # Artifact outputs directory
    artifacts_out = FEEDBACK_DIR / "artifacts" / "outputs"
    if artifacts_out.exists():
        n = len(list(artifacts_out.glob("*.yaml")))
        checker.ok(f"feedbackloops/artifacts/outputs/ present ({n} templates)")
    else:
        checker.fail("feedbackloops/artifacts/outputs/ directory missing")

    # Autofix templates directory (may be empty at start — warn only)
    autofix_dir = FEEDBACK_DIR / "autofix-templates"
    if autofix_dir.exists():
        n = len(list(autofix_dir.glob("*.yaml")))
        checker.ok(f"feedbackloops/autofix-templates/ present ({n} template(s))")
    else:
        checker.warn("feedbackloops/autofix-templates/ directory not yet created")

    # Validate paths declared in feedback-loops.yaml header
    data = load_yaml(FEEDBACK_FILE)
    process_ref = data.get("process")
    if process_ref:
        p = FEEDBACK_DIR / process_ref
        if p.exists():
            checker.ok(f"feedback-loops.yaml: process ref resolves — {process_ref}")
        else:
            checker.fail(f"feedback-loops.yaml: process ref not found — {process_ref}")

    for art_path in (data.get("artifacts") or {}).get("outputs", []):
        p = FEEDBACK_DIR / art_path
        if p.exists():
            checker.ok(f"feedback-loops.yaml: artifact ref resolves — {art_path}")
        else:
            checker.warn(f"feedback-loops.yaml: artifact ref not found — {art_path}")

    loops = data.get("feedback_loops", [])

    def extract_control_ids(value):
        """Recursively extract control IDs from heterogeneous minimum_controls structures."""
        ids = []
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and "id" in item:
                    if CONTROL_ID_RE.match(item["id"]):
                        ids.append(item["id"])
                elif isinstance(item, str) and CONTROL_ID_RE.match(item):
                    ids.append(item)
                elif isinstance(item, dict):
                    ids.extend(extract_control_ids(list(item.values())))
        elif isinstance(value, dict):
            for v in value.values():
                ids.extend(extract_control_ids(v))
        return ids

    for loop in loops:
        lid = loop.get("id", "?")
        mc = loop.get("minimum_controls", [])
        ctrl_ids = extract_control_ids(mc)
        if not ctrl_ids:
            checker.warn(f"Feedback loop {lid}: no resolvable control IDs in minimum_controls")
            continue
        for cid in ctrl_ids:
            if cid in registry_ids:
                checker.ok(f"Feedback loop {lid}: control {cid} exists")
            else:
                checker.fail(f"Feedback loop {lid}: control {cid} not in registry")

    checker.ok(f"Checked {len(loops)} feedback loop paths")

# ── section 7: stage structure ────────────────────────────────────────────────

def check_stage_structure(checker) -> None:
    checker.section("7/7  Stage directory structure — README + process.md presence")

    for stage_num in range(1, 7):
        stage_dirs = sorted(STAGES_DIR.glob(f"0{stage_num}-*"))
        if not stage_dirs:
            checker.fail(f"Stage {stage_num}: directory not found in stages/")
            continue
        stage_dir = stage_dirs[0]

        readme  = stage_dir / "README.md"
        process = stage_dir / "process.md"

        if readme.exists():
            checker.ok(f"Stage {stage_num} ({stage_dir.name}): README.md present")
        else:
            checker.fail(f"Stage {stage_num} ({stage_dir.name}): README.md missing")

        if process.exists():
            checker.ok(f"Stage {stage_num} ({stage_dir.name}): process.md present")
        else:
            checker.fail(f"Stage {stage_num} ({stage_dir.name}): process.md missing")

        # Artifact output directory
        artifacts_dir = stage_dir / "artifacts" / "outputs"
        if artifacts_dir.exists():
            n = len(list(artifacts_dir.glob("*.yaml")))
            checker.ok(f"Stage {stage_num} ({stage_dir.name}): {n} artifact template(s) in artifacts/outputs/")
        else:
            checker.warn(f"Stage {stage_num} ({stage_dir.name}): no artifacts/outputs/ directory")

# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="A-SDLC Framework Self-Audit — validates schemas and cross-references"
    )
    parser.add_argument(
        "--no-schema", action="store_true",
        help="Skip JSON Schema validation (cross-reference checks still run)"
    )
    parser.add_argument(
        "--no-xref", action="store_true",
        help="Skip cross-reference checks (schema validation still runs)"
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Only print failures and warnings (suppress passing checks)"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  A-SDLC Framework Self-Audit")
    print(f"  Repository: {REPO}")
    print("=" * 60)

    if not HAS_JSONSCHEMA and not args.no_schema:
        print("\n  WARNING: jsonschema not installed — schema validation skipped.")
        print("           Install: pip install -r scripts/requirements.txt\n")

    checker = Checker(quiet=args.quiet)

    # Always run: control files and registry (needed for xref)
    control_ids  = check_control_files(checker)
    registry_ids = check_registry(checker, control_ids)

    if not args.no_schema:
        check_directive_files(checker)
        check_stage_files(checker, registry_ids)

    if not args.no_xref:
        check_control_dependencies(checker, registry_ids)
        check_feedback_loops(checker, registry_ids)

    check_stage_structure(checker)

    print(f"\n{'=' * 60}")
    print(f"  Passed   : {checker.passed}")
    print(f"  Failed   : {checker.failed}")
    print(f"  Warnings : {checker.warnings}")
    print(f"{'=' * 60}")

    if checker.failed:
        print("\n  AUDIT FAILED — resolve failures before committing.\n")
        sys.exit(1)
    elif checker.warnings:
        print("\n  AUDIT PASSED with warnings.\n")
        sys.exit(0)
    else:
        print("\n  AUDIT PASSED.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
