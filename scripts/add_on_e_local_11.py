from pathlib import Path
import json

script_path = Path("script.js")
text = script_path.read_text(encoding="utf-8")
marker = "const categoryData = "
start = text.index(marker) + len(marker)
function_start = text.index("function escapeHTML", start)
raw_json = text[start:function_start].rstrip()
if raw_json.endswith(";"):
    raw_json = raw_json[:-1].rstrip()

data = json.loads(raw_json)
category = data.get("on-e-channel")
if not category:
    raise SystemExit("ON E standalone category not found")

projects = category.setdefault("projects", [])
projects = [p for p in projects if p.get("index") != "ON11" and p.get("video") != "assets/on-e-11.mp4"]
projects.append({
    "title": "ON E — Event Promo",
    "subtitle": "ON E · TV Program Edit",
    "index": "ON11",
    "image": "assets/on-e-11.jpg",
    "video": "assets/on-e-11.mp4",
    "badge": "Watch Video",
})
category["projects"] = projects

updated = json.dumps(data, ensure_ascii=False, indent=2)
text = text[:start] + updated + ";\n\n" + text[function_start:]
script_path.write_text(text, encoding="utf-8")
