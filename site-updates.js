(() => {
  // Keep manual movement consistent in both marquee directions.
  document.querySelectorAll('[data-client-row]').forEach(row => {
    const track = row.querySelector('.clients-v3-track');
    const viewport = row.querySelector('.clients-v3-viewport');
    const prev = row.querySelector('.client-scroll-prev');
    const next = row.querySelector('.client-scroll-next');
    if (!track || !viewport || !prev || !next) return;
    const nudge = direction => {
      const card = track.querySelector('.client-brand-v3');
      const group = track.querySelector('.clients-v3-group');
      const step = (card?.offsetWidth || 232) + (parseFloat(getComputedStyle(group).gap) || 20);
      const animation = track.getAnimations().find(a => a.effect);
      if (animation) {
        const duration = Number(animation.effect.getTiming().duration);
        const distance = track.scrollWidth / 2;
        if (!duration || !distance) return;
        const now = Number(animation.currentTime) || 0;
        const sign = row.classList.contains('clients-v3-right') ? -1 : 1;
        const delta = direction * sign * step / distance * duration;
        animation.currentTime = ((now + delta) % duration + duration) % duration;
      } else {
        viewport.scrollBy({ left: direction * step, behavior: 'auto' });
      }
    };
    prev.addEventListener('click', () => nudge(-1));
    next.addEventListener('click', () => nudge(1));
  });
})();
