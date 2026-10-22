(() => {
  'use strict';
  const links = [...document.querySelectorAll('[data-work]')];
  const dialog = document.querySelector('#viewer');
  if (!dialog || !links.length || typeof dialog.showModal !== 'function') return;
  const image = dialog.querySelector('img');
  const title = dialog.querySelector('#viewer-title');
  const count = dialog.querySelector('#viewer-count');
  const error = dialog.querySelector('.viewer-error');
  const previous = dialog.querySelector('[data-previous]');
  const next = dialog.querySelector('[data-next]');
  let current = 0;
  let trigger;
  const render = () => {
    const link = links[current];
    image.hidden = false;
    error.hidden = true;
    image.alt = link.querySelector('img').alt;
    image.src = link.href;
    title.textContent = link.dataset.title;
    count.textContent = `${String(current + 1).padStart(2, '0')} / ${String(links.length).padStart(2, '0')}`;
    previous.disabled = current === 0;
    next.disabled = current === links.length - 1;
  };
  const move = step => {
    const target = current + step;
    if (target < 0 || target >= links.length) return;
    current = target;
    render();
  };
  links.forEach((link, i) => link.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    current = i;
    trigger = link;
    render();
    dialog.showModal();
    dialog.querySelector('[data-close]').focus();
  }));
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft') { event.preventDefault(); move(-1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); move(1); }
  });
  dialog.addEventListener('close', () => trigger?.focus());
  image.addEventListener('error', () => { image.hidden = true; error.hidden = false; });
  document.querySelectorAll('.work img').forEach(img => img.addEventListener('error', () => {
    const caption = img.closest('.work').querySelector('figcaption');
    if (!caption.querySelector('[data-error]')) {
      const note = document.createElement('span');
      note.dataset.error = '';
      note.textContent = error.textContent;
      caption.append(note);
    }
  }));
})();
