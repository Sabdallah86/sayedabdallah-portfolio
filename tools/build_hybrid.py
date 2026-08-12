from pathlib import Path
import json

CLIENTS = [
    ("Al-Ahram Agency", "ahram.org.eg"),
    ("Al-Jala Military Hospital", None),
    ("3DI - Yasser Sami", None),
    ("TERA SOFT", None),
    ("MICA EGYPT", "micaegypt.com"),
    ("Al Tahrir Channel", None),
    ("TEN Channel", None),
    ("Al Ahly Club", "alahlyegypt.com"),
    ("CBC Channel", None),
    ("Cairo International Film Festival", "ciff.org.eg"),
    ("Egypt Air", "egyptair.com"),
    ("Egyptian Countryside", None),
    ("Egyptian Television", "maspero.eg"),
    ("EL Nahar Channel", None),
    ("El Gouna Film Festival", "elgouna.com"),
    ("Good News", None),
    ("Hama Film Production", None),
    ("Hospital 57357", "57357.org"),
    ("I Production", None),
    ("Misr El Kheir Foundation", "misrelkheir.org"),
    ("Ministry of Migration", "emigration.gov.eg"),
    ("Motor TV", None),
    ("ON E Channel", None),
    ("ON Sport Channel", None),
    ("Rotary", "rotary.org"),
    ("Sada El Balad Channel", None),
    ("SATUC", None),
    ("Saudi Arabia", "saudi.gov.sa"),
    ("Souad Kafafi Hospital", None),
    ("SQUARE Media Production", None),
    ("Studio 24", None),
    ("Sudanese Television", None),
    ("Toto Link", "totolink.net"),
    ("Turkish Factory", None),
    ("AlWathaeqya Channel", None),
    ("Kuwait Television", "media.gov.kw"),
    ("Shasha Platform", None),
]

MY_GUEST_TITLES = {
    "_5EHAht5a1M": "Nader Abbassy — My Guest with Moataz El Demerdash",
    "_Sd8QUoXoaI": "Magdy Abdelghany — My Guest with Moataz El Demerdash",
    "_7irVnrKMmM": "Hany Ramzy — My Guest with Moataz El Demerdash",
    "_vUQ8quTX-w": "Salah Abdallah — My Guest with Moataz El Demerdash",
    "FwVPJqsdXBc": "Amr Mostafa — My Guest with Moataz El Demerdash",
}


def esc(value):
    return (str(value).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def initials(name):
    words = [w for w in name.replace("-", " ").split() if w.lower() not in {"channel", "foundation", "production", "hospital", "television", "platform"}]
    if not words:
        words = name.split()
    return "".join(w[0] for w in words[:2]).upper()


def client_item(item):
    name, domain = item
    fallback = initials(name)
    if domain:
        icon = f"https://www.google.com/s2/favicons?domain_url=https://{domain}&sz=128"
        mark = f'<span class="client-monogram" aria-hidden="true">{esc(fallback)}</span><img src="{icon}" alt="" loading="lazy" referrerpolicy="no-referrer" onerror="this.hidden=true;this.previousElementSibling.style.display=\'grid\'">'
    else:
        mark = f'<span class="client-monogram always" aria-hidden="true">{esc(fallback)}</span>'
    return f'<div class="client-logo-card">{mark}<span>{esc(name)}</span></div>'


row1 = CLIENTS[::2]
row2 = CLIENTS[1::2]
row1_markup = "".join(client_item(c) for c in row1)
row2_markup = "".join(client_item(c) for c in row2)

index = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sayed Abdallah — Senior Video Editor</title>
  <meta name="description" content="Portfolio of Sayed Abdallah, Senior Video Editor and Promo Editor working across television, film, branded content, sports and post-production.">
  <meta name="theme-color" content="#030303">
  <meta property="og:title" content="Sayed Abdallah — Video Editor">
  <meta property="og:description" content="Stories edited with rhythm, clarity and impact.">
  <meta property="og:type" content="website">
  <meta property="og:image" content="assets/og-image.webp">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <aside class="portfolio-sidebar" aria-label="Portfolio navigation">
    <a class="sidebar-brand" href="index.html" aria-label="Sayed Abdallah home">
      <strong>SA</strong><span>Sayed Abdallah<small>Video Editor</small></span>
    </a>
    <nav class="sidebar-nav">
      <a class="active" href="#top"><b>01</b><span>Home</span></a>
      <a href="#work"><b>02</b><span>Work</span></a>
      <a href="#categories"><b>03</b><span>Categories</span></a>
      <a href="#about"><b>04</b><span>About</span></a>
      <a href="#clients"><b>05</b><span>Clients</span></a>
      <a href="#contact"><b>06</b><span>Contact</span></a>
    </nav>
    <div class="sidebar-bottom">
      <a href="mailto:sayedabdallah@micaegypt.com">Let's create<br>something memorable <span>→</span></a>
      <div class="sidebar-socials">
        <a href="https://www.linkedin.com/in/sayed-abdallah" target="_blank" rel="noopener">in</a>
        <a href="https://wa.me/201200071998" target="_blank" rel="noopener">wa</a>
        <a href="mailto:sayedabdallah@micaegypt.com">@</a>
      </div>
    </div>
  </aside>

  <header class="site-header" id="top">
    <a class="brand" href="index.html">SA</a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
    <nav class="main-nav" aria-label="Primary navigation">
      <a class="active" href="#top">Home</a><a href="#work">Work</a><a href="#about">About</a><a href="#clients">Clients</a><a href="#contact">Contact</a>
    </nav>
    <a class="button button-outline header-cta" href="#showreel">Play Showreel</a>
  </header>

  <main class="site-main">
    <section class="hero-clean section-shell" id="home">
      <div class="hero-intro reveal">
        <p class="kicker">Senior Video Editor · Promo Editor</p>
        <h1>Stories edited.<br><span>Impact delivered.</span></h1>
        <p class="hero-copy">More than two decades shaping television, film, promos and branded stories through strong pacing, clear storytelling and polished post-production.</p>
        <div class="hero-actions">
          <a class="button button-gold" href="#showreel"><span>▶</span> Play Showreel</a>
          <a class="button button-outline" href="#work">View Selected Work <span>→</span></a>
        </div>
        <div class="hero-stats" aria-label="Professional highlights">
          <div><strong>20+</strong><span>Years Experience</span></div>
          <div><strong>{len(CLIENTS)}</strong><span>Selected Clients</span></div>
          <div><strong>6+</strong><span>Creative Disciplines</span></div>
        </div>
      </div>

      <a class="featured-project reveal" href="index.html?category=tv-programs&collection=my-guest-moataz-el-demerdash" aria-label="Open My Guest with Moataz El Demerdash collection">
        <img src="https://i.ytimg.com/vi/_5EHAht5a1M/hqdefault.jpg" alt="My Guest with Moataz El Demerdash" referrerpolicy="no-referrer">
        <div class="featured-shade"></div>
        <div class="featured-copy">
          <p class="kicker">Featured Project</p>
          <h2>My Guest<br><span>with Moataz El Demerdash</span></h2>
          <p>TV Program · Video Editing</p>
          <span class="featured-watch"><i>▶</i> Open Collection</span>
        </div>
        <div class="featured-index"><b>01</b><span></span><small>05</small></div>
      </a>
    </section>

    <section class="selected-section section-shell" id="work">
      <div class="section-top reveal"><div><p class="kicker">Portfolio</p><h2>Selected Work</h2></div><a href="#categories">View All Projects <span>→</span></a></div>
      <div class="selected-row">
        <article class="selected-card project-video reveal" data-youtube="2KVyASYThgw" data-title="Hospital 57357 — Qowa Fi Alby" role="button" tabindex="0" aria-label="Play Hospital 57357 Qowa Fi Alby">
          <div class="selected-media"><img src="https://i.ytimg.com/vi/2KVyASYThgw/hqdefault.jpg" alt="Hospital 57357 Qowa Fi Alby" referrerpolicy="no-referrer"><span class="play-button">▶</span></div>
          <div class="selected-meta"><p>Music Video</p><h3>Hospital 57357<br>Qowa Fi Alby</h3><small>Video Editing</small></div>
        </article>
        <a class="selected-card reveal" href="index.html?category=sports-events">
          <div class="selected-media"><img src="assets/ciff.webp" alt="Cairo International Film Festival"><span class="play-button">▶</span></div>
          <div class="selected-meta"><p>Event Coverage</p><h3>Cairo International<br>Film Festival</h3><small>Event Highlights</small></div>
        </a>
        <a class="selected-card reveal" href="index.html?category=sports-events">
          <div class="selected-media"><img src="assets/al-ahly.webp" alt="Al Ahly Club"><span class="play-button">▶</span></div>
          <div class="selected-meta"><p>Sports Content</p><h3>Al Ahly Club</h3><small>Promotional Content</small></div>
        </a>
        <a class="selected-card reveal" href="index.html?category=on-e-channel">
          <div class="selected-media"><img src="assets/on-e.webp" alt="ON E Channel"><span class="play-button">▶</span></div>
          <div class="selected-meta"><p>TV Channel</p><h3>ON E Channel</h3><small>Broadcast Editing</small></div>
        </a>
        <article class="selected-card project-video reveal" data-video="assets/teatro-series-promo.mp4" data-poster="assets/teatro-series-promo.webp" data-title="Teatro — Series Promo" role="button" tabindex="0" aria-label="Play Teatro series promo">
          <div class="selected-media"><img src="assets/teatro-series-promo.webp" alt="Teatro"><span class="play-button">▶</span></div>
          <div class="selected-meta"><p>Series Promo</p><h3>Teatro</h3><small>Video Editing</small></div>
        </article>
      </div>
    </section>

    <section class="clients-section section-shell" id="clients">
      <div class="client-heading reveal"><div><p class="kicker">Trusted Across Different Screens</p><h2>Selected Clients</h2></div><p>All {len(CLIENTS)} clients from the portfolio are restored here. The two rows move in opposite directions and pause on hover.</p></div>
      <div class="client-marquee client-marquee-left reveal"><div class="client-track"><div class="client-group">{row1_markup}</div><div class="client-group" aria-hidden="true">{row1_markup}</div></div></div>
      <div class="client-marquee client-marquee-right reveal"><div class="client-track"><div class="client-group">{row2_markup}</div><div class="client-group" aria-hidden="true">{row2_markup}</div></div></div>
    </section>

    <section class="categories-section section-shell" id="categories">
      <div class="section-top reveal"><div><p class="kicker">Full Portfolio</p><h2>Work Categories</h2></div><p>Browse the complete archive without changing the videos, collections or project data already on the site.</p></div>
      <div class="category-grid">
        <a class="category-card reveal category-link" href="index.html?category=commercial"><span>01</span><h3>Commercial &amp;<br>Branded Content</h3><p>Campaigns, ads and brand films.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=tv-programs"><span>02</span><h3>TV Programs</h3><p>Programs, formats and television edits.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=series"><span>03</span><h3>Series</h3><p>Promos, songs and selected series edits.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=sports-events"><span>04</span><h3>Sports &amp;<br>Events</h3><p>Fast-paced stories and event coverage.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=institutional"><span>05</span><h3>Institutional &amp;<br>Social Impact</h3><p>Human stories with purpose.</p><b>View Projects →</b></a>
        <a class="category-card reveal category-link" href="index.html?category=motion-graphics"><span>06</span><h3>Motion Graphics<br>&amp; 3D</h3><p>Titles, graphics and visual systems.</p><b>View Projects →</b></a>
      </div>
    </section>

    <section class="showreel-section section-shell" id="showreel">
      <div class="showreel-card reveal"><div><p class="kicker">Showreel & Archive</p><h2>Watch the work.<br>Then explore the full archive.</h2><p>A focused entry point to television, promos, events, branded content and post-production work.</p></div><a class="button button-gold" href="https://drive.google.com/drive/folders/1O656ZwZUH_o2PfoBo-ZIYB9jgC9WAlYh" target="_blank" rel="noopener">Open Work Archive <span>→</span></a></div>
    </section>

    <section class="about-section section-shell" id="about">
      <figure class="about-photo reveal"><img src="assets/sayed-abdallah.webp" alt="Portrait of Sayed Abdallah"><figcaption><strong>Sayed Abdallah</strong><span>Senior Video Editor</span></figcaption></figure>
      <div class="about-copy reveal"><p class="kicker">About</p><h2>Stories built<br>in the edit.</h2><p>Senior Video Editor and Promo Editor with more than 20 years of experience across television, film and post-production.</p><p>I work across promos, trailers, commercials, documentaries, broadcast content, music videos and social content — always with a focus on storytelling, pacing and visual rhythm.</p><div class="about-tags"><span>Avid Media Composer</span><span>Adobe Premiere Pro</span><span>After Effects</span><span>Final Cut Pro</span><span>Pro Tools</span></div></div>
    </section>

    <section class="contact-section section-shell" id="contact">
      <div class="contact-copy reveal"><p class="kicker">Available for selected projects & opportunities</p><h2>Let's create<br>something memorable.</h2><div class="contact-links"><a href="mailto:sayedabdallah@micaegypt.com">sayedabdallah@micaegypt.com</a><a href="tel:+201200071998">+20 120 007 1998</a><a href="https://wa.me/201200071998" target="_blank" rel="noopener">WhatsApp</a><a href="https://www.linkedin.com/in/sayed-abdallah" target="_blank" rel="noopener">LinkedIn</a></div></div>
      <a class="button button-gold reveal" href="mailto:sayedabdallah@micaegypt.com?subject=Video%20Editing%20Project">Get In Touch <span>→</span></a>
    </section>
  </main>

  <footer class="site-footer"><strong>SA</strong><p>© <span id="year"></span> Sayed Abdallah. All rights reserved.</p><div><a href="https://www.linkedin.com/in/sayed-abdallah" target="_blank" rel="noopener">LinkedIn</a><a href="https://wa.me/201200071998" target="_blank" rel="noopener">WhatsApp</a></div></footer>

  <div class="video-modal" id="video-modal" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Project video"><button class="video-modal-close" type="button" aria-label="Close video">×</button><div class="video-modal-inner"><div class="video-modal-heading"><p class="kicker">Video Portfolio</p><h2 id="video-modal-title">Project Video</h2></div><video id="project-video-player" controls playsinline preload="metadata"></video></div></div>
  <div class="toast" role="status" aria-live="polite"></div>
  <script src="script.js"></script>
</body>
</html>'''

styles = r'''*:where(*,::before,::after){box-sizing:border-box}html{scroll-behavior:smooth}:root{--bg:#030303;--panel:#080808;--panel2:#0c0c0b;--gold:#d9a620;--gold2:#b9830c;--text:#f1f0eb;--muted:#8b8a84;--line:rgba(255,255,255,.12);--display:"Bebas Neue",sans-serif;--body:"Inter",sans-serif;--sidebar:220px}body{margin:0;background:var(--bg);color:var(--text);font-family:var(--body);font-size:14px;line-height:1.55;overflow-x:hidden}a{color:inherit;text-decoration:none}img{max-width:100%}button,input{font:inherit}.kicker{margin:0 0 10px;color:var(--gold);font-size:10px;font-weight:800;letter-spacing:.17em;text-transform:uppercase}.button{min-height:46px;padding:0 18px;display:inline-flex;align-items:center;justify-content:center;gap:10px;border:1px solid var(--line);font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;transition:.25s}.button-gold{border-color:var(--gold);color:#090806;background:var(--gold)}.button-gold:hover{background:#f0c14b}.button-outline{border-color:rgba(255,255,255,.2);color:#ddd}.button-outline:hover{border-color:var(--gold);color:var(--gold)}
.portfolio-sidebar{position:fixed;z-index:50;inset:0 auto 0 0;width:var(--sidebar);padding:30px 24px;border-right:1px solid var(--line);background:#050505;display:flex;flex-direction:column}.sidebar-brand{display:flex;align-items:center;gap:12px}.sidebar-brand strong{font-family:Georgia,serif;color:var(--gold);font-size:42px;line-height:1;font-weight:400;letter-spacing:-.08em}.sidebar-brand span{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#aaa}.sidebar-brand small{display:block;color:var(--gold);font-size:8px;margin-top:4px}.sidebar-nav{display:flex;flex-direction:column;gap:2px;margin:auto 0}.sidebar-nav a{position:relative;display:grid;grid-template-columns:26px 1fr;gap:11px;padding:12px 0;color:#787878;font-size:9px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;transition:.2s}.sidebar-nav b{font-size:8px;font-weight:600;color:#565656}.sidebar-nav a.active,.sidebar-nav a:hover{color:var(--gold)}.sidebar-nav a.active:before{content:"";position:absolute;left:-24px;top:10px;bottom:10px;width:2px;background:var(--gold)}.sidebar-bottom>a{display:block;color:var(--gold);font-family:var(--display);font-size:18px;line-height:1.1;text-transform:uppercase;letter-spacing:.07em;padding-bottom:16px;border-bottom:1px solid rgba(217,166,32,.35)}.sidebar-bottom>a span{float:right}.sidebar-socials{display:flex;gap:7px;margin-top:18px}.sidebar-socials a{width:30px;height:30px;display:grid;place-items:center;border:1px solid var(--line);font-size:9px;color:#888}.sidebar-socials a:hover{color:var(--gold);border-color:var(--gold)}
.site-header{display:none}.site-main{margin-left:var(--sidebar)}.section-shell{padding:42px clamp(26px,4vw,64px);border-bottom:1px solid var(--line)}.hero-clean{min-height:650px;display:grid;grid-template-columns:minmax(340px,.85fr) minmax(520px,1.45fr);gap:44px;align-items:center;background:#030303}.hero-intro h1{margin:7px 0 22px;font-family:var(--display);font-size:clamp(74px,7vw,122px);font-weight:400;line-height:.82;letter-spacing:.005em;text-transform:uppercase}.hero-intro h1 span{color:#fff}.hero-copy{max-width:520px;color:#aaa;font-size:14px;line-height:1.75}.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.hero-stats{display:grid;grid-template-columns:repeat(3,1fr);max-width:560px;margin-top:28px;border-top:1px solid var(--line)}.hero-stats div{padding:18px 16px 0 0;border-right:1px solid var(--line)}.hero-stats div:last-child{border-right:0;padding-left:14px}.hero-stats strong{display:block;color:var(--gold);font-family:var(--display);font-size:34px;font-weight:400}.hero-stats span{color:#777;font-size:8px;font-weight:800;letter-spacing:.13em;text-transform:uppercase}.featured-project{position:relative;min-height:450px;border:1px solid rgba(217,166,32,.55);overflow:hidden;background:#080808}.featured-project img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;filter:saturate(.85) contrast(1.08);transition:transform .7s}.featured-project:hover img{transform:scale(1.025)}.featured-shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(2,2,2,.96) 0%,rgba(3,3,3,.7) 43%,rgba(3,3,3,.14) 76%,rgba(3,3,3,.05) 100%),linear-gradient(to top,rgba(0,0,0,.7),transparent 48%)}.featured-copy{position:absolute;z-index:2;left:30px;top:32px;max-width:54%}.featured-copy h2{margin:12px 0 10px;font-family:var(--display);font-size:clamp(48px,5vw,78px);font-weight:400;line-height:.83;text-transform:uppercase}.featured-copy h2 span{color:var(--gold);font-size:.58em;letter-spacing:.04em}.featured-copy>p:not(.kicker){color:#aaa}.featured-watch{display:inline-flex;align-items:center;gap:12px;margin-top:18px;color:var(--gold);font-size:9px;font-weight:800;letter-spacing:.13em;text-transform:uppercase}.featured-watch i{width:42px;height:42px;display:grid;place-items:center;border:1px solid var(--gold);border-radius:50%;font-style:normal}.featured-index{position:absolute;z-index:2;right:24px;bottom:20px;display:flex;align-items:center;gap:12px}.featured-index b{color:var(--gold);font-family:var(--display);font-size:24px;font-weight:400}.featured-index span{width:64px;height:1px;background:var(--gold)}.featured-index small{color:#666}
.section-top,.client-heading{display:flex;justify-content:space-between;align-items:end;gap:30px;margin-bottom:20px}.section-top h2,.client-heading h2,.about-copy h2,.contact-copy h2,.showreel-card h2{font-family:var(--display);font-weight:400;text-transform:uppercase;margin:0;font-size:clamp(48px,5.2vw,82px);line-height:.88}.section-top>a{color:var(--gold);font-size:9px;font-weight:800;letter-spacing:.13em;text-transform:uppercase}.section-top>p,.client-heading>p{max-width:440px;color:#777;font-size:12px}.selected-row{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}.selected-card{min-width:0;border:1px solid var(--line);background:#080808;cursor:pointer;transition:.25s;overflow:hidden}.selected-card:hover{border-color:rgba(217,166,32,.55);transform:translateY(-3px)}.selected-media{position:relative;aspect-ratio:16/9;overflow:hidden;background:#111}.selected-media img{width:100%;height:100%;object-fit:cover;display:block;transition:.45s}.selected-card:hover img{transform:scale(1.04)}.play-button{position:absolute;left:13px;bottom:13px;width:34px;height:34px;border:1px solid rgba(217,166,32,.8);border-radius:50%;display:grid;place-items:center;background:rgba(0,0,0,.66);color:var(--gold);font-size:10px}.selected-meta{padding:13px 14px 15px;min-height:112px}.selected-meta p{margin:0 0 5px;color:var(--gold);font-size:8px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}.selected-meta h3{font-family:var(--display);font-size:25px;line-height:.94;font-weight:400;text-transform:uppercase;margin:0 0 7px}.selected-meta small{color:#777;font-size:9px}
.clients-section{overflow:hidden}.client-heading{align-items:end}.client-marquee{width:100%;overflow:hidden;border-top:1px solid rgba(217,166,32,.22);border-bottom:1px solid rgba(217,166,32,.22);padding:8px 0}.client-marquee+.client-marquee{margin-top:8px}.client-track{display:flex;width:max-content;will-change:transform}.client-group{display:flex;gap:8px;padding-right:8px}.client-logo-card{flex:0 0 auto;width:220px;height:80px;padding:10px 16px;border:1px solid var(--line);background:#060606;display:flex;align-items:center;gap:13px;transition:.25s}.client-logo-card:hover{border-color:rgba(217,166,32,.65);background:#0a0906}.client-logo-card img{width:34px;height:34px;object-fit:contain;filter:grayscale(1) brightness(1.55) contrast(.9);opacity:.8}.client-logo-card:hover img{filter:grayscale(0) brightness(1.1);opacity:1}.client-monogram{display:none;width:34px;height:34px;place-items:center;border:1px solid rgba(217,166,32,.45);color:var(--gold);font-family:var(--display);font-size:17px;line-height:1}.client-monogram.always{display:grid}.client-logo-card>span:last-child{color:#aaa;font-family:var(--display);font-size:17px;line-height:1;text-transform:uppercase;letter-spacing:.045em}.client-logo-card:hover>span:last-child{color:#fff}.client-marquee-left .client-track{animation:clientLeft 78s linear infinite}.client-marquee-right .client-track{animation:clientRight 86s linear infinite}.clients-section:hover .client-track{animation-play-state:paused}@keyframes clientLeft{from{transform:translateX(0)}to{transform:translateX(-50%)}}@keyframes clientRight{from{transform:translateX(-50%)}to{transform:translateX(0)}}
.category-grid{display:grid;grid-template-columns:repeat(3,1fr);border-left:1px solid var(--line);border-top:1px solid var(--line)}.category-card{position:relative;min-height:190px;padding:22px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);background:#050505;transition:.25s}.category-card:hover{background:#0a0906}.category-card>span{color:#5b5b57;font-size:9px}.category-card h3{font-family:var(--display);font-size:34px;line-height:.92;font-weight:400;text-transform:uppercase;margin:26px 0 10px}.category-card p{color:#777;margin:0;max-width:250px}.category-card b{position:absolute;left:22px;bottom:18px;color:var(--gold);font-size:8px;letter-spacing:.12em;text-transform:uppercase}.showreel-card{display:flex;justify-content:space-between;align-items:end;gap:40px;padding:34px;border:1px solid rgba(217,166,32,.32);background:#050505}.showreel-card p:not(.kicker){max-width:580px;color:#888}.about-section{display:grid;grid-template-columns:minmax(300px,.8fr) minmax(360px,1.2fr);gap:36px;align-items:stretch}.about-photo{position:relative;margin:0;border:1px solid var(--line);min-height:460px;overflow:hidden}.about-photo img{width:100%;height:100%;min-height:460px;object-fit:cover;object-position:center 8%;display:block;filter:saturate(.86)}.about-photo:after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.9),transparent 58%)}.about-photo figcaption{position:absolute;z-index:2;left:20px;right:20px;bottom:18px;display:flex;justify-content:space-between;align-items:end}.about-photo strong{font-family:var(--display);font-size:30px;font-weight:400;text-transform:uppercase}.about-photo span{color:var(--gold);font-size:8px;letter-spacing:.13em;text-transform:uppercase}.about-copy{padding:24px 0}.about-copy>p:not(.kicker){max-width:700px;color:#999;font-size:14px;line-height:1.75}.about-tags{display:flex;gap:8px;flex-wrap:wrap;margin-top:22px}.about-tags span{border:1px solid var(--line);padding:9px 11px;color:#aaa;font-size:8px;letter-spacing:.11em;text-transform:uppercase}.contact-section{display:flex;align-items:end;justify-content:space-between;gap:30px;padding-top:72px;padding-bottom:72px}.contact-links{display:flex;gap:18px;flex-wrap:wrap;margin-top:22px}.contact-links a{color:#999;border-bottom:1px solid var(--line);padding-bottom:4px;font-size:10px}.contact-links a:hover{color:var(--gold);border-color:var(--gold)}.site-footer{margin-left:var(--sidebar);padding:24px clamp(26px,4vw,64px);display:flex;align-items:center;justify-content:space-between;gap:24px;border-top:1px solid var(--line);color:#666}.site-footer>strong{color:var(--gold);font-family:Georgia,serif;font-size:30px;font-weight:400}.site-footer p{margin:0;font-size:9px}.site-footer>div{display:flex;gap:15px;font-size:9px;text-transform:uppercase}.reveal{opacity:0;transform:translateY(16px);transition:opacity .65s ease,transform .65s ease}.reveal.visible{opacity:1;transform:none}
.video-modal{position:fixed;inset:0;z-index:200;display:grid;place-items:center;padding:32px;background:rgba(0,0,0,.95);opacity:0;visibility:hidden;transition:.25s}.video-modal.open{opacity:1;visibility:visible}.video-modal-inner{width:min(1180px,100%);max-height:calc(100svh - 64px);overflow:auto}.video-modal-heading{margin-bottom:14px}.video-modal-heading h2{font-family:var(--display);font-size:clamp(42px,6vw,76px);font-weight:400;line-height:.95;text-transform:uppercase;margin:0}.video-modal video{display:block;width:100%;max-height:74svh;background:#000;border:1px solid var(--line)}.video-modal-close{position:fixed;top:18px;right:22px;width:46px;height:46px;border:1px solid rgba(255,255,255,.25);background:#050505;color:#fff;font-size:30px;cursor:pointer}.video-modal-close:hover{color:var(--gold);border-color:var(--gold)}body.video-open{overflow:hidden}.toast{display:none}
@media(max-width:1250px){:root{--sidebar:190px}.hero-clean{grid-template-columns:1fr;min-height:auto}.featured-project{min-height:430px}.selected-row{grid-template-columns:repeat(3,1fr)}.selected-card:nth-child(n+4){display:block}.client-logo-card{width:205px}.category-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:860px){:root{--sidebar:0px}.portfolio-sidebar{display:none}.site-main,.site-footer{margin-left:0}.site-header{position:sticky;top:0;z-index:80;height:70px;padding:0 20px;display:flex;align-items:center;justify-content:space-between;background:rgba(3,3,3,.96);border-bottom:1px solid var(--line)}.brand{font-family:Georgia,serif;color:var(--gold);font-size:28px}.header-cta{display:none}.menu-toggle{width:42px;height:42px;border:1px solid var(--line);background:#050505;display:flex;flex-direction:column;justify-content:center;gap:6px;padding:0 10px}.menu-toggle span{display:block;height:1px;background:#ddd}.main-nav{position:fixed;inset:70px 0 auto 0;background:#050505;border-bottom:1px solid var(--line);padding:18px 20px;display:none;flex-direction:column}.main-nav.open{display:flex}.main-nav a{padding:12px 0;border-bottom:1px solid var(--line);font-size:10px;text-transform:uppercase;letter-spacing:.12em}.section-shell{padding:34px 20px}.hero-clean{gap:24px}.hero-intro h1{font-size:clamp(64px,18vw,94px)}.featured-project{min-height:400px}.featured-copy{left:20px;top:24px;max-width:68%}.featured-copy h2{font-size:56px}.selected-row{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:10px}.selected-card{min-width:280px;scroll-snap-align:start}.client-heading,.section-top{align-items:flex-start;flex-direction:column}.client-heading>p,.section-top>p{max-width:100%}.client-marquee{overflow-x:auto;scrollbar-width:none}.client-marquee::-webkit-scrollbar{display:none}.client-track{animation:none!important;transform:none!important}.client-group[aria-hidden="true"]{display:none}.client-logo-card{width:210px}.category-grid{grid-template-columns:1fr 1fr}.about-section{grid-template-columns:1fr}.showreel-card,.contact-section{align-items:flex-start;flex-direction:column}.site-footer{align-items:flex-start;flex-direction:column}}
@media(max-width:560px){.hero-stats{grid-template-columns:1fr 1fr}.hero-stats div:nth-child(2){border-right:0}.hero-stats div:last-child{grid-column:1/-1;padding-left:0}.featured-project{min-height:370px}.featured-copy{max-width:82%}.featured-copy h2{font-size:48px}.category-grid{grid-template-columns:1fr}.client-logo-card{width:188px;height:70px}.client-logo-card>span:last-child{font-size:15px}.contact-section{padding-top:50px;padding-bottom:50px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.reveal{opacity:1;transform:none;transition:none}.client-track{animation:none!important;transform:none!important}.client-marquee{overflow-x:auto}.client-group[aria-hidden="true"]{display:none}}
'''

Path("index.html").write_text(index, encoding="utf-8")
Path("styles.css").write_text(styles, encoding="utf-8")

# Preserve all current category data and video placements from the live script,
# while pinning the two areas that have previously regressed during deployments.
script_path = Path("script.js")
if script_path.exists():
    text = script_path.read_text(encoding="utf-8")
    marker = "const categoryData = "
    try:
        start = text.index(marker) + len(marker)
        function_start = text.index("function escapeHTML", start)
        raw = text[start:function_start].rstrip()
        if raw.endswith(";"):
            raw = raw[:-1].rstrip()
        data = json.loads(raw)

        # Qowa Fi Alby: always use the verified YouTube source, never the broken local files.
        institutional = data.get("institutional", {})
        qowa = next((p for p in institutional.get("projects", []) if p.get("index") == "SI01" or "Qowa Fi Alby" in p.get("title", "")), None)
        if qowa:
            qowa.update({
                "title": "Hospital 57357 — Qowa Fi Alby",
                "subtitle": "Music Video · Video Editing",
                "image": "https://i.ytimg.com/vi/2KVyASYThgw/hqdefault.jpg",
                "imageFallback": "assets/hospital-57357.webp",
                "youtube": "2KVyASYThgw",
                "badge": "Watch Music Video",
            })
            qowa.pop("video", None)
            institutional["cover"] = "https://i.ytimg.com/vi/2KVyASYThgw/hqdefault.jpg"

        # My Guest: keep all five videos and their English titles fixed.
        tv = data.get("tv-programs", {})
        collections = tv.setdefault("collections", {})
        guest_key = "my-guest-moataz-el-demerdash"
        guest = collections.get(guest_key)
        if guest:
            for project in guest.get("projects", []):
                video_id = project.get("youtube")
                if video_id in MY_GUEST_TITLES:
                    project["title"] = MY_GUEST_TITLES[video_id]
                    project["subtitle"] = "TV Program Edit"
        updated = json.dumps(data, ensure_ascii=False, indent=2)
        text = text[:start] + updated + ";\n\n" + text[function_start:]
        script_path.write_text(text, encoding="utf-8")
    except Exception as exc:
        print(f"Category data patch skipped: {exc}")

print(f"Hybrid black-gold portfolio built with {len(CLIENTS)} restored clients.")
