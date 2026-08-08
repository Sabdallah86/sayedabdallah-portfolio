from pathlib import Path
import json
import re

# Remove Ramadan 2025 from TV Programs category data only.
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

# Restore Selected Work to the intended set, with Ramadan 2025 omitted.
# This explicit block avoids the previous broad regex that accidentally removed
# every card before the Ramadan card.
index_path = Path("index.html")
html = index_path.read_text(encoding="utf-8")

selected_work = '''<div class="project-grid">
        <a class="project-card reveal project-link-card" href="index.html?category=sports-events" data-category="Sports">
          <div class="project-image">
            <img src="assets/al-ahly.webp" alt="Al Ahly Club sports content project" loading="lazy">
            <span class="play-button" aria-hidden="true">▶</span>
          </div>
          <div class="project-info">
            <div><h3>Al Ahly Club</h3><p>Sports Content</p></div>
            <span class="project-index">01</span>
          </div>
        </a>

        <a class="project-card reveal project-link-card" href="index.html?category=sports-events" data-category="Events">
          <div class="project-image">
            <img src="assets/ciff.webp" alt="Cairo International Film Festival project" loading="lazy">
            <span class="play-button" aria-hidden="true">▶</span>
          </div>
          <div class="project-info">
            <div><h3>Cairo International Film Festival</h3><p>Event Coverage</p></div>
            <span class="project-index">02</span>
          </div>
        </a>

        <article class="project-card reveal project-video"
          data-category="TV"
          data-video="assets/abu-el-arousa.mp4"
          data-poster="assets/abu-el-arousa.webp"
          data-title="Abu Al-Arousa — Season 2"
          role="button"
          tabindex="0"
          aria-label="Play Abu Al-Arousa Season 2 video">
          <div class="project-image">
            <img src="assets/abu-el-arousa.webp" alt="Abu Al-Arousa Season 2 editing project" loading="lazy">
            <span class="play-button" aria-hidden="true">▶</span>
            <span class="available-badge">Watch Project</span>
          </div>
          <div class="project-info">
            <div><h3>Abu Al-Arousa — Season 2</h3><p>TV Series · Video Editing</p></div>
            <span class="project-index">03</span>
          </div>
        </article>

        <a class="project-card reveal project-link-card" href="index.html?category=on-e-channel" data-category="TV">
          <div class="project-image">
            <img src="assets/on-e.webp" alt="ON E television project" loading="lazy">
            <span class="play-button" aria-hidden="true">▶</span>
          </div>
          <div class="project-info">
            <div><h3>ON E Channel</h3><p>TV Channel</p></div>
            <span class="project-index">04</span>
          </div>
        </a>

        <article class="project-card reveal project-video"
          data-category="Institutional & Social Impact"
          data-video="assets/hospital-57357-qewa-fi-alby.mp4"
          data-poster="assets/hospital-57357-qewa-fi-alby.webp"
          data-title="Hospital 57357 — Qowa Fi Alby"
          role="button"
          tabindex="0"
          aria-label="Play Hospital 57357 Qowa Fi Alby music video">
          <div class="project-image">
            <img src="assets/hospital-57357-qewa-fi-alby.webp" alt="Hospital 57357 Qowa Fi Alby music video edited by Sayed Abdallah" loading="lazy">
            <span class="play-button" aria-hidden="true">▶</span>
            <span class="available-badge">Watch Project</span>
          </div>
          <div class="project-info">
            <div><h3>Hospital 57357</h3><p>Qowa Fi Alby · Music Video</p></div>
            <span class="project-index">06</span>
          </div>
        </article>
      </div>'''

# Replace only the project grid inside the Selected Work section.
section_start = html.index('<section class="section" id="work">')
section_end = html.index('</section>', section_start)
work_section = html[section_start:section_end]
grid_start = work_section.index('<div class="project-grid">')
draft_marker = '<p class="draft-note reveal">'
grid_end = work_section.index(draft_marker, grid_start)
new_work_section = work_section[:grid_start] + selected_work + '\n      ' + work_section[grid_end:]
html = html[:section_start] + new_work_section + html[section_end:]

index_path.write_text(html, encoding="utf-8")
