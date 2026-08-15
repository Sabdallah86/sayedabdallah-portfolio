from pathlib import Path
import re

p = Path('index.html')
html = p.read_text(encoding='utf-8')

# Selected Work must point directly to the live collections, never the legacy
# combined sports-events category.
html = re.sub(
    r'href="index\.html\?category=sports-events"(?=\s*>\s*<div class="selected-media"><img src="assets/ciff\.webp")',
    'href="index.html?category=events&collection=ciff"',
    html,
    count=1,
)
html = re.sub(
    r'href="index\.html\?category=sports-events"(?=\s*>\s*<div class="selected-media"><img src="assets/al-ahly\.webp")',
    'href="index.html?category=sports&collection=al-ahly-club"',
    html,
    count=1,
)

# Be defensive in case a previous build already rewrote the base category URL.
html = html.replace(
    'href="index.html?category=events">\n          <div class="selected-media"><img src="assets/ciff.webp"',
    'href="index.html?category=events&collection=ciff">\n          <div class="selected-media"><img src="assets/ciff.webp"',
    1,
)
html = html.replace(
    'href="index.html?category=sports">\n          <div class="selected-media"><img src="assets/al-ahly.webp"',
    'href="index.html?category=sports&collection=al-ahly-club">\n          <div class="selected-media"><img src="assets/al-ahly.webp"',
    1,
)

# Teatro in Selected Work should always lead somewhere usable. The direct MP4
# player is kept inside Series, while the homepage card opens the Series page.
teatro_article = re.compile(
    r'<article class="selected-card project-video reveal" data-video="assets/teatro-series-promo\.mp4"[\s\S]*?</article>',
    re.M,
)
teatro_link = '''<a class="selected-card reveal" href="index.html?category=series" aria-label="Open Teatro in Series">
          <div class="selected-media"><img src="assets/teatro-series-promo.webp" alt="Teatro"><span class="play-button">▶</span></div>
          <div class="selected-meta"><p>Series Promo</p><h3>Teatro</h3><small>Video Editing</small></div>
        </a>'''
html, _ = teatro_article.subn(teatro_link, html, count=1)

new_grid = '''<div class="category-grid">
        <a class="category-card reveal category-link" href="index.html?category=commercial"><span>01</span><h3>Commercial &amp;<br>Branded Content</h3><p>Campaigns, ads and brand films.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=tv-programs"><span>02</span><h3>TV Programs</h3><p>Programs, formats and television edits.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=series"><span>03</span><h3>Series</h3><p>Promos, songs and selected series edits.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=sports"><span>04</span><h3>Sports</h3><p>Sports edits, promos and club content.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=events"><span>05</span><h3>Events</h3><p>Festival and event coverage.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=institutional"><span>06</span><h3>Institutional &amp;<br>Social Impact</h3><p>Human stories with purpose.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=ai-work"><span>07</span><h3>AI Work</h3><p>AI-assisted visual storytelling and creative experiments.</p><b>View Projects →</b></a>
      </div>'''

html, n = re.subn(r'<div class="category-grid">[\s\S]*?</div>\n    </section>', new_grid + '\n    </section>', html, count=1)
if n != 1:
    raise RuntimeError('Could not replace category grid')

# No homepage link should ever point to the old combined category.
html = html.replace('index.html?category=sports-events', 'index.html?category=sports')

p.write_text(html, encoding='utf-8')

css = Path('styles.css')
text = css.read_text(encoding='utf-8')
text = re.sub(r'/\* SAFE CATEGORY FIX START \*/[\s\S]*?/\* SAFE CATEGORY FIX END \*/', '', text)
text += r'''
/* SAFE CATEGORY FIX START */
.category-grid{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;align-items:stretch!important}
.category-card{display:flex!important;flex-direction:column!important;min-height:220px!important;visibility:visible!important;opacity:1!important;transform:none!important}
.category-card b{margin-top:auto!important}
.client-logo-v3-mark{width:112px!important;min-width:112px!important;height:72px!important;padding:6px!important;background:#fff!important;border-radius:2px!important;overflow:hidden!important}
.client-brand-v3 img{display:block!important;width:100%!important;height:100%!important;max-width:100%!important;max-height:100%!important;object-fit:contain!important;object-position:center!important;filter:none!important}
@media(max-width:1200px){.category-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:680px){.category-grid{grid-template-columns:1fr!important}.category-card{min-height:180px!important}.client-logo-v3-mark{width:92px!important;min-width:92px!important;height:62px!important}}
/* SAFE CATEGORY FIX END */
'''
css.write_text(text, encoding='utf-8')
print('Separated Sports and Events, fixed Selected Work collection links, and routed Teatro to Series.')
