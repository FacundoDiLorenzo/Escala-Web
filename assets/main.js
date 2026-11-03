/* Escala Web — shared behaviour: language, menu, reveals, copy buttons, floating WhatsApp. */
(function(){
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
const $ = (s, r=document) => r.querySelector(s);
const $$ = (s, r=document) => [...r.querySelectorAll(s)];

/* ── language ── */
let current = 'es';
function applyLang(l){
  current = l;
  document.documentElement.lang = l;
  $$('[data-i18n]').forEach(el => { const v = T[l][el.dataset.i18n]; if (v) el.textContent = v; });
  $$('[data-i18n-label]').forEach(el => { const v = T[l][el.dataset.i18nLabel]; if (v) el.setAttribute('aria-label', v); });
  $$('[data-lang-block]').forEach(el => { el.hidden = el.dataset.langBlock !== l; });
  $$('.lang button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === l)));
  const tk = document.body.dataset.title; if (tk && T[l][tk]) document.title = T[l][tk];
  syncMenuLabel();
  try { localStorage.setItem('lang', l); } catch (e) {}
}
function setLang(l){
  if (!T[l] || l === current) return;
  const parts = $$('main, footer.site, nav.main .links, .menu-panel, #wa-float');
  if (reduceMotion.matches || !parts[0] || !parts[0].animate) { applyLang(l); return; }
  // quick crossfade so the swap reads as one change, not a flicker
  const out = parts.map(p => p.animate([{opacity:1},{opacity:0}], {duration:120, easing:'ease-out', fill:'forwards'}));
  out[0].finished.then(() => {
    applyLang(l);
    parts.forEach((p,i) => { out[i].cancel(); p.animate([{opacity:0, filter:'blur(2px)'},{opacity:1, filter:'blur(0)'}], {duration:240, easing:'cubic-bezier(0.23,1,0.32,1)'}); });
  });
}
$$('.lang button').forEach(b => b.addEventListener('click', () => setLang(b.dataset.lang)));

/* ── mobile menu ── */
const header = $('header.site'), menuBtn = $('#menu-btn'), panel = $('#menu-panel');
function syncMenuLabel(){
  if (!menuBtn) return;
  const open = menuBtn.getAttribute('aria-expanded') === 'true';
  menuBtn.setAttribute('aria-label', T[current][open ? 'menuClose' : 'menuOpen']);
}
function setMenu(open, focusBack){
  if (!menuBtn) return;
  menuBtn.setAttribute('aria-expanded', String(open));
  panel.toggleAttribute('data-open', open);
  header.toggleAttribute('data-menu-open', open);
  $$('a', panel).forEach(a => a.tabIndex = open ? 0 : -1);
  syncMenuLabel();
  if (open) { const first = $('a', panel); if (first) first.focus({preventScroll:true}); }
  else if (focusBack) menuBtn.focus();
}
if (menuBtn){
  setMenu(false);
  menuBtn.addEventListener('click', () => setMenu(menuBtn.getAttribute('aria-expanded') !== 'true'));
  addEventListener('keydown', e => { if (e.key === 'Escape' && panel.hasAttribute('data-open')) setMenu(false, true); });
  document.addEventListener('click', e => { if (panel.hasAttribute('data-open') && !header.contains(e.target)) setMenu(false); });
  matchMedia('(min-width: 821px)').addEventListener('change', e => { if (e.matches) setMenu(false); });
}

/* ── header hairline once the page scrolls ── */
const onScroll = () => header && header.toggleAttribute('data-scrolled', scrollY > 8);
addEventListener('scroll', onScroll, {passive:true}); onScroll();

/* ── flip card (tap / keyboard) ── */
const flip = $('#flip-card');
if (flip) flip.addEventListener('click', () => flip.setAttribute('aria-pressed', String(flip.getAttribute('aria-pressed') !== 'true')));

/* ── copy buttons: icon morph + label swap ── */
$$('.copy').forEach(b => {
  let t;
  b.addEventListener('click', () => {
    const label = $('.copy-txt', b);
    const done = () => { b.dataset.state = 'copied'; label.textContent = T[current].copied; clearTimeout(t); t = setTimeout(() => { delete b.dataset.state; label.textContent = T[current].copy; }, 1800); };
    const fallback = () => { const v = $('.val', b.parentElement); const r = document.createRange(); r.selectNodeContents(v); const s = getSelection(); s.removeAllRanges(); s.addRange(r); };
    try { navigator.clipboard.writeText(b.dataset.copy).then(done, fallback); } catch (e) { fallback(); }
  });
});

/* ── reveals: what enters together cascades in reading order ── */
const rvTargets = $$('[data-rv]');
if ('IntersectionObserver' in window){
  const rv = new IntersectionObserver(es => {
    let n = 0;
    es.filter(e => e.isIntersecting)
      .sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top || a.boundingClientRect.left - b.boundingClientRect.left)
      .forEach(e => { e.target.style.setProperty('--d', Math.min(n++ * 90, 450) + 'ms'); e.target.classList.add('in'); rv.unobserve(e.target); });
  }, {threshold:0.15});
  rvTargets.forEach(el => rv.observe(el));
} else rvTargets.forEach(el => el.classList.add('in'));

/* ── floating WhatsApp on phones: after the first screen, hidden near a real contact block ── */
const wa = $('#wa-float');
if (wa && 'IntersectionObserver' in window){
  let past = false, near = false;
  const sync = () => { const show = past && !near; wa.toggleAttribute('data-show', show); wa.tabIndex = show ? 0 : -1; };
  const first = $('main > :first-child');
  if (first) new IntersectionObserver(([e]) => { past = !e.isIntersecting && e.boundingClientRect.top < 0; sync(); }).observe(first);
  const blocks = $$('[data-wa-hide]');
  const seen = new Set();
  if (blocks.length) { const io = new IntersectionObserver(es => { es.forEach(e => e.isIntersecting ? seen.add(e.target) : seen.delete(e.target)); near = seen.size > 0; sync(); }, {rootMargin:'0px 0px -20% 0px'}); blocks.forEach(b => io.observe(b)); }
}

/* ── start ── */
let saved = null; try { saved = localStorage.getItem('lang'); } catch (e) {}
applyLang(T[saved] ? saved : 'es');
})();
