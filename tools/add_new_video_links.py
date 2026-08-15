from pathlib import Path
import re

script_path = Path('script.js')
text = script_path.read_text(encoding='utf-8')

marker = "function escapeHTML(value='')"
if marker not in text:
    raise RuntimeError('Could not find categoryData insertion point')

patch = r'''
// PORTFOLIO VIDEO ADDITIONS START
if (!categoryData.commercial.projects.some(p => p.youtube === 'SYQvIrjg8qw')) {
  categoryData.commercial.projects.push({
    title:'Commercial — Selected Ad', subtitle:'Commercial · Video Editing', index:'AD03',
    image:'https://i.ytimg.com/vi/SYQvIrjg8qw/hqdefault.jpg', imageFallback:'assets/toto-link-commercial.webp',
    youtube:'SYQvIrjg8qw', badge:'Watch Ad'
  });
}

if (!categoryData.series.projects.some(p => p.youtube === 'gLtyCZRuCCo')) {
  categoryData.series.projects.push({
    title:'Series — Selected Video', subtitle:'Series · Video Editing', index:'S03',
    image:'https://i.ytimg.com/vi/gLtyCZRuCCo/hqdefault.jpg', imageFallback:'assets/teatro-series-promo.webp',
    youtube:'gLtyCZRuCCo', badge:'Watch Video'
  });
}

categoryData['more-work'] = {
  title:'More Selected Work',
  kicker:'Additional Projects',
  description:'A curated collection of additional edits across different formats and subjects.',
  cover:'https://i.ytimg.com/vi/G1aMXgXTAog/hqdefault.jpg',
  projects:[
    { title:'Selected Work 01', subtitle:'Additional Project · Video Editing', index:'MW01', image:'https://i.ytimg.com/vi/G1aMXgXTAog/hqdefault.jpg', youtube:'G1aMXgXTAog', badge:'Watch Video' },
    { title:'Selected Work 02', subtitle:'Additional Project · Video Editing', index:'MW02', image:'https://i.ytimg.com/vi/fbrKZPloehw/hqdefault.jpg', youtube:'fbrKZPloehw', badge:'Watch Video' },
    { title:'Selected Work 03', subtitle:'Additional Project · Video Editing', index:'MW03', image:'https://i.ytimg.com/vi/T1VOBnWPwtE/hqdefault.jpg', youtube:'T1VOBnWPwtE', badge:'Watch Video' },
    { title:'Selected Work 04', subtitle:'Additional Project · Video Editing', index:'MW04', image:'https://i.ytimg.com/vi/0UY-_mTpUDA/hqdefault.jpg', youtube:'0UY-_mTpUDA', badge:'Watch Video' },
    { title:'Selected Work 05', subtitle:'Additional Project · Video Editing', index:'MW05', image:'https://i.ytimg.com/vi/oIS4SghLtSs/hqdefault.jpg', youtube:'oIS4SghLtSs', badge:'Watch Video' },
    { title:'Selected Work 06', subtitle:'Additional Project · Video Editing', index:'MW06', image:'https://i.ytimg.com/vi/s72BulxLJgM/hqdefault.jpg', youtube:'s72BulxLJgM', badge:'Watch Video' },
    { title:'Selected Work 07', subtitle:'Additional Project · Video Editing', index:'MW07', image:'https://i.ytimg.com/vi/5jaNOku5Tw0/hqdefault.jpg', youtube:'5jaNOku5Tw0', badge:'Watch Video' }
  ]
};
// PORTFOLIO VIDEO ADDITIONS END

'''

block = re.compile(r"// PORTFOLIO VIDEO ADDITIONS START[\s\S]*?// PORTFOLIO VIDEO ADDITIONS END\n*", re.M)
if block.search(text):
    text = block.sub(patch, text, count=1)
else:
    text = text.replace(marker, patch + marker, 1)

script_path.write_text(text, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
if 'category=more-work' not in html:
    ai_card = '<a class="category-card reveal category-link" href="index.html?category=ai-work"><span>07</span><h3>AI Work</h3><p>AI-assisted visual storytelling and creative experiments.</p><b>View Projects →</b></a>'
    more_card = '<a class="category-card reveal category-link" href="index.html?category=more-work"><span>08</span><h3>More Selected<br>Work</h3><p>Additional selected projects across different formats.</p><b>View Projects →</b></a>'
    if ai_card not in html:
        raise RuntimeError('AI Work category-card insertion anchor not found')
    html = html.replace(ai_card, ai_card + '\n        ' + more_card, 1)
index_path.write_text(html, encoding='utf-8')

print('Added commercial, series and More Selected Work YouTube videos without duplicates.')
