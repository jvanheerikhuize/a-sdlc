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

# ── color support ─────────────────────────────────────────────────────────────

if [[ -t 1 ]]; then
    C_RED='\033[0;31m'
    C_GREEN='\033[0;32m'
    C_YELLOW='\033[0;33m'
    C_BLUE='\033[0;34m'
    C_CYAN='\033[0;36m'
    C_BOLD='\033[1m'
    C_DIM='\033[2m'
    C_RESET='\033[0m'
else
    C_RED='' C_GREEN='' C_YELLOW='' C_BLUE='' C_CYAN='' C_BOLD='' C_DIM='' C_RESET=''
fi

# ── dependency check ──────────────────────────────────────────────────────────

if ! command -v jq &>/dev/null; then
    printf "${C_RED}ERROR:${C_RESET} jq is not installed. Please install jq and retry.\n" >&2
    exit 2
fi

if ! python3 -c "import yaml" &>/dev/null 2>&1; then
    printf "${C_RED}ERROR:${C_RESET} pyyaml not installed.\n" >&2
    printf "       Run: pip install -r scripts/requirements.txt\n" >&2
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
    printf "${C_RED}ERROR:${C_RESET} Cannot find repo root (no asdlc.yaml found in parent directories)\n" >&2
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
            printf "${C_RED}ERROR:${C_RESET} Unknown argument: %s\n" "$arg" >&2
            printf "       Run with --help for usage.\n" >&2
            exit 2
            ;;
    esac
done

# ── result tracking ───────────────────────────────────────────────────────────

PASSED=0
FAILED=0
WARNINGS=0

# Collect all failures and warnings for the final remediation report
FAIL_MESSAGES=()
WARN_MESSAGES=()
# Also track which section each failure came from
FAIL_SECTIONS=()
WARN_SECTIONS=()

CURRENT_SECTION=""

section() {
    CURRENT_SECTION="$1"
    printf "\n${C_BOLD}${C_BLUE}┌─ %s${C_RESET}\n" "$1"
    printf "${C_BLUE}│${C_RESET}\n"
}

section_end() {
    printf "${C_BLUE}└%s${C_RESET}\n" "$(printf '─%.0s' {1..59})"
}

ok() {
    PASSED=$(( PASSED + 1 ))
    if [[ "$OPT_QUIET" == false ]]; then
        printf "${C_BLUE}│${C_RESET}  ${C_GREEN}✓${C_RESET}  %s\n" "$1"
    fi
}

fail() {
    FAILED=$(( FAILED + 1 ))
    FAIL_MESSAGES+=("$1")
    FAIL_SECTIONS+=("$CURRENT_SECTION")
    printf "${C_BLUE}│${C_RESET}  ${C_RED}✗${C_RESET}  ${C_RED}%s${C_RESET}\n" "$1"
}

warn() {
    WARNINGS=$(( WARNINGS + 1 ))
    WARN_MESSAGES+=("$1")
    WARN_SECTIONS+=("$CURRENT_SECTION")
    printf "${C_BLUE}│${C_RESET}  ${C_YELLOW}⚠${C_RESET}  ${C_YELLOW}%s${C_RESET}\n" "$1"
}

# Compute path relative to REPO for display
rel() {
    local p="$1"
    if [[ "$p" == "$REPO/"* ]]; then
        echo "${p#$REPO/}"
    else
        echo "$p"
    fi
}

# ── remediation lookup ────────────────────────────────────────────────────────
# Maps a failure/warning message to a human-readable remediation hint.

remediation_for() {
    local msg="$1"
    local hint=""

    if [[ "$msg" == *"id '"*"' does not match filename"* ]]; then
        local stem; stem="$(echo "$msg" | grep -oP "filename '\K[^']+")"
        hint="Edit the file and set  id: ${stem}  to match the filename (stem without .yaml)."

    elif [[ "$msg" == *"does not match pattern [Track]-NN"* ]]; then
        hint="Rename the file or update 'id:' to follow the format QC-01, SC-12, etc."

    elif [[ "$msg" == *"process.md not found"* ]]; then
        local path; path="$(echo "$msg" | grep -oP '— \K.+')"
        hint="Create the missing file:  touch ${path}"

    elif [[ "$msg" == *"process.md missing"* ]]; then
        hint="Create a process.md in the indicated stage or feedbackloops directory."

    elif [[ "$msg" == *"README.md missing"* ]]; then
        hint="Create a README.md in the indicated directory describing its purpose."

    elif [[ "$msg" == *"control file not found"* ]]; then
        local fp; fp="$(echo "$msg" | grep -oP '— \K.+')"
        hint="Create the missing control file at: ${fp}  or remove the entry from controls/registry.yaml."

    elif [[ "$msg" == *"missing from registry"* ]]; then
        local cid; cid="$(echo "$msg" | grep -oP 'Control \K[^ ]+')"
        hint="Add  ${cid}  to controls/registry.yaml with its 'file:' path."

    elif [[ "$msg" == *"has no matching file in controls/"* ]]; then
        local rid; rid="$(echo "$msg" | grep -oP 'Registry entry \K[^ ]+')"
        hint="Create the control file for  ${rid}  or remove the entry from registry.yaml."

    elif [[ "$msg" == *"Duplicate ID in registry"* ]]; then
        local dup; dup="$(echo "$msg" | grep -oP 'registry: \K.+')"
        hint="Remove the duplicate entry for  ${dup}  from controls/registry.yaml."

    elif [[ "$msg" == *"directive_payload not found"* ]]; then
        local dp; dp="$(echo "$msg" | grep -oP '— \K.+')"
        hint="Create the missing directive file at: ${dp}  or correct the path in registry.yaml."

    elif [[ "$msg" == *"directive not found"* ]]; then
        local dp; dp="$(echo "$msg" | grep -oP '— \K.+')"
        hint="Create the missing directive file at: ${dp}  or correct the path in the stage YAML."

    elif [[ "$msg" == *"required control"*"not found in registry"* ]]; then
        local cid; cid="$(echo "$msg" | grep -oP 'required control \K[^ ]+')"
        hint="Add  ${cid}  to controls/registry.yaml, or remove the reference from the stage YAML."

    elif [[ "$msg" == *"dependency"*"not found in registry"* ]]; then
        local dep; dep="$(echo "$msg" | grep -oP 'dependency \K[^ ]+')"
        hint="Add  ${dep}  to controls/registry.yaml, or remove it from the 'dependencies:' list."

    elif [[ "$msg" == *"Circular dependency"* ]]; then
        hint="Remove or reorder the dependency to break the cycle. Use a DAG visualizer to identify the loop."

    elif [[ "$msg" == *"artifact ref not found"* ]]; then
        local ap; ap="$(echo "$msg" | grep -oP '— \K.+')"
        hint="Create the missing artifact file at:  feedbackloops/${ap}"

    elif [[ "$msg" == *"artifact template not found"* ]]; then
        local ap; ap="$(echo "$msg" | grep -oP '— \K.+')"
        hint="Create the missing artifact template (can be an empty YAML stub):  touch <stage-dir>/${ap}"

    elif [[ "$msg" == *"artifacts/outputs/ directory missing"* || "$msg" == *"no artifacts/outputs/"* ]]; then
        hint="Run:  mkdir -p <stage-dir>/artifacts/outputs/"

    elif [[ "$msg" == *"Feedback loop"*"not in registry"* ]]; then
        local cid; cid="$(echo "$msg" | grep -oP 'control \K[^ ]+')"
        hint="Add  ${cid}  to controls/registry.yaml, or correct the ID in feedback-loops.yaml."

    elif [[ "$msg" == *"no resolvable control IDs in minimum_controls"* ]]; then
        hint="Add valid control IDs (e.g. QC-01) to the 'minimum_controls:' list in feedback-loops.yaml."

    elif [[ "$msg" == *"autofix-templates/"* ]]; then
        hint="Run:  mkdir -p feedbackloops/autofix-templates/"

    elif [[ "$msg" == *"No control files found"* ]]; then
        hint="Ensure controls/ has subdirectories (qc/, sc/, etc.) each containing [ID].yaml files."

    elif [[ "$msg" == *"No stage YAML files found"* ]]; then
        hint="Ensure stages/ has subdirectories like 01-intent-ingestion/ each with a matching YAML."

    elif [[ "$msg" == *"No directive files found"* ]]; then
        hint="Ensure directives/core/ and directives/stages/ contain *.yaml files."

    elif [[ "$msg" == *"Stage"*"directory not found"* ]]; then
        hint="Create the missing stage directory under stages/ named  0N-<stage-slug>/."

    else
        hint="Inspect the file path in the message above and correct the structural issue."
    fi

    echo "$hint"
}

# ── section 1: control files ──────────────────────────────────────────────────

check_control_files() {
    section "1/7  Control files — schema + filename alignment"

    local control_files=()
    while IFS= read -r -d '' f; do
        control_files+=("$f")
    done < <(find "$CONTROLS_DIR" -mindepth 2 -maxdepth 2 -name "*.yaml" -print0 | sort -z)

    if [[ ${#control_files[@]} -eq 0 ]]; then
        fail "No control files found in controls/*/"
        FOUND_CONTROL_IDS=()
        section_end
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

    FOUND_CONTROL_IDS=("${found_ids[@]+"${found_ids[@]}"}")
    section_end
}

# ── section 2: registry ───────────────────────────────────────────────────────

check_registry() {
    section "2/7  Registry — completeness + file existence"

    if [[ ! -f "$REGISTRY_FILE" ]]; then
        fail "controls/registry.yaml not found"
        REGISTRY_IDS=()
        section_end
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

        local is_dup=false
        for sid in "${seen_ids[@]+"${seen_ids[@]}"}"; do
            if [[ "$sid" == "$eid" ]]; then is_dup=true; break; fi
        done
        if [[ "$is_dup" == true ]]; then
            fail "Duplicate ID in registry: $eid"
        fi
        seen_ids+=("$eid")
        registry_ids+=("$eid")

        file_path="$(printf '%s' "$entry" | jq -r '.file // ""')"
        if [[ -n "$file_path" && -f "$REPO/$file_path" ]]; then
            ok "$eid: control file exists"
        else
            fail "$eid: control file not found — $file_path"
        fi

        dp="$(printf '%s' "$entry" | jq -r '.directive_payload // ""')"
        if [[ -n "$dp" ]]; then
            if [[ -f "$REPO/$dp" ]]; then
                ok "$eid: directive_payload exists"
            else
                fail "$eid: directive_payload not found — $dp"
            fi
        fi

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
    section_end
}

# ── section 3: stage files ────────────────────────────────────────────────────

check_stage_files() {
    section "3/7  Stage files — schema + control + artifact references"

    local stage_files=()
    while IFS= read -r -d '' f; do
        stage_files+=("$f")
    done < <(find "$STAGES_DIR" -mindepth 2 -maxdepth 2 -name "0[1-6]-*.yaml" -print0 | sort -z)

    if [[ ${#stage_files[@]} -eq 0 ]]; then
        fail "No stage YAML files found in stages/*/"
        section_end
        return
    fi

    for path in "${stage_files[@]}"; do
        local json stage_dir
        json="$(yaml2json "$path")"
        stage_dir="$(dirname "$path")"

        local proc_ref proc_path
        proc_ref="$(printf '%s' "$json" | jq -r '.process // "process.md"')"
        proc_path="$stage_dir/$proc_ref"
        if [[ -f "$proc_path" ]]; then
            ok "$(rel "$path"): process.md exists"
        else
            fail "$(rel "$path"): process.md not found — $(rel "$proc_path")"
        fi

        local n_ctrls
        n_ctrls="$(printf '%s' "$json" | jq '(.required_controls // []) | length')"
        for (( i=0; i<n_ctrls; i++ )); do
            local ctrl_json cid
            ctrl_json="$(printf '%s' "$json" | jq --argjson idx "$i" '.required_controls[$idx]')"
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
    section_end
}

# ── section 4: directive files ────────────────────────────────────────────────

check_directive_files() {
    section "4/7  Directive files — parse validation"

    local directive_files=()
    while IFS= read -r -d '' f; do
        directive_files+=("$f")
    done < <(find "$DIRECTIVES_DIR/core" "$DIRECTIVES_DIR/stages" \
                  -maxdepth 1 -name "*.yaml" -print0 2>/dev/null | sort -z)

    if [[ ${#directive_files[@]} -eq 0 ]]; then
        fail "No directive files found in directives/"
        section_end
        return
    fi

    for path in "${directive_files[@]}"; do
        if yaml2json "$path" &>/dev/null; then
            ok "$(rel "$path") — parseable YAML"
        else
            fail "$(rel "$path") — failed to parse as YAML"
        fi
    done

    ok "Checked ${#directive_files[@]} directive files"
    section_end
}

# ── section 5: control dependency chains ─────────────────────────────────────

check_control_dependencies() {
    section "5/7  Control dependency chains"

    local node_ids=()
    declare -A node_deps

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

    local cycle_found=false
    declare -A visited_set=()

    has_cycle_dfs() {
        local start="$1"
        declare -A rec_set=()
        local -a node_stack=("$start")
        local -a state_stack=("ENTER")

        while [[ ${#node_stack[@]} -gt 0 ]]; do
            local current="${node_stack[-1]}"
            local state="${state_stack[-1]}"
            unset 'node_stack[-1]'
            unset 'state_stack[-1]'

            if [[ "$state" == "EXIT" ]]; then
                unset 'rec_set[$current]'
                continue
            fi

            if [[ -n "${visited_set[$current]+x}" ]]; then
                continue
            fi

            visited_set["$current"]=1
            rec_set["$current"]=1

            node_stack+=("$current")
            state_stack+=("EXIT")

            local deps="${node_deps[$current]:-}"
            for dep in $deps; do
                if [[ -n "${rec_set[$dep]+x}" ]]; then
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
    section_end
}

# ── section 6: feedback loops ─────────────────────────────────────────────────

extract_control_ids_from_json() {
    local json_value="$1"
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
        section_end
        return
    fi

    for required_file in process.md README.md; do
        local p="$FEEDBACK_DIR/$required_file"
        if [[ -f "$p" ]]; then
            ok "feedbackloops/$required_file present"
        else
            fail "feedbackloops/$required_file missing"
        fi
    done

    local artifacts_out="$FEEDBACK_DIR/artifacts/outputs"
    if [[ -d "$artifacts_out" ]]; then
        local n_templates
        n_templates="$(find "$artifacts_out" -maxdepth 1 -name "*.yaml" | wc -l | tr -d ' ')"
        ok "feedbackloops/artifacts/outputs/ present ($n_templates templates)"
    else
        fail "feedbackloops/artifacts/outputs/ directory missing"
    fi

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
    section_end
}

# ── section 7: stage directory structure ──────────────────────────────────────

check_stage_structure() {
    section "7/7  Stage directory structure — README + process.md presence"

    for stage_num in 1 2 3 4 5 6; do
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

    section_end
}

# ── main ──────────────────────────────────────────────────────────────────────

# Header
printf "\n${C_BOLD}╔%s╗${C_RESET}\n" "$(printf '═%.0s' {1..60})"
printf "${C_BOLD}║  %-58s║${C_RESET}\n" "A-SDLC Framework Self-Audit"
printf "${C_BOLD}║  %-58s║${C_RESET}\n" "$(date '+%Y-%m-%d %H:%M:%S')"
printf "${C_BOLD}║  %-58s║${C_RESET}\n" "Repo: $(rel "$REPO" 2>/dev/null || echo "$REPO")"
printf "${C_BOLD}╚%s╝${C_RESET}\n" "$(printf '═%.0s' {1..60})"

if [[ "$OPT_NO_SCHEMA" == true ]]; then
    printf "\n  ${C_DIM}NOTE: --no-schema is a no-op in this bash port.${C_RESET}\n"
    printf "  ${C_DIM}      JSON Schema validation requires scripts/validate.py.${C_RESET}\n"
fi

# Globals used to pass data between sections
FOUND_CONTROL_IDS=()
REGISTRY_IDS=()

check_control_files
check_registry
check_stage_files
check_directive_files

if [[ "$OPT_NO_XREF" == false ]]; then
    check_control_dependencies
    check_feedback_loops
fi

check_stage_structure

# ── summary ───────────────────────────────────────────────────────────────────

printf "\n${C_BOLD}%s${C_RESET}\n" "$(printf '═%.0s' {1..62})"
printf "${C_BOLD}  AUDIT SUMMARY${C_RESET}\n"
printf "${C_BOLD}%s${C_RESET}\n" "$(printf '─%.0s' {1..62})"
printf "  ${C_GREEN}✓ Passed   :${C_RESET}  %d\n" "$PASSED"
if [[ "$FAILED" -gt 0 ]]; then
    printf "  ${C_RED}✗ Failed   :${C_RESET}  ${C_BOLD}${C_RED}%d${C_RESET}\n" "$FAILED"
else
    printf "  ${C_GREEN}✗ Failed   :${C_RESET}  %d\n" "$FAILED"
fi
if [[ "$WARNINGS" -gt 0 ]]; then
    printf "  ${C_YELLOW}⚠ Warnings :${C_RESET}  ${C_BOLD}${C_YELLOW}%d${C_RESET}\n" "$WARNINGS"
else
    printf "  ${C_GREEN}⚠ Warnings :${C_RESET}  %d\n" "$WARNINGS"
fi
printf "${C_BOLD}%s${C_RESET}\n" "$(printf '═%.0s' {1..62})"

# ── remediation report ────────────────────────────────────────────────────────

hint=""  # used in report loops (not inside a function, so 'local' not valid)

if [[ "$FAILED" -gt 0 ]]; then
    printf "\n${C_BOLD}${C_RED}┌─ FAILURES  (%d)%s${C_RESET}\n" "$FAILED" "$(printf '─%.0s' {1..44})"
    for (( i=0; i<${#FAIL_MESSAGES[@]}; i++ )); do
        local_msg="${FAIL_MESSAGES[$i]}"
        local_sec="${FAIL_SECTIONS[$i]}"
        hint="$(remediation_for "$local_msg")"
        printf "${C_RED}│${C_RESET}\n"
        printf "${C_RED}│${C_RESET}  ${C_RED}✗${C_RESET}  %s\n" "$local_msg"
        printf "${C_RED}│${C_RESET}     ${C_DIM}Section: %s${C_RESET}\n" "$local_sec"
        printf "${C_RED}│${C_RESET}     ${C_CYAN}Fix:${C_RESET} %s\n" "$hint"
    done
    printf "${C_RED}└%s${C_RESET}\n" "$(printf '─%.0s' {1..59})"
fi

if [[ "$WARNINGS" -gt 0 ]]; then
    printf "\n${C_BOLD}${C_YELLOW}┌─ WARNINGS  (%d)%s${C_RESET}\n" "$WARNINGS" "$(printf '─%.0s' {1..44})"
    for (( i=0; i<${#WARN_MESSAGES[@]}; i++ )); do
        local_msg="${WARN_MESSAGES[$i]}"
        local_sec="${WARN_SECTIONS[$i]}"
        hint="$(remediation_for "$local_msg")"
        printf "${C_YELLOW}│${C_RESET}\n"
        printf "${C_YELLOW}│${C_RESET}  ${C_YELLOW}⚠${C_RESET}  %s\n" "$local_msg"
        printf "${C_YELLOW}│${C_RESET}     ${C_DIM}Section: %s${C_RESET}\n" "$local_sec"
        printf "${C_YELLOW}│${C_RESET}     ${C_CYAN}Fix:${C_RESET} %s\n" "$hint"
    done
    printf "${C_YELLOW}└%s${C_RESET}\n" "$(printf '─%.0s' {1..59})"
fi

# ── agent auto-fix prompt ─────────────────────────────────────────────────────

if [[ "$FAILED" -gt 0 || "$WARNINGS" -gt 0 ]]; then
    printf "\n${C_BOLD}${C_CYAN}┌─ AGENT AUTO-FIX PROMPT%s${C_RESET}\n" "$(printf '─%.0s' {1..37})"
    printf "${C_CYAN}│${C_RESET}\n"
    printf "${C_CYAN}│${C_RESET}  Copy the prompt below and paste it to an agent:\n"
    printf "${C_CYAN}│${C_RESET}\n"
    printf "${C_CYAN}│${C_RESET}  ${C_DIM}─────────────────────────────────────────────────────────${C_RESET}\n"
    printf "${C_CYAN}│${C_RESET}\n"
    printf "${C_CYAN}│${C_RESET}  You are maintaining the A-SDLC governance framework.\n"
    printf "${C_CYAN}│${C_RESET}  Run  bash scripts/validate.sh  and fix ALL failures\n"
    printf "${C_CYAN}│${C_RESET}  and warnings listed in the output.\n"
    printf "${C_CYAN}│${C_RESET}\n"
    printf "${C_CYAN}│${C_RESET}  Current issues to resolve:\n"
    printf "${C_CYAN}│${C_RESET}\n"

    if [[ "$FAILED" -gt 0 ]]; then
        printf "${C_CYAN}│${C_RESET}  FAILURES (%d):\n" "$FAILED"
        for (( i=0; i<${#FAIL_MESSAGES[@]}; i++ )); do
            local_msg="${FAIL_MESSAGES[$i]}"
            hint="$(remediation_for "$local_msg")"
            printf "${C_CYAN}│${C_RESET}    %d. %s\n" "$(( i + 1 ))" "$local_msg"
            printf "${C_CYAN}│${C_RESET}       Suggested fix: %s\n" "$hint"
        done
        printf "${C_CYAN}│${C_RESET}\n"
    fi

    if [[ "$WARNINGS" -gt 0 ]]; then
        printf "${C_CYAN}│${C_RESET}  WARNINGS (%d):\n" "$WARNINGS"
        for (( i=0; i<${#WARN_MESSAGES[@]}; i++ )); do
            local_msg="${WARN_MESSAGES[$i]}"
            hint="$(remediation_for "$local_msg")"
            printf "${C_CYAN}│${C_RESET}    %d. %s\n" "$(( i + 1 ))" "$local_msg"
            printf "${C_CYAN}│${C_RESET}       Suggested fix: %s\n" "$hint"
        done
        printf "${C_CYAN}│${C_RESET}\n"
    fi

    printf "${C_CYAN}│${C_RESET}  Rules:\n"
    printf "${C_CYAN}│${C_RESET}  - Fix failures first (they block the audit).\n"
    printf "${C_CYAN}│${C_RESET}  - Address warnings after (they indicate missing structure).\n"
    printf "${C_CYAN}│${C_RESET}  - After fixing, re-run  bash scripts/validate.sh  to confirm\n"
    printf "${C_CYAN}│${C_RESET}    zero failures and zero warnings.\n"
    printf "${C_CYAN}│${C_RESET}  - Do not modify AGENTS.md, README.md, or context/*.md directly;\n"
    printf "${C_CYAN}│${C_RESET}    those are generated — run  bash scripts/generate-docs.sh  instead.\n"
    printf "${C_CYAN}│${C_RESET}  - Keep control IDs in the format [Track]-NN (e.g. QC-01, SC-12).\n"
    printf "${C_CYAN}│${C_RESET}\n"
    printf "${C_CYAN}│${C_RESET}  ${C_DIM}─────────────────────────────────────────────────────────${C_RESET}\n"
    printf "${C_CYAN}└%s${C_RESET}\n" "$(printf '─%.0s' {1..59})"
fi

# ── exit status ───────────────────────────────────────────────────────────────

if [[ "$FAILED" -gt 0 ]]; then
    printf "\n${C_BOLD}${C_RED}  AUDIT FAILED${C_RESET} — resolve %d failure(s) before committing.\n\n" "$FAILED"
    exit 1
elif [[ "$WARNINGS" -gt 0 ]]; then
    printf "\n${C_BOLD}${C_YELLOW}  AUDIT PASSED${C_RESET} with %d warning(s).\n\n" "$WARNINGS"
    exit 0
else
    printf "\n${C_BOLD}${C_GREEN}  AUDIT PASSED${C_RESET} — all checks clean.\n\n"
    exit 0
fi
