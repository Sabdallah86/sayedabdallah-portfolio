(() => {
  const translations = {
    'Home':'الرئيسية','Work':'الأعمال','About':'عني','Contact':'تواصل','Language':'اللغة','Play Showreel':'شاهد العرض','Senior Video Editor & Post-Production Specialist':'مونتير أول ومتخصص في مرحلة ما بعد الإنتاج','Crafting compelling stories across television, advertising, sports and entertainment.':'أصنع قصصًا قوية ومؤثرة في التلفزيون والإعلانات والرياضة والترفيه.','View My Work':'شاهد أعمالي','Portfolio':'معرض الأعمال','Selected Work':'أعمال مختارة','Explore Categories':'استكشف الأقسام','Sports Content':'محتوى رياضي','Event Coverage':'تغطية فعاليات','Watch Project':'شاهد المشروع','TV Series · Video Editing':'مسلسل تلفزيوني · مونتاج فيديو','TV Programs':'برامج تلفزيونية','TV Promo':'برومو تلفزيوني','Qowa Fi Alby · Music Video':'قوة في قلبي · فيديو موسيقي','More selected projects will be added as the portfolio grows.':'سيتم إضافة المزيد من الأعمال المختارة تباعًا.','Specialties':'التخصصات','Work Categories':'أقسام الأعمال','Commercial & Branded Content':'إعلانات ومحتوى للعلامات التجارية','Campaigns, ads and brand films.':'حملات وإعلانات وأفلام للعلامات التجارية.','Programs, formats and television content.':'برامج وفورمات ومحتوى تلفزيوني.','Series':'مسلسلات','Promos, songs and selected series edits.':'بروموهات وأغاني ومختارات من مونتاج المسلسلات.','Sports & Events':'رياضة وفعاليات','Fast-paced stories and event coverage.':'قصص سريعة الإيقاع وتغطيات للفعاليات.','Institutional & Social Impact':'مؤسسات وتأثير مجتمعي','Human stories with purpose.':'قصص إنسانية لها هدف.','Motion Graphics & 3D':'موشن جرافيك وثري دي','Titles, graphics and visual systems.':'تايتلز وجرافيك وأنظمة بصرية.','View Projects →':'شاهد المشاريع ←','Featured Reel':'عرض مميز','Showreel':'شوريل','A focused selection of work across television, entertainment, sports and branded content.':'مختارات مركزة من أعمال التلفزيون والترفيه والرياضة والمحتوى التجاري.','Open Work Archive':'افتح أرشيف الأعمال','About Me':'عني','Stories built in the edit.':'الحكاية تبدأ من المونتاج.','I’m Sayed Abdallah, a video editor and post-production specialist with experience across television, entertainment, advertising, sports and institutional content.':'أنا سيد عبدالله، مونتير ومتخصص في مرحلة ما بعد الإنتاج، ولدي خبرة في التلفزيون والترفيه والإعلانات والرياضة والمحتوى المؤسسي.','My focus is clear storytelling, strong pacing and polished delivery that serves both the audience and the project.':'أركز على الحكي الواضح، والإيقاع القوي، والتنفيذ المصقول بما يخدم الجمهور والمشروع معًا.','Video Editing':'مونتاج فيديو','Storytelling':'سرد قصصي','TV Promos':'بروموهات تلفزيونية','Post-Production':'ما بعد الإنتاج','Motion Graphics':'موشن جرافيك','Sound Design':'تصميم صوتي','Programs & Series':'برامج ومسلسلات','Commercial Content':'محتوى إعلاني','Events & Promos':'فعاليات وبروموهات','Selected Clients & Projects':'عملاء ومشاريع مختارة','Have a project in mind?':'عندك مشروع؟','Let’s Work Together.':'خلينا نشتغل مع بعض.','Message on WhatsApp':'راسلني على واتساب','Send an Email':'أرسل بريدًا إلكترونيًا','All rights reserved.':'جميع الحقوق محفوظة.','Video Portfolio':'معرض الفيديو','Project Video':'فيديو المشروع','Project video will be added after the final selection.':'سيتم إضافة فيديو المشروع بعد الاختيار النهائي.','Open Collection':'افتح المجموعة','Watch Video':'شاهد الفيديو','Watch Promo':'شاهد البرومو','Watch Music Video':'شاهد الفيديو الموسيقي','TV Program':'برنامج تلفزيوني','TV Program Edit':'مونتاج برنامج تلفزيوني','Video Collection':'مجموعة فيديوهات','Production & Entertainment':'إنتاج وترفيه','Selected editing work created for Good News.':'مختارات من أعمال المونتاج التي تم تنفيذها لصالح Good News.','Selected sports promos and content created for Al Ahly Club.':'مختارات من البروموهات والمحتوى الرياضي الذي تم تنفيذه للنادي الأهلي.','Selected ON E television editing work.':'مختارات من أعمال المونتاج التلفزيوني لقناة ON E.','Selected work from Program Bedaya.':'مختارات من أعمال برنامج بداية.','Selected work from MAKHMAK on SHASHA Kuwait.':'مختارات من أعمال برنامج مخمخ على منصة شاشة الكويت.','Phone':'الهاتف','LinkedIn Profile':'لينكدإن','WhatsApp':'واتساب','LinkedIn':'لينكدإن'
  };

  const textOriginals = new WeakMap();
  const attrOriginals = new WeakMap();
  let currentLang = localStorage.getItem('sa-lang') || 'en';

  const normalize = value => String(value || '').replace(/\s+/g, ' ').trim();

  function translatedText(value) {
    const key = normalize(value);
    return translations[key] || null;
  }

  function processTextNode(node, lang) {
    if (!node || node.nodeType !== Node.TEXT_NODE || !node.parentElement) return;
    const tag = node.parentElement.tagName;
    if (['SCRIPT','STYLE','NOSCRIPT'].includes(tag)) return;
    if (!textOriginals.has(node)) textOriginals.set(node, node.nodeValue);
    const original = textOriginals.get(node);
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
    if (!attrOriginals.has(el)) attrOriginals.set(el, {});
    const originals = attrOriginals.get(el);
    ['aria-label','title','placeholder'].forEach(attr => {
      if (!el.hasAttribute(attr)) return;
      if (!(attr in originals)) originals[attr] = el.getAttribute(attr);
      const original = originals[attr];
      if (lang === 'en') el.setAttribute(attr, original);
      else el.setAttribute(attr, translatedText(original) || original);
    });
  }

  function applyTo(root, lang) {
    if (!root) return;
    if (root.nodeType === Node.TEXT_NODE) processTextNode(root, lang);
    if (root.nodeType === Node.ELEMENT_NODE) processElement(root, lang);
    if (![Node.ELEMENT_NODE, Node.DOCUMENT_NODE, Node.DOCUMENT_FRAGMENT_NODE].includes(root.nodeType)) return;
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
    updateButtons(currentLang);
  }

  function mountSwitcher() {
    const header = document.querySelector('.site-header');
    if (!header || header.querySelector('.language-switcher')) return;
    const switcher = document.createElement('div');
    switcher.className = 'language-switcher';
    switcher.setAttribute('aria-label', 'Language');
    switcher.innerHTML = '<button type="button" data-lang="en" aria-pressed="false">EN</button><span class="divider">|</span><button type="button" data-lang="ar" aria-pressed="false">AR</button>';
    const cta = header.querySelector('.header-cta');
    if (cta) header.insertBefore(switcher, cta); else header.appendChild(switcher);
    switcher.addEventListener('click', event => {
      const button = event.target.closest('button[data-lang]');
      if (button) setLanguage(button.dataset.lang);
    });
  }

  const observer = new MutationObserver(mutations => {
    if (currentLang !== 'ar') return;
    for (const mutation of mutations) {
      mutation.addedNodes.forEach(node => applyTo(node, 'ar'));
    }
  });

  function init() {
    mountSwitcher();
    setLanguage(currentLang);
    observer.observe(document.body, {childList:true, subtree:true});
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();