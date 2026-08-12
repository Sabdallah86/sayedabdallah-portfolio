from pathlib import Path
import base64, gzip, json

PAYLOADS = {
    "index.html": "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",
    "styles.css": "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",
    "category-pages.css": "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",
}

for path, packed in PAYLOADS.items():
    Path(path).write_bytes(gzip.decompress(base64.b64decode(packed)))

script_path = Path("script.js")
text = script_path.read_text(encoding="utf-8")
marker = "const categoryData = "
start = text.index(marker) + len(marker)
function_start = text.index("function escapeHTML", start)
raw = text[start:function_start].rstrip()
if raw.endswith(";"):
    raw = raw[:-1].rstrip()
data = json.loads(raw)

tv = data.setdefault("tv-programs", {})
tv.setdefault("projects", [])
tv.setdefault("collections", {})

my_guest_slug = "my-guest-moataz-el-demerdash"
my_guest_title = "My Guest with Moataz El Demerdash"
my_guest_ids = ["_5EHAht5a1M", "_Sd8QUoXoaI", "_7irVnrKMmM", "_vUQ8quTX-w", "FwVPJqsdXBc"]
guest_names = ["Nader Abbassy", "Magdy Abdelghany", "Hany Ramzy", "Salah Abdallah", "Amr Mostafa"]

tv["projects"] = [p for p in tv["projects"] if p.get("collection") != my_guest_slug]
tv["projects"].append({
    "title": my_guest_title,
    "subtitle": "TV Program · Video Collection",
    "index": "TV09",
    "image": f"https://i.ytimg.com/vi/{my_guest_ids[0]}/hqdefault.jpg",
    "imageFallback": "assets/on-e.webp",
    "collection": my_guest_slug,
    "badge": "Open Collection",
})
tv["collections"][my_guest_slug] = {
    "title": my_guest_title,
    "kicker": "TV Program",
    "description": f"Selected episodes and edits from {my_guest_title}.",
    "cover": f"https://i.ytimg.com/vi/{my_guest_ids[0]}/hqdefault.jpg",
    "projects": [
        {
            "title": f"{guest} — {my_guest_title}",
            "subtitle": f"{my_guest_title} · TV Program Edit",
            "index": f"MG{i:02d}",
            "image": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": video_id,
            "badge": "Watch Video",
        }
        for i, (guest, video_id) in enumerate(zip(guest_names, my_guest_ids), 1)
    ],
}

qowa_id = "2KVyASYThgw"
institutional = data.setdefault("institutional", {})
institutional.setdefault("projects", [])
qowa = next((p for p in institutional["projects"] if p.get("index") == "SI01"), None)
if qowa is None:
    qowa = {}
    institutional["projects"].insert(0, qowa)
qowa.clear()
qowa.update({
    "title": "Hospital 57357 — Qowa Fi Alby",
    "subtitle": "Music Video · Video Editing",
    "index": "SI01",
    "image": f"https://i.ytimg.com/vi/{qowa_id}/hqdefault.jpg",
    "imageFallback": "assets/hospital-57357.webp",
    "youtube": qowa_id,
    "badge": "Watch Music Video",
})
institutional["cover"] = f"https://i.ytimg.com/vi/{qowa_id}/hqdefault.jpg"

haytan_id = "hyYa8IUSJJc"
series = data.setdefault("series", {})
series.setdefault("projects", [])
abu = next((p for p in series["projects"] if p.get("index") == "S02"), None)
if abu is None:
    abu = {}
    series["projects"].append(abu)
abu.clear()
abu.update({
    "title": "Abu Al-Arousa — Haytan Beitna",
    "subtitle": "Series Song · Video Editing",
    "index": "S02",
    "image": f"https://i.ytimg.com/vi/{haytan_id}/hqdefault.jpg",
    "imageFallback": "assets/abu-el-arousa.webp",
    "youtube": haytan_id,
    "badge": "Watch Video",
})

updated = json.dumps(data, ensure_ascii=False, indent=2)
text = text[:start] + updated + ";\n\n" + text[function_start:]

old_nav = "nav.innerHTML = '<a href=\"index.html\">Home</a><a class=\"active\" href=\"index.html#categories\">Work</a><a href=\"index.html#about\">About</a><a href=\"index.html#contact\">Contact</a>';"
new_nav = "nav.innerHTML = '<a href=\"index.html\"><span>01</span> Home</a><a class=\"active\" href=\"index.html#work\"><span>02</span> Work</a><a href=\"index.html#categories\"><span>03</span> Categories</a><a href=\"index.html#about\"><span>04</span> About</a><a href=\"index.html#contact\"><span>05</span> Contact</a>';"
if old_nav in text:
    text = text.replace(old_nav, new_nav, 1)

script_path.write_text(text, encoding="utf-8")

final = script_path.read_text(encoding="utf-8")
assert 'class="selected-showcase"' in Path("index.html").read_text(encoding="utf-8")
assert "Abu Al-Arousa" not in Path("index.html").read_text(encoding="utf-8")
for guest in guest_names:
    assert f"{guest} — {my_guest_title}" in final
assert '"youtube": "2KVyASYThgw"' in final
assert '"youtube": "hyYa8IUSJJc"' in final
print("Black-gold redesign built and portfolio data normalized.")
