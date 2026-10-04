(() => {
  // Routing and portfolio data are initialized once in script.js.
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

  clientControls();
})();
