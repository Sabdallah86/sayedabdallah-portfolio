const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'script.js'), 'utf8');
const updates = fs.readFileSync(path.join(root, 'site-updates.js'), 'utf8');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
function run(query = '') {
  const listeners = {}, main = { innerHTML: '' };
  const el = () => {
    const classes = new Set();
    return { rel:'', href:'', hidden:false, src:'', textContent:'',
      classList:{add(...names){names.forEach(n=>classes.add(n));},remove(...names){names.forEach(n=>classes.delete(n));},toggle(n,on){if(on)classes.add(n);else classes.delete(n);},contains(n){return classes.has(n);}},
      appendChild(){},addEventListener(){},querySelector(){return null;},
      setAttribute(){},removeAttribute(name){this[name]='';},pause(){},load(){},focus(){}
    };
  };
  const modal=el(), player=el(), iframe=el(), title=el(), close=el();
  modal.querySelector=() => el();
  const document = {
    title:'Home', head:el(), body:el(), createElement:el,
    querySelector:selector => selector === 'main' ? main : selector === '.video-modal-close' ? close : null,
    querySelectorAll:() => [], getElementById:id => ({'video-modal':modal,'project-video-player':player,'youtube-video-player':iframe,'video-modal-title':title}[id] || null),
    addEventListener(type, callback) { (listeners[type] ||= []).push(callback); }
  };
  const location = { href:'https://portfolio.test/index.html'+query, search:query };
  const context = { document, location, URL, URLSearchParams, Date, console,
    window:{addEventListener(){}}, history:{replaceState(_,__,url){ location.normalized=url; }} };
  vm.createContext(context);
  vm.runInContext(source, context);
  const before = main.innerHTML;
  vm.runInContext(updates, context);
  assert.equal(main.innerHTML, before, 'site-updates must not replace initialized cards');
  return { context, document, main, listeners, location, modal, player, iframe, title, data:vm.runInContext('categoryData',context) };
}
const data = run().data;
test('all category, collection and homepage targets exist', () => {
  assert.ok(!data['sports-events']);
  assert.ok(!data['motion-graphics']);
  for (const [key, category] of Object.entries(data)) {
    assert.ok(category.projects.length, `${key} must retain its published projects`);
    for (const project of category.projects) {
      if (project.collection) assert.ok(category.collections?.[project.collection], `${key}/${project.collection}`);
    }
    for (const [slug, collection] of Object.entries(category.collections || {})) {
      assert.ok(collection.projects.length, `${key}/${slug} must contain projects`);
      const result = run(`?category=${key}&collection=${slug}`);
      assert.equal(result.document.title, `${collection.title} — Sayed Abdallah`);
      assert.match(result.main.innerHTML, /collection-card|project-video/);
    }
  }
  for (const match of html.matchAll(/href="(index\.html\?[^\"]+)"/g)) {
    const url = new URL(match[1].replaceAll('&amp;', '&'), 'https://portfolio.test');
    const key = url.searchParams.get('category'), collection = url.searchParams.get('collection');
    assert.ok(data[key], match[1]);
    if (collection) assert.ok(data[key].collections?.[collection], match[1]);
  }
  assert.doesNotMatch(html, /category=sports-events|category=motion-graphics|Ramadan 2025/);
});
test('legacy bookmarks keep collection intent and normalize URLs', () => {
  const cases = [
    ['?category=sports-events&collection=al-ahly','sports','al-ahly-club'],
    ['?category=sports-events&collection=al-ahly-club','sports','al-ahly-club'],
    ['?category=sports-events&collection=ciff','events','ciff'],
    ['?category=sports&collection=al-ahly','sports','al-ahly-club'],
    ['?category=motion-graphics','ai-work',null],
    ['?category=tv-programs&collection=on-e','on-e-channel',null]
  ];
  for (const [query,key,collection] of cases) {
    const result = run(query), normalized = new URL(result.location.normalized, 'https://portfolio.test');
    assert.equal(normalized.searchParams.get('category'), key);
    assert.equal(normalized.searchParams.get('collection'), collection);
    assert.equal(result.document.title, `${(collection ? data[key].collections[collection] : data[key]).title} — Sayed Abdallah`);
  }
  const combined = run('?category=sports-events&utm_source=bookmark');
  assert.equal(combined.main.innerHTML, '');
  assert.equal(combined.location.normalized, '/index.html?utm_source=bookmark#categories');
});
test('invalid or inherited keys are explicit unavailable routes', () => {
  for (const query of ['?category=unknown','?category=tv-programs&collection=unknown','?category=toString','?category=tv-programs&collection=toString','?collection=arabwood']) {
    assert.equal(run(query).document.title, 'Work not found — Sayed Abdallah');
  }
});
test('related navigation uses canonical data and player events are delegated', () => {
  for (const key of Object.keys(data)) {
    const result = run(`?category=${key}`);
    assert.doesNotMatch(result.main.innerHTML, /category=sports-events|category=motion-graphics/);
    assert.ok(result.listeners.click?.length);
    assert.ok(result.listeners.keydown?.length);
    assert.ok(result.listeners.error?.length);
  }
  assert.equal(data['ai-work'].projects.length, 5);
  assert.equal(data['on-e-channel'].projects.length, 11);
  assert.equal(data['tv-programs'].collections['my-guest-moataz-el-demerdash'].projects.length, 5);
  assert.match(run('?category=on-e-channel').main.innerHTML, /data-vimeo="813971630"/);
});

test('delegated cards open the matching player by click and keyboard', () => {
  const result = run('?category=sports&collection=al-ahly-club');
  for (const [kind,id,expected] of [
    ['youtube','N4uGPUETGb4','https://www.youtube-nocookie.com/embed/N4uGPUETGb4'],
    ['vimeo','813971630','https://player.vimeo.com/video/813971630'],
    ['video','assets/ai-work-01.mp4','assets/ai-work-01.mp4']
  ]) {
    const card = { dataset:{[kind]:id,title:'Test Project'}, matches:()=>false, focus(){} };
    let prevented=false;
    const event = {type:'click', target:{closest:()=>card}, preventDefault(){prevented=true;}};
    result.listeners.click.forEach(callback=>callback(event));
    assert.ok(prevented);
    assert.ok(result.modal.classList.contains('open'));
    assert.equal(result.title.textContent,'Test Project');
    const target = kind === 'video' ? result.player : result.iframe;
    assert.ok(target.src.startsWith(expected));
    assert.equal(target.hidden,false);
    result.context.closeProjectVideo();
    assert.equal(result.modal.classList.contains('open'),false);
    result.listeners.keydown.forEach(callback=>callback({...event,type:'keydown',key:'Enter'}));
    assert.ok(result.modal.classList.contains('open'));
    result.context.closeProjectVideo();
    result.listeners.keydown.forEach(callback=>callback({...event,type:'keydown',key:'Tab'}));
    assert.equal(result.modal.classList.contains('open'),false);
  }
});
