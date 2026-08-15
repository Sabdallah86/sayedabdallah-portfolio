from pathlib import Path
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

NAME_TO_LOGO = {
    'Al-Ahram Agency':'al-ahram', 'Al-Jala Military Hospital':'galaa-medical',
    'MICA EGYPT':'mica', 'Al Tahrir Channel':'al-tahrir', 'TEN Channel':'ten',
    'Al Ahly Club':'al-ahly', 'CBC Channel':'cbc',
    'Cairo International Film Festival':'ciff', 'Egypt Air':'egyptair',
    'EL Nahar Channel':'al-nahar', 'Good News':'good-news',
    'Hospital 57357':'hospital-57357', 'Ministry of Migration':'ministry-migration',
    'ON E Channel':'on', 'ON Sport Channel':'on-sport',
    'Sada El Balad Channel':'sada-el-balad', 'SATUC':'satuc',
    'Souad Kafafi Hospital':'souad-kafafi', 'SQUARE Media Production':'square',
    'Sudanese Television':'sudan-tv', 'Toto Link':'toto-link',
    'AlWathaeqya Channel':'al-wathaeqya', 'Kuwait Television':'kuwait-tv',
    'Shasha Platform':'shasha'
}


def initials(name):
    ignored = {'channel','foundation','production','hospital','television','platform'}
    words = [w for w in name.replace('-', ' ').split() if w.lower() not in ignored]
    words = words or name.split()
    return ''.join(w[0] for w in words[:2]).upper()


def logo_source(slug):
    # Exact user-approved white-background/color images always win.
    preferred = Path('assets/client-logos-white') / f'{slug}.webp'
    if preferred.exists() and preferred.stat().st_size:
        return str(preferred).replace('\\','/')
    # All remaining merged logo data is decoded before this script runs.
    generated = Path('assets/client-logos') / f'{slug}.png'
    if generated.exists() and generated.stat().st_size:
        return str(generated).replace('\\','/')
    return None


def brand(name):
    safe = escape(name)
    mark = escape(initials(name))
    slug = NAME_TO_LOGO.get(name)
    if slug:
        src = logo_source(slug)
        if src:
            return (
                f'<div class="client-brand-v3 client-brand-v3-logo">'
                f'<span class="client-logo-v3-mark">'
                f'<img src="{src}" alt="{safe} logo" loading="lazy" decoding="async" '
                f'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'">'
                f'<i class="client-logo-v3-fallback" aria-hidden="true">{mark}</i></span>'
                f'<span class="client-name-v3">{safe}</span></div>'
            )
    return (
        f'<div class="client-brand-v3 client-brand-v3-wordmark">'
        f'<span class="client-logo-v3-mark"><i class="client-logo-v3-fallback visible" aria-hidden="true">{mark}</i></span>'
        f'<span class="client-name-v3">{safe}</span></div>'
    )


def row_markup(items, direction):
    html = ''.join(brand(x) for x in items)
    return f'''<div class="clients-v3-row clients-v3-{direction} reveal" data-client-row>
      <button class="client-scroll-btn client-scroll-prev" type="button" aria-label="Move client logos left">←</button>
      <div class="clients-v3-viewport">
        <div class="clients-v3-track"><div class="clients-v3-group">{html}</div><div class="clients-v3-group" aria-hidden="true">{html}</div></div>
      </div>
      <button class="client-scroll-btn client-scroll-next" type="button" aria-label="Move client logos right">→</button>
    </div>'''

row1 = CLIENTS[::2]
row2 = CLIENTS[1::2]
section = f'''<section class="clients-v3 section-shell" id="clients">
  <div class="clients-v3-title reveal"><p class="kicker">Trusted By Great Brands</p><span></span></div>
  {row_markup(row1, 'left')}
  {row_markup(row2, 'right')}
</section>'''

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
patterns = [
    r'<section class="clients-logo-section[\s\S]*?</section>',
    r'<section class="clients-section[\s\S]*?</section>',
    r'<section class="clients-v3[\s\S]*?</section>',
    r'<section class="clients section">[\s\S]*?</section>'
]
for pattern in patterns:
    if re.search(pattern, html):
        html = re.sub(pattern, section, html, count=1)
        break
else:
    raise RuntimeError('Could not locate clients section')

if 'site-updates.js' not in html:
    html = html.replace('<script src="script.js"></script>', '<script src="script.js"></script>\n  <script src="site-updates.js"></script>')
index_path.write_text(html, encoding='utf-8')

styles_path = Path('styles.css')
css = styles_path.read_text(encoding='utf-8')
css = re.sub(r'/\* CLIENT LOGO V3 START \*/[\s\S]*?/\* CLIENT LOGO V3 END \*/', '', css)
css += r'''
/* CLIENT LOGO V3 START */
.clients-v3{overflow:hidden;padding-top:54px!important;padding-bottom:54px!important;background:#030303}
.clients-v3-title{display:flex;align-items:center;gap:22px;margin-bottom:18px}.clients-v3-title .kicker{margin:0;white-space:nowrap}.clients-v3-title>span{height:1px;flex:1;background:rgba(211,164,47,.62)}
.clients-v3-row{display:grid;grid-template-columns:46px minmax(0,1fr) 46px;align-items:center;border-top:1px solid rgba(211,164,47,.58)}.clients-v3-row:last-child{border-bottom:1px solid rgba(211,164,47,.58)}
.clients-v3-viewport{overflow:hidden;min-width:0}.clients-v3-track{display:flex;width:max-content;will-change:transform}.clients-v3-group{display:flex;align-items:center;gap:34px;padding:22px 19px;flex:0 0 auto}
.clients-v3-left .clients-v3-track{animation:clientsV3Left 78s linear infinite}.clients-v3-right .clients-v3-track{animation:clientsV3Right 82s linear infinite}.clients-v3-row:hover .clients-v3-track{animation-play-state:paused}
.client-scroll-btn{appearance:none;border:0;background:transparent;color:#d3a42f;font-size:24px;line-height:1;cursor:pointer;height:100%;min-height:90px;transition:.2s ease;z-index:2}.client-scroll-btn:hover{color:#fff;background:rgba(211,164,47,.08)}
.client-brand-v3{display:flex;align-items:center;gap:12px;width:245px;min-width:245px;max-width:245px;height:92px;flex:0 0 245px;overflow:hidden;background:transparent!important;border:0!important;box-shadow:none!important;padding:0!important}
.client-logo-v3-mark{width:112px;min-width:112px;height:78px;display:flex;align-items:center;justify-content:center;overflow:hidden;background:#fff!important;border:0!important;padding:6px}.client-brand-v3 img{display:block!important;width:100%!important;height:100%!important;object-fit:contain!important;object-position:center!important;filter:none!important;opacity:1!important;transform:none!important}
.client-logo-v3-fallback{display:none;align-items:center;justify-content:center;width:100%;height:100%;font-family:'Bebas Neue',Inter,Arial,sans-serif;font-style:normal;font-size:27px;letter-spacing:.06em;color:#d3a42f;background:#030303}.client-logo-v3-fallback.visible{display:flex}.client-name-v3{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap!important;font-family:Inter,Arial,sans-serif;color:#d8d8d5;font-size:11px!important;font-weight:700;letter-spacing:.075em;text-transform:uppercase;line-height:1.2!important}
@keyframes clientsV3Left{from{transform:translate3d(0,0,0)}to{transform:translate3d(-50%,0,0)}}@keyframes clientsV3Right{from{transform:translate3d(-50%,0,0)}to{transform:translate3d(0,0,0)}}
@media(max-width:760px){.clients-v3{padding-top:38px!important;padding-bottom:38px!important}.clients-v3-title{gap:14px;margin-bottom:12px}.clients-v3-title .kicker{font-size:11px!important;letter-spacing:.16em}.clients-v3-row{grid-template-columns:34px minmax(0,1fr) 34px}.client-scroll-btn{font-size:19px;min-height:82px}.clients-v3-group{gap:20px;padding:17px 10px}.client-brand-v3{width:205px;min-width:205px;max-width:205px;height:80px;flex-basis:205px;gap:9px}.client-logo-v3-mark{width:94px;min-width:94px;height:68px;padding:5px}.client-name-v3{font-size:9.5px!important;letter-spacing:.055em}.clients-v3-left .clients-v3-track{animation-duration:64s}.clients-v3-right .clients-v3-track{animation-duration:68s}}
@media(max-width:420px){.clients-v3-group{gap:14px;padding-left:8px;padding-right:8px}.client-brand-v3{width:190px;min-width:190px;max-width:190px;flex-basis:190px}.client-logo-v3-mark{width:86px;min-width:86px;height:64px}.client-name-v3{font-size:9px!important}}
@media(prefers-reduced-motion:reduce){.clients-v3-track{animation:none!important}}
/* CLIENT LOGO V3 END */
'''
styles_path.write_text(css, encoding='utf-8')
print(f'Rebuilt client strip with {len(CLIENTS)} clients, exact color logo priority, manual arrows and automatic animation.')