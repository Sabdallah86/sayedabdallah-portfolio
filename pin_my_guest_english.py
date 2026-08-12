from pathlib import Path
import json
import re
import urllib.parse
import urllib.request

BASE = 'https://sayedabdallah.pages.dev/'
TITLES = {
    '_5EHAht5a1M': 'Nader Abbassy — My Guest with Moataz El Demerdash',
    '_Sd8QUoXoaI': 'Magdy Abdelghany — My Guest with Moataz El Demerdash',
    '_7irVnrKMmM': 'Hany Ramzy — My Guest with Moataz El Demerdash',
    '_vUQ8quTX-w': 'Salah Abdallah — My Guest with Moataz El Demerdash',
    'FwVPJqsdXBc': 'Amr Mostafa — My Guest with Moataz El Demerdash',
}


def download(url, target, required=True):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()
        if not data:
            raise RuntimeError('empty response')
        path = Path(target)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return True
    except Exception as exc:
        if required:
            raise
        print(f'Skipping {url}: {exc}')
        return False


for filename in ['index.html', 'script.js', 'styles.css', 'category-pages.css', 'favicon.svg', 'robots.txt']:
    download(urllib.parse.urljoin(BASE, filename), filename)

refs = set()
for filename in ['index.html', 'script.js', 'styles.css', 'category-pages.css']:
    text = Path(filename).read_text(encoding='utf-8', errors='ignore')
    refs.update(re.findall(r'assets/[A-Za-z0-9_./-]+\.(?:webp|png|jpg|jpeg|svg|mp4|webm)', text, flags=re.I))
for ref in sorted(refs):
    download(urllib.parse.urljoin(BASE, ref), ref, required=False)

# Pin titles in categoryData.
script_path = Path('script.js')
text = script_path.read_text(encoding='utf-8')
marker = 'const categoryData = '
start = text.index(marker) + len(marker)
function_start = text.index('function escapeHTML', start)
raw = text[start:function_start].rstrip()
if raw.endswith(';'):
    raw = raw[:-1].rstrip()
data = json.loads(raw)
collection = data.get('tv-programs', {}).get('collections', {}).get('my-guest-moataz-el-demerdash')
if not collection:
    raise RuntimeError('My Guest collection not found')
found = set()
for project in collection.get('projects', []):
    video_id = project.get('youtube')
    if video_id in TITLES:
        project['title'] = TITLES[video_id]
        project['subtitle'] = 'TV Program Edit'
        found.add(video_id)
if found != set(TITLES):
    raise RuntimeError(f'Missing My Guest videos: {set(TITLES) - found}')
updated = json.dumps(data, ensure_ascii=False, indent=2)
text = text[:start] + updated + ';\n\n' + text[function_start:]
script_path.write_text(text, encoding='utf-8')

# Persistent UI lock. The primary deploy workflow starts from the current live
# index.html, so this block is carried forward in later deployments.
index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
html = re.sub(r'\n?<!-- MY_GUEST_ENGLISH_LOCK_START -->[\s\S]*?<!-- MY_GUEST_ENGLISH_LOCK_END -->\n?', '\n', html)
lock = '''
<!-- MY_GUEST_ENGLISH_LOCK_START -->
<script id="my-guest-english-title-lock">
(() => {
  const titles = new Map([
    ['_5EHAht5a1M', 'Nader Abbassy — My Guest with Moataz El Demerdash'],
    ['_Sd8QUoXoaI', 'Magdy Abdelghany — My Guest with Moataz El Demerdash'],
    ['_7irVnrKMmM', 'Hany Ramzy — My Guest with Moataz El Demerdash'],
    ['_vUQ8quTX-w', 'Salah Abdallah — My Guest with Moataz El Demerdash'],
    ['FwVPJqsdXBc', 'Amr Mostafa — My Guest with Moataz El Demerdash']
  ]);
  let applying = false;
  const apply = () => {
    if (applying) return;
    applying = true;
    document.querySelectorAll('[data-youtube]').forEach(card => {
      const title = titles.get(card.dataset.youtube);
      if (!title) return;
      card.dataset.title = title;
      card.setAttribute('aria-label', `Play ${title}`);
      const heading = card.querySelector('.project-info h3, h3');
      if (heading && heading.textContent.trim() !== title) heading.textContent = title;
      const subtitle = card.querySelector('.project-info p, p');
      if (subtitle && subtitle.textContent.trim() !== 'TV Program Edit') subtitle.textContent = 'TV Program Edit';
      const image = card.querySelector('img');
      if (image) image.alt = title;
    });
    applying = false;
  };
  const start = () => {
    apply();
    new MutationObserver(apply).observe(document.body, {childList: true, subtree: true});
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, {once: true});
  else start();
})();
</script>
<!-- MY_GUEST_ENGLISH_LOCK_END -->
'''
if '</body>' not in html:
    raise RuntimeError('Closing body tag not found')
html = html.replace('</body>', lock + '\n</body>', 1)
index_path.write_text(html, encoding='utf-8')

print('Pinned all five My Guest titles in English.')
