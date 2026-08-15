(() => {
  function ensureCategoryData() {
    if (typeof categoryData !== 'undefined') {
      categoryData.sports = {
        title: 'Sports',
        kicker: 'Sports Content',
        description: 'Fast-paced sports edits, promotional content and club-focused storytelling.',
        cover: 'assets/al-ahly.webp',
        projects: [
          { title:'Al Ahly Club', subtitle:'Sports Content · Video Collection', index:'SP01', image:'assets/al-ahly.webp', collection:'al-ahly-club', badge:'Open Collection' }
        ],
        collections: {
          'al-ahly-club': {
            title:'Al Ahly Club',
            kicker:'Sports Content',
            description:'Selected Al Ahly Club edits and promotional sports content.',
            cover:'assets/al-ahly.webp',
            projects:[
              { title:'Al Ahly Club — Selected Video 01', subtitle:'Al Ahly Club · Sports Edit', index:'AH01', image:'https://i.ytimg.com/vi/N4uGPUETGb4/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'N4uGPUETGb4', badge:'Watch Video' },
              { title:'Al Ahly Club — Selected Video 02', subtitle:'Al Ahly Club · Sports Edit', index:'AH02', image:'https://i.ytimg.com/vi/1eFghNwpODA/hqdefault.jpg', imageFallback:'assets/al-ahly.webp', youtube:'1eFghNwpODA', badge:'Watch Video' }
            ]
          }
        }
      };
      categoryData.events = {
        title: 'Events',
        kicker: 'Event Coverage',
        description: 'Festival coverage, live-event storytelling and event-driven edits.',
        cover: 'assets/ciff.webp',
        projects: [
          { title:'Cairo International Film Festival', subtitle:'Event Coverage · Video Collection', index:'EV01', image:'assets/ciff.webp', collection:'ciff', badge:'Open Collection' }
        ],
        collections: {
          ciff: {
            title:'Cairo International Film Festival',
            kicker:'Event Coverage',
            description:'Selected Cairo International Film Festival edits and event coverage.',
            cover:'assets/ciff.webp',
            projects:[
              { title:'Cairo International Film Festival — Selected Video', subtitle:'CIFF · Event Edit', index:'CIFF01', image:'https://i.ytimg.com/vi/8YHgTTQOKdo/hqdefault.jpg', imageFallback:'assets/ciff.webp', youtube:'8YHgTTQOKdo', badge:'Watch Video' }
            ]
          }
        }
      };
      categoryData['ai-work'] = {
        title: 'AI Work',
        kicker: 'AI-Driven Creativity',
        description: 'AI-assisted visual storytelling, creative development and selected experiments.',
        cover: 'assets/ciff.webp',
        projects: []
      };
    }

    const params = new URLSearchParams(location.search);
    const requested = params.get('category');
    if ((requested === 'sports' || requested === 'events' || requested === 'ai-work') && typeof renderCategoryPage === 'function') {
      renderCategoryPage(requested, params.get('collection'));
    } else if (requested === 'sports-events' && typeof renderCategoryPage === 'function') {
      history.replaceState(null, '', 'index.html?category=sports');
      renderCategoryPage('sports');
    }
  }

  function clientControls() {
    document.querySelectorAll('[data-client-row]').forEach(row => {
      const track = row.querySelector('.clients-v3-track');
      const prev = row.querySelector('.client-scroll-prev');
      const next = row.querySelector('.client-scroll-next');
      if (!track || !prev || !next) return;
      const nudge = delta => {
        const animation = track.getAnimations().find(a => a.effect);
        if (animation) {
          const duration = animation.effect.getTiming().duration || 60000;
          const now = typeof animation.currentTime === 'number' ? animation.currentTime : 0;
          animation.currentTime = (now + delta + duration) % duration;
        } else {
          track.style.transform = `translateX(${delta > 0 ? '-220px' : '220px'})`;
          setTimeout(() => track.style.transform = '', 180);
        }
      };
      prev.addEventListener('click', () => nudge(-3500));
      next.addEventListener('click', () => nudge(3500));
    });
  }

  ensureCategoryData();
  clientControls();
})();
