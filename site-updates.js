(() => {
  function splitSportsEvents() {
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
      delete categoryData['sports-events'];
    }

    document.querySelectorAll('a[href*="category=sports-events"]').forEach(link => {
      const type = (link.dataset.category || '').toLowerCase();
      link.href = type === 'events' ? 'index.html?category=events' : 'index.html?category=sports';
    });

    const grid = document.querySelector('.category-grid');
    if (grid) {
      const combined = [...grid.querySelectorAll('.category-link')].find(a => /sports\s*&\s*events/i.test(a.textContent));
      if (combined) {
        const sports = document.createElement('a');
        sports.className = combined.className;
        sports.href = 'index.html?category=sports';
        sports.innerHTML = '<span class="category-icon">◉</span><h3>Sports</h3><p>Sports edits, promos and club content.</p><span class="category-action">View Projects →</span>';
        const events = document.createElement('a');
        events.className = combined.className;
        events.href = 'index.html?category=events';
        events.innerHTML = '<span class="category-icon">◆</span><h3>Events</h3><p>Festival and event coverage.</p><span class="category-action">View Projects →</span>';
        combined.replaceWith(sports, events);
      }
    }

    const params = new URLSearchParams(location.search);
    const requested = params.get('category');
    if ((requested === 'sports' || requested === 'events') && typeof renderCategoryPage === 'function') {
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

  splitSportsEvents();
  clientControls();
})();