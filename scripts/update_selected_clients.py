from pathlib import Path
import json
import re

index_path = Path("index.html")
styles_path = Path("styles.css")
script_path = Path("script.js")

html = index_path.read_text(encoding="utf-8")
styles = styles_path.read_text(encoding="utf-8")
script = script_path.read_text(encoding="utf-8")

clients = [
    "Al-Ahram Agency",
    "Al-Jala Military Hospital",
    "3DI - Yasser Sami",
    "TERA SOFT",
    "MICA EGYPT",
    "Al Tahrir Channel",
    "TEN Channel",
    "Al Ahly Club",
    "CBC Channel",
    "Cairo International Film Festival",
    "Egypt Air",
    "Egyptian Countryside",
    "Egyptian Television",
    "EL Nahar TV",
    "El Gouna Film Festival",
    "Good News",
    "Hama Film Production",
    "Hospital 57357",
    "I Production",
    "Misr El Kheir Foundation",
    "Ministry of Migration",
    "Motor TV",
    "ON E Channel",
    "ON Sport Channel",
    "Rotary",
    "Sada El Balad Channel",
    "SATUC",
    "Saudi Arabia",
    "Souad Kafafi Hospital",
    "SQUARE Media Production",
    "Studio 24",
    "Sudanese Television",
    "Toto Link",
    "Turkish Factory",
    "AlWathaeqya Channel",
    "Kuwait Television",
    "Shasha Platform",
]

# -----------------------------------------------------------------------------
# Separate ON E from TV Programs and make it a standalone portfolio category.
# -----------------------------------------------------------------------------
marker = "const categoryData = "
start = script.index(marker) + len(marker)
function_start = script.index("function escapeHTML", start)
raw_json = script[start:function_start].rstrip()
if raw_json.endswith(";"):
    raw_json = raw_json[:-1].rstrip()

data = json.loads(raw_json)
tv = data.get("tv-programs", {})
tv_projects = tv.get("projects", [])
tv_collections = tv.get("collections", {})
on_collection = tv_collections.get("on-e")

if on_collection:
    data["on-e-channel"] = {
        "title": "ON E Channel",
        "kicker": "TV Channel",
        "description": "Selected channel promos, television edits and broadcast work for ON E Channel.",
        "cover": on_collection.get("cover", "assets/on-e.webp"),
        "projects": on_collection.get("projects", []),
    }

    tv["projects"] = [
        project for project in tv_projects
        if project.get("collection") != "on-e" and project.get("title") != "ON E Channel"
    ]
    tv_collections.pop("on-e", None)

    # Keep TV card numbering clean after removing ON E.
    for i, project in enumerate(tv.get("projects", []), 1):
        project["index"] = f"TV{i:02d}"

updated = json.dumps(data, ensure_ascii=False, indent=2)
script = script[:start] + updated + ";\n\n" + script[function_start:]
script_path.write_text(script, encoding="utf-8")

# Add a standalone ON E card to Work Categories if it is not already there.
if 'href="index.html?category=on-e-channel"' not in html:
    tv_card_pattern = re.compile(
        r'(<a class="category-card reveal category-link" href="index\.html\?category=tv-programs">.*?</a>)',
        re.S,
    )
    on_e_card = (
        '<a class="category-card reveal category-link" href="index.html?category=on-e-channel">'
        '<span class="category-icon">▦</span>'
        '<h3>ON E<br>Channel</h3>'
        '<p>Channel promos, broadcast edits and television content.</p>'
        '<span class="category-action">View Projects →</span>'
        '</a>'
    )
    html, count = tv_card_pattern.subn(lambda m: m.group(1) + "\n        " + on_e_card, html, count=1)
    if count != 1:
        raise SystemExit("Could not find TV Programs category card to insert ON E Channel")

# Make the Selected Work ON E card open the new standalone category.
def update_selected_on_e(match):
    block = match.group(0)
    if "<h3>ON E Channel</h3>" in block:
        block = re.sub(
            r'href="index\.html\?category=[^"]+"',
            'href="index.html?category=on-e-channel"',
            block,
            count=1,
        )
    return block

html = re.sub(
    r'<a class="project-card reveal project-link-card".*?</a>',
    update_selected_on_e,
    html,
    flags=re.S,
)

# -----------------------------------------------------------------------------
# Cinematic three-row client wall.
# -----------------------------------------------------------------------------
rows = [clients[i::3] for i in range(3)]

def group_markup(items, hidden=False):
    hidden_attr = ' aria-hidden="true"' if hidden else ''
    chips = "\n".join(f'            <span class="client-name">{name}</span>' for name in items)
    return f'          <div class="client-group"{hidden_attr}>\n{chips}\n          </div>'

row_markup = []
for i, row in enumerate(rows, 1):
    direction = "left" if i != 2 else "right"
    row_markup.append(
        f'''        <div class="client-marquee client-marquee-{direction} client-row-{i}" aria-label="Selected clients row {i}">
          <div class="client-track">
{group_markup(row)}
{group_markup(row, True)}
          </div>
        </div>'''
    )

replacement = f'''<!-- CLIENT WALL START -->
<div class="client-wall reveal" aria-label="Selected clients">
        <div class="client-wall-intro">
          <span>TV NETWORKS · PRODUCTION HOUSES · INSTITUTIONS · BRANDS</span>
          <small>EGYPT · KUWAIT · SAUDI ARABIA · REGIONAL PRODUCTIONS</small>
        </div>
{chr(10).join(row_markup)}
      </div>
<!-- CLIENT WALL END -->'''

start_comment = "<!-- CLIENT WALL START -->"
end_comment = "<!-- CLIENT WALL END -->"
if start_comment in html and end_comment in html:
    html = re.sub(
        re.escape(start_comment) + r".*?" + re.escape(end_comment),
        replacement,
        html,
        count=1,
        flags=re.S,
    )
else:
    old_pattern = r'<div class="client-strip(?: client-grid)? reveal" aria-label="Selected clients">.*?</div>'
    html, count = re.subn(old_pattern, replacement, html, count=1, flags=re.S)
    if count != 1:
        raise SystemExit("Could not find selected clients block")

index_path.write_text(html, encoding="utf-8")

# Remove earlier injected client styling before appending the current version.
for start_marker, end_marker in [
    ("/* CLIENT GRID START */", "/* CLIENT GRID END */"),
    ("/* CLIENT WALL START */", "/* CLIENT WALL END */"),
]:
    styles = re.sub(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        "",
        styles,
        flags=re.S,
    )
styles = styles.rstrip()

client_css = r'''

/* CLIENT WALL START */
.client-wall {
  margin-top: 24px;
  width: 100%;
  overflow: hidden;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  padding: 26px 0 28px;
  position: relative;
}

/* No edge fades: client names remain crisp instead of looking erased. */
.client-wall::before,
.client-wall::after {
  display: none !important;
}

.client-wall-intro {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 0 28px 22px;
}

.client-wall-intro span,
.client-wall-intro small {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .13em;
  line-height: 1.5;
}

.client-wall-intro span {
  color: var(--gold);
}

.client-wall-intro small {
  color: var(--muted);
  text-align: right;
}

.client-marquee {
  position: relative;
  overflow: hidden;
  width: calc(100% - 40px);
  margin-inline: 20px;
  padding: 6px 0;
}

.client-marquee + .client-marquee {
  margin-top: 7px;
}

.client-track {
  display: flex;
  width: max-content;
  will-change: transform;
}

.client-group {
  display: flex;
  gap: 12px;
  padding-right: 12px;
}

.client-name {
  flex: 0 0 auto;
  min-height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 27px;
  border: 1px solid rgba(255,255,255,.14);
  background: rgba(255,255,255,.018);
  color: #c8c8c5;
  font-family: var(--display);
  font-size: clamp(17px, 1.55vw, 24px);
  letter-spacing: .055em;
  line-height: 1;
  text-transform: uppercase;
  white-space: nowrap;
  transition: color .25s ease, border-color .25s ease, background .25s ease, transform .25s ease;
}

.client-name::before {
  content: "•";
  color: var(--gold);
  font-family: var(--body);
  font-size: 8px;
  margin-right: 12px;
  opacity: .85;
}

/* Deliberately slower than the previous two-row version. */
.client-row-1 .client-track {
  animation: clientScrollLeft 76s linear infinite;
}

.client-row-2 .client-track {
  animation: clientScrollRight 84s linear infinite;
}

.client-row-3 .client-track {
  animation: clientScrollLeft 92s linear infinite;
}

.client-wall:hover .client-track {
  animation-play-state: paused;
}

.client-name:hover {
  color: #fff;
  border-color: rgba(214,169,50,.75);
  background: rgba(214,169,50,.085);
  transform: translateY(-2px);
}

@keyframes clientScrollLeft {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

@keyframes clientScrollRight {
  from { transform: translateX(-50%); }
  to { transform: translateX(0); }
}

@media (max-width: 760px) {
  .client-wall {
    padding: 22px 0 24px;
  }

  .client-wall-intro {
    flex-direction: column;
    align-items: flex-start;
    gap: 7px;
    padding: 0 20px 18px;
  }

  .client-wall-intro small {
    text-align: left;
  }

  .client-marquee {
    width: calc(100% - 20px);
    margin-left: 20px;
    margin-right: 0;
    overflow-x: auto;
    scrollbar-width: none;
    scroll-snap-type: x proximity;
    -webkit-overflow-scrolling: touch;
    touch-action: pan-x;
  }

  .client-marquee::-webkit-scrollbar {
    display: none;
  }

  .client-track {
    animation: none !important;
    transform: none !important;
  }

  .client-group[aria-hidden="true"] {
    display: none;
  }

  .client-name {
    min-height: 56px;
    padding: 0 19px;
    font-size: 19px;
    scroll-snap-align: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .client-track {
    animation: none !important;
    transform: none !important;
  }

  .client-marquee {
    overflow-x: auto;
  }

  .client-group[aria-hidden="true"] {
    display: none;
  }
}
/* CLIENT WALL END */
'''

styles_path.write_text(styles + client_css, encoding="utf-8")
