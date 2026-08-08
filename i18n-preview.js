(() => {
  const translations = {
    'Home':'الرئيسية','Work':'الأعمال','About':'نبذة عني','Contact':'تواصل','Play Showreel':'شاهد الشوريل',
    'Senior Video Editor & Post-Production Specialist':'مونتير أول ومتخصص في ما بعد الإنتاج',
    'Crafting compelling stories across television, advertising, sports and entertainment.':'صناعة قصص قوية بصريًا للتلفزيون والإعلانات والرياضة والترفيه.',
    'View My Work':'شاهد أعمالي','Portfolio':'أعمالي','Selected Work':'مختارات من أعمالي','Explore Categories':'استكشف التخصصات',
    'Sports Content':'محتوى رياضي','Event Coverage':'تغطية فعاليات','Watch Project':'شاهد العمل','TV Programs':'برامج تلفزيونية','TV Promo':'برومو تلفزيوني',
    'More selected projects will be added as the portfolio grows.':'المزيد من الأعمال قريبًا.','Specialties':'التخصصات','Work Categories':'مجالات العمل',
    'Commercial & Branded Content':'إعلانات ومحتوى للعلامات التجارية','Campaigns, ads and brand films.':'حملات إعلانية وأفلام للعلامات التجارية.',
    'Programs, formats and television content.':'برامج وفورمات ومحتوى تلفزيوني.','Series':'مسلسلات','Promos, songs and selected series edits.':'بروموهات وأغاني ومختارات من مونتاج المسلسلات.',
    'Sports & Events':'رياضة وفعاليات','Fast-paced stories and event coverage.':'محتوى سريع الإيقاع وتغطيات فعاليات.',
    'Institutional & Social Impact':'محتوى مؤسسي ومجتمعي','Human stories with purpose.':'قصص إنسانية هادفة.',
    'Motion Graphics & 3D':'موشن جرافيك و3D','Titles, graphics and visual systems.':'تايتلز وجرافيك وحلول بصرية.','View Projects':'عرض المشاريع','View Projects →':'عرض المشاريع ←',
    'Featured Reel':'مختارات','Showreel':'شوريل','A focused selection of work across television, entertainment, sports and branded content.':'مختارات من أعمالي في التلفزيون والترفيه والرياضة والمحتوى التجاري.',
    'Open Work Archive':'عرض أرشيف الأعمال','About Me':'نبذة عني','Stories built in the edit.':'القصة تُصنع في المونتاج.',
    'I’m Sayed Abdallah, a video editor and post-production specialist with experience across television, entertainment, advertising, sports and institutional content.':'أنا سيد عبدالله، مونتير ومتخصص في ما بعد الإنتاج، بخبرة في التلفزيون والترفيه والإعلانات والرياضة والمحتوى المؤسسي.',
    'My focus is clear storytelling, strong pacing and polished delivery that serves both the audience and the project.':'أركز على الحكي الواضح، والإيقاع القوي، وتنفيذ احترافي يخدم الفكرة والجمهور.',
    'Video Editing':'مونتاج','Storytelling':'سرد بصري','TV Promos':'بروموهات تلفزيونية','Post-Production':'ما بعد الإنتاج','Motion Graphics':'موشن جرافيك','Sound Design':'تصميم صوتي',
    'Programs & Series':'برامج ومسلسلات','Commercial Content':'محتوى إعلاني','Events & Promos':'فعاليات وبروموهات','Selected Clients & Projects':'عملاء ومشاريع مختارة',
    'Have a project in mind?':'لديك مشروع؟','Let’s Work Together.':'لنعمل معًا.','Message on WhatsApp':'تواصل عبر واتساب','Send an Email':'أرسل بريدًا','All rights reserved.':'جميع الحقوق محفوظة.',
    'Video Portfolio':'معرض الفيديو','Project Video':'فيديو المشروع','Project video will be added after the final selection.':'سيتم إضافة فيديو المشروع بعد الاختيار النهائي.',
    'Open Collection':'عرض المجموعة','Watch Video':'شاهد الفيديو','Watch Promo':'شاهد البرومو','Watch Music Video':'شاهد الفيديو','Watch Ad':'شاهد الإعلان','Coming Soon':'قريبًا',
    'TV Program':'برنامج تلفزيوني','TV Program Edit':'مونتاج برنامج تلفزيوني','Video Collection':'مجموعة فيديوهات','Production & Entertainment':'إنتاج وترفيه',
    'Selected editing work created for Good News.':'مختارات من أعمال المونتاج لصالح Good News.','Selected sports promos and content created for Al Ahly Club.':'مختارات من البروموهات والمحتوى الرياضي للنادي الأهلي.',
    'Selected ON E television editing work.':'مختارات من أعمال المونتاج لقناة ON E.','Selected work from Program Bedaya.':'مختارات من أعمال برنامج بداية.','Selected work from MAKHMAK on SHASHA Kuwait.':'مختارات من برنامج مخمخ على منصة SHASHA الكويت.',
    'Phone':'الهاتف','LinkedIn Profile':'لينكدإن','WhatsApp':'واتساب','LinkedIn':'لينكدإن',

    'All Work Categories':'كل مجالات العمل','TV & Entertainment':'تلفزيون وترفيه','Advertising':'إعلانات','Television':'تلفزيون','Live Energy':'رياضة وفعاليات','Purpose-Driven Stories':'قصص هادفة','Design in Motion':'تصميم متحرك',
    'Projects':'المشاريع','Episodes & Promos':'حلقات وبروموهات','Explore More':'استكشف المزيد','Return':'رجوع',
    'Projects are being prepared':'الأعمال قيد التجهيز','Selected work will be added here.':'سيتم إضافة أعمال مختارة هنا قريبًا.','Discuss a Project':'ناقش مشروعك معي',
    'Commercials, campaigns and promotional content edited for brands and organizations.':'إعلانات وحملات ومحتوى ترويجي للعلامات التجارية والمؤسسات.',
    'Programs, formats, channel content and television promos.':'برامج وفورمات ومحتوى قنوات وبروموهات تلفزيونية.',
    'Promos, songs and selected edits created for television series.':'بروموهات وأغاني ومختارات من مونتاج المسلسلات.',
    'Sports content, festival coverage and event-driven storytelling.':'محتوى رياضي وتغطيات مهرجانات وفعاليات.',
    'Human-centered films and campaigns created for institutions and social-impact organizations.':'أفلام وحملات إنسانية للمؤسسات والجهات ذات التأثير المجتمعي.',
    'Titles, graphic packages, animation and visual systems created for screen.':'تايتلز وحزم جرافيك وأنيميشن وحلول بصرية للشاشة.',
    'Selected entertainment edits and event coverage created for ArabWood.':'مختارات من أعمال المونتاج والتغطيات لبرنامج ArabWood.',
    'Selected work from MAKHMAK on SHASHA Kuwait.':'مختارات من أعمال برنامج مخمخ على منصة شاشة الكويت.',
    'Selected work from Program Bedaya.':'مختارات من أعمال برنامج بداية.',

    'Commercial':'إعلان','Branded Promo':'برومو إعلاني','Series Promo':'برومو مسلسل','Series Song':'أغنية مسلسل','Music Video':'فيديو كليب','Entertainment Program':'برنامج ترفيهي','Program Promo':'برومو برنامج','Entertainment Edit':'مونتاج ترفيهي','Event Edit':'مونتاج فعالية','Brand Edit':'مونتاج براند','TV Programs':'برامج تلفزيونية','Sports Content':'محتوى رياضي','Event Coverage':'تغطية فعالية',

    'Al Ahly Club':'النادي الأهلي','Cairo International Film Festival':'مهرجان القاهرة السينمائي الدولي','Ramadan 2025':'رمضان 2025','Abu Al-Arousa — Season 2':'أبو العروسة — الموسم الثاني','Abu Al-Arousa — Song':'أبو العروسة — الأغنية','Abu Al-Arousa — Haytan Beitna':'أبو العروسة — حيطان بيتنا','Hospital 57357 — Qowa Fi Alby':'مستشفى 57357 — قوة في قلبي','Program Bedaya':'برنامج بداية','Program MAKHMAK — Platform SHASHA Kuwait':'برنامج مخمخ — منصة شاشة الكويت','Promo — Teatro':'برومو — تياترو'
  };

  const originals = new WeakMap();
  const originalAttrs = new WeakMap();
  let currentLang = localStorage.getItem('sa-lang') || 'en';
  const normalize = value => String(value || '').replace(/\s+/g, ' ').trim();

  function translatedText(value) {
    const key = normalize(value);
    if (!key) return null;
    if (translations[key]) return translations[key];

    if (key === '← All Work Categories') return 'كل مجالات العمل →';
    if (key.startsWith('← Back to ')) {
      const target = key.slice('← Back to '.length);
      return `العودة إلى ${translatedText(target) || target} →`;
    }
    if (key.startsWith('Play ')) {
      const target = key.slice(5);
      return `تشغيل ${translatedText(target) || target}`;
    }
    if (key.startsWith('Open ') && key.endsWith(' collection')) {
      const target = key.slice(5, -11);
      return `فتح مجموعة ${translatedText(target) || target}`;
    }
    if (key.includes(' · ')) {
      return key.split(' · ').map(part => translations[part] || part).join(' · ');
    }
    if (key.endsWith(' →')) {
      const base = key.slice(0, -2).trim();
      const translated = translations[base];
      return translated ? `${translated} ←` : null;
    }
    return null;
  }

  function rememberAttribute(el, attr) {
    let attrs = originalAttrs.get(el);
    if (!attrs) { attrs = {}; originalAttrs.set(el, attrs); }
    if (!(attr in attrs)) attrs[attr] = el.getAttribute(attr);
    return attrs[attr];
  }

  function processTextNode(node, lang) {
    if (!node || node.nodeType !== Node.TEXT_NODE || !node.parentElement) return;
    if (['SCRIPT','STYLE','NOSCRIPT'].includes(node.parentElement.tagName)) return;
    if (!originals.has(node)) originals.set(node, node.nodeValue);
    const original = originals.get(node);
    if (lang === 'en') { node.nodeValue = original; return; }
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
      el.setAttribute(attr, lang === 'en' ? original : (translatedText(original) || original));
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
    applyTo(document.body, currentLang);
    document.title = currentLang === 'ar' ? 'سيد عبدالله — مونتير أول' : (document.body.classList.contains('category-page') ? document.title.replace('سيد عبدالله — مونتير أول','Sayed Abdallah — Senior Video Editor') : 'Sayed Abdallah — Senior Video Editor');
    updateButtons(currentLang);
    document.documentElement.classList.remove('i18n-pending');
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
