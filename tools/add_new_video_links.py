from pathlib import Path
import json
import re
import urllib.parse
import urllib.request


def youtube_title(video_id, fallback):
    url = 'https://www.youtube.com/oembed?' + urllib.parse.urlencode({
        'url': f'https://www.youtube.com/watch?v={video_id}',
        'format': 'json'
    })
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as response:
            data = json.loads(response.read().decode('utf-8'))
        title = str(data.get('title') or '').strip()
        if title:
            print(f'YouTube title {video_id}: {title}')
            return title
    except Exception as exc:
        print(f'Could not resolve YouTube title for {video_id}: {exc}')
    return fallback


def js(value):
    return json.dumps(value, ensure_ascii=False)

# Resolve titles directly from YouTube so cards always use the real uploaded video name.
ids = {
    'SYQvIrjg8qw': 'Commercial',
    'gLtyCZRuCCo': 'Series Video',
    'G1aMXgXTAog': 'Selected Work',
    'fbrKZPloehw': 'Selected Work',
    'T1VOBnWPwtE': 'Selected Work',
    '0UY-_mTpUDA': 'Selected Work',
    'oIS4SghLtSs': 'Selected Work',
    's72BulxLJgM': 'Selected Work',
    '5jaNOku5Tw0': 'Selected Work',
    'N4uGPUETGb4': 'Al Ahly Club Video',
    '1eFghNwpODA': 'Al Ahly Club Video',
    '8YHgTTQOKdo': 'Cairo International Film Festival Video',
}
titles = {video_id: youtube_title(video_id, fallback) for video_id, fallback in ids.items()}

script_path = Path('script.js')
text = script_path.read_text(encoding='utf-8')
marker = "function escapeHTML(value='')"
if marker not in text:
    raise RuntimeError('Could not find categoryData insertion point')

more_ids = ['G1aMXgXTAog','fbrKZPloehw','T1VOBnWPwtE','0UY-_mTpUDA','oIS4SghLtSs','s72BulxLJgM','5jaNOku5Tw0']
more_projects = []
for i, video_id in enumerate(more_ids, start=1):
    more_projects.append(
        "    { title:%s, subtitle:'Additional Project · Video Editing', index:'MW%02d', image:'https://i.ytimg.com/vi/%s/hqdefault.jpg', youtube:'%s', badge:'Watch Video' }"
        % (js(titles[video_id]), i, video_id, video_id)
    )

patch = f'''\n// PORTFOLIO VIDEO ADDITIONS START\nif (!categoryData.commercial.projects.some(p => p.youtube === 'SYQvIrjg8qw')) {{\n  categoryData.commercial.projects.push({{\n    title:{js(titles['SYQvIrjg8qw'])}, subtitle:'Commercial · Video Editing', index:'AD03',\n    image:'https://i.ytimg.com/vi/SYQvIrjg8qw/hqdefault.jpg', imageFallback:'assets/toto-link-commercial.webp',\n    youtube:'SYQvIrjg8qw', badge:'Watch Ad'\n  }});\n}}\n\nif (!categoryData.series.projects.some(p => p.youtube === 'gLtyCZRuCCo')) {{\n  categoryData.series.projects.push({{\n    title:{js(titles['gLtyCZRuCCo'])}, subtitle:'Series · Video Editing', index:'S03',\n    image:'https://i.ytimg.com/vi/gLtyCZRuCCo/hqdefault.jpg', imageFallback:'assets/teatro-series-promo.webp',\n    youtube:'gLtyCZRuCCo', badge:'Watch Video'\n  }});\n}}\n\ncategoryData['more-work'] = {{\n  title:'More Selected Work',\n  kicker:'Additional Projects',\n  description:'A curated collection of additional edits across different formats and subjects.',\n  cover:'https://i.ytimg.com/vi/G1aMXgXTAog/hqdefault.jpg',\n  projects:[\n{',\n'.join(more_projects)}\n  ]\n}};\n// PORTFOLIO VIDEO ADDITIONS END\n\n'''

block = re.compile(r"// PORTFOLIO VIDEO ADDITIONS START[\s\S]*?// PORTFOLIO VIDEO ADDITIONS END\n*", re.M)
if block.search(text):
    text = block.sub(patch, text, count=1)
else:
    text = text.replace(marker, patch + marker, 1)
script_path.write_text(text, encoding='utf-8')

# Build the live Sports and Events categories too. site-updates.js is loaded after script.js,
# so these are the definitions visitors actually see.
updates_path = Path('site-updates.js')
updates = updates_path.read_text(encoding='utf-8')

sports_block = f'''categoryData.sports = {{
        title: 'Sports',
        kicker: 'Sports Content',
        description: 'Fast-paced sports edits, promotional content and club-focused storytelling.',
        cover: 'assets/al-ahly.webp',
        projects: [
          {{ title:'Al Ahly Club', subtitle:'Sports Content · Video Collection', index:'SP01', image:'assets/al-ahly.webp', collection:'al-ahly-club', badge:'Open Collection' }},
          {{ title:'ON Sport', subtitle:'Sports Channel · Selected Work', index:'SP02', image:'assets/client-logos/on-sport.png', imageFallback:'assets/al-ahly.webp' }}
        ],
        collections: {{
          'al-ahly-club': {{
            title:'Al Ahly Club',
            kicker:'Sports Content',
            description:'Selected Al Ahly Club edits and promotional sports content.',
            cover:'assets/al-ahly.webp',
            projects:[
              {{ title:{js(titles['N4uGPUETGb4'])}, subtitle:'Al Ahly Club · Sports Edit', index:'AH01', image:'https://i.ytimg.com/vi/N4uGPUETGb4/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'N4uGPUETGb4', badge:'Watch Video' }},
              {{ title:{js(titles['1eFghNwpODA'])}, subtitle:'Al Ahly Club · Sports Edit', index:'AH02', image:'https://i.ytimg.com/vi/1eFghNwpODA/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'1eFghNwpODA', badge:'Watch Video' }}
            ]
          }}
        }}
      }};'''

events_block = f'''categoryData.events = {{
        title: 'Events',
        kicker: 'Event Coverage',
        description: 'Festival coverage, live-event storytelling and event-driven edits.',
        cover: 'assets/ciff.webp',
        projects: [
          {{ title:'Cairo International Film Festival', subtitle:'Event Coverage · Video Collection', index:'EV01', image:'assets/ciff.webp', collection:'ciff', badge:'Open Collection' }}
        ],
        collections: {{
          ciff: {{
            title:'Cairo International Film Festival',
            kicker:'Event Coverage',
            description:'Selected Cairo International Film Festival edits and event coverage.',
            cover:'assets/ciff.webp',
            projects:[
              {{ title:{js(titles['8YHgTTQOKdo'])}, subtitle:'CIFF · Event Edit', index:'CIFF01', image:'https://i.ytimg.com/vi/8YHgTTQOKdo/hqdefault.jpg', imageFallback:'assets/ciff.webp', youtube:'8YHgTTQOKdo', badge:'Watch Video' }}
            ]
          }}
        }}
      }};'''

updates, n1 = re.subn(r"categoryData\.sports = \{[\s\S]*?\n      \};", sports_block, updates, count=1)
updates, n2 = re.subn(r"categoryData\.events = \{[\s\S]*?\n      \};", events_block, updates, count=1)
if n1 != 1 or n2 != 1:
    raise RuntimeError(f'Could not update live Sports/Events blocks: sports={n1}, events={n2}')
updates_path.write_text(updates, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
if 'category=more-work' not in html:
    ai_card = '<a class="category-card reveal category-link" href="index.html?category=ai-work"><span>07</span><h3>AI Work</h3><p>AI-assisted visual storytelling and creative experiments.</p><b>View Projects →</b></a>'
    more_card = '<a class="category-card reveal category-link" href="index.html?category=more-work"><span>08</span><h3>More Selected<br>Work</h3><p>Additional selected projects across different formats.</p><b>View Projects →</b></a>'
    if ai_card not in html:
        raise RuntimeError('AI Work category-card insertion anchor not found')
    html = html.replace(ai_card, ai_card + '\n        ' + more_card, 1)
index_path.write_text(html, encoding='utf-8')

print('Applied real YouTube titles and organized Sports, CIFF Events, Series and More Selected Work.')
