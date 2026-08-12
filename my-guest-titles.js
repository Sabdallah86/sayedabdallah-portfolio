(() => {
  const titles = new Map([
    ['_5EHAht5a1M', 'Nader Abbassy — My Guest with Moataz El Demerdash'],
    ['_Sd8QUoXoaI', 'Magdy Abdelghany — My Guest with Moataz El Demerdash'],
    ['_7irVnrKMmM', 'Hany Ramzy — My Guest with Moataz El Demerdash'],
    ['_vUQ8quTX-w', 'Salah Abdallah — My Guest with Moataz El Demerdash'],
    ['FwVPJqsdXBc', 'Amr Mostafa — My Guest with Moataz El Demerdash'],
  ]);

  function applyTitles() {
    document.querySelectorAll('[data-youtube]').forEach(card => {
      const title = titles.get(card.dataset.youtube);
      if (!title) return;

      if (card.dataset.title !== title) card.dataset.title = title;
      card.setAttribute('aria-label', `Play ${title}`);

      const heading = card.querySelector('.project-info h3, h3');
      if (heading && heading.textContent.trim() !== title) {
        heading.textContent = title;
      }
    });
  }

  function start() {
    applyTitles();
    const observer = new MutationObserver(() => applyTitles());
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start, { once: true });
  } else {
    start();
  }
})();
