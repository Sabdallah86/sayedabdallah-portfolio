const categoryStyles=document.createElement('link');
categoryStyles.rel='stylesheet';
categoryStyles.href='category-pages.css';
document.head.appendChild(categoryStyles);

const categoryData = {
  commercial: {
    title: 'Commercial & Branded Content',
    kicker: 'Advertising',
    description: 'Commercials, campaigns and promotional content edited for brands and organizations.',
    cover: 'assets/toto-link-commercial.webp',
    projects: [
      { title:'ToTo Link', subtitle:'Commercial · Video Editing', index:'AD01', image:'assets/toto-link-commercial.webp', video:'assets/toto-link-commercial.mp4', badge:'Watch Ad' },
      { title:'SATUC', subtitle:'Branded Promo · Video Editing', index:'AD02', image:'assets/satuc-branded-promo.webp', video:'assets/satuc-branded-promo.mp4', badge:'Watch Promo' }
    ]
  },
  'tv-programs': {
    title:'TV Programs',
    kicker:'Television',
    description:'Programs, formats, channel content and television promos.',
    cover:'assets/on-the-road-first-journey.webp',
    sections:[
      {
        title:'On the Road',
        kicker:'Program Collection',
        description:'A selected collection of promos and social edits created for On the Road.',
        layout:'portrait',
        projects:[
          { title:'First Journey', subtitle:'On the Road · Program Promo', index:'OTR01', image:'assets/on-the-road-first-journey.webp', video:'assets/on-the-road-first-journey.mp4', badge:'Watch Video', format:'portrait' },
          { title:'Nelly Karim Teaser', subtitle:'On the Road · Social Promo', index:'OTR02', image:'assets/on-the-road-nelly-karim.webp', video:'assets/on-the-road-nelly-karim.mp4', badge:'Watch Video', format:'portrait' },
          { title:'The Road of Life', subtitle:'On the Road · Program Teaser', index:'OTR03', image:'assets/on-the-road-life-road.webp', video:'assets/on-the-road-life-road.mp4', badge:'Watch Video', format:'portrait' },
          { title:'Back After 25 Years', subtitle:'On the Road · Launch Promo', index:'OTR04', image:'assets/on-the-road-25-years.webp', video:'assets/on-the-road-25-years.mp4', badge:'Watch Video', format:'portrait' }
        ]
      },
      {
        title:'Other TV Work',
        kicker:'Selected Television',
        description:'Channel content and television promos.',
        projects:[
          { title:'ON E Channel', subtitle:'TV Programs · Video Editing', index:'TV01', image:'assets/on-e.webp' },
          { title:'Ramadan 2025', subtitle:'TV Promo · Video Editing', index:'TV02', image:'assets/ramadan-2025.webp' }
        ]
      }
    ]
  },
  series: {
    title:'Series',
    kicker:'TV & Entertainment',
    description:'Promos, songs and selected edits created for television series.',
    cover:'assets/teatro-series-promo.webp',
    projects:[
      { title:'Promo — Teatro', subtitle:'Series Promo · Video Editing', index:'S01', image:'assets/teatro-series-promo.webp', video:'assets/teatro-series-promo.mp4', badge:'Watch Promo' },
      { title:'Abu Al-Arousa — Song', subtitle:'Series Song · Video Editing', index:'S02', image:'assets/abu-el-arousa.webp', video:'assets/abu-el-arousa.mp4', badge:'Watch Video' }
    ]
  },
  'sports-events': {
    title:'Sports & Events',
    kicker:'Live Energy',
    description:'Sports content, festival coverage and event-driven storytelling.',
    cover:'assets/al-ahly.webp',
    projects:[
      { title:'Al Ahly Club', subtitle:'Sports Content · Video Editing', index:'SE01', image:'assets/al-ahly.webp' },
      { title:'Cairo International Film Festival', subtitle:'Event Coverage · Video Editing', index:'SE02', image:'assets/ciff.webp' }
    ]
  },
  institutional: {
    title:'Institutional & Social Impact',
    kicker:'Purpose-Driven Stories',
    description:'Human-centered films and campaigns created for institutions and social-impact organizations.',
    cover:'assets/hospital-57357-qewa-fi-alby.webp',
    projects:[
      { title:'Hospital 57357 — Qowa Fi Alby', subtitle:'Music Video · Video Editing', index:'SI01', image:'assets/hospital-57357-qewa-fi-alby.webp', video:'assets/hospital-57357-qewa-fi-alby.mp4', badge:'Watch Music Video' }
    ]
  },
  'motion-graphics': {
    title:'Motion Graphics & 3D',
    kicker:'Design in Motion',
    description:'Titles, graphic packages, animation and visual systems created for screen.',
    cover:'assets/showreel.webp',
    projects:[]
  }
};

function escapeHTML(value='') {
  return String(value).replace(/[&<>'"]/g, ch => ({
    '&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'
  }[ch]));
}

function projectMarkup(project) {
  const attrs = project.video
    ? ` data-video="${escapeHTML(project.video)}" data-poster="${escapeHTML(project.image)}" data-title="${escapeHTML(project.title)}" role="button" tabindex="0" aria-label="Play ${escapeHTML(project.title)}"`
    : '';
  const formatClass = project.format === 'portrait' ? ' portrait-project' : '';
  return `<article class="project-card reveal category-project-card${project.video ? ' project-video' : ''}${formatClass}"${attrs}>
    <div class="project-image">
      <img src="${escapeHTML(project.image)}" alt="${escapeHTML(project.title)}" loading="lazy">
      <span class="play-button" aria-hidden="true">▶</span>
      <span class="available-badge">${escapeHTML(project.video ? project.badge : 'Coming Soon')}</span>
    </div>
    <div class="project-info">
      <div><h3>${escapeHTML(project.title)}</h3><p>${escapeHTML(project.subtitle)}</p></div>
      <span class="project-index">${escapeHTML(project.index)}</span>
    </div>
  </article>`;
}

function projectSectionMarkup(section) {
  const projects = section.projects?.length
    ? section.projects.map(projectMarkup).join('')
    : `<div class="empty-state reveal"><span>◇</span><h3>Projects are being prepared</h3><p>Selected work will be added here.</p></div>`;
  const gridClass = section.layout === 'portrait' ? 'portrait-project-grid' : 'category-project-grid';
  return `<div class="collection-block">
    <div class="collection-heading reveal">
      <div>
        <p class="kicker">${escapeHTML(section.kicker || 'Selected Work')}</p>
        <h2>${escapeHTML(section.title)}</h2>
      </div>
      ${section.description ? `<p>${escapeHTML(section.description)}</p>` : ''}
    </div>
    <div class="promo-grid ${gridClass}">${projects}</div>
  </div>`;
}

function renderCategoryPage(key) {
  const data=categoryData[key];
  if(!data) return false;

  document.body.classList.add('category-page');
  document.title=`${data.title} — Sayed Abdallah`;
  const main=document.querySelector('main');
  const related=Object.entries(categoryData)
    .filter(([id])=>id!==key)
    .map(([id,item])=>`<a href="index.html?category=${id}">${escapeHTML(item.title)}<span>→</span></a>`)
    .join('');

  let projectContent='';
  if(data.sections?.length) {
    projectContent=data.sections.map(projectSectionMarkup).join('');
  } else if(data.projects?.length) {
    projectContent=`<div class="section-heading reveal"><div><p class="kicker">Selected Work</p><h2>Projects</h2></div></div>
      <div class="promo-grid category-project-grid">${data.projects.map(projectMarkup).join('')}</div>`;
  } else {
    projectContent=`<div class="empty-state reveal"><span>◇</span><h3>Projects are being prepared</h3><p>Selected motion graphics and 3D work will be added here.</p><a class="button button-outline" href="index.html#contact">Discuss a Project</a></div>`;
  }

  main.innerHTML=`<section class="portfolio-page-hero" style="--page-cover:url('${escapeHTML(data.cover)}')">
      <div class="page-hero-overlay"></div>
      <div class="page-hero-content reveal">
        <a class="back-link" href="index.html#categories">← All Work Categories</a>
        <p class="kicker">${escapeHTML(data.kicker)}</p>
        <h1>${escapeHTML(data.title)}</h1>
        <p>${escapeHTML(data.description)}</p>
      </div>
    </section>
    <section class="section page-projects" id="projects">${projectContent}</section>
    <section class="section explore-more">
      <p class="kicker reveal">Explore More</p>
      <div class="category-nav reveal">${related}</div>
    </section>`;

  const nav=document.querySelector('.main-nav');
  if(nav) nav.innerHTML='<a href="index.html">Home</a><a class="active" href="index.html#categories">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact</a>';
  const cta=document.querySelector('.header-cta');
  if(cta) cta.href='index.html#showreel';
  return true;
}

const requestedCategory=new URLSearchParams(location.search).get('category');
renderCategoryPage(requestedCategory);

const header=document.querySelector('.site-header');
const menuButton=document.querySelector('.menu-toggle');
const nav=document.querySelector('.main-nav');
const toast=document.querySelector('.toast');

if(header) {
  window.addEventListener('scroll',()=>header.classList.toggle('scrolled',window.scrollY>24));
}

if(menuButton&&nav){
  menuButton.addEventListener('click',()=>{
    const open=!nav.classList.contains('open');
    nav.classList.toggle('open',open);
    menuButton.classList.toggle('active',open);
    menuButton.setAttribute('aria-expanded',String(open));
    document.body.classList.toggle('menu-open',open);
  });
  nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{
    nav.classList.remove('open');
    menuButton.classList.remove('active');
    menuButton.setAttribute('aria-expanded','false');
    document.body.classList.remove('menu-open');
  }));
}

if('IntersectionObserver' in window){
  const revealObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  }),{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>revealObserver.observe(el));

  const sections=[...document.querySelectorAll('main section[id]')];
  const localNavLinks=[...document.querySelectorAll('.main-nav a[href^="#"]')];
  if(sections.length&&localNavLinks.length){
    const sectionObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{
      if(entry.isIntersecting){
        localNavLinks.forEach(link=>link.classList.toggle('active',link.getAttribute('href')===`#${entry.target.id}`));
      }
    }),{rootMargin:'-35% 0px -55% 0px'});
    sections.forEach(section=>sectionObserver.observe(section));
  }
}else{
  document.querySelectorAll('.reveal').forEach(el=>el.classList.add('visible'));
}

const videoModal=document.getElementById('video-modal');
const videoPlayer=document.getElementById('project-video-player');
const videoTitle=document.getElementById('video-modal-title');
const videoClose=document.querySelector('.video-modal-close');
let lastTrigger=null;

function openProjectVideo(card){
  if(!videoModal||!videoPlayer||!videoTitle||!card.dataset.video) return;
  lastTrigger=card;
  videoModal.classList.remove('portrait-video');
  videoPlayer.src=card.dataset.video;
  videoPlayer.poster=card.dataset.poster||'';
  videoTitle.textContent=card.dataset.title||'Project Video';
  videoModal.classList.add('open');
  videoModal.setAttribute('aria-hidden','false');
  document.body.classList.add('video-open');
  videoClose?.focus();
}

function closeProjectVideo(){
  if(!videoModal||!videoPlayer) return;
  videoPlayer.pause();
  videoPlayer.removeAttribute('src');
  videoPlayer.removeAttribute('poster');
  videoPlayer.load();
  videoModal.classList.remove('open','portrait-video');
  videoModal.setAttribute('aria-hidden','true');
  document.body.classList.remove('video-open');
  lastTrigger?.focus();
}

videoPlayer?.addEventListener('loadedmetadata',()=>{
  videoModal?.classList.toggle('portrait-video',videoPlayer.videoHeight>videoPlayer.videoWidth);
});

document.querySelectorAll('.project-card').forEach(card=>{
  if(card.matches('a')&&!card.dataset.video) return;
  const activate=event=>{
    if(card.dataset.video){
      event?.preventDefault();
      openProjectVideo(card);
      return;
    }
    if(toast){
      toast.classList.add('show');
      clearTimeout(window.__toastTimer);
      window.__toastTimer=setTimeout(()=>toast.classList.remove('show'),2600);
    }
  };
  card.addEventListener('click',activate);
  card.addEventListener('keydown',event=>{
    if(event.key==='Enter'||event.key===' '){
      event.preventDefault();
      activate(event);
    }
  });
});

videoClose?.addEventListener('click',closeProjectVideo);
videoModal?.addEventListener('click',event=>{
  if(event.target===videoModal) closeProjectVideo();
});
document.addEventListener('keydown',event=>{
  if(event.key==='Escape'&&videoModal?.classList.contains('open')) closeProjectVideo();
});

const year=document.getElementById('year');
if(year) year.textContent=new Date().getFullYear();
