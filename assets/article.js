'use strict';

// This is an illustrative single-line SHA-256 demo, not a launch measurement.
(() => {
  const published = 'send(message) if sentinel.approves(message)';
  const input = document.getElementById('demo-line');
  const hex = document.getElementById('demo-hex');
  const publishedHex = document.getElementById('demo-published-hex');
  const seal = document.getElementById('demo-seal');
  const reset = document.getElementById('demo-reset');
  const note = document.getElementById('demo-note');
  if (!input || !hex || !publishedHex || !seal || !reset || !note) return;
  const card = input.closest('.demo');
  let sequence = 0;
  let timer;

  const format = hash => '0x' + hash.slice(0, 24).toUpperCase().match(/.{4}/g).join('-');
  async function sha256(value) {
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value));
    return Array.from(new Uint8Array(digest), byte => byte.toString(16).padStart(2, '0')).join('');
  }
  function unavailable() {
    input.disabled = true;
    reset.disabled = true;
    hex.textContent = 'SHA-256 unavailable';
    seal.textContent = 'DEMO\nOFF';
    note.textContent = 'Interactive hashing needs browser crypto on HTTPS or localhost. The published value above is a shortened SHA-256 example.';
    card.setAttribute('aria-busy', 'false');
  }
  async function update() {
    const current = ++sequence;
    const value = input.value;
    card.setAttribute('aria-busy', 'true');
    try {
      const hash = await sha256(value);
      if (current !== sequence) return;
      hex.textContent = format(hash);
      hex.title = 'Full SHA-256: ' + hash;
      const matches = value === published;
      seal.classList.toggle('red', !matches);
      seal.textContent = matches ? 'MATCH' : 'NO\nMATCH';
      card.setAttribute('aria-busy', 'false');
    } catch {
      if (current === sequence) unavailable();
    }
  }
  if (!globalThis.crypto?.subtle || !globalThis.TextEncoder) {
    unavailable();
    return;
  }
  input.disabled = false;
  reset.disabled = false;
  input.addEventListener('input', () => {
    ++sequence; // Invalidate a slower digest immediately, before the debounce.
    clearTimeout(timer);
    timer = setTimeout(update, 120);
  });
  reset.addEventListener('click', () => {
    clearTimeout(timer);
    input.value = published;
    update();
    // Keep the software keyboard closed when restoring on a touch device.
    if (matchMedia('(hover:hover) and (pointer:fine)').matches) input.focus({preventScroll:true});
  });
  addEventListener('pageshow', () => {
    clearTimeout(timer);
    update();
  });
  sha256(published).then(hash => {
    publishedHex.textContent = format(hash);
    publishedHex.title = 'Full SHA-256: ' + hash;
  }).catch(unavailable);
  update();
})();

// Example report bytes are explicitly labeled as examples in the article.
(() => {
  const card = document.getElementById('meas');
  const button = document.getElementById('meas-toggle');
  if (!card || !button) return;
  const rows = card.querySelectorAll('[data-mrow]');
  const digest2 = document.getElementById('meas-d2');
  const digest3 = document.getElementById('meas-d3');
  const kernelHash = document.getElementById('meas-kh');
  const status = document.getElementById('meas-status');
  const measurement = {
    pub: 'a7f39c2e4b1d8e60f2a911c47fee13a9b9812fb440c4578944e3f68978f9ff25db2ef423b6bdfe4c7f894698a0d8269c',
    mod: '0681db03f04cc040d00b4f047128bfedaf393fbd3fd9f7f1dcd849baff048e86e6d9a886eba7e52c786aaa64f2165d7f'
  };
  let changed = false;
  button.disabled = false;
  button.addEventListener('click', () => {
    changed = !changed;
    const hash = changed ? measurement.mod : measurement.pub;
    rows.forEach((row, index) => {
      const bytes = hash.slice(index * 32, index * 32 + 32).match(/../g);
      row.textContent = bytes.slice(0, 8).join(' ') + '  ' + bytes.slice(8).join(' ');
    });
    digest2.textContent = changed ? '4f74 0124 …' : 'cf46 0482 …';
    kernelHash.textContent = changed ? '6fba 0925…' : '032b 6a39…';
    const label = document.createElement('small');
    label.textContent = '= MEASUREMENT';
    digest3.replaceChildren(label, hash.slice(0, 4) + ' ' + hash.slice(4, 8) + ' …');
    const differences = measurement.pub.match(/../g).filter((byte, index) => byte !== hash.slice(index * 2, index * 2 + 2)).length;
    status.textContent = changed
      ? `One kernel byte changed · ${differences} of 48 bytes differ`
      : 'Published kernel · the value verifiers expect';
    card.classList.toggle('changed', changed);
    button.textContent = changed ? 'Restore the published kernel' : 'Change one byte of the kernel';
    button.setAttribute('aria-pressed', String(changed));
  });
})();

// Only overflow regions need a tab stop. Touch stays native; arrows also work in WebKit.
(() => {
  const regions = document.querySelectorAll('.mt-wrap,.scroll-x,.mc-hex,.term pre');
  regions.forEach(region => region.addEventListener('keydown', event => {
    if (event.target !== region || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    if (region.scrollWidth <= region.clientWidth + 1) return;
    const direction = event.key === 'ArrowRight' ? 1 : event.key === 'ArrowLeft' ? -1 : 0;
    if (!direction) return;
    event.preventDefault();
    region.scrollLeft += direction * 40;
  }));
  function update() {
    regions.forEach(region => {
      if (region.scrollWidth > region.clientWidth + 1) region.tabIndex = 0;
      else region.removeAttribute('tabindex');
    });
  }
  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(update);
    regions.forEach(region => observer.observe(region));
  } else {
    addEventListener('resize', update, {passive:true});
  }
  document.fonts?.ready.then(update);
  update();
})();
