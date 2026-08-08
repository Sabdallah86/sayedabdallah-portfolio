from pathlib import Path
import json
import re

# Remove Ramadan 2025 from category data.
script_path = Path("script.js")
script = script_path.read_text(encoding="utf-8")
marker = "const categoryData = "
start = script.index(marker) + len(marker)
function_start = script.index("function escapeHTML", start)
raw_json = script[start:function_start].rstrip()
if raw_json.endswith(";"):
    raw_json = raw_json[:-1].rstrip()

data = json.loads(raw_json)
tv = data.get("tv-programs", {})
tv["projects"] = [
    project for project in tv.get("projects", [])
    if project.get("title") != "Ramadan 2025"
    and "ramadan-2025" not in str(project.get("image", "")).lower()
]

# Renumber remaining TV program cards after removal.
for i, project in enumerate(tv.get("projects", []), 1):
    project["index"] = f"TV{i:02d}"

updated = json.dumps(data, ensure_ascii=False, indent=2)
script = script[:start] + updated + ";\n\n" + script[function_start:]
script_path.write_text(script, encoding="utf-8")

# Remove any Ramadan 2025 card from the homepage Selected Work section.
index_path = Path("index.html")
html = index_path.read_text(encoding="utf-8")
html = re.sub(
    r'<a class="project-card reveal project-link-card"[^>]*>.*?<h3>Ramadan 2025</h3>.*?</a>\s*',
    "",
    html,
    flags=re.S,
)
html = re.sub(
    r'<article class="project-card reveal[^>]*>.*?<h3>Ramadan 2025</h3>.*?</article>\s*',
    "",
    html,
    flags=re.S,
)
index_path.write_text(html, encoding="utf-8")
