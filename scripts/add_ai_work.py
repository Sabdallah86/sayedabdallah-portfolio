from pathlib import Path
import json
import re

script_path = Path("script.js")
index_path = Path("index.html")

script = script_path.read_text(encoding="utf-8")
marker = "const categoryData = "
start = script.index(marker) + len(marker)
function_start = script.index("function escapeHTML", start)
raw_json = script[start:function_start].rstrip()
if raw_json.endswith(";"):
    raw_json = raw_json[:-1].rstrip()

data = json.loads(raw_json)

# Reuse the existing AI / motion-graphics category key so old links keep working.
ai_key = None
for key, value in data.items():
    title = str(value.get("title", "")).strip().lower() if isinstance(value, dict) else ""
    if key in ("motion-graphics", "ai-work") or title == "ai work":
        ai_key = key
        break

if ai_key is None:
    ai_key = "motion-graphics"

projects = []
for i in range(1, 6):
    projects.append({
        "title": f"AI Work {i:02d}",
        "subtitle": "AI Visuals · Creative Editing",
        "index": f"AI{i:02d}",
        "image": f"assets/ai-work-{i:02d}.jpg",
        "video": f"assets/ai-work-{i:02d}.mp4",
        "badge": "Watch Project",
    })

data[ai_key] = {
    "title": "AI WORK",
    "kicker": "AI & Creative Technology",
    "description": "AI-generated visuals, creative experiments and cinematic AI work.",
    "cover": "assets/ai-work-01.jpg",
    "projects": projects,
}

updated = json.dumps(data, ensure_ascii=False, indent=2)
script = script[:start] + updated + ";\n\n" + script[function_start:]
script_path.write_text(script, encoding="utf-8")

# Keep the homepage category card labelled AI WORK as well.
html = index_path.read_text(encoding="utf-8")
html = html.replace("<h3>Motion Graphics<br>&amp; 3D</h3>", "<h3>AI WORK</h3>")
html = html.replace("<h3>Motion Graphics &amp; 3D</h3>", "<h3>AI WORK</h3>")
html = html.replace("<h3>Motion Graphics & 3D</h3>", "<h3>AI WORK</h3>")
html = html.replace("<p>Titles, graphics and visual systems.</p>", "<p>AI-generated visuals and creative experiments.</p>")
index_path.write_text(html, encoding="utf-8")
