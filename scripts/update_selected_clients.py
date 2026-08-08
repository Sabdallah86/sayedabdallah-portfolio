from pathlib import Path
import re

index_path = Path("index.html")
styles_path = Path("styles.css")

html = index_path.read_text(encoding="utf-8")
styles = styles_path.read_text(encoding="utf-8")

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
    "Egyptian Countryside",
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
    "Egyptian Television",
]

replacement = '<div class="client-strip client-grid reveal" aria-label="Selected clients">\n'
replacement += "\n".join(
    f'        <span class="client-tile" style="--client-i:{i}">{name}</span>'
    for i, name in enumerate(clients)
)
replacement += '\n      </div>'

pattern = r'<div class="client-strip(?: client-grid)? reveal" aria-label="Selected clients">.*?</div>'
html, count = re.subn(pattern, replacement, html, count=1, flags=re.S)
if count != 1:
    raise SystemExit("Could not find selected clients block")

index_path.write_text(html, encoding="utf-8")

start_marker = "/* CLIENT GRID START */"
end_marker = "/* CLIENT GRID END */"
styles = re.sub(
    re.escape(start_marker) + r".*?" + re.escape(end_marker),
    "",
    styles,
    flags=re.S,
).rstrip()

client_css = r'''

/* CLIENT GRID START */
.client-strip.client-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 14px;
  width: 100%;
  overflow: visible;
  white-space: normal;
  align-items: stretch;
}

.client-strip.client-grid .client-tile {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 92px;
  padding: 18px 16px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.035), rgba(255, 255, 255, 0.012));
  color: rgba(255, 255, 255, 0.88);
  font-size: clamp(0.78rem, 0.92vw, 0.98rem);
  font-weight: 700;
  letter-spacing: 0.06em;
  line-height: 1.35;
  text-align: center;
  text-transform: uppercase;
  overflow: hidden;
  isolation: isolate;
  opacity: 0;
  transform: translateY(18px) scale(0.985);
  animation: clientTileIn 620ms cubic-bezier(.2,.75,.25,1) forwards;
  animation-delay: calc(var(--client-i) * 45ms);
  transition: transform 260ms ease, border-color 260ms ease, background 260ms ease, box-shadow 260ms ease, color 260ms ease;
}

.client-strip.client-grid .client-tile::before {
  content: "";
  position: absolute;
  inset: -1px;
  z-index: -1;
  background: linear-gradient(115deg, transparent 20%, rgba(214, 165, 43, 0.16) 50%, transparent 80%);
  transform: translateX(-120%);
  transition: transform 600ms ease;
}

.client-strip.client-grid .client-tile:hover {
  transform: translateY(-6px);
  border-color: rgba(214, 165, 43, 0.78);
  background: linear-gradient(145deg, rgba(214, 165, 43, 0.08), rgba(255, 255, 255, 0.018));
  box-shadow: 0 18px 34px rgba(0, 0, 0, 0.24);
  color: #fff;
}

.client-strip.client-grid .client-tile:hover::before {
  transform: translateX(120%);
}

@keyframes clientTileIn {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@media (max-width: 1050px) {
  .client-strip.client-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (max-width: 760px) {
  .client-strip.client-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;
  }

  .client-strip.client-grid .client-tile {
    min-height: 78px;
    padding: 14px 10px;
    font-size: 0.72rem;
  }
}

@media (max-width: 430px) {
  .client-strip.client-grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .client-strip.client-grid .client-tile {
    opacity: 1;
    transform: none;
    animation: none;
    transition: none;
  }
}
/* CLIENT GRID END */
'''

styles_path.write_text(styles + client_css, encoding="utf-8")
