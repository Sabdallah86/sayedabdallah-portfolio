from pathlib import Path
import base64
import json
import re
from html import escape

CLIENTS = [
    'Al-Ahram Agency', 'Al-Jala Military Hospital', '3DI - Yasser Sami', 'TERA SOFT',
    'MICA EGYPT', 'Al Tahrir Channel', 'TEN Channel', 'Al Ahly Club', 'CBC Channel',
    'Cairo International Film Festival', 'Egypt Air', 'Egyptian Countryside',
    'Egyptian Television', 'EL Nahar Channel', 'El Gouna Film Festival', 'Good News',
    'Hama Film Production', 'Hospital 57357', 'I Production', 'Misr El Kheir Foundation',
    'Ministry of Migration', 'Motor TV', 'ON E Channel', 'ON Sport Channel', 'Rotary',
    'Sada El Balad Channel', 'SATUC', 'Saudi Arabia', 'Souad Kafafi Hospital',
    'SQUARE Media Production', 'Studio 24', 'Sudanese Television', 'Toto Link',
    'Turkish Factory', 'AlWathaeqya Channel', 'Kuwait Television', 'Shasha Platform'
]

# Logos supplied and confirmed by the user in this conversation.
NAME_TO_LOGO = {
    'Al-Ahram Agency': 'al-ahram',
    'Al-Jala Military Hospital': 'galaa-medical',
    'MICA EGYPT': 'mica',
    'Al Tahrir Channel': 'al-tahrir',
    'TEN Channel': 'ten',
    'Al Ahly Club': 'al-ahly',
    'CBC Channel': 'cbc',
    'Cairo International Film Festival': 'ciff',
    'Egypt Air': 'egyptair',
    'EL Nahar Channel': 'al-nahar',
    'Good News': 'good-news',
    'Hospital 57357': 'hospital-57357',
    'Ministry of Migration': 'ministry-migration',
    'ON E Channel': 'on',
    'ON Sport Channel': 'on-sport',
    'Sada El Balad Channel': 'sada-el-balad',
    'SATUC': 'satuc',
    'Souad Kafafi Hospital': 'souad-kafafi',
    'SQUARE Media Production': 'square',
    'Sudanese Television': 'sudan-tv',
    'Toto Link': 'toto-link',
    'AlWathaeqya Channel': 'al-wathaeqya',
    'Kuwait Television': 'kuwait-tv',
    'Shasha Platform': 'shasha',
}

# Decode the newest uploaded logos from a data-only JSON file. The earlier confirmed
# logos are already written by apply_client_logos.py immediately before this script.
data_path = Path('assets/client-logos-src/logos.json')
new_logos = json.loads(data_path.read_text(encoding='utf-8'))
expected = {
    'al-ahly', 'ciff', 'good-news', 'ministry-migration', 'on-sport',
    'sada-el-balad', 'square', 'sudan-tv', 'kuwait-tv'
}
missing = expected - set(new_logos)
if missing:
    raise RuntimeError('Missing supplied client logo data: ' + ', '.join(sorted(missing)))

logo_dir = Path('assets/client-logos')
logo_dir.mkdir(parents=True, exist_ok=True)
for slug in sorted(expected):
    raw = base64.b64decode(new_logos[slug], validate=True)
    if not raw.startswith(b'\x89PNG\r\n\x1a\n'):
        raise RuntimeError(f'{slug} is not a valid PNG payload')
    (logo_dir / f'{slug}.png').write_bytes(raw)

# Ensure every mapped logo file exists before we reference it.
for name, slug in NAME_TO_LOGO.items():
    path = logo_dir / f'{slug}.png'
    if not path.exists() or path.stat().st_size < 100:
        raise RuntimeError(f'Logo file missing or empty for {name}: {path}')


def initials(name):
    ignored = {'channel', 'foundation', 'production', 'hospital', 'television', 'platform'}
    words = [w for w in name.replace('-', ' ').split() if w.lower() not in ignored]
    words = words or name.split()
    return ''.join(w[0] for w in words[:2]).upper()


def brand(name):
    safe_name = escape(name)
    slug = NAME_TO_LOGO.get(name)
    if slug:
        return (
            f'<div class="client-brand-v3 client-brand-v3-logo">'
            f'<img src="assets/client-logos/{slug}.png" alt="{safe_name} logo" loading="lazy">'
            f'<span>{safe_name}</span></div>'
        )
    return (
        f'<div class="client-brand-v3 client-brand-v3-wordmark">'
        f'<b aria-hidden="true">{escape(initials(name))}</b><span>{safe_name}</span></div>'
    )

row1 = CLIENTS[::2]
row2 = CLIENTS[1::2]
row1_html = ''.join(brand(x) for x in row1)
row2_html = ''.join(brand(x) for x in row2)

section = f'''<section class="clients-v3 section-shell" id="clients">
  <div class="clients-v3-title reveal">
    <p class="kicker">Trusted By Great Brands</p>
    <span></span>
  </div>
  <div class="clients-v3-row clients-v3-left reveal" aria-label="Selected clients row one">
    <div class="clients-v3-track"><div class="clients-v3-group">{row1_html}</div><div class="clients-v3-group" aria-hidden="true">{row1_html}</div></div>
  </div>
  <div class="clients-v3-row clients-v3-right reveal" aria-label="Selected clients row two">
    <div class="clients-v3-track"><div class="clients-v3-group">{row2_html}</div><div class="clients-v3-group" aria-hidden="true">{row2_html}</div></div>
  </div>
</section>'''

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
patterns = [
    r'<section class="clients-logo-section[\s\S]*?</section>',
    r'<section class="clients-section[\s\S]*?</section>',
    r'<section class="clients-v3[\s\S]*?</section>',
]
replaced = False
for pattern in patterns:
    if re.search(pattern, html):
        html = re.sub(pattern, section, html, count=1)
        replaced = True
        break
if not replaced:
    raise RuntimeError('Could not locate the clients section to replace')
index_path.write_text(html, encoding='utf-8')

styles_path = Path('styles.css')
css = styles_path.read_text(encoding='utf-8')
css = re.sub(r'/\* CLIENT LOGO V3 START \*/[\s\S]*?/\* CLIENT LOGO V3 END \*/', '', css)
css += r'''
/* CLIENT LOGO V3 START */
.clients-v3{overflow:hidden;padding-top:54px!important;padding-bottom:54px!important;background:#030303}
.clients-v3-title{display:flex;align-items:center;gap:22px;margin-bottom:18px}
.clients-v3-title .kicker{margin:0;white-space:nowrap}
.clients-v3-title>span{height:1px;flex:1;background:rgba(211,164,47,.55)}
.clients-v3-row{overflow:hidden;border-top:1px solid rgba(211,164,47,.55);position:relative}
.clients-v3-row:last-child{border-bottom:1px solid rgba(211,164,47,.55)}
.clients-v3-track{display:flex;width:max-content;will-change:transform}
.clients-v3-group{display:flex;align-items:center;gap:58px;padding:28px 29px;flex-shrink:0}
.clients-v3-left .clients-v3-track{animation:clientsV3Left 62s linear infinite}
.clients-v3-right .clients-v3-track{animation:clientsV3Right 68s linear infinite}
.clients-v3-row:hover .clients-v3-track{animation-play-state:paused}
.client-brand-v3{display:flex;align-items:center;gap:13px;min-width:max-content;background:transparent!important;border:0!important;box-shadow:none!important;padding:0!important}
.client-brand-v3 img{display:block;width:auto;height:auto;max-width:148px;max-height:70px;object-fit:contain;filter:brightness(0) invert(1)!important;opacity:.94}
.client-brand-v3 span{font-family:Inter,Arial,sans-serif;color:#d5d5d2;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;max-width:175px;line-height:1.3}
.client-brand-v3-wordmark b{display:grid;place-items:center;min-width:52px;height:52px;color:#f0f0ed;border:1px solid rgba(255,255,255,.22);font-family:'Bebas Neue',sans-serif;font-size:25px;letter-spacing:.04em}
@keyframes clientsV3Left{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@keyframes clientsV3Right{from{transform:translateX(-50%)}to{transform:translateX(0)}}
@media(max-width:760px){.clients-v3{padding-top:38px!important;padding-bottom:38px!important}.clients-v3-group{gap:38px;padding:22px 18px}.client-brand-v3 img{max-width:112px;max-height:55px}.client-brand-v3 span{font-size:9px;max-width:130px}.clients-v3-left .clients-v3-track{animation-duration:48s}.clients-v3-right .clients-v3-track{animation-duration:52s}}
@media(prefers-reduced-motion:reduce){.clients-v3-track{animation:none!important}.clients-v3-row{overflow-x:auto}}
/* CLIENT LOGO V3 END */
'''
styles_path.write_text(css, encoding='utf-8')

print(f'Rebuilt client strip with {len(CLIENTS)} clients and {len(NAME_TO_LOGO)} supplied logos.')
