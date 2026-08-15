from pathlib import Path

script_path = Path('script.js')
text = script_path.read_text(encoding='utf-8')

commercial_anchor = "{ title:'SATUC', subtitle:'Branded Promo · Video Editing', index:'AD02', image:'assets/satuc-branded-promo.webp', video:'assets/satuc-branded-promo.mp4', badge:'Watch Promo' }"
commercial_new = commercial_anchor + ",\n      { title:'Commercial — Selected Ad', subtitle:'Commercial · Video Editing', index:'AD03', image:'https://i.ytimg.com/vi/SYQvIrjg8qw/hqdefault.jpg', imageFallback:'assets/toto-link-commercial.webp', youtube:'SYQvIrjg8qw', badge:'Watch Ad' }"
if 'SYQvIrjg8qw' not in text:
    if commercial_anchor not in text:
        raise RuntimeError('Commercial insertion anchor not found')
    text = text.replace(commercial_anchor, commercial_new, 1)

ahly_old = "{ title:'Al Ahly Club', subtitle:'Sports Content · Video Editing', index:'SE01', image:'assets/al-ahly.webp' }"
ahly_new = "{ title:'Al Ahly Club', subtitle:'Sports Content · Video Collection', index:'SE01', image:'assets/al-ahly.webp', collection:'al-ahly-club', badge:'Open Collection' }"
if "collection:'al-ahly-club'" not in text:
    if ahly_old not in text:
        raise RuntimeError('Al Ahly project anchor not found')
    text = text.replace(ahly_old, ahly_new, 1)

sports_projects_end = "      { title:'Cairo International Film Festival', subtitle:'Event Coverage · Video Editing', index:'SE02', image:'assets/ciff.webp' }\n    ]\n  },"
if "'al-ahly-club':{" not in text:
    sports_replacement = "      { title:'Cairo International Film Festival', subtitle:'Event Coverage · Video Editing', index:'SE02', image:'assets/ciff.webp' }\n    ],\n    collections:{\n      'al-ahly-club':{\n        title:'Al Ahly Club',\n        kicker:'Sports Content',\n        description:'Selected Al Ahly Club edits and promotional sports content.',\n        cover:'assets/al-ahly.webp',\n        projects:[\n          { title:'Al Ahly Club — Selected Video 01', subtitle:'Al Ahly Club · Sports Edit', index:'AH01', image:'https://i.ytimg.com/vi/N4uGPUETGb4/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'N4uGPUETGb4', badge:'Watch Video' },\n          { title:'Al Ahly Club — Selected Video 02', subtitle:'Al Ahly Club · Sports Edit', index:'AH02', image:'https://i.ytimg.com/vi/1eFghNwpODA/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'1eFghNwpODA', badge:'Watch Video' }\n        ]\n      }\n    }\n  },"
    if sports_projects_end not in text:
        raise RuntimeError('Sports collection insertion anchor not found')
    text = text.replace(sports_projects_end, sports_replacement, 1)

if "'more-work': {" not in text:
    motion_anchor = "  'motion-graphics': {"
    more_category = "  'more-work': {\n    title:'More Selected Work',\n    kicker:'Additional Projects',\n    description:'A curated collection of additional edits across different formats and subjects.',\n    cover:'https://i.ytimg.com/vi/G1aMXgXTAog/hqdefault.jpg',\n    projects:[\n      { title:'Selected Work 01', subtitle:'Additional Project · Video Editing', index:'MW01', image:'https://i.ytimg.com/vi/G1aMXgXTAog/hqdefault.jpg', youtube:'G1aMXgXTAog', badge:'Watch Video' },\n      { title:'Selected Work 02', subtitle:'Additional Project · Video Editing', index:'MW02', image:'https://i.ytimg.com/vi/fbrKZPloehw/hqdefault.jpg', youtube:'fbrKZPloehw', badge:'Watch Video' },\n      { title:'Selected Work 03', subtitle:'Additional Project · Video Editing', index:'MW03', image:'https://i.ytimg.com/vi/T1VOBnWPwtE/hqdefault.jpg', youtube:'T1VOBnWPwtE', badge:'Watch Video' },\n      { title:'Selected Work 04', subtitle:'Additional Project · Video Editing', index:'MW04', image:'https://i.ytimg.com/vi/0UY-_mTpUDA/hqdefault.jpg', youtube:'0UY-_mTpUDA', badge:'Watch Video' }\n    ]\n  },\n"
    if motion_anchor not in text:
        raise RuntimeError('More Work category insertion anchor not found')
    text = text.replace(motion_anchor, more_category + motion_anchor, 1)

script_path.write_text(text, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
if 'category=more-work' not in html:
    old_motion = '<a class="category-card reveal category-link" href="index.html?category=motion-graphics"><span>06</span><h3>Motion Graphics<br>&amp; 3D</h3><p>Titles, graphics and visual systems.</p><b>View Projects →</b></a>'
    more_card = '<a class="category-card reveal category-link" href="index.html?category=more-work"><span>06</span><h3>More Selected<br>Work</h3><p>Additional selected projects across different formats.</p><b>View Projects →</b></a>'
    new_motion = '<a class="category-card reveal category-link" href="index.html?category=motion-graphics"><span>07</span><h3>Motion Graphics<br>&amp; 3D</h3><p>Titles, graphics and visual systems.</p><b>View Projects →</b></a>'
    if old_motion not in html:
        raise RuntimeError('Home category-card insertion anchor not found')
    html = html.replace(old_motion, more_card + '\n        ' + new_motion, 1)
index_path.write_text(html, encoding='utf-8')

print('Added Al Ahly collection, commercial YouTube ad, and More Selected Work category.')
