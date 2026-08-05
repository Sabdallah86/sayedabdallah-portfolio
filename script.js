const categoryStyles=document.createElement('link');categoryStyles.rel='stylesheet';categoryStyles.href='category-pages.css';document.head.appendChild(categoryStyles);
const arabwoodStyles=document.createElement('style');arabwoodStyles.textContent=`
.collection-card{display:block;color:inherit;text-decoration:none}.collection-card .collection-arrow{font-size:28px;line-height:1}.collection-card:hover .collection-arrow{background:var(--gold);color:#050505;border-color:var(--gold)}
.collection-page .page-hero-content h1{font-size:clamp(80px,12vw,170px)}
.video-modal iframe{display:block;width:100%;aspect-ratio:16/9;max-height:74svh;border:1px solid rgba(255,255,255,.16);background:#000;box-shadow:0 30px 90px rgba(0,0,0,.55)}
.video-modal iframe[hidden],.video-modal video[hidden]{display:none}.video-modal.youtube-video .video-modal-inner{width:min(1180px,100%)}
`;document.head.appendChild(arabwoodStyles);

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
    cover:'assets/on-e.webp',
    projects:[
      { title:'ON E Channel', subtitle:'TV Programs · Video Editing', index:'TV01', image:'assets/on-e.webp' },
      { title:'Ramadan 2025', subtitle:'TV Promo · Video Editing', index:'TV02', image:'assets/ramadan-2025.webp' },
      { title:'ArabWood', subtitle:'Entertainment Program · Video Collection', index:'TV03', image:'https://i.ytimg.com/vi/sCGh1JRMK3E/hqdefault.jpg', imageFallback:'assets/on-e.webp', collection:'arabwood', badge:'Open Collection' }
    ],
    collections:{
      'arabwood':{
        title:'ArabWood',
        kicker:'Entertainment Program',
        description:'Selected entertainment edits and event coverage created for ArabWood.',
        cover:'https://i.ytimg.com/vi/sCGh1JRMK3E/hqdefault.jpg',
        projects:[
          { title:'Promo General', subtitle:'ArabWood · Program Promo', index:'AW01', image:'https://i.ytimg.com/vi/sCGh1JRMK3E/hqdefault.jpg', imageFallback:'assets/on-e.webp', youtube:'sCGh1JRMK3E', badge:'Watch Video' },
          { title:'Giorgio Armani', subtitle:'ArabWood · Entertainment Edit', index:'AW02', image:'https://i.ytimg.com/vi/hO5xZWLdrTo/hqdefault.jpg', imageFallback:'assets/on-e.webp', youtube:'hO5xZWLdrTo', badge:'Watch Video' },
          { title:'Emmy Awards 2025', subtitle:'ArabWood · Event Edit', index:'AW03', image:'https://i.ytimg.com/vi/sCjBAIkHqQw/hqdefault.jpg', imageFallback:'assets/on-e.webp', youtube:'sCjBAIkHqQw', badge:'Watch Video' },
          { title:'Brand Personality', subtitle:'ArabWood · Brand Edit', index:'AW04', image:'https://i.ytimg.com/vi/Me1dDAzhkVM/hqdefault.jpg', imageFallback:'assets/on-e.webp', youtube:'Me1dDAzhkVM', badge:'Watch Video' }
        ]
      }
    }
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
    '&':'&amp;',
    '<':'&lt;',
    '>':'&gt;',
    "'":'&#39;',
    '"':'&quot;'
  }[ch]));
}

function projectMarkup(project, categoryKey) {
  const formatClass = project.format === 'portrait' ? ' portrait-project' : '';
  const fallbackAttr = project.imageFallback
    ? ` data-fallback="${escapeHTML(project.imageFallback)}"`
    : '';

  if (project.collection) {
    const href = `index.html?category=${encodeURIComponent(categoryKey)}&collection=${encodeURIComponent(project.collection)}`;
    return `<a class="project-card reveal category-project-card project-link-card collection-card${formatClass}" href="${href}" aria-label="Open ${escapeHTML(project.title)} collection">
      <div class="project-image">
        <img src="${escapeHTML(project.image)}"${fallbackAttr} alt="${escapeHTML(project.title)}" loading="lazy">
        <span class="play-button collection-arrow" aria-hidden="true">→</span>
        <span class="available-badge">${escapeHTML(project.badge || 'Open Collection')}</span>
      </div>
      <div class="project-info">
        <div><h3>${escapeHTML(project.title)}</h3><p>${escapeHTML(project.subtitle)}</p></div>
        <span class="project-index">${escapeHTML(project.index)}</span>
      </div>
    </a>`;
  }

  const hasPlayable = Boolean(project.video || project.youtube);
  let attrs = '';

  if (project.video) {
    attrs = ` data-video="${escapeHTML(project.video)}" data-poster="${escapeHTML(project.image)}" data-title="${escapeHTML(project.title)}" role="button" tabindex="0" aria-label="Play ${escapeHTML(project.title)}"`;
  } else if (project.youtube) {
    attrs = ` data-youtube="${escapeHTML(project.youtube)}" data-title="${escapeHTML(project.title)}" role="button" tabindex="0" aria-label="Play ${escapeHTML(project.title)}"`;
  }

  return `<article class="project-card reveal category-project-card${hasPlayable ? ' project-video' : ''}${formatClass}"${attrs}>
    <div class="project-image">
      <img src="${escapeHTML(project.image)}"${fallbackAttr} alt="${escapeHTML(project.title)}" loading="lazy">
      <span class="play-button" aria-hidden="true">▶</span>
      <span class="available-badge">${escapeHTML(hasPlayable ? project.badge : 'Coming Soon')}</span>
    </div>
    <div class="project-info">
      <div><h3>${escapeHTML(project.title)}</h3><p>${escapeHTML(project.subtitle)}</p></div>
      <span class="project-index">${escapeHTML(project.index)}</span>
    </div>
  </article>`;
}

function renderCategoryPage(categoryKey, collectionKey) {
  const category = categoryData[categoryKey];
  if (!category) return false;

  const collection = collectionKey ? category.collections?.[collectionKey] : null;
  const pageData = collection || category;
  const isCollection = Boolean(collection);

  document.body.classList.add('category-page');
  document.body.classList.toggle('collection-page', isCollection);
  document.title = `${pageData.title} — Sayed Abdallah`;

  const main = document.querySelector('main');
  const projects = pageData.projects?.length
    ? pageData.projects.map(project => projectMarkup(project, categoryKey)).join('')
    : `<div class="empty-state reveal"><span>◇</span><h3>Projects are being prepared</h3><p>Selected work will be added here.</p><a class="button button-outline" href="index.html#contact">Discuss a Project</a></div>`;

  const gridClass = pageData.layout === 'portrait'
    ? 'portrait-project-grid'
    : 'category-project-grid';

  const backLink = isCollection
    ? `<a class="back-link" href="index.html?category=${encodeURIComponent(categoryKey)}">← Back to ${escapeHTML(category.title)}</a>`
    : `<a class="back-link" href="index.html#categories">← All Work Categories</a>`;

  const related = isCollection
    ? `<a href="index.html?category=${encodeURIComponent(categoryKey)}">${escapeHTML(category.title)}<span>←</span></a>`
    : Object.entries(categoryData)
        .filter(([id]) => id !== categoryKey)
        .map(([id,item]) => `<a href="index.html?category=${id}">${escapeHTML(item.title)}<span>→</span></a>`)
        .join('');

  main.innerHTML = `<section class="portfolio-page-hero" style="--page-cover:url('${escapeHTML(pageData.cover)}')">
      <div class="page-hero-overlay"></div>
      <div class="page-hero-content reveal">
        ${backLink}
        <p class="kicker">${escapeHTML(pageData.kicker)}</p>
        <h1>${escapeHTML(pageData.title)}</h1>
        <p>${escapeHTML(pageData.description)}</p>
      </div>
    </section>
    <section class="section page-projects" id="projects">
      <div class="section-heading reveal">
        <div>
          <p class="kicker">${isCollection ? 'Video Collection' : 'Selected Work'}</p>
          <h2>${isCollection ? 'Episodes & Promos' : 'Projects'}</h2>
        </div>
      </div>
      <div class="promo-grid ${gridClass}">${projects}</div>
    </section>
    <section class="section explore-more">
      <p class="kicker reveal">${isCollection ? 'Return' : 'Explore More'}</p>
      <div class="category-nav reveal">${related}</div>
    </section>`;

  const nav = document.querySelector('.main-nav');
  if (nav) {
    nav.innerHTML = '<a href="index.html">Home</a><a class="active" href="index.html#categories">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact</a>';
  }

  const cta = document.querySelector('.header-cta');
  if (cta) cta.href = 'index.html#showreel';

  return true;
}

const params = new URLSearchParams(location.search);
const requestedCategory = params.get('category');
const requestedCollection = params.get('collection');
renderCategoryPage(requestedCategory, requestedCollection);

document.querySelectorAll('img[data-fallback]').forEach(image => {
  image.addEventListener('error', () => {
    const fallback = image.dataset.fallback;
    if (fallback && !image.src.endsWith(fallback)) image.src = fallback;
  }, { once:true });
});

const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');
const toast = document.querySelector('.toast');

if (header) {
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 24);
  });
}

if (menuButton && nav) {
  menuButton.addEventListener('click', () => {
    const open = !nav.classList.contains('open');
    nav.classList.toggle('open', open);
    menuButton.classList.toggle('active', open);
    menuButton.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('menu-open', open);
  });

  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      menuButton.classList.remove('active');
      menuButton.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('menu-open');
    });
  });
}

if ('IntersectionObserver' in window) {
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: .12 });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  const sections = [...document.querySelectorAll('main section[id]')];
  const localNavLinks = [...document.querySelectorAll('.main-nav a[href^="#"]')];

  if (sections.length && localNavLinks.length) {
    const sectionObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          localNavLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
          });
        }
      });
    }, { rootMargin: '-35% 0px -55% 0px' });

    sections.forEach(section => sectionObserver.observe(section));
  }
} else {
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
}

const videoModal = document.getElementById('video-modal');
const videoPlayer = document.getElementById('project-video-player');
let youtubePlayer = document.getElementById('youtube-video-player');
if (!youtubePlayer && videoModal) {
  youtubePlayer = document.createElement('iframe');
  youtubePlayer.id = 'youtube-video-player';
  youtubePlayer.title = 'YouTube video player';
  youtubePlayer.src = 'about:blank';
  youtubePlayer.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
  youtubePlayer.allowFullscreen = true;
  youtubePlayer.referrerPolicy = 'strict-origin-when-cross-origin';
  youtubePlayer.hidden = true;
  videoModal.querySelector('.video-modal-inner')?.appendChild(youtubePlayer);
}
const videoTitle = document.getElementById('video-modal-title');
const videoClose = document.querySelector('.video-modal-close');
let lastTrigger = null;

function resetModalPlayers() {
  if (videoPlayer) {
    videoPlayer.pause();
    videoPlayer.removeAttribute('src');
    videoPlayer.removeAttribute('poster');
    videoPlayer.load();
    videoPlayer.hidden = true;
  }

  if (youtubePlayer) {
    youtubePlayer.src = 'about:blank';
    youtubePlayer.hidden = true;
  }
}

function openProjectVideo(card) {
  if (!videoModal || !videoTitle || (!card.dataset.video && !card.dataset.youtube)) return;

  lastTrigger = card;
  resetModalPlayers();
  videoModal.classList.remove('portrait-video', 'youtube-video');
  videoTitle.textContent = card.dataset.title || 'Project Video';

  if (card.dataset.youtube && youtubePlayer) {
    const videoId = encodeURIComponent(card.dataset.youtube);
    youtubePlayer.src = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0&playsinline=1`;
    youtubePlayer.hidden = false;
    videoModal.classList.add('youtube-video');
  } else if (card.dataset.video && videoPlayer) {
    videoPlayer.src = card.dataset.video;
    videoPlayer.poster = card.dataset.poster || '';
    videoPlayer.hidden = false;
  }

  videoModal.classList.add('open');
  videoModal.setAttribute('aria-hidden', 'false');
  document.body.classList.add('video-open');
  videoClose?.focus();
}

function closeProjectVideo() {
  if (!videoModal) return;

  resetModalPlayers();
  videoModal.classList.remove('open', 'portrait-video', 'youtube-video');
  videoModal.setAttribute('aria-hidden', 'true');
  document.body.classList.remove('video-open');
  lastTrigger?.focus();
}

videoPlayer?.addEventListener('loadedmetadata', () => {
  videoModal?.classList.toggle('portrait-video', videoPlayer.videoHeight > videoPlayer.videoWidth);
});

document.querySelectorAll('.project-card').forEach(card => {
  if (card.matches('a') && !card.dataset.video && !card.dataset.youtube) return;

  const activate = event => {
    if (card.dataset.video || card.dataset.youtube) {
      event?.preventDefault();
      openProjectVideo(card);
      return;
    }

    if (toast) {
      toast.classList.add('show');
      clearTimeout(window.__toastTimer);
      window.__toastTimer = setTimeout(() => toast.classList.remove('show'), 2600);
    }
  };

  card.addEventListener('click', activate);
  card.addEventListener('keydown', event => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      activate(event);
    }
  });
});

videoClose?.addEventListener('click', closeProjectVideo);
videoModal?.addEventListener('click', event => {
  if (event.target === videoModal) closeProjectVideo();
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && videoModal?.classList.contains('open')) {
    closeProjectVideo();
  }
});

const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
