(() => {
  'use strict';
  const links = [...document.querySelectorAll('[data-language]')];
  const preserveSection = () => links.forEach(link => {
    const target = new URL(link.href);
    target.hash = location.hash;
    link.href = target.href;
  });
  preserveSection();
  window.addEventListener('hashchange', preserveSection);
  const remember = language => {
    try { localStorage.setItem('monoloco-language', language); } catch (_) { /* Storage may be disabled. */ }
  };
  links.forEach(link => link.addEventListener('click', () => remember(link.dataset.language)));
  // Offer the remembered language on the homepage; shared URLs always open as written.
  const homepage = document.querySelector('.hero-four');
  if (!homepage) return;
  let preferred;
  let dismissed;
  try {
    preferred = localStorage.getItem('monoloco-language');
    dismissed = sessionStorage.getItem('monoloco-language-hint-dismissed');
  } catch (_) { /* Language links work without storage. */ }
  if (!preferred && navigator.language.toLowerCase().startsWith('en')) preferred = 'en';
  const target = links.find(link => link.dataset.language === preferred);
  if (!target || dismissed) return;
  const hint = document.createElement('div');
  hint.className = 'language-hint wrap';
  const action = document.createElement('a');
  action.href = target.href;
  action.lang = preferred;
  action.textContent = preferred === 'en' ? 'Continue in English ↗' : '切换到中文 ↗';
  action.addEventListener('click', () => remember(preferred));
  const close = document.createElement('button');
  close.type = 'button';
  close.textContent = '×';
  close.setAttribute('aria-label', document.documentElement.lang === 'en' ? 'Dismiss language suggestion' : '关闭语言提示');
  close.addEventListener('click', () => {
    hint.remove();
    try { sessionStorage.setItem('monoloco-language-hint-dismissed', '1'); } catch (_) { /* Optional. */ }
  });
  hint.append(action, close);
  document.querySelector('.masthead').after(hint);
})();
