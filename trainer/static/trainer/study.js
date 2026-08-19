(() => {
  const root = document.querySelector('[data-study-root]');
  if (!root) return;

  const els = {
    card: root.querySelector('[data-card]'), front: root.querySelector('[data-front]'), back: root.querySelector('[data-back]'),
    question: root.querySelector('[data-question]'), context: root.querySelector('[data-context]'), answer: root.querySelector('[data-answer]'),
    explanation: root.querySelector('[data-explanation]'), explanationWrap: root.querySelector('[data-explanation-wrap]'),
    code: root.querySelector('[data-code]'), answerCode: root.querySelector('[data-answer-code]'), kind: root.querySelector('[data-kind]'), difficulty: root.querySelector('[data-difficulty]'),
    source: root.querySelector('[data-source]'), reveal: root.querySelector('[data-reveal]'), rating: root.querySelector('[data-rating]'),
    verdictPanel: root.querySelector('[data-verdict-panel]'), verdictFeedback: root.querySelector('[data-verdict-feedback]'),
    verdictResult: root.querySelector('[data-verdict-result]'), verdictLabel: root.querySelector('[data-verdict-label]'),
    select: root.querySelector('[data-module-select]'), mode: root.querySelector('[data-mode-select]'), progress: root.querySelector('[data-progress-bar]'), empty: root.querySelector('[data-empty]'),
    statDue: root.querySelector('[data-stat-due]'), statSeen: root.querySelector('[data-stat-seen]'), statMastered: root.querySelector('[data-stat-mastered]')
  };

  const STORAGE_KEY = 'backend-recall-progress-v1';
  let allCards = [], queue = [], current = null, completed = 0, revealed = false, verdictAnswered = false;
  const progress = loadProgress();

  function loadProgress() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; } catch { return {}; }
  }
  function saveProgress() { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); }
  function shuffle(items) {
    const copy = [...items];
    for (let i = copy.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [copy[i], copy[j]] = [copy[j], copy[i]]; }
    return copy;
  }
  function selectedModule() { return els.select.value; }
  function matchesMode(card) {
    if (els.mode.value === 'all') return true;
    if (els.mode.value === 'entrevista') return card.module === 'entrevista';
    if (els.mode.value === 'debugging') return card.kind === 'debugging';
    if (els.mode.value === 'completar') return card.kind === 'completar';
    if (els.mode.value === 'veredicto') return card.verdict !== null;
    if (els.mode.value === 'casos') return card.kind === 'mini caso';
    return card.code && !['debugging', 'completar'].includes(card.kind) && card.module !== 'entrevista';
  }
  function eligibleCards() {
    const module = selectedModule();
    return allCards.filter(c => (module === 'all' || c.module === module) && matchesMode(c));
  }
  function buildQueue() {
    const now = Date.now();
    const cards = eligibleCards();
    const due = cards.filter(c => progress[c.id]?.due && progress[c.id].due <= now);
    const fresh = cards.filter(c => !progress[c.id]);
    const future = cards.filter(c => progress[c.id]?.due > now).sort((a,b) => progress[a.id].due - progress[b.id].due);
    queue = shuffle([...due, ...fresh]).slice(0, 25);
    if (!queue.length) queue = future.slice(0, 10);
    completed = 0;
    renderStats();
    nextCard();
  }
  function nextCard() {
    current = queue.shift() || null;
    revealed = false;
    verdictAnswered = false;
    els.rating.hidden = true;
    if (!current) {
      els.card.hidden = true; els.empty.hidden = false; els.progress.style.width = '100%'; return;
    }
    els.card.hidden = false; els.empty.hidden = true; els.front.hidden = false; els.back.hidden = true;
    const isVerdictCard = current.verdict !== null;
    els.verdictPanel.hidden = !isVerdictCard;
    els.verdictFeedback.hidden = true;
    els.verdictFeedback.className = 'verdict-feedback';
    els.reveal.hidden = isVerdictCard;
    els.question.textContent = current.question;
    els.context.textContent = current.context || '';
    els.context.hidden = !current.context;
    els.answer.textContent = current.answer;
    els.explanation.textContent = current.explanation || '';
    els.explanationWrap.hidden = !current.explanation;
    els.kind.textContent = current.kind.toUpperCase();
    els.difficulty.textContent = current.difficulty.toUpperCase();
    els.source.href = current.source;
    const codeEl = els.code.querySelector('code');
    if (current.code) { codeEl.textContent = current.code; els.code.hidden = false; } else { codeEl.textContent = ''; els.code.hidden = true; }
    const answerCodeEl = els.answerCode.querySelector('code');
    if (current.answer_code) { answerCodeEl.textContent = current.answer_code; els.answerCode.hidden = false; } else { answerCodeEl.textContent = ''; els.answerCode.hidden = true; }
    const total = completed + queue.length + 1;
    els.progress.style.width = `${total ? (completed / total) * 100 : 0}%`;
    els.card.focus({preventScroll:true});
  }
  function reveal() {
    if (!current || revealed) return;
    if (current.verdict !== null && !verdictAnswered) return;
    revealed = true; els.front.hidden = true; els.back.hidden = false; els.rating.hidden = false;
  }
  function answerVerdict(choice) {
    if (!current || current.verdict === null || revealed) return;
    verdictAnswered = true;
    const correct = choice === current.verdict;
    els.verdictFeedback.hidden = false;
    els.verdictFeedback.classList.add(correct ? 'is-correct' : 'is-wrong');
    els.verdictResult.textContent = correct ? 'Acertaste' : 'No era esa';
    els.verdictLabel.textContent = current.verdict ? 'El código está bien' : 'El código tiene un problema';
    reveal();
  }
  function grade(level) {
    if (!current || !revealed) return;
    const old = progress[current.id] || { seen: 0, streak: 0, interval: 0 };
    const now = Date.now();
    const day = 24 * 60 * 60 * 1000;
    let interval, streak = old.streak || 0;
    if (level === 'again') { interval = 10 * 60 * 1000; streak = 0; }
    else if (level === 'hard') { interval = Math.max(day, (old.interval || day) * 1.35); streak = Math.max(0, streak); }
    else if (level === 'good') { interval = old.interval ? Math.max(2 * day, old.interval * 2.15) : 2 * day; streak += 1; }
    else { interval = old.interval ? Math.max(4 * day, old.interval * 3.2) : 4 * day; streak += 1; }
    progress[current.id] = { seen: (old.seen || 0) + 1, streak, interval, due: now + interval, lastGrade: level, updated: now };
    saveProgress(); completed += 1; renderStats(); nextCard();
  }
  function renderStats() {
    const now = Date.now(), cards = eligibleCards();
    els.statDue.textContent = cards.filter(c => !progress[c.id] || progress[c.id].due <= now).length;
    els.statSeen.textContent = cards.filter(c => progress[c.id]?.seen > 0).length;
    els.statMastered.textContent = cards.filter(c => (progress[c.id]?.streak || 0) >= 3).length;
  }
  function setFiltersFromUrl() {
    const params = new URLSearchParams(location.search);
    const module = params.get('module');
    const mode = params.get('mode');
    if (module && [...els.select.options].some(o => o.value === module)) els.select.value = module;
    if (mode && [...els.mode.options].some(o => o.value === mode)) els.mode.value = mode;
  }
  function syncFiltersToUrl() {
    const params = new URLSearchParams();
    if (els.select.value !== 'all') params.set('module', els.select.value);
    if (els.mode.value !== 'all') params.set('mode', els.mode.value);
    const query = params.toString();
    history.replaceState(null, '', query ? `?${query}` : location.pathname);
  }

  els.reveal.addEventListener('click', reveal);
  root.querySelectorAll('[data-verdict-choice]').forEach(btn => btn.addEventListener('click', () => answerVerdict(btn.dataset.verdictChoice === 'true')));
  root.querySelectorAll('[data-grade]').forEach(btn => btn.addEventListener('click', () => grade(btn.dataset.grade)));
  els.select.addEventListener('change', () => { syncFiltersToUrl(); buildQueue(); });
  els.mode.addEventListener('change', () => { syncFiltersToUrl(); buildQueue(); });
  root.querySelector('[data-reset-session]').addEventListener('click', buildQueue);
  root.querySelector('[data-restart]').addEventListener('click', buildQueue);
  root.querySelector('[data-reset-progress]').addEventListener('click', () => {
    if (!confirm('¿Reiniciar todo tu progreso de estudio?')) return;
    Object.keys(progress).forEach(k => delete progress[k]); saveProgress(); buildQueue();
  });
  document.addEventListener('keydown', (e) => {
    if (e.code === 'Space' && !['INPUT','SELECT','TEXTAREA','BUTTON'].includes(document.activeElement.tagName)) { e.preventDefault(); reveal(); }
    if (revealed && ['1','2','3','4'].includes(e.key)) grade({1:'again',2:'hard',3:'good',4:'easy'}[e.key]);
  });

  fetch('/api/cards/')
    .then(r => { if (!r.ok) throw new Error('No se pudo cargar el mazo'); return r.json(); })
    .then(data => { allCards = data.cards; setFiltersFromUrl(); buildQueue(); })
    .catch(err => { els.question.textContent = err.message; els.reveal.hidden = true; });
})();
