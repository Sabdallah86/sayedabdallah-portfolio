const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');
const toast = document.querySelector('.toast');

// Keep the public contact email in one place.
const publicEmail = 'sayedabdallah@micaegypt.com';
document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
  const subject = link.href.includes('?') ? link.href.slice(link.href.indexOf('?')) : '';
  link.href = `mailto:${publicEmail}${subject}`;
  if (link.textContent.includes('@')) link.textContent = publicEmail;
});

window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 24);
});

menuButton.addEventListener('click', () => {
  const open = !nav.classList.contains('open');
  nav.classList.toggle('open', open);
  menuButton.setAttribute('aria-expanded', open);
  document.body.classList.toggle('menu-open', open);
});

document.querySelectorAll('.main-nav a').forEach(link => {
  link.addEventListener('click', () => {
    nav.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  });
});

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

document.querySelectorAll('.project-card').forEach(card => {
  card.addEventListener('click', () => {
    toast.classList.add('show');
    clearTimeout(window.__toastTimer);
    window.__toastTimer = setTimeout(() => toast.classList.remove('show'), 2600);
  });
});

document.getElementById('year').textContent = new Date().getFullYear();
