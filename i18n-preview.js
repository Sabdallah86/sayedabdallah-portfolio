(() => {
  const translations = {
    'Home':'الرئيسية',
    'Work':'الأعمال',
    'About':'نبذة عني',
    'Contact':'تواصل',
    'Play Showreel':'شاهد الشوريل',
    'Senior Video Editor & Post-Production Specialist':'مونتير أول ومتخصص في ما بعد الإنتاج',
    'Crafting compelling stories across television, advertising, sports and entertainment.':'صناعة قصص قوية بصريًا للتلفزيون والإعلانات والرياضة والترفيه.',
    'View My Work':'شاهد أعمالي',
    'Portfolio':'أعمالي',
    'Selected Work':'مختارات من أعمالي',
    'Explore Categories':'استكشف التخصصات',
    'Sports Content':'محتوى رياضي',
    'Event Coverage':'تغطية فعاليات',
    'Watch Project':'شاهد العمل',
    'TV Series · Video Editing':'مسلسل تلفزيوني · مونتاج',
    'TV Programs':'برامج تلفزيونية',
    'TV Promo':'برومو تلفزيوني',
    'Qowa Fi Alby · Music Video':'قوة في قلبي · فيديو كليب',
    'More selected projects will be added as the portfolio grows.':'المزيد من الأعمال قريبًا.',
    'Specialties':'التخصصات',
    'Work Categories':'مجالات العمل',
    'Commercial & Branded Content':'إعلانات ومحتوى للعلامات التجارية',
    'Campaigns, ads and brand films.':'حملات إعلانية وأفلام للعلامات التجارية.',
    'Programs, formats and television content.':'برامج وفورمات ومحتوى تلفزيوني.',
    'Series':'مسلسلات',
    'Promos, songs and selected series edits.':'بروموهات وأغاني ومختارات من مونتاج المسلسلات.',
    'Sports & Events':'رياضة وفعاليات',
    'Fast-paced stories and event coverage.':'محتوى سريع الإيقاع وتغطيات فعاليات.',
    'Institutional & Social Impact':'محتوى مؤسسي ومجتمعي',
    'Human stories with purpose.':'قصص إنسانية هادفة.',
    'Motion Graphics & 3D':'موشن جرافيك و3D',
    'Titles, graphics and visual systems.':'تايتلز وجرافيك وحلول بصرية.',
    'View Projects →':'عرض المشاريع ←',
    'Featured Reel':'مختارات',
    'Showreel':'Showreel',
    'A focused selection of work across television, entertainment, sports and branded content.':'مختارات من أعمالي في التلفزيون والترفيه والرياضة والمحتوى التجاري.',
    'Open Work Archive':'عرض أرشيف الأعمال',
    'About Me':'نبذة عني',
    'Stories built in the edit.':'القصة تُصنع في المونتاج.',
    'I’m Sayed Abdallah, a video editor and post-production specialist with experience across television, entertainment, advertising, sports and institutional content.':'أنا سيد عبدالله، مونتير ومتخصص في ما بعد الإنتاج، بخبرة في التلفزيون والترفيه والإعلانات والرياضة والمحتوى المؤسسي.',
    'My focus is clear storytelling, strong pacing and polished delivery that serves both the audience and the project.':'أركز على الحكي الواضح، والإيقاع القوي، وتنفيذ احترافي يخدم الفكرة والجمهور.',
    'Video Editing':'مونتاج',
    'Storytelling':'سرد بصري',
    'TV Promos':'بروموهات تلفزيونية',
    'Post-Production':'ما بعد الإنتاج',
    'Motion Graphics':'موشن جرافيك',
    'Sound Design':'تصميم صوتي',
    'Programs & Series':'برامج ومسلسلات',
    'Commercial Content':'محتوى إعلاني',
    'Events & Promos':'فعاليات وبروموهات',
    'Selected Clients & Projects':'عملاء ومشاريع مختارة',
    'Have a project in mind?':'لديك مشروع؟',
    'Let’s Work Together.':'لنعمل معًا.',
    'Message on WhatsApp':'تواصل عبر واتساب',
    'Send an Email':'أرسل بريدًا',
    'All rights reserved.':'جميع الحقوق محفوظة.',
    'Video Portfolio':'معرض الفيديو',
    'Project Video':'فيديو المشروع',
    'Project video will be added after the final selection.':'سيتم إضافة فيديو المشروع بعد الاختيار النهائي.',
    'Open Collection':'عرض المجموعة',
    'Watch Video':'شاهد الفيديو',
    'Watch Promo':'شاهد البرومو',
    'Watch Music Video':'شاهد الفيديو',
    'TV Program':'برنامج تلفزيوني',
    'TV Program Edit':'مونتاج برنامج تلفزيوني',
    'Video Collection':'مجموعة فيديوهات',
    'Production & Entertainment':'إنتاج وترفيه',
    'Selected editing work created for Good News.':'مختارات من أعمال المونتاج لصالح Good News.',
    'Selected sports promos and content created for Al Ahly Club.':'مختارات من البروموهات والمحتوى الرياضي للنادي الأهلي.',
    'Selected ON E television editing work.':'مختارات من أعمال المونتاج لقناة ON E.',
    'Selected work from Program Bedaya.':'مختارات من أعمال برنامج بداية.',
    'Selected work from MAKHMAK on SHASHA Kuwait.':'مختارات من برنامج MAKHMAK على منصة SHASHA الكويت.',
    'Phone':'الهاتف',
    'LinkedIn Profile':'لينكدإن',
    'WhatsApp':'واتساب',
    'LinkedIn':'لينكدإن'
  };

  const originals = new WeakMap();
  const originalAttrs = new WeakMap();
  let currentLang = localStorage.getItem('sa-lang') || 'en';

  const normalize = value => String(value || '').replace(/\s+/g, ' ').trim();
  const translatedText = value => translations[normalize(value)] || null;

  function rememberAttribute(el, attr) {
    let attrs = originalAttrs.get(el);
    if (!attrs) {
      attrs = {};
      originalAttrs.set(el, attrs);
    }
    if (!(attr in attrs)) attrs[attr] = el.getAttribute(attr);
    return attrs[attr];
  }

  function processTextNode(node, lang) {
    if (!node || node.nodeType !== Node.TEXT_NODE || !node.parentElement) return;
    if (['SCRIPT','STYLE','NOSCRIPT'].includes(node.parentElement.tagName)) return;
    if (!originals.has(node)) originals.set(node, node.nodeValue);
    const original = originals.get(node);
    if (lang === 'en') {
      node.nodeValue = original;
      return;
    }
    const translated = translatedText(original);
    if (!translated) return;
    const leading = original.match(/^\s*/)?.[0] || '';
    const trailing = original.match(/\s*$/)?.[0] || '';
    node.nodeValue = `${leading}${translated}${trailing}`;
  }

  function processElement(el, lang) {
    if (!(el instanceof Element)) return;
    ['aria-label','title','placeholder'].forEach(attr => {
      if (!el.hasAttribute(attr)) return;
      const original = rememberAttribute(el, attr);
      if (lang === 'en') el.setAttribute(attr, original);
      else el.setAttribute(attr, translatedText(original) || original);
    });
  }

  function applyTo(root, lang) {
    if (!root) return;
    if (root.nodeType === Node.TEXT_NODE) processTextNode(root, lang);
    if (root.nodeType === Node.ELEMENT_NODE) processElement(root, lang);
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      if (node.nodeType === Node.TEXT_NODE) processTextNode(node, lang);
      else processElement(node, lang);
    }
  }

  function updateButtons(lang) {
    document.querySelectorAll('.language-switcher button[data-lang]').forEach(btn => {
      const active = btn.dataset.lang === lang;
      btn.classList.toggle('active', active);
      btn.setAttribute('aria-pressed', String(active));
    });
  }

  function setLanguage(lang) {
    currentLang = lang === 'ar' ? 'ar' : 'en';
    localStorage.setItem('sa-lang', currentLang);
    document.documentElement.lang = currentLang;
    document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
    document.body.classList.toggle('lang-ar', currentLang === 'ar');
    document.title = currentLang === 'ar' ? 'سيد عبدالله — مونتير أول' : 'Sayed Abdallah — Senior Video Editor';
    applyTo(document.body, currentLang);
    updateButtons(currentLang);
  }

  function mountSwitcher() {
    const header = document.querySelector('.site-header');
    if (!header || header.querySelector('.language-switcher')) return;
    const switcher = document.createElement('div');
    switcher.className = 'language-switcher';
    switcher.setAttribute('aria-label', 'Language');
    switcher.innerHTML = '<button type="button" data-lang="en" aria-pressed="false">EN</button><span class="divider">|</span><button type="button" data-lang="ar" aria-pressed="false">عربي</button>';
    const cta = header.querySelector('.header-cta');
    if (cta) header.insertBefore(switcher, cta); else header.appendChild(switcher);
    switcher.addEventListener('click', event => {
      const button = event.target.closest('button[data-lang]');
      if (button) setLanguage(button.dataset.lang);
    });
  }

  const observer = new MutationObserver(mutations => {
    if (currentLang !== 'ar') return;
    for (const mutation of mutations) mutation.addedNodes.forEach(node => applyTo(node, 'ar'));
  });

  function init() {
    mountSwitcher();
    setLanguage(currentLang);
    observer.observe(document.body, {childList:true, subtree:true});
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();