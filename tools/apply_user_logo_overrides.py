from pathlib import Path
import re
from html import escape

# Exact logos approved by Sayed. Only these clients are overridden.
OVERRIDES = {
    'ON E Channel': 'on',
    'SATUC': 'satuc',
    'Souad Kafafi Hospital': 'souad-kafafi',
    'TEN Channel': 'ten',
    'Toto Link': 'toto-link',
    'Egypt Air': 'egyptair',
    'ON Sport Channel': 'on-sport',
    'Sada El Balad Channel': 'sada-el-balad',
    'Al-Ahram Agency': 'al-ahram',
    'MICA EGYPT': 'mica',
    'El Gouna Film Festival': 'el-gouna',
}


def exact_brand(name, slug):
    safe = escape(name)
    b64_path = Path('assets/client-logos-user') / f'{slug}.b64'
    if not b64_path.exists():
        raise RuntimeError(f'Missing exact user logo: {b64_path}')
    data = b64_path.read_text(encoding='utf-8').strip()
    if not data:
        raise RuntimeError(f'Empty exact user logo: {b64_path}')
    dark = ' client-brand-v3-user-dark' if slug == 'on-sport' else ' client-brand-v3-user-exact'
    return (
        f'<div class="client-brand-v3 client-brand-v3-logo{dark}" data-exact-logo="{slug}">'
        f'<span class="client-logo-v3-mark">'
        f'<img src="data:image/webp;base64,{data}" alt="{safe} logo" loading="lazy" decoding="async">'
        f'</span><span class="client-name-v3">{safe}</span></div>'
    )


index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')

for name, slug in OVERRIDES.items():
    replacement = exact_brand(name, slug)
    # Never cross a client-card closing div. Each replacement is isolated to one card.
    pattern = re.compile(
        r'<div class="client-brand-v3[^>]*>(?:(?!</div>)[\s\S])*?'
        r'<span class="client-name-v3">' + re.escape(name) + r'</span></div>'
    )
    html, count = pattern.subn(replacement, html)
    if count == 0:
        raise RuntimeError(f'Could not find client entry to override: {name}')
    print(f'Applied exact logo for {name}: {count} occurrence(s)')

index_path.write_text(html, encoding='utf-8')

styles_path = Path('styles.css')
css = styles_path.read_text(encoding='utf-8')
css = re.sub(r'/\* EXACT USER LOGO OVERRIDES START \*/[\s\S]*?/\* EXACT USER LOGO OVERRIDES END \*/', '', css)
css += r'''
/* EXACT USER LOGO OVERRIDES START */
.client-brand-v3[data-exact-logo] .client-logo-v3-mark{
  background:#fff!important;
  padding:5px!important;
  overflow:hidden!important;
}
.client-brand-v3[data-exact-logo] img{
  display:block!important;
  width:100%!important;
  height:100%!important;
  object-fit:contain!important;
  object-position:center!important;
  filter:none!important;
  transform:none!important;
  opacity:1!important;
}
.client-brand-v3-user-dark .client-logo-v3-mark{
  background:#000!important;
  padding:0!important;
}
/* EXACT USER LOGO OVERRIDES END */
'''
styles_path.write_text(css, encoding='utf-8')

print(f'Applied {len(OVERRIDES)} exact user-provided client logo overrides. All other clients unchanged.')
