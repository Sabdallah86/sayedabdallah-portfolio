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

row_one = clients[::2]
row_two = clients[1::2]

def group_markup(items, hidden=False):
    hidden_attr = ' aria-hidden="true"' if hidden else ''
    chips = "\n".join(f'            <span class="client-name">{name}</span>' for name in items)
    return f'          <div class="client-group"{hidden_attr}>\n{chips}\n          </div>'

replacement = f'''<!-- CLIENT WALL START -->
<div class="client-wall reveal" aria-label="Selected clients">
        <div class="client-wall-intro">
          <strong>35+ CLIENTS</strong>
          <span>TV NETWORKS · PRODUCTION HOUSES · INSTITUTIONS · BRANDS</span>
          <small>EGYPT · KUWAIT · SAUDI ARABIA · REGIONAL PRODUCTIONS</small>
        </div>
        <div class="client-marquee client-marquee-left" aria-label="Selected clients row one">
          <div class="client-track">
{group_markup(row_one)}
{group_markup(row_one, True)}
          </div>
        </div>
        <div class="client-marquee client-marquee-right" aria-label="Selected clients row two">
          <div class="client-track">
{group_markup(row_two)}
{group_markup(row_two, True)}
          </div>
        </div>
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

# Remove the previous client-grid/client-wall injected CSS, then append the new wall styling.
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
  padding: 28px 0 30px;
  position: relative;
}

.client-wall::before,
.client-wall::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  width: clamp(36px, 7vw, 120px);
  z-index: 4;
  pointer-events: none;
}

.client-wall::before {
  left: 0;
  background: linear-gradient(90deg, var(--bg), transparent);
}

.client-wall::after {
  right: 0;
  background: linear-gradient(270deg, var(--bg), transparent);
}

.client-wall-intro {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: end;
  gap: 18px;
  padding: 0 4px 24px;
}

.client-wall-intro strong {
  font-family: var(--display);
  font-size: clamp(40px, 5vw, 72px);
  line-height: .9;
  font-weight: 400;
  color: var(--text);
  letter-spacing: .025em;
}

.client-wall-intro span,
.client-wall-intro small {
  color: var(--muted);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .13em;
  line-height: 1.5;
}

.client-wall-intro span {
  color: var(--gold);
}

.client-wall-intro small {
  text-align: right;
}

.client-marquee {
  position: relative;
  overflow: hidden;
  width: 100%;
  padding: 6px 0;
}

.client-marquee + .client-marquee {
  margin-top: 8px;
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
  min-height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 28px;
  border: 1px solid rgba(255,255,255,.14);
  background: rgba(255,255,255,.018);
  color: #c8c8c5;
  font-family: var(--display);
  font-size: clamp(18px, 1.7vw, 26px);
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
  font-size: 9px;
  margin-right: 12px;
  opacity: .8;
}

.client-marquee-left .client-track {
  animation: clientScrollLeft 46s linear infinite;
}

.client-marquee-right .client-track {
  animation: clientScrollRight 52s linear infinite;
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

  .client-wall::before,
  .client-wall::after {
    display: none;
  }

  .client-wall-intro {
    grid-template-columns: 1fr;
    align-items: start;
    gap: 8px;
    padding-bottom: 18px;
  }

  .client-wall-intro strong {
    font-size: 48px;
  }

  .client-wall-intro small {
    text-align: left;
  }

  .client-marquee {
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
    min-height: 58px;
    padding: 0 20px;
    font-size: 20px;
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
