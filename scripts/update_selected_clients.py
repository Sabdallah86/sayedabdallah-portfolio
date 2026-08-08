from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

clients = [
    "Al-Ahram Agency",
    "Al-Jala Military Hospital",
    "3DI - Yasser Sami",
    "TERA SOFT",
    "MICA EGYPT",
    "Al Tahrir Channel",
    "TEN Channel",
    "Al Ahly Club",
    "CBC",
    "Cairo International Film Festival",
    "Egyptian Countryside",
    "EL Nahar TV",
    "El Gouna Film Festival",
    "Good News",
    "Hama Film Production",
    "Hospital 57357",
    "I Production",
    "Masr El Khair",
    "Ministry of Migration",
    "Motor TV",
    "ON E Channel",
    "ON Sport",
    "Rotary",
    "Sada El Balad TV",
    "SATUC",
    "Saudi Arabia",
    "Souad Kafafi Hospital",
    "SQUARE Media Production",
    "Studio 24",
    "Sudanese Television",
    "Toto Link",
    "Turkish Factory Branch in Egypt",
]

replacement = '<div class="client-strip reveal" aria-label="Selected clients">\n'
replacement += "\n".join(f"        <span>{name}</span>" for name in clients)
replacement += '\n      </div>'

pattern = r'<div class="client-strip reveal" aria-label="Selected clients">.*?</div>'
html, count = re.subn(pattern, replacement, html, count=1, flags=re.S)
if count != 1:
    raise SystemExit("Could not find selected clients block")

path.write_text(html, encoding="utf-8")
