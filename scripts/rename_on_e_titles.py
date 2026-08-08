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

on_e_titles = {
    "ON01": "Promo — 7 Years Gouna",
    "ON02": "Style Talk — Sherine Hamdy",
    "ON03": "Lamees El Hadidy and the Creators of Al-Hashashin",
    "ON04": "Naguib Sawiris — Interview on Egypt’s Investment Climate",
    "ON05": "Disney On Ice — Cairo Stadium",
    "ON06": "Interview with Egypt’s Minister of Investment",
    "ON07": "El Gouna Film Festival — 7th Edition Opening",
    "ON08": "El Gouna Film Festival — 5th Edition Opening",
    "ON09": "teaser Ahla Akla_01",
    "ON10": "teaser Ahla Akla_02",
}

projects = data.get("on-e-channel", {}).get("projects", [])
for project in projects:
    index = project.get("index")
    if index in on_e_titles:
        project["title"] = on_e_titles[index]

updated = json.dumps(data, ensure_ascii=False, indent=2)
text = text[:start] + updated + ";\n\n" + text[function_start:]
script_path.write_text(text, encoding="utf-8")
