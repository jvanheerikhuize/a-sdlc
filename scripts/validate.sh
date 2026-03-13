#!/usr/bin/env bash
# =============================================================================
# A-SDLC Framework Self-Audit (bash port of scripts/validate.py)
# =============================================================================
# Validates control files, registry, stage files, directive files, control
# dependency chains, feedback loops, and stage directory structure.
#
# Usage:
#   bash scripts/validate.sh              # full audit
#   bash scripts/validate.sh --no-schema  # no-op (schema checks dropped in bash port)
#   bash scripts/validate.sh --no-xref   # skip cross-reference checks
#   bash scripts/validate.sh --quiet     # only show failures and warnings
#
# Note: JSON Schema validation is not available in this bash port.
#   The --no-schema flag is accepted but is a no-op (schema validation is
#   already omitted). Use scripts/validate.py for full schema validation.
#
# Requirements: python3 (pyyaml), jq
# =============================================================================

set -euo pipefail

# ── dependency check ──────────────────────────────────────────────────────────

if ! command -v jq &>/dev/null; then
    echo "ERROR: jq is not installed. Please install jq and retry." >&2
    exit 2
fi

if ! python3 -c "import yaml" &>/dev/null 2>&1; then
    echo "ERROR: pyyaml not installed." >&2
    echo "       Run: pip install -r scripts/requirements.txt" >&2
    exit 2
fi

# ── YAML-to-JSON helper ───────────────────────────────────────────────────────
# All YAML parsing goes through Python (yaml) → JSON → jq.
# Never call yq; it is not available.

yaml2json() {
    # Usage: yaml2json <file.yaml>
    python3 -c "import yaml,json,sys; print(json.dumps(yaml.safe_load(sys.stdin) or {}))" < "$1"
}

# ── REPO root discovery ───────────────────────────────────────────────────────
# Walk up from the script's own directory until we find a directory that
# contains asdlc.yaml. Works whether the script is run from the repo root,
# scripts/, or any subdirectory.

find_repo_root() {
    local dir
    dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    while [[ "$dir" != "/" ]]; do
        if [[ -f "$dir/asdlc.yaml" ]]; then
            echo "$dir"
            return 0
        fi
        dir="$(dirname "$dir")"
    done
    echo "ERROR: Cannot find repo root (no asdlc.yaml found in parent directories)" >&2
    exit 2
}

REPO="$(find_repo_root)"
CONTROLS_DIR="$REPO/controls"
STAGES_DIR="$REPO/stages"
DIRECTIVES_DIR="$REPO/directives"
REGISTRY_FILE="$CONTROLS_DIR/registry.yaml"
FEEDBACK_DIR="$REPO/feedbackloops"
FEEDBACK_FILE="$FEEDBACK_DIR/feedback-loops.yaml"

CONTROL_ID_PATTERN='^(QC|RC|SC|AC|GC)-[0-9]{2}$'

# ── argument parsing ──────────────────────────────────────────────────────────

OPT_QUIET=false
OPT_NO_XREF=false
OPT_NO_SCHEMA=false   # accepted but no-op

for arg in "$@"; do
    case "$arg" in
        --quiet)     OPT_QUIET=true ;;
        --no-xref)   OPT_NO_XREF=true ;;
        --no-schema) OPT_NO_SCHEMA=true ;;
        --help|-h)
            sed -n '/^# Usage:/,/^#$/p' "$0" | sed 's/^# \?//'
            exit 0
            ;;
        *)
            echo "ERROR: Unknown argument: $arg" >&2
            echo "       Run with --help for usage." >&2
            exit 2
            ;;
    esac
done

# ── result tracking ───────────────────────────────────────────────────────────

PASSED=0
FAILED=0
WARNINGS=0

section() {
    printf "\n%s\n" "$(printf '─%.0s' {1..60})"
    printf "  %s\n" "$1"
    printf "%s\n"   "$(printf '─%.0s' {1..60})"
}

ok() {
    PASSED=$(( PASSED + 1 ))
    if [[ "$OPT_QUIET" == false ]]; then
        printf "  \u2713  %s\n" "$1"
    fi
}

fail() {
    FAILED=$(( FAILED + 1 ))
    printf "  \u2717  %s\n" "$1"
}

warn() {
    WARNINGS=$(( WARNINGS + 1 ))
    printf "  \u26a0  %s\n" "$1"
}

# Compute path relative to REPO for display
rel() {
    # Strip leading REPO/ prefix if present
    local p="$1"
    if [[ "$p" == "$REPO/"* ]]; then
        echo "${p#$REPO/}"
    else
        echo "$p"
    fi
}

# ── section 1: control files ──────────────────────────────────────────────────

check_control_files() {
    section "1/7  Control files — schema + filename alignment"

    # Collect all YAML files in controls/*/ (one level deep)
    local control_files=()
    while IFS= read -r -d '' f; do
        control_files+=("$f")
    done < <(find "$CONTROLS_DIR" -mindepth 2 -maxdepth 2 -name "*.yaml" -print0 | sort -z)

    if [[ ${#control_files[@]} -eq 0 ]]; then
        fail "No control files found in controls/*/"
        FOUND_CONTROL_IDS=()
        return
    fi

    local found_ids=()
    for path in "${control_files[@]}"; do
        local json stem cid
        json="$(yaml2json "$path")"
        stem="$(basename "$path" .yaml)"
        cid="$(printf '%s' "$json" | jq -r '.id // ""')"

        if [[ "$cid" != "$stem" ]]; then
            fail "$(rel "$path") — id '$cid' does not match filename '$stem'"
        else
            ok "$(rel "$path") — id matches filename"
        fi

        if ! echo "$cid" | grep -qE "$CONTROL_ID_PATTERN"; then
            fail "$(rel "$path") — id '$cid' does not match pattern [Track]-NN"
        fi

        found_ids+=("$cid")
    done

    ok "Found ${#found_ids[@]} control files"

    # Export to caller via global
    FOUND_CONTROL_IDS=("${found_ids[@]+"${found_ids[@]}"}")
}

# ── section 2: registry ───────────────────────────────────────────────────────

check_registry() {
    section "2/7  Registry — completeness + file existence"

    if [[ ! -f "$REGISTRY_FILE" ]]; then
        fail "controls/registry.yaml not found"
        REGISTRY_IDS=()
        return
    fi

    local json
    json="$(yaml2json "$REGISTRY_FILE")"

    local n_entries
    n_entries="$(printf '%s' "$json" | jq '.registry | length')"

    local registry_ids=()
    local seen_ids=()

    for (( i=0; i<n_entries; i++ )); do
        local entry eid file_path dp
        entry="$(printf '%s' "$json" | jq --argjson idx "$i" '.registry[$idx]')"
        eid="$(printf '%s' "$entry" | jq -r '.id // ""')"

        # Duplicate check
        local is_dup=false
        for sid in "${seen_ids[@]+"${seen_ids[@]}"}"; do
            if [[ "$sid" == "$eid" ]]; then is_dup=true; break; fi
        done
        if [[ "$is_dup" == true ]]; then
            fail "Duplicate ID in registry: $eid"
        fi
        seen_ids+=("$eid")
        registry_ids+=("$eid")

        # Control file exists
        file_path="$(printf '%s' "$entry" | jq -r '.file // ""')"
        if [[ -n "$file_path" && -f "$REPO/$file_path" ]]; then
            ok "$eid: control file exists"
        else
            fail "$eid: control file not found — $file_path"
        fi

        # Single directive_payload (optional)
        dp="$(printf '%s' "$entry" | jq -r '.directive_payload // ""')"
        if [[ -n "$dp" ]]; then
            if [[ -f "$REPO/$dp" ]]; then
                ok "$eid: directive_payload exists"
            else
                fail "$eid: directive_payload not found — $dp"
            fi
        fi

        # Array directive_payloads (optional)
        local n_dps
        n_dps="$(printf '%s' "$entry" | jq '(.directive_payloads // []) | length')"
        for (( j=0; j<n_dps; j++ )); do
            local dp_item
            dp_item="$(printf '%s' "$entry" | jq -r --argjson jj "$j" '.directive_payloads[$jj]')"
            if [[ -f "$REPO/$dp_item" ]]; then
                ok "$eid: directive_payload exists — $dp_item"
            else
                fail "$eid: directive_payload not found — $dp_item"
            fi
        done
    done

    # Every control file → in registry
    for cid in "${FOUND_CONTROL_IDS[@]+"${FOUND_CONTROL_IDS[@]}"}"; do
        local in_reg=false
        for rid in "${registry_ids[@]+"${registry_ids[@]}"}"; do
            if [[ "$rid" == "$cid" ]]; then in_reg=true; break; fi
        done
        if [[ "$in_reg" == true ]]; then
            ok "Control $cid present in registry"
        else
            fail "Control $cid found in controls/ but missing from registry"
        fi
    done

    # Every registry entry → control file exists
    for rid in "${registry_ids[@]+"${registry_ids[@]}"}"; do
        local in_found=false
        for cid in "${FOUND_CONTROL_IDS[@]+"${FOUND_CONTROL_IDS[@]}"}"; do
            if [[ "$cid" == "$rid" ]]; then in_found=true; break; fi
        done
        if [[ "$in_found" == false ]]; then
            fail "Registry entry $rid has no matching file in controls/"
        fi
    done

    ok "Registry: ${#registry_ids[@]} entries"

    REGISTRY_IDS=("${registry_ids[@]+"${registry_ids[@]}"}")
}

# ── section 3: stage files ────────────────────────────────────────────────────

check_stage_files() {
    section "3/7  Stage files — schema + control + artifact references"

    # Collect stage YAML files matching 0[1-6]-*.yaml inside stages/*/
    local stage_files=()
    while IFS= read -r -d '' f; do
        stage_files+=("$f")
    done < <(find "$STAGES_DIR" -mindepth 2 -maxdepth 2 -name "0[1-6]-*.yaml" -print0 | sort -z)

    if [[ ${#stage_files[@]} -eq 0 ]]; then
        fail "No stage YAML files found in stages/*/"
        return
    fi

    for path in "${stage_files[@]}"; do
        local json stage_dir
        json="$(yaml2json "$path")"
        stage_dir="$(dirname "$path")"

        # process.md: use data.process field or default "process.md"
        local proc_ref proc_path
        proc_ref="$(printf '%s' "$json" | jq -r '.process // "process.md"')"
        proc_path="$stage_dir/$proc_ref"
        if [[ -f "$proc_path" ]]; then
            ok "$(rel "$path"): process.md exists"
        else
            fail "$(rel "$path"): process.md not found — $(rel "$proc_path")"
        fi

        # required_controls — each entry may be a string or object with .id
        local n_ctrls
        n_ctrls="$(printf '%s' "$json" | jq '(.required_controls // []) | length')"
        for (( i=0; i<n_ctrls; i++ )); do
            local ctrl_json cid
            ctrl_json="$(printf '%s' "$json" | jq --argjson idx "$i" '.required_controls[$idx]')"
            # If it's an object with .id, use that; otherwise treat as string
            cid="$(printf '%s' "$ctrl_json" | jq -r 'if type == "object" then .id else . end')"

            local in_reg=false
            for rid in "${REGISTRY_IDS[@]+"${REGISTRY_IDS[@]}"}"; do
                if [[ "$rid" == "$cid" ]]; then in_reg=true; break; fi
            done
            if [[ "$in_reg" == true ]]; then
                ok "$(rel "$path"): required control $cid in registry"
            else
                fail "$(rel "$path"): required control $cid not found in registry"
            fi
        done

        # Artifact paths — resolve relative to stage directory
        for section_name in inputs outputs; do
            local n_artifacts
            n_artifacts="$(printf '%s' "$json" | jq --arg s "$section_name" '(.artifacts[$s] // []) | length')"
            for (( i=0; i<n_artifacts; i++ )); do
                local apath full_apath
                apath="$(printf '%s' "$json" | jq -r --arg s "$section_name" --argjson idx "$i" '.artifacts[$s][$idx]')"
                full_apath="$stage_dir/$apath"
                if [[ -e "$full_apath" ]]; then
                    ok "$(rel "$path"): artifact $section_name exists — $apath"
                else
                    warn "$(rel "$path"): artifact template not found — $apath"
                fi
            done
        done

        # Directive paths — relative to REPO root
        local n_directives
        n_directives="$(printf '%s' "$json" | jq '(.directives // []) | length')"
        for (( i=0; i<n_directives; i++ )); do
            local dpath
            dpath="$(printf '%s' "$json" | jq -r --argjson idx "$i" '.directives[$idx]')"
            if [[ -f "$REPO/$dpath" ]]; then
                ok "$(rel "$path"): directive exists — $dpath"
            else
                fail "$(rel "$path"): directive not found — $dpath"
            fi
        done
    done

    ok "Checked ${#stage_files[@]} stage files"
}

# ── section 4: directive files ────────────────────────────────────────────────

check_directive_files() {
    section "4/7  Directive files — schema validation"

    local directive_files=()
    while IFS= read -r -d '' f; do
        directive_files+=("$f")
    done < <(find "$DIRECTIVES_DIR/core" "$DIRECTIVES_DIR/stages" \
                  -maxdepth 1 -name "*.yaml" -print0 2>/dev/null | sort -z)

    if [[ ${#directive_files[@]} -eq 0 ]]; then
        fail "No directive files found in directives/"
        return
    fi

    # JSON Schema validation is dropped in this bash port.
    # We confirm each file is valid YAML (parseable) and exists.
    for path in "${directive_files[@]}"; do
        if yaml2json "$path" &>/dev/null; then
            ok "$(rel "$path") — parseable YAML"
        else
            fail "$(rel "$path") — failed to parse as YAML"
        fi
    done

    ok "Checked ${#directive_files[@]} directive files"
}

# ── section 5: control dependency chains ─────────────────────────────────────

check_control_dependencies() {
    section "5/7  Control dependency chains"

    # Build arrays: GRAPH_NODES and GRAPH_DEPS_<idx> for cycle detection
    # We use a flat representation: node_ids array + deps_<i> arrays
    local node_ids=()
    declare -A node_deps  # node_deps[cid]="dep1 dep2 ..."  (space-separated)

    local control_files=()
    while IFS= read -r -d '' f; do
        control_files+=("$f")
    done < <(find "$CONTROLS_DIR" -mindepth 2 -maxdepth 2 -name "*.yaml" -print0 | sort -z)

    for path in "${control_files[@]}"; do
        local json cid
        json="$(yaml2json "$path")"
        cid="$(printf '%s' "$json" | jq -r '.id // ""')"
        [[ -z "$cid" ]] && cid="$(basename "$path" .yaml)"

        node_ids+=("$cid")

        local n_deps
        n_deps="$(printf '%s' "$json" | jq '(.dependencies // []) | length')"
        local deps_str=""
        for (( i=0; i<n_deps; i++ )); do
            local dep
            dep="$(printf '%s' "$json" | jq -r --argjson idx "$i" '.dependencies[$idx]')"

            # Check dep exists in registry
            local in_reg=false
            for rid in "${REGISTRY_IDS[@]+"${REGISTRY_IDS[@]}"}"; do
                if [[ "$rid" == "$dep" ]]; then in_reg=true; break; fi
            done
            if [[ "$in_reg" == true ]]; then
                ok "$cid → dependency $dep exists"
            else
                fail "$cid → dependency $dep not found in registry"
            fi

            deps_str+="$dep "
        done
        node_deps["$cid"]="${deps_str% }"
    done

    # Cycle detection: iterative DFS using bash arrays as stacks
    # visited: space-separated string of visited node IDs
    # rec_stack: the current recursion path

    local cycle_found=false

    # visited_set: nodes fully processed across all DFS trees (global across trees)
    declare -A visited_set=()

    # Iterative DFS with ENTER/EXIT state markers to simulate the recursion stack.
    # has_cycle_dfs sets cycle_found=true (outer variable) if a back-edge is found.
    has_cycle_dfs() {
        local start="$1"

        # rec_set tracks nodes currently on the active recursion path for this tree
        declare -A rec_set=()

        # Each entry on node_stack/state_stack is a paired (node, ENTER|EXIT) frame
        local -a node_stack=("$start")
        local -a state_stack=("ENTER")

        while [[ ${#node_stack[@]} -gt 0 ]]; do
            local current="${node_stack[-1]}"
            local state="${state_stack[-1]}"
            # Pop both stacks together
            unset 'node_stack[-1]'
            unset 'state_stack[-1]'

            if [[ "$state" == "EXIT" ]]; then
                # Backtracking past this node — remove from active recursion path
                unset 'rec_set[$current]'
                continue
            fi

            # ENTER processing
            if [[ -n "${visited_set[$current]+x}" ]]; then
                # Already fully explored in a prior DFS tree — safe to skip.
                # (If it were in rec_set we would have caught it before pushing.)
                continue
            fi

            # Mark node as visited globally and as on the current recursion path
            visited_set["$current"]=1
            rec_set["$current"]=1

            # Push the paired EXIT frame first so it runs after all children
            node_stack+=("$current")
            state_stack+=("EXIT")

            # Push children as ENTER frames
            local deps="${node_deps[$current]:-}"
            for dep in $deps; do
                if [[ -n "${rec_set[$dep]+x}" ]]; then
                    # Back-edge detected → cycle
                    cycle_found=true
                    return 0
                fi
                if [[ -z "${visited_set[$dep]+x}" ]]; then
                    node_stack+=("$dep")
                    state_stack+=("ENTER")
                fi
            done
        done
        return 0
    }

    for node in "${node_ids[@]}"; do
        if [[ -z "${visited_set[$node]+x}" ]]; then
            has_cycle_dfs "$node"
            if [[ "$cycle_found" == true ]]; then
                fail "Circular dependency detected involving $node"
                cycle_found=false
            fi
        fi
    done

    ok "No circular dependencies detected"
}

# ── section 6: feedback loops ─────────────────────────────────────────────────

# Recursively extract control IDs (matching CONTROL_ID_PATTERN) from a JSON
# value. Mirrors the Python extract_control_ids() function.
# Usage: extract_control_ids_from_json <json_string>
# Outputs one ID per line.
extract_control_ids_from_json() {
    local json_value="$1"
    # Use Python for the recursive extraction — it's the cleanest approach
    # for heterogeneous nested structures (arrays of objects, dicts of arrays).
    python3 - "$json_value" <<'PYEOF'
import sys, json, re

CONTROL_ID_RE = re.compile(r'^(QC|RC|SC|AC|GC)-\d{2}$')

def extract(value):
    ids = []
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict) and 'id' in item:
                if CONTROL_ID_RE.match(str(item['id'])):
                    ids.append(item['id'])
            elif isinstance(item, str) and CONTROL_ID_RE.match(item):
                ids.append(item)
            elif isinstance(item, dict):
                ids.extend(extract(list(item.values())))
    elif isinstance(value, dict):
        for v in value.values():
            ids.extend(extract(v))
    return ids

data = json.loads(sys.argv[1])
for cid in extract(data):
    print(cid)
PYEOF
}

check_feedback_loops() {
    section "6/7  Feedback loops — structure + control reference validation"

    if [[ ! -f "$FEEDBACK_FILE" ]]; then
        fail "Feedback loops file not found: $(rel "$FEEDBACK_FILE")"
        return
    fi

    # Required structural files
    for required_file in process.md README.md; do
        local p="$FEEDBACK_DIR/$required_file"
        if [[ -f "$p" ]]; then
            ok "feedbackloops/$required_file present"
        else
            fail "feedbackloops/$required_file missing"
        fi
    done

    # Artifact outputs directory
    local artifacts_out="$FEEDBACK_DIR/artifacts/outputs"
    if [[ -d "$artifacts_out" ]]; then
        local n_templates
        n_templates="$(find "$artifacts_out" -maxdepth 1 -name "*.yaml" | wc -l | tr -d ' ')"
        ok "feedbackloops/artifacts/outputs/ present ($n_templates templates)"
    else
        fail "feedbackloops/artifacts/outputs/ directory missing"
    fi

    # Autofix templates directory (warn only if missing)
    local autofix_dir="$FEEDBACK_DIR/autofix-templates"
    if [[ -d "$autofix_dir" ]]; then
        local n_autofix
        n_autofix="$(find "$autofix_dir" -maxdepth 1 -name "*.yaml" | wc -l | tr -d ' ')"
        ok "feedbackloops/autofix-templates/ present ($n_autofix template(s))"
    else
        warn "feedbackloops/autofix-templates/ directory not yet created"
    fi

    local json
    json="$(yaml2json "$FEEDBACK_FILE")"

    # process ref declared in the YAML header
    local process_ref
    process_ref="$(printf '%s' "$json" | jq -r '.process // ""')"
    if [[ -n "$process_ref" ]]; then
        local p="$FEEDBACK_DIR/$process_ref"
        if [[ -f "$p" ]]; then
            ok "feedback-loops.yaml: process ref resolves — $process_ref"
        else
            fail "feedback-loops.yaml: process ref not found — $process_ref"
        fi
    fi

    # Artifact output refs declared in the YAML header
    local n_art_outputs
    n_art_outputs="$(printf '%s' "$json" | jq '(.artifacts.outputs // []) | length')"
    for (( i=0; i<n_art_outputs; i++ )); do
        local art_path
        art_path="$(printf '%s' "$json" | jq -r --argjson idx "$i" '.artifacts.outputs[$idx]')"
        local p="$FEEDBACK_DIR/$art_path"
        if [[ -f "$p" ]]; then
            ok "feedback-loops.yaml: artifact ref resolves — $art_path"
        else
            warn "feedback-loops.yaml: artifact ref not found — $art_path"
        fi
    done

    # feedback_loops array — validate minimum_controls control IDs
    local n_loops
    n_loops="$(printf '%s' "$json" | jq '(.feedback_loops // []) | length')"
    for (( i=0; i<n_loops; i++ )); do
        local loop_json lid mc_json
        loop_json="$(printf '%s' "$json" | jq --argjson idx "$i" '.feedback_loops[$idx]')"
        lid="$(printf '%s' "$loop_json" | jq -r '.id // "?"')"
        mc_json="$(printf '%s' "$loop_json" | jq '.minimum_controls // []')"

        local ctrl_ids=()
        while IFS= read -r cid_line; do
            [[ -n "$cid_line" ]] && ctrl_ids+=("$cid_line")
        done < <(extract_control_ids_from_json "$mc_json")

        if [[ ${#ctrl_ids[@]} -eq 0 ]]; then
            warn "Feedback loop $lid: no resolvable control IDs in minimum_controls"
            continue
        fi

        for cid in "${ctrl_ids[@]}"; do
            local in_reg=false
            for rid in "${REGISTRY_IDS[@]+"${REGISTRY_IDS[@]}"}"; do
                if [[ "$rid" == "$cid" ]]; then in_reg=true; break; fi
            done
            if [[ "$in_reg" == true ]]; then
                ok "Feedback loop $lid: control $cid exists"
            else
                fail "Feedback loop $lid: control $cid not in registry"
            fi
        done
    done

    ok "Checked $n_loops feedback loop paths"
}

# ── section 7: stage directory structure ──────────────────────────────────────

check_stage_structure() {
    section "7/7  Stage directory structure — README + process.md presence"

    for stage_num in 1 2 3 4 5 6; do
        # Find the stage directory matching 0N-*
        local stage_dir=""
        while IFS= read -r -d '' d; do
            stage_dir="$d"
            break
        done < <(find "$STAGES_DIR" -mindepth 1 -maxdepth 1 -type d \
                      -name "0${stage_num}-*" -print0 | sort -z)

        if [[ -z "$stage_dir" ]]; then
            fail "Stage $stage_num: directory not found in stages/"
            continue
        fi

        local dir_name
        dir_name="$(basename "$stage_dir")"

        local readme="$stage_dir/README.md"
        local process="$stage_dir/process.md"

        if [[ -f "$readme" ]]; then
            ok "Stage $stage_num ($dir_name): README.md present"
        else
            fail "Stage $stage_num ($dir_name): README.md missing"
        fi

        if [[ -f "$process" ]]; then
            ok "Stage $stage_num ($dir_name): process.md present"
        else
            fail "Stage $stage_num ($dir_name): process.md missing"
        fi

        local artifacts_dir="$stage_dir/artifacts/outputs"
        if [[ -d "$artifacts_dir" ]]; then
            local n_templates
            n_templates="$(find "$artifacts_dir" -maxdepth 1 -name "*.yaml" | wc -l | tr -d ' ')"
            ok "Stage $stage_num ($dir_name): $n_templates artifact template(s) in artifacts/outputs/"
        else
            warn "Stage $stage_num ($dir_name): no artifacts/outputs/ directory"
        fi
    done
}

# ── main ──────────────────────────────────────────────────────────────────────

printf "%s\n" "$(printf '=%.0s' {1..60})"
printf "  A-SDLC Framework Self-Audit\n"
printf "  Repository: %s\n" "$REPO"
printf "%s\n" "$(printf '=%.0s' {1..60})"

if [[ "$OPT_NO_SCHEMA" == true ]]; then
    printf "\n  NOTE: --no-schema is a no-op in this bash port.\n"
    printf "        JSON Schema validation is not available here.\n"
    printf "        Use scripts/validate.py for full schema validation.\n\n"
fi

# Globals used to pass data between sections
FOUND_CONTROL_IDS=()
REGISTRY_IDS=()

# Section 1 & 2 always run (required for xref)
check_control_files
check_registry

# Section 3 & 4: schema-related sections (always run in bash port — schema
# validation itself is dropped, but file existence / reference checks remain)
check_directive_files
check_stage_files

# Section 5 & 6: cross-reference checks (skippable via --no-xref)
if [[ "$OPT_NO_XREF" == false ]]; then
    check_control_dependencies
    check_feedback_loops
fi

# Section 7 always runs
check_stage_structure

printf "\n%s\n" "$(printf '=%.0s' {1..60})"
printf "  Passed   : %d\n" "$PASSED"
printf "  Failed   : %d\n" "$FAILED"
printf "  Warnings : %d\n" "$WARNINGS"
printf "%s\n" "$(printf '=%.0s' {1..60})"

if [[ "$FAILED" -gt 0 ]]; then
    printf "\n  AUDIT FAILED — resolve failures before committing.\n\n"
    exit 1
elif [[ "$WARNINGS" -gt 0 ]]; then
    printf "\n  AUDIT PASSED with warnings.\n\n"
    exit 0
else
    printf "\n  AUDIT PASSED.\n\n"
    exit 0
fi
