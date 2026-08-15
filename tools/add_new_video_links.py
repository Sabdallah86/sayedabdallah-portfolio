from pathlib import Path

script_path = Path('script.js')
text = script_path.read_text(encoding='utf-8')

marker = "function escapeHTML(value='')"
if marker not in text:
    raise RuntimeError('Could not find categoryData insertion point')

if 'PORTFOLIO VIDEO ADDITIONS START' not in text:
    patch = r'''
// PORTFOLIO VIDEO ADDITIONS START
if (!categoryData.commercial.projects.some(p => p.youtube === 'SYQvIrjg8qw')) {
  categoryData.commercial.projects.push({
    title:'Commercial — Selected Ad', subtitle:'Commercial · Video Editing', index:'AD03',
    image:'https://i.ytimg.com/vi/SYQvIrjg8qw/hqdefault.jpg', imageFallback:'assets/toto-link-commercial.webp',
    youtube:'SYQvIrjg8qw', badge:'Watch Ad'
  });
}

const sportsCategory = categoryData['sports-events'];
if (sportsCategory) {
  const ahlyIndex = sportsCategory.projects.findIndex(p => p.title === 'Al Ahly Club');
  const ahlyProject = {
    title:'Al Ahly Club', subtitle:'Sports Content · Video Collection', index:'SE01',
    image:'assets/al-ahly.webp', collection:'al-ahly-club', badge:'Open Collection'
  };
  if (ahlyIndex >= 0) sportsCategory.projects[ahlyIndex] = ahlyProject;
  else sportsCategory.projects.unshift(ahlyProject);
  sportsCategory.collections = sportsCategory.collections || {};
  sportsCategory.collections['al-ahly-club'] = {
    title:'Al Ahly Club', kicker:'Sports Content',
    description:'Selected Al Ahly Club edits and promotional sports content.',
    cover:'assets/al-ahly.webp',
    projects:[
      { title:'Al Ahly Club — Selected Video 01', subtitle:'Al Ahly Club · Sports Edit', index:'AH01', image:'https://i.ytimg.com/vi/N4uGPUETGb4/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'N4uGPUETGb4', badge:'Watch Video' },
      { title:'Al Ahly Club — Selected Video 02', subtitle:'Al Ahly Club · Sports Edit', index:'AH02', image:'https://i.ytimg.com/vi/1eFghNwpODA/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'1eFghNwpODA', badge:'Watch Video' }
    ]
  };
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
    { title:'Selected Work 04', subtitle:'Additional Project · Video Editing', index:'MW04', image:'https://i.ytimg.com/vi/0UY-_mTpUDA/hqdefault.jpg', youtube:'0UY-_mTpUDA', badge:'Watch Video' }
  ]
};
// PORTFOLIO VIDEO ADDITIONS END

'''
    text = text.replace(marker, patch + marker, 1)

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
