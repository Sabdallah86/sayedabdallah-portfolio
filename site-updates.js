(() => {
  function ensureCategoryData() {
    if (typeof categoryData !== 'undefined') {
      categoryData.sports = {
        title: 'Sports',
        kicker: 'Sports Content',
        description: 'Fast-paced sports edits, promotional content and club-focused storytelling.',
        cover: 'assets/al-ahly.webp',
        projects: [
          { title:'Al Ahly Club', subtitle:'Sports Content · Video Editing', index:'SP01', image:'assets/al-ahly.webp' }
        ]
      };
      categoryData.events = {
        title: 'Events',
        kicker: 'Event Coverage',
        description: 'Festival coverage, live-event storytelling and event-driven edits.',
        cover: 'assets/ciff.webp',
        projects: [
          { title:'Cairo International Film Festival', subtitle:'Event Coverage · Video Editing', index:'EV01', image:'assets/ciff.webp' }
        ]
      };
      categoryData['ai-work'] = {
        title: 'AI Work',
        kicker: 'AI-Driven Creativity',
        description: 'AI-assisted visual storytelling, creative development and selected experiments.',
        cover: 'assets/showreel.webp',
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