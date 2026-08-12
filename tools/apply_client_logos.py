from pathlib import Path
import base64
import re
from html import escape

CLIENTS = ['Al-Ahram Agency', 'Al-Jala Military Hospital', '3DI - Yasser Sami', 'TERA SOFT', 'MICA EGYPT', 'Al Tahrir Channel', 'TEN Channel', 'Al Ahly Club', 'CBC Channel', 'Cairo International Film Festival', 'Egypt Air', 'Egyptian Countryside', 'Egyptian Television', 'EL Nahar Channel', 'El Gouna Film Festival', 'Good News', 'Hama Film Production', 'Hospital 57357', 'I Production', 'Misr El Kheir Foundation', 'Ministry of Migration', 'Motor TV', 'ON E Channel', 'ON Sport Channel', 'Rotary', 'Sada El Balad Channel', 'SATUC', 'Saudi Arabia', 'Souad Kafafi Hospital', 'SQUARE Media Production', 'Studio 24', 'Sudanese Television', 'Toto Link', 'Turkish Factory', 'AlWathaeqya Channel', 'Kuwait Television', 'Shasha Platform']
NAME_TO_LOGO = {'Al-Ahram Agency': 'al-ahram', 'Al-Jala Military Hospital': 'galaa-medical', 'MICA EGYPT': 'mica', 'Al Tahrir Channel': 'al-tahrir', 'TEN Channel': 'ten', 'CBC Channel': 'cbc', 'Egypt Air': 'egyptair', 'EL Nahar Channel': 'al-nahar', 'Hospital 57357': 'hospital-57357', 'ON E Channel': 'on', 'SATUC': 'satuc', 'Souad Kafafi Hospital': 'souad-kafafi', 'Toto Link': 'toto-link', 'AlWathaeqya Channel': 'al-wathaeqya', 'Shasha Platform': 'shasha'}
LOGOS = {'al-wathaeqya': 'iVBORw0KGgoAAAANSUhEUgAAAJYAAABfCAYAAABH4j8SAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42uydCZxV1ZX/v3ftu+9BQJqCgigiKEYRF4oJMdpk1DaxSROjA1GbNJpMbXJt0jQm1JiYxuhYozEm0WiwR+NCKiIiqGBYQRQUVlQGEFjz3rv3/2jzg3Pvnvvvfe+6wTn+X4eufec+6959zznve95z0vCIIAAQIECBAgQIAAATIFAUKcDgiWTAECBAgQIECAAAECBAhxxCWAAAECBAgQIECAAAECBBYFQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'galaa-medical': 'iVBORw0KGgoAAAANSUhEUgAAAG4AAABuCAYAAACf0P7lAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAeqUlEQVR42u2de3wUxd3HP7N7eXK5QEhCCBEuKigQiSgQESqCiiKCNVBRxYJItf5r21q1tbZaq1Vr/WmrVv1i7VqtVav1VUQRRARRxYJIgQRCQggQcpOTk3u7sz/2Y3Z3N3vn7j2bMzM7u7M7uzfz+XzmzM7OzvM7M/v7zPd5N5fDMIzD/9+/gCnwgQB3CBAgQIAAAT9NgBDnBIIIAQIECBAgQIAAAQIE4nEKECBAgAABAgQIECBAgMCiAAgQIECBAgQIEPif+A/4m4mvMOsjPAAAAABJRU5ErkJggg==', 'shasha': 'iVBORw0KGgoAAAANSUhEUgAAAS0AAABiCAYAAAAWTwCPAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAdY0lEQVR42u2deZxV1ZnHP/e5d+4FAgKCKIpuQkSJUdQFRa1VZ0yM3Vo3ph1rbWotOq22qk2jddpqrdVq61y3VmuNMfE2TgxIY4yAKKIIigIKsgC979z5//5Q55xb53HuuXfvvfc5v1+vXHLOPfece865z/s8z/s8B4ZhGP7//QucAh8IcIcAAQIECBAgQOA6AUJcDgiWTAECBAgQIECAAAECBAhxxCWAAAECBAgQIECAAAECBBYFQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'mica': 'iVBORw0KGgoAAAANSUhEUgAAAHIAAABfCAYAAAB7r8BBAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42u2deXxV1bnHP/e+e+95QEiEUBQFQRQXcUWxLl1c1WoqtVbXq1Wr1q1W/9rXr1qtVmvVWrXWq1Vbrda6uC5VXBQFcYgKiggqIIKELBAg5Jxz7j3//1/l3PGe97xzzr0n53m+XpJzzz33nHPPeZ7neZ7n+R4Gg8Hg/9+/wCnwQQEPCBAgQIAAAT+YABGPCQQRAgQIECBAgAABAgQIxONAAgQIECBAgAABAgQIEDgUAAGC/wn/A38z8RVm7fmbAAAAAElFTkSuQmCC', 'al-nahar': 'iVBORw0KGgoAAAANSUhEUgAAAOQAAABdCAYAAACa5QReAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42uydeZxV5Z3HP+ec+759gUBWBBXFBUQX0VU0zqZxY0xTtG5q49q0Ws1Wm7RWq7Va67Va61q1dVpN0WjTxNiYxjQxRoMQFBEQFUEX2AHB3Hvu3Pn/n+Wc8Z7znu+c8+45z/P1lPfec875zjnv87zP8zzP8zwMBgMDAwP/B14CT4EPBLhDgAABAgQIEPADCxDiMkCwZAoQIECAAAECBAgQIIgjLgECBAgQIECAAAECBAgsCoAAAQJ+Ev8H/E3EV5i15m/DAAAAAElFTkSuQmCC', 'cbc': 'iVBORw0KGgoAAAANSUhEUgAAAUwAAABeCAYAAADzryF/AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42uyde5xV1ZnHP+eec++9QECCKCIICogLFxQ1Lq1Vq8XoYk3bpm3aNmmbtmnbpG3atmmblGmM0yRxopHExAQFKSiIioogIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'egyptair': 'iVBORw0KGgoAAAANSUhEUgAAAMgAAABMCAYAAABtKx0rAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAedUlEQVR42u2de3wUxd3HP7N7eXK5QEiEUCgKiooRFxQ1q7Va1Wo1W61Wq7Va67VWrVa1Vq1Wq7VqrdVqrdVqrdVqrdVqrdXqurhU1yEoigiigiIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'ten': 'iVBORw0KGgoAAAANSUhEUgAAAOwAAABgCAYAAAAiStVKAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAezUlEQVR42u2de3wUxd3HP7N7eXK5QEiEUCgKiooRFxQ1q7Va1Wo1W61Wq7Va67VWrVa1Vq1Wq7VqrdVqrdVqrdVqrdVqrdXqurhU1yEoigiigiIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'on': 'iVBORw0KGgoAAAANSUhEUgAAAG0AAABfCAYAAADekq/9AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAe6UlEQVR42u2de3wUxd3HP7N7eXK5QEiEUCgKiooRFxQ1q7Va1Wo1W61Wq7Va67VWrVa1Vq1Wq7VqrdVqrdVqrdVqrdVqrdXqurhU1yEoigiigiIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'toto-link': 'iVBORw0KGgoAAAANSUhEUgAAATgAAABQCAYAAACtR6HqAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAeH0lEQVR42u2de3wUxd3HP7N7eXK5QEiEUCgKiooRFxQ1q7Va1Wo1W61Wq7Va67VWrVa1Vq1Wq7VqrdVqrdVqrdVqrdVqrdXqurhU1yEoigiigiIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'souad-kafafi': 'iVBORw0KGgoAAAANSUhEUgAAAXIAAABfCAYAAAD3S0dLAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42uyde5xV1ZnHP+eec++9QECCKCIICogLFxQ1Lq1Vq8XoYk3bpm3aNmmbtmnbpG3atmmblGmM0yRxopHExAQFKSiIioogIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'satuc': 'iVBORw0KGgoAAAANSUhEUgAAANgAAABpCAYAAABmJHGkAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAeZUlEQVR42u2de3wUxd3HP7N7eXK5QEiEUCgKiooRFxQ1q7Va1Wo1W61Wq7Va67VWrVa1Vq1Wq7VqrdVqrdVqrdVqrdVqrdXqurhU1yEoigiigiIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'al-tahrir': 'iVBORw0KGgoAAAANSUhEUgAAAIwAAABfCAYAAABN9i/7AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAfHUlEQVR42u2de3wUxd3HP7N7eXK5QEiEUCgKiooRFxQ1q7Va1Wo1W61Wq7Va67VWrVa1Vq1Wq7VqrdVqrdVqrdVqrdVqrdXqurhU1yEoigiigiIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'hospital-57357': 'iVBORw0KGgoAAAANSUhEUgAAAMgAAABPCAYAAAC+eMMoAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAeAElEQVR42u2de3wUxd3HP7N7eXK5QEiEUCgKiooRFxQ1q7Va1Wo1W61Wq7Va67VWrVa1Vq1Wq7VqrdVqrdVqrdVqrdVqrdXqurhU1yEoigiigiIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg==', 'al-ahram': 'iVBORw0KGgoAAAANSUhEUgAAARQAAAB2CAYAAADK2flgAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42uyde5xV1ZnHP+eec++9QECCKCIICogLFxQ1Lq1Vq8XoYk3bpm3aNmmbtmnbpG3atmmblGmM0yRxopHExAQFKSiIioogIIKCBQJk7r333P//K+eM95xz7j33nHvP8/V65pxzzjnnnPO8z/M8z/M8DwMDAwMD/3//AqfABwLcIUCAAAECBAj4QQWIeEwgQIAAAT+J/wP+ZuIrTE32GwAAAABJRU5ErkJggg=='}

ASSET_DIR = Path("assets/client-logos")
ASSET_DIR.mkdir(parents=True, exist_ok=True)
for slug, payload in LOGOS.items():
    (ASSET_DIR / f"{slug}.png").write_bytes(base64.b64decode(payload))

def brand_item(name):
    slug = NAME_TO_LOGO.get(name)
    safe_name = escape(name)
    if slug:
        return (
            f'<div class="client-brand client-brand-has-logo">'
            f'<span class="client-brand-logo"><img src="assets/client-logos/{slug}.png" alt="{safe_name} logo" loading="lazy"></span>'
            f'<span class="client-brand-name">{safe_name}</span>'
            f'</div>'
        )
    return (
        f'<div class="client-brand client-wordmark">'
        f'<span class="client-brand-name">{safe_name}</span>'
        f'</div>'
    )

row1 = CLIENTS[::2]
row2 = CLIENTS[1::2]
row1_markup = "".join(brand_item(name) for name in row1)
row2_markup = "".join(brand_item(name) for name in row2)

section = f"""
<section class="clients-section section-shell clients-logo-section" id="clients">
  <div class="clients-logo-title reveal"><span>Trusted by Great Brands</span><i></i></div>
  <div class="client-marquee client-marquee-left logo-marquee reveal" aria-label="Client logos row one">
    <span class="client-row-arrow client-row-arrow-left" aria-hidden="true">←</span>
    <div class="client-track">
      <div class="client-group">{row1_markup}</div>
      <div class="client-group" aria-hidden="true">{row1_markup}</div>
    </div>
    <span class="client-row-arrow client-row-arrow-right" aria-hidden="true">→</span>
  </div>
  <div class="client-marquee client-marquee-right logo-marquee reveal" aria-label="Client logos row two">
    <span class="client-row-arrow client-row-arrow-left" aria-hidden="true">←</span>
    <div class="client-track">
      <div class="client-group">{row2_markup}</div>
      <div class="client-group" aria-hidden="true">{row2_markup}</div>
    </div>
    <span class="client-row-arrow client-row-arrow-right" aria-hidden="true">→</span>
  </div>
</section>
"""

index_path = Path("index.html")
html = index_path.read_text(encoding="utf-8")
pattern = re.compile(r'<section class="clients-section section-shell" id="clients">.*?</section>', re.S)
html, count = pattern.subn(section, html, count=1)
if count != 1:
    pattern = re.compile(r'<section class="clients-section section-shell clients-logo-section" id="clients">.*?</section>', re.S)
    html, count = pattern.subn(section, html, count=1)
if count != 1:
    raise RuntimeError("Could not replace clients section")
index_path.write_text(html, encoding="utf-8")

styles_path = Path("styles.css")
styles = styles_path.read_text(encoding="utf-8")
start = "/* CLIENT LOGO STRIP V2 START */"
end = "/* CLIENT LOGO STRIP V2 END */"
styles = re.sub(re.escape(start) + r".*?" + re.escape(end), "", styles, flags=re.S)
css = r"""
/* CLIENT LOGO STRIP V2 START */
.clients-logo-section {
  padding-top: 72px;
  padding-bottom: 76px;
  overflow: hidden;
  background: #030303;
}
.clients-logo-title {
  display:flex;align-items:center;gap:24px;margin-bottom:22px;color:var(--gold);font-size:11px;font-weight:800;letter-spacing:.20em;text-transform:uppercase;
}
.clients-logo-title i {display:block;height:1px;flex:1;background:linear-gradient(90deg,var(--gold),rgba(214,169,50,.12));}
.logo-marquee {position:relative;width:100%;margin:0;padding:24px 44px;overflow:hidden;border-top:1px solid rgba(214,169,50,.48);background:#030303;}
.logo-marquee + .logo-marquee {border-bottom:1px solid rgba(214,169,50,.48);}
.logo-marquee .client-track {display:flex;width:max-content;will-change:transform;}
.logo-marquee .client-group {display:flex;align-items:center;gap:58px;padding-right:58px;}
.client-brand {flex:0 0 auto;display:inline-flex;align-items:center;gap:15px;min-height:78px;padding:0;border:0 !important;background:transparent !important;box-shadow:none !important;color:#d7d7d3;white-space:nowrap;}
.client-brand-logo {width:112px;height:64px;display:flex;align-items:center;justify-content:center;flex:0 0 auto;}
.client-brand-logo img {display:block;max-width:112px;max-height:62px;width:auto;height:auto;object-fit:contain;filter:grayscale(1) brightness(2.7) contrast(.90);opacity:.88;transition:filter .25s ease,opacity .25s ease,transform .25s ease;}
.client-brand-name {font-family:var(--body);font-size:12px;font-weight:700;letter-spacing:.10em;line-height:1.25;text-transform:uppercase;color:#d5d5d2;max-width:190px;white-space:normal;}
.client-wordmark {min-width:160px;}
.client-wordmark .client-brand-name {font-family:var(--display);font-size:23px;font-weight:400;letter-spacing:.055em;color:#bdbdb9;max-width:none;white-space:nowrap;}
.client-brand:hover .client-brand-logo img {filter:grayscale(0) brightness(1.08) contrast(1.02);opacity:1;transform:translateY(-1px);}
.client-brand:hover .client-brand-name {color:#fff;}
.client-row-arrow {position:absolute;top:50%;transform:translateY(-50%);z-index:4;color:var(--gold);font-size:24px;line-height:1;pointer-events:none;}
.client-row-arrow-left {left:6px}.client-row-arrow-right {right:6px}
.logo-marquee::before,.logo-marquee::after {content:"";position:absolute;top:0;bottom:0;width:46px;z-index:3;pointer-events:none;}
.logo-marquee::before {left:0;background:linear-gradient(90deg,#030303 20%,rgba(3,3,3,0));}
.logo-marquee::after {right:0;background:linear-gradient(270deg,#030303 20%,rgba(3,3,3,0));}
.logo-marquee.client-marquee-left .client-track {animation:clientLogoLeft 92s linear infinite;}
.logo-marquee.client-marquee-right .client-track {animation:clientLogoRight 98s linear infinite;}
.logo-marquee:hover .client-track {animation-play-state:paused;}
@keyframes clientLogoLeft {from {transform:translateX(0)} to {transform:translateX(-50%)}}
@keyframes clientLogoRight {from {transform:translateX(-50%)} to {transform:translateX(0)}}
@media (max-width:760px) {
  .clients-logo-section {padding-top:54px;padding-bottom:56px;}
  .logo-marquee {padding:18px 26px;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch;}
  .logo-marquee::-webkit-scrollbar {display:none}
  .logo-marquee .client-track {animation:none !important;transform:none !important;}
  .logo-marquee .client-group[aria-hidden="true"] {display:none;}
  .logo-marquee .client-group {gap:36px;padding-right:0;}
  .client-brand {min-height:70px;gap:12px;}
  .client-brand-logo {width:92px;height:54px;}
  .client-brand-logo img {max-width:92px;max-height:52px;}
  .client-brand-name {font-size:10px;max-width:150px;}
  .client-wordmark {min-width:auto;}
  .client-wordmark .client-brand-name {font-size:20px;}
  .client-row-arrow {display:none;}
}
@media (prefers-reduced-motion: reduce) {
  .logo-marquee .client-track {animation:none !important;transform:none !important;}
  .logo-marquee {overflow-x:auto;}
  .logo-marquee .client-group[aria-hidden="true"] {display:none;}
}
/* CLIENT LOGO STRIP V2 END */
"""
styles_path.write_text(styles.rstrip() + "\n\n" + css + "\n", encoding="utf-8")
print("Applied exact client logos to the two-row black/gold client strip.")