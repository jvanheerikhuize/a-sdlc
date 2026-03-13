#!/usr/bin/env bash
# =============================================================================
# generate-diagram.sh
# Generate the A-SDLC framework diagram from YAML source-of-truth files.
#
# Reads:
#   asdlc.yaml                          (stages, controls, control_tracks, cross_cutting)
#   feedbackloops/feedback-loops.yaml   (feedback loop paths)
#
# Outputs:
#   docs/diagram.html   (self-contained HTML/SVG dashboard, default)
#
# Usage:
#   bash scripts/generate-diagram.sh              # writes docs/diagram.html
#   bash scripts/generate-diagram.sh -o out.html  # custom output path
#
# Requirements: python3 (stdlib yaml+json only), jq
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Repo root auto-discovery
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "${SCRIPT_DIR}/.." && pwd)"

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------
OUTPUT="${REPO}/docs/diagram.html"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--output)
      OUTPUT="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      echo "Usage: $0 [-o|--output PATH]" >&2
      exit 1
      ;;
  esac
done

# ---------------------------------------------------------------------------
# YAML → JSON helper
# ---------------------------------------------------------------------------
yaml_to_json() {
  python3 -c "import yaml,json,sys; print(json.dumps(yaml.safe_load(sys.stdin) or {}))" < "$1"
}

# ---------------------------------------------------------------------------
# Load YAML sources
# ---------------------------------------------------------------------------
MANIFEST_JSON="$(yaml_to_json "${REPO}/asdlc.yaml")"
FEEDBACK_JSON="$(yaml_to_json "${REPO}/feedbackloops/feedback-loops.yaml")"
REGISTRY_JSON="$(yaml_to_json "${REPO}/controls/registry.yaml")"

# ---------------------------------------------------------------------------
# Build file_map: {id: file} from registry
# ---------------------------------------------------------------------------
FILE_MAP_JSON="$(echo "${REGISTRY_JSON}" | jq '
  .registry
  | map({ (.id): (.file // ("controls/" + (.track | ascii_downcase) + "/" + .id + ".yaml")) })
  | add // {}
')"

# ---------------------------------------------------------------------------
# Build stages array
# ---------------------------------------------------------------------------
STAGES_JSON="$(echo "${MANIFEST_JSON}" | jq --argjson file_map "${FILE_MAP_JSON}" '
  .stages | map({
    number: .number,
    name:   .name,
    readme: (.readme // ("stages/" + .slug + "/README.md")),
    controls: (.controls | map({
      id:    .id,
      name:  .name,
      track: .track,
      file:  ($file_map[.id] // ("controls/" + (.track | ascii_downcase) + "/" + .id + ".yaml"))
    }))
  })
')"

# ---------------------------------------------------------------------------
# Build cross_cutting array
# ---------------------------------------------------------------------------
CROSS_CUTTING_JSON="$(echo "${MANIFEST_JSON}" | jq --argjson file_map "${FILE_MAP_JSON}" '
  .cross_cutting.controls | map({
    id:    .id,
    name:  .name,
    track: .track,
    file:  ($file_map[.id] // ("controls/" + (.track | ascii_downcase) + "/" + .id + ".yaml"))
  })
')"

# ---------------------------------------------------------------------------
# Build track_meta object: {code: name}
# ---------------------------------------------------------------------------
TRACK_META_JSON="$(echo "${MANIFEST_JSON}" | jq '
  .framework.control_tracks
  | map({ (.code): .name })
  | add // {}
')"

# ---------------------------------------------------------------------------
# Build feedback_loops array
# ---------------------------------------------------------------------------
FEEDBACK_LOOPS_JSON="$(echo "${FEEDBACK_JSON}" | jq '
  .feedback_loops | map({
    id:             .id,
    name:           .name,
    re_entry_stage: .re_entry_stage,
    trigger_stages: [.trigger_sources[].stage]
  })
')"

# ---------------------------------------------------------------------------
# Assemble final JSON payload
# ---------------------------------------------------------------------------
FRAMEWORK_NAME="$(echo "${MANIFEST_JSON}" | jq -r '.framework.name')"
ABBREVIATION="$(echo "${MANIFEST_JSON}"   | jq -r '.framework.abbreviation')"

JSON_DATA="$(jq -n \
  --arg     framework_name   "${FRAMEWORK_NAME}" \
  --arg     abbreviation     "${ABBREVIATION}" \
  --argjson stages           "${STAGES_JSON}" \
  --argjson cross_cutting    "${CROSS_CUTTING_JSON}" \
  --argjson track_meta       "${TRACK_META_JSON}" \
  --argjson feedback_loops   "${FEEDBACK_LOOPS_JSON}" \
  '{
    framework_name:  $framework_name,
    abbreviation:    $abbreviation,
    stages:          $stages,
    cross_cutting:   $cross_cutting,
    track_meta:      $track_meta,
    feedback_loops:  $feedback_loops
  }')"

# ---------------------------------------------------------------------------
# Compute totals for the summary line
# ---------------------------------------------------------------------------
STAGE_COUNT="$(echo "${STAGES_JSON}"     | jq 'length')"
LOOP_COUNT="$(echo "${FEEDBACK_LOOPS_JSON}" | jq 'length')"

# Unique control IDs across cross_cutting + all stage controls
CONTROL_COUNT="$(echo "${JSON_DATA}" | jq '
  [ .cross_cutting[].id, (.stages[].controls[].id) ] | unique | length
')"

# ---------------------------------------------------------------------------
# HTML template (%%JSON_DATA%% is replaced below)
# ---------------------------------------------------------------------------
# shellcheck disable=SC2016
HTML_TEMPLATE='<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A-SDLC Framework Diagram</title>
<style>
  :root {
    --bg: #1a1e2e;
    --bg-light: #242940;
    --text: #e8e8e8;
    --text-muted: #8892b0;
    --teal: #2ec4a0;
    --teal-dark: #1a8a6e;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html, body {
    height: 100%;
    overflow: hidden;
  }

  body {
    font-family: '"'"'SF Mono'"'"', '"'"'Fira Code'"'"', '"'"'JetBrains Mono'"'"', '"'"'Cascadia Code'"'"', '"'"'Consolas'"'"', monospace;
    background: var(--bg);
    color: var(--text);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .container {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px;
  }

  .diagram-area {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
  }

  .diagram-area svg {
    width: 100%;
    height: 100%;
  }

  /* Tooltip */
  .tooltip {
    position: fixed;
    background: var(--bg-light);
    border: 1px solid var(--teal-dark);
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.75rem;
    color: var(--text);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.15s;
    z-index: 100;
    max-width: 280px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.4);
  }
  .tooltip.visible { opacity: 1; }
  .tooltip h4 { font-size: 0.8rem; margin-bottom: 4px; color: var(--teal); }
  .tooltip .ctrl-id { color: #fff; font-weight: 600; }
  .tooltip .ctrl-name { color: var(--text-muted); }

</style>
</head>
<body>

<div class="container">
  <div class="diagram-area">
    <svg id="diagram" viewBox="60 60 780 780" xmlns="http://www.w3.org/2000/svg"></svg>
  </div>
</div>

<div class="tooltip" id="tooltip"></div>

<script>
const DATA = %%JSON_DATA%%;

const TRACK_COLORS = {
  QC: '"'"'#3b82f6'"'"',
  RC: '"'"'#f59e0b'"'"',
  SC: '"'"'#ef4444'"'"',
  AC: '"'"'#a855f7'"'"',
  GC: '"'"'#6366f1'"'"',
};

// --- Hexagon geometry (flat-top orientation) ---
function hexPoints(cx, cy, r) {
  const pts = [];
  for (let i = 0; i < 6; i++) {
    const angle = (Math.PI / 180) * (60 * i);
    pts.push([cx + r * Math.cos(angle), cy + r * Math.sin(angle)]);
  }
  return pts;
}

function hexPath(cx, cy, r) {
  const pts = hexPoints(cx, cy, r);
  return '"'"'M '"'"' + pts.map(p => p[0] + '"'"','"'"' + p[1]).join('"'"' L '"'"') + '"'"' Z'"'"';
}

function pointOnHex(cx, cy, r, angleDeg) {
  const angleRad = (angleDeg - 90) * Math.PI / 180;
  const dx = Math.cos(angleRad);
  const dy = Math.sin(angleRad);
  const pts = hexPoints(cx, cy, r);
  let minT = Infinity;
  for (let i = 0; i < 6; i++) {
    const [x1, y1] = pts[i];
    const [x2, y2] = pts[(i + 1) % 6];
    const ex = x2 - x1, ey = y2 - y1;
    const denom = dx * ey - dy * ex;
    if (Math.abs(denom) < 1e-9) continue;
    const t = ((x1 - cx) * ey - (y1 - cy) * ex) / denom;
    const s = ((x1 - cx) * dy - (y1 - cy) * dx) / denom;
    if (t > 0.01 && s >= -0.001 && s <= 1.001) {
      minT = Math.min(minT, t);
    }
  }
  return [cx + dx * minT, cy + dy * minT];
}

// --- SVG helpers ---
const SVG_NS = '"'"'http://www.w3.org/2000/svg'"'"';
function svgEl(tag, attrs = {}) {
  const el = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, v);
  return el;
}

function svgText(text, attrs) {
  const el = svgEl('"'"'text'"'"', attrs);
  el.textContent = text;
  return el;
}

// --- Layout constants ---
const HEX_R = 130;
const RING_R = Math.round(HEX_R * Math.sqrt(3)); // ~225 — hexes touch side-to-side
const CX = 450, CY = 450;
const BADGE_W = 36, BADGE_H = 14, BADGE_GAP_X = 3, BADGE_GAP_Y = 3;
const BADGES_PER_ROW = 3;
const TITLE_BADGE_GAP = 14;

const STAGE_ANGLES = [0, 60, 120, 180, 240, 300];

function stagePos(index) {
  const angleDeg = STAGE_ANGLES[index];
  const angleRad = (angleDeg - 90) * Math.PI / 180;
  return [CX + RING_R * Math.cos(angleRad), CY + RING_R * Math.sin(angleRad)];
}

// --- Draw control badges as a grid centered at (cx, cy) ---
function drawBadges(parent, controls, cx, cy, perRow) {
  const n = controls.length;
  const rows = Math.ceil(n / perRow);
  const totalH = rows * BADGE_H + (rows - 1) * BADGE_GAP_Y;
  const startY = cy - totalH / 2;

  for (let i = 0; i < n; i++) {
    const c = controls[i];
    const col = i % perRow;
    const row = Math.floor(i / perRow);
    // Center last row if not full
    const itemsInRow = row === rows - 1 ? n - row * perRow : perRow;
    const rowW = itemsInRow * BADGE_W + (itemsInRow - 1) * BADGE_GAP_X;
    const rowStartX = cx - rowW / 2;
    const bx = rowStartX + col * (BADGE_W + BADGE_GAP_X);
    const by = startY + row * (BADGE_H + BADGE_GAP_Y);
    const color = TRACK_COLORS[c.track] || '"'"'#666'"'"';

    // Wrap in an SVG <a> link to the control YAML file (resolve relative to docs/)
    const link = svgEl('"'"'a'"'"', { href: '"'"'../'"'"' + c.file, target: '"'"'_blank'"'"' });
    link.style.cursor = '"'"'pointer'"'"';

    link.appendChild(svgEl('"'"'rect'"'"', {
      x: bx, y: by, width: BADGE_W, height: BADGE_H, rx: '"'"'3'"'"',
      fill: color, opacity: '"'"'0.9'"'"',
    }));
    link.appendChild(svgText(c.id, {
      x: bx + BADGE_W / 2, y: by + BADGE_H / 2,
      '"'"'text-anchor'"'"': '"'"'middle'"'"', '"'"'dominant-baseline'"'"': '"'"'central'"'"',
      fill: '"'"'#ffffff'"'"',
      '"'"'font-size'"'"': '"'"'8'"'"', '"'"'font-weight'"'"': '"'"'700'"'"',
      '"'"'pointer-events'"'"': '"'"'none'"'"',
    }));

    link.addEventListener('"'"'mouseenter'"'"', (e) => showCtrlTooltip(e, c));
    link.addEventListener('"'"'mousemove'"'"', moveTooltip);
    link.addEventListener('"'"'mouseleave'"'"', hideTooltip);

    parent.appendChild(link);
  }
}

// --- Build SVG ---
function buildDiagram() {
  const svg = document.getElementById('"'"'diagram'"'"');

  // Defs
  const defs = svgEl('"'"'defs'"'"');

  // Glow filter
  const filter = svgEl('"'"'filter'"'"', { id: '"'"'hex-glow'"'"', x: '"'"'-20%'"'"', y: '"'"'-20%'"'"', width: '"'"'140%'"'"', height: '"'"'140%'"'"' });
  const blur = svgEl('"'"'feGaussianBlur'"'"', { stdDeviation: '"'"'3'"'"', result: '"'"'glow'"'"' });
  const merge = svgEl('"'"'feMerge'"'"');
  merge.appendChild(svgEl('"'"'feMergeNode'"'"', { in: '"'"'glow'"'"' }));
  merge.appendChild(svgEl('"'"'feMergeNode'"'"', { in: '"'"'SourceGraphic'"'"' }));
  filter.appendChild(blur);
  filter.appendChild(merge);
  defs.appendChild(filter);

  svg.appendChild(defs);

  const positions = DATA.stages.map((_, i) => stagePos(i));

  // --- Hexagons with individual control badges ---
  for (let i = 0; i < 6; i++) {
    const [hx, hy] = positions[i];
    const stage = DATA.stages[i];
    const g = svgEl('"'"'g'"'"', { class: '"'"'hex-group'"'"', '"'"'data-stage'"'"': i });

    // Stage link — wraps hex shape + number + name
    const stageLink = svgEl('"'"'a'"'"', { href: '"'"'../'"'"' + stage.readme, target: '"'"'_blank'"'"' });
    stageLink.style.cursor = '"'"'pointer'"'"';
    // Hex shape
    stageLink.appendChild(svgEl('"'"'path'"'"', {
      d: hexPath(hx, hy, HEX_R),
      fill: '"'"'#0f3d33'"'"', stroke: '"'"'#2ec4a0'"'"', '"'"'stroke-width'"'"': '"'"'2.5'"'"',
      filter: '"'"'url(#hex-glow)'"'"',
    }));

    // Stage name (compute lines first so we can position the number above)
    const words = stage.name.toUpperCase().split(/\s+/);
    let lines;
    if (words.length <= 2) {
      lines = [words.join('"'"' '"'"')];
    } else {
      const mid = Math.ceil(words.length / 2);
      lines = [words.slice(0, mid).join('"'"' '"'"'), words.slice(mid).join('"'"' '"'"')];
    }
    const nameLineH = 24;
    const nameBlockH = lines.length * nameLineH;
    const nameStartY = hy - 14 - ((lines.length - 1) * nameLineH) / 2;

    // Stage number (watermark) — fixed gap above the first name line
    stageLink.appendChild(svgText(stage.number, {
      x: hx, y: nameStartY - 30, '"'"'text-anchor'"'"': '"'"'middle'"'"', fill: '"'"'#ffffff'"'"',
      '"'"'font-size'"'"': '"'"'36'"'"', '"'"'font-weight'"'"': '"'"'800'"'"', opacity: '"'"'0.2'"'"',
    }));

    for (let li = 0; li < lines.length; li++) {
      stageLink.appendChild(svgText(lines[li], {
        x: hx, y: nameStartY + li * nameLineH,
        '"'"'text-anchor'"'"': '"'"'middle'"'"', fill: '"'"'#ffffff'"'"',
        '"'"'font-size'"'"': '"'"'20'"'"', '"'"'font-weight'"'"': '"'"'700'"'"', '"'"'letter-spacing'"'"': '"'"'0.04em'"'"',
      }));
    }

    g.appendChild(stageLink);

    // Control badges grid — consistent gap below the last name line
    const lastNameY = nameStartY + (lines.length - 1) * nameLineH;
    const stageRows = Math.ceil(stage.controls.length / BADGES_PER_ROW);
    const stageBadgesH = stageRows * BADGE_H + (stageRows - 1) * BADGE_GAP_Y;
    const badgeCenterY = lastNameY + TITLE_BADGE_GAP + stageBadgesH / 2;
    drawBadges(g, stage.controls, hx, badgeCenterY, BADGES_PER_ROW);

    // Bring hex group to front on hover (SVG z-order = DOM order)
    g.addEventListener('"'"'mouseenter'"'"', () => g.parentNode.appendChild(g));

    svg.appendChild(g);
  }

  // --- Center: cross-cutting controls ---
  const ccG = svgEl('"'"'g'"'"', { class: '"'"'center-group'"'"' });

  // Vertically center title + badge grid as a group
  const titleFontSize = 42;
  const ccRows = Math.ceil(DATA.cross_cutting.length / 3);
  const ccBadgesH = ccRows * BADGE_H + (ccRows - 1) * BADGE_GAP_Y;
  const totalBlockH = titleFontSize + TITLE_BADGE_GAP + ccBadgesH;
  const blockTop = CY - totalBlockH / 2;

  // Center label — "A" in white + "SDLC" in teal on one line
  const titleG = svgEl('"'"'text'"'"', {
    x: CX, y: blockTop + titleFontSize * 0.75, '"'"'text-anchor'"'"': '"'"'middle'"'"',
    '"'"'font-size'"'"': titleFontSize, '"'"'font-weight'"'"': '"'"'800'"'"', '"'"'letter-spacing'"'"': '"'"'0.08em'"'"',
  });
  const tspanA = svgEl('"'"'tspan'"'"', { fill: '"'"'#ffffff'"'"' });
  tspanA.textContent = '"'"'A'"'"';
  const tspanSDLC = svgEl('"'"'tspan'"'"', { fill: '"'"'#2ec4a0'"'"' });
  tspanSDLC.textContent = '"'"'SDLC'"'"';
  titleG.appendChild(tspanA);
  titleG.appendChild(tspanSDLC);
  ccG.appendChild(titleG);

  // Cross-cutting control badges
  const badgesCenterY = blockTop + titleFontSize + TITLE_BADGE_GAP + ccBadgesH / 2;
  drawBadges(ccG, DATA.cross_cutting, CX, badgesCenterY, 3);

  svg.appendChild(ccG);
}

// --- Tooltip ---
const tooltipEl = document.getElementById('"'"'tooltip'"'"');

function showCtrlTooltip(e, ctrl) {
  tooltipEl.innerHTML = `<span class="ctrl-id" style="color:${TRACK_COLORS[ctrl.track]}">${ctrl.id}</span> <span class="ctrl-name">${ctrl.name}</span>`;
  tooltipEl.classList.add('"'"'visible'"'"');
  moveTooltip(e);
}

function moveTooltip(e) {
  let x = e.clientX + 14;
  let y = e.clientY + 14;
  if (x + 280 > window.innerWidth) x = e.clientX - 280;
  if (y + 60 > window.innerHeight) y = e.clientY - 60;
  tooltipEl.style.left = x + '"'"'px'"'"';
  tooltipEl.style.top = y + '"'"'px'"'"';
}

function hideTooltip() {
  tooltipEl.classList.remove('"'"'visible'"'"');
}

// --- Init ---
buildDiagram();
</script>
</body>
</html>'

# ---------------------------------------------------------------------------
# Inject JSON data into template (replace %%JSON_DATA%%) and write output
# ---------------------------------------------------------------------------
# Write both the template and JSON to temp files so Python reads from files,
# avoiding any ARG_MAX or newline-quoting issues with large shell variables.
OUTPUT_DIR="$(dirname "${OUTPUT}")"
mkdir -p "${OUTPUT_DIR}"

_TMPDIR="$(mktemp -d)"
trap 'rm -rf "${_TMPDIR}"' EXIT

printf '%s' "${HTML_TEMPLATE}" > "${_TMPDIR}/template.html"
printf '%s' "${JSON_DATA}"     > "${_TMPDIR}/data.json"

python3 - "${_TMPDIR}/template.html" "${_TMPDIR}/data.json" "${OUTPUT}" <<'PYEOF'
import sys

template_path, json_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]

with open(template_path) as f:
    template = f.read()
with open(json_path) as f:
    json_data = f.read()

html = template.replace('%%JSON_DATA%%', json_data)

with open(output_path, 'w') as f:
    f.write(html)
    f.write('\n')
PYEOF

echo "Diagram generated: ${OUTPUT}"
echo "  Stages:         ${STAGE_COUNT}"
echo "  Controls:       ${CONTROL_COUNT}"
echo "  Feedback loops: ${LOOP_COUNT}"
