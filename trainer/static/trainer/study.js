(() => {
  const root = document.querySelector('[data-study-root]');
  if (!root) return;

  const els = {
    card: root.querySelector('[data-card]'), front: root.querySelector('[data-front]'), back: root.querySelector('[data-back]'),
    question: root.querySelector('[data-question]'), context: root.querySelector('[data-context]'), answer: root.querySelector('[data-answer]'),
    explanation: root.querySelector('[data-explanation]'), explanationWrap: root.querySelector('[data-explanation-wrap]'),
    code: root.querySelector('[data-code]'), answerCode: root.querySelector('[data-answer-code]'), kind: root.querySelector('[data-kind]'),
    difficulty: root.querySelector('[data-difficulty]'), cardLevel: root.querySelector('[data-card-level]'), source: root.querySelector('[data-source]'),
    reveal: root.querySelector('[data-reveal]'), rating: root.querySelector('[data-rating]'), verdictPanel: root.querySelector('[data-verdict-panel]'),
    verdictFeedback: root.querySelector('[data-verdict-feedback]'), verdictResult: root.querySelector('[data-verdict-result]'),
    verdictLabel: root.querySelector('[data-verdict-label]'), select: root.querySelector('[data-module-select]'), mode: root.querySelector('[data-mode-select]'),
    progress: root.querySelector('[data-progress-bar]'), empty: root.querySelector('[data-empty]'), emptyMessage: root.querySelector('[data-empty-message]'),
    statDue: root.querySelector('[data-stat-due]'), statSeen: root.querySelector('[data-stat-seen]'), statMastered: root.querySelector('[data-stat-mastered]'),
    levelHeading: root.querySelector('[data-level-heading]'), levelLede: root.querySelector('[data-level-lede]'),
    levelGuidance: root.querySelector('[data-level-guidance]'), levelChoices: [...root.querySelectorAll('[data-level-choice]')],
  };

  const STORAGE_KEY = 'backend-recall-progress-v1';
  const LEVEL_KEY = 'backend-recall-level-v1';
  const GRADE_POINTS = { again: 0, hard: 40, good: 80, easy: 100 };
  const MASTERED_GRADES = new Set(['good', 'easy']);
  const UNLOCK_SCORE = 75;
  const UNLOCK_MASTERY = 80;
  let allCards = [], curriculum = [], queue = [], current = null, selectedLevel = 1, completed = 0;
  let revealed = false, verdictAnswered = false;
  const progress = loadProgress();

  function loadProgress() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; } catch { return {}; }
  }
  function saveProgress() { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); }
  function shuffle(items) {
    const copy = [...items];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
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
  function cardsForLevel(level) { return allCards.filter(card => card.level === level); }
  function eligibleCards() {
    const module = selectedModule();
    return cardsForLevel(selectedLevel).filter(card => (module === 'all' || card.module === module) && matchesMode(card));
  }
  function pointsFor(cardProgress) { return GRADE_POINTS[cardProgress?.lastGrade] ?? 0; }
  function statsForLevel(level) {
    const cards = cardsForLevel(level);
    const seen = cards.filter(card => (progress[card.id]?.seen || 0) > 0).length;
    const mastered = cards.filter(card => MASTERED_GRADES.has(progress[card.id]?.lastGrade)).length;
    const failed = cards.filter(card => progress[card.id]?.lastGrade === 'again').length;
    const totalPoints = cards.reduce((sum, card) => sum + pointsFor(progress[card.id]), 0);
    const total = cards.length;
    return {
      total, seen, mastered, failed,
      coverage: total ? Math.round((seen / total) * 100) : 0,
      mastery: total ? Math.round((mastered / total) * 100) : 0,
      score: total ? Math.round(totalPoints / total) : 0,
    };
  }
  function levelPassed(stats) {
    return stats.total > 0 && stats.seen === stats.total && stats.mastery >= UNLOCK_MASTERY
      && stats.score >= UNLOCK_SCORE && stats.failed === 0;
  }
  function unlockedLevels() {
    const unlocked = new Set([1]);
    const maxLevel = curriculum.length || 4;
    for (let level = 2; level <= maxLevel; level += 1) {
      if (levelPassed(statsForLevel(level - 1))) unlocked.add(level);
      else break;
    }
    return unlocked;
  }
  function recommendedLevel() {
    const unlocked = unlockedLevels();
    for (let level = 1; level <= (curriculum.length || 4); level += 1) {
      if (unlocked.has(level) && !levelPassed(statsForLevel(level))) return level;
    }
    return Math.max(...unlocked);
  }
  function levelInfo(level) {
    return curriculum.find(item => item.id === level) || { id: level, name: `Nivel ${level}`, goal: 'Seguí construyendo criterio backend.' };
  }

  function renderCurriculum() {
    const unlocked = unlockedLevels();
    const recommended = recommendedLevel();
    els.levelChoices.forEach(button => {
      const level = Number(button.dataset.levelChoice);
      const stats = statsForLevel(level);
      const passed = levelPassed(stats);
      const locked = !unlocked.has(level);
      const currentLevel = level === selectedLevel;
      button.classList.toggle('is-current', currentLevel);
      button.classList.toggle('is-passed', passed);
      button.classList.toggle('is-locked', locked);
      button.setAttribute('aria-pressed', String(currentLevel));
      button.querySelector('[data-level-seen]').textContent = `${stats.seen}/${stats.total}`;
      button.querySelector('[data-level-mastery]').textContent = `${stats.mastery}%`;
      button.querySelector('[data-level-score]').textContent = stats.score;
      button.querySelector('[data-level-bar]').style.width = `${stats.score}%`;
      button.querySelector('[data-level-state]').textContent = passed ? 'SUPERADO'
        : currentLevel ? (locked ? 'EXPLORANDO' : 'EN CURSO')
          : locked ? 'ADELANTADO' : 'DISPONIBLE';
    });

    const info = levelInfo(selectedLevel);
    const stats = statsForLevel(selectedLevel);
    const missingSeen = stats.total - stats.seen;
    const missingMastered = Math.max(0, Math.ceil(stats.total * .8) - stats.mastered);
    els.levelHeading.textContent = `Nivel ${selectedLevel} · ${info.name}`;
    els.levelLede.textContent = info.goal;
    if (!unlocked.has(selectedLevel)) {
      const recommendedInfo = levelInfo(recommended);
      els.levelGuidance.textContent = `Estás explorando contenido adelantado. La ruta recomendada continúa en Nivel ${recommended}: ${recommendedInfo.name}.`;
    } else if (levelPassed(stats) && selectedLevel === curriculum.length) {
      els.levelGuidance.textContent = 'Ruta completa. Mantené el dominio con repasos espaciados y simulaciones de entrevista.';
    } else if (levelPassed(stats)) {
      els.levelGuidance.textContent = `Nivel superado. El Nivel ${selectedLevel + 1} está disponible.`;
    } else {
      const needs = [];
      if (missingSeen) needs.push(`ver ${missingSeen} card${missingSeen === 1 ? '' : 's'}`);
      if (missingMastered) needs.push(`dominar ${missingMastered} más`);
      if (stats.score < UNLOCK_SCORE) needs.push(`subir ${UNLOCK_SCORE - stats.score} puntos`);
      if (stats.failed) needs.push(`recuperar ${stats.failed} “No salió”`);
      els.levelGuidance.textContent = `Para avanzar te falta ${needs.join(', ') || 'consolidar el repaso'}.`;
    }
  }

  function renderStats() {
    const now = Date.now(), cards = cardsForLevel(selectedLevel), stats = statsForLevel(selectedLevel);
    els.statDue.textContent = cards.filter(card => !progress[card.id] || progress[card.id].due <= now).length;
    els.statSeen.textContent = stats.seen;
    els.statMastered.textContent = stats.mastered;
    renderCurriculum();
  }
  function buildQueue({ mix = false } = {}) {
    const now = Date.now(), cards = eligibleCards();
    const bySequence = (a, b) => a.sequence - b.sequence;
    const due = cards.filter(card => progress[card.id]?.due && progress[card.id].due <= now)
      .sort((a, b) => progress[a.id].due - progress[b.id].due || bySequence(a, b));
    const fresh = cards.filter(card => !progress[card.id]).sort(bySequence);
    const future = cards.filter(card => progress[card.id]?.due > now)
      .sort((a, b) => progress[a.id].due - progress[b.id].due || bySequence(a, b));
    queue = [...(mix ? shuffle(due) : due), ...fresh].slice(0, 25);
    if (!queue.length) queue = (mix ? shuffle(future) : future).slice(0, 10);
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
      els.card.hidden = true;
      els.empty.hidden = false;
      els.progress.style.width = '100%';
      els.emptyMessage.textContent = eligibleCards().length
        ? 'Terminaste esta tanda. Podés repasar, cambiar filtros o continuar cuando haya cards vencidas.'
        : 'No hay cards de este nivel que coincidan con los filtros actuales.';
      return;
    }
    els.card.hidden = false;
    els.empty.hidden = true;
    els.front.hidden = false;
    els.back.hidden = true;
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
    els.cardLevel.textContent = `NIVEL ${current.level}`;
    els.source.href = current.source;
    const codeEl = els.code.querySelector('code');
    if (current.code) { codeEl.textContent = current.code; els.code.hidden = false; }
    else { codeEl.textContent = ''; els.code.hidden = true; }
    const answerCodeEl = els.answerCode.querySelector('code');
    if (current.answer_code) { answerCodeEl.textContent = current.answer_code; els.answerCode.hidden = false; }
    else { answerCodeEl.textContent = ''; els.answerCode.hidden = true; }
    const total = completed + queue.length + 1;
    els.progress.style.width = `${total ? (completed / total) * 100 : 0}%`;
    els.card.focus({ preventScroll: true });
  }
  function reveal() {
    if (!current || revealed || (current.verdict !== null && !verdictAnswered)) return;
    revealed = true;
    els.front.hidden = true;
    els.back.hidden = false;
    els.rating.hidden = false;
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
    const unlockedBefore = unlockedLevels();
    const old = progress[current.id] || { seen: 0, streak: 0, interval: 0 };
    const now = Date.now(), day = 24 * 60 * 60 * 1000;
    let interval, streak = old.streak || 0;
    if (level === 'again') { interval = 10 * 60 * 1000; streak = 0; }
    else if (level === 'hard') interval = Math.max(day, (old.interval || day) * 1.35);
    else if (level === 'good') { interval = old.interval ? Math.max(2 * day, old.interval * 2.15) : 2 * day; streak += 1; }
    else { interval = old.interval ? Math.max(4 * day, old.interval * 3.2) : 4 * day; streak += 1; }
    progress[current.id] = {
      seen: (old.seen || 0) + 1, streak, interval, due: now + interval,
      lastGrade: level, lastScore: GRADE_POINTS[level], updated: now,
    };
    saveProgress();
    completed += 1;
    const unlockedAfter = unlockedLevels(), nextLevel = selectedLevel + 1;
    if (!unlockedBefore.has(nextLevel) && unlockedAfter.has(nextLevel)) {
      selectedLevel = nextLevel;
      localStorage.setItem(LEVEL_KEY, String(selectedLevel));
      syncFiltersToUrl();
      buildQueue();
      return;
    }
    renderStats();
    nextCard();
  }
  function chooseLevel(level) {
    if (!Number.isInteger(level) || level < 1 || level > curriculum.length) return;
    selectedLevel = level;
    localStorage.setItem(LEVEL_KEY, String(level));
    syncFiltersToUrl();
    buildQueue();
  }
  function setFiltersFromUrl() {
    const params = new URLSearchParams(location.search);
    const module = params.get('module'), mode = params.get('mode');
    const requestedLevel = Number(params.get('level')), savedLevel = Number(localStorage.getItem(LEVEL_KEY));
    if (module && [...els.select.options].some(option => option.value === module)) els.select.value = module;
    if (mode && [...els.mode.options].some(option => option.value === mode)) els.mode.value = mode;
    if (Number.isInteger(requestedLevel) && requestedLevel >= 1 && requestedLevel <= curriculum.length) selectedLevel = requestedLevel;
    else if (Number.isInteger(savedLevel) && savedLevel >= 1 && savedLevel <= curriculum.length) selectedLevel = savedLevel;
    else selectedLevel = recommendedLevel();
  }
  function syncFiltersToUrl() {
    const params = new URLSearchParams();
    if (selectedLevel !== 1) params.set('level', selectedLevel);
    if (els.select.value !== 'all') params.set('module', els.select.value);
    if (els.mode.value !== 'all') params.set('mode', els.mode.value);
    const query = params.toString();
    history.replaceState(null, '', query ? `?${query}` : location.pathname);
  }

  els.reveal.addEventListener('click', reveal);
  root.querySelectorAll('[data-verdict-choice]').forEach(button => button.addEventListener('click', () => answerVerdict(button.dataset.verdictChoice === 'true')));
  root.querySelectorAll('[data-grade]').forEach(button => button.addEventListener('click', () => grade(button.dataset.grade)));
  els.levelChoices.forEach(button => button.addEventListener('click', () => chooseLevel(Number(button.dataset.levelChoice))));
  els.select.addEventListener('change', () => { syncFiltersToUrl(); buildQueue(); });
  els.mode.addEventListener('change', () => { syncFiltersToUrl(); buildQueue(); });
  root.querySelector('[data-reset-session]').addEventListener('click', () => buildQueue({ mix: true }));
  root.querySelector('[data-restart]').addEventListener('click', buildQueue);
  root.querySelector('[data-reset-progress]').addEventListener('click', () => {
    if (!confirm('¿Reiniciar todo tu progreso y volver al Nivel 1?')) return;
    Object.keys(progress).forEach(key => delete progress[key]);
    saveProgress();
    selectedLevel = 1;
    localStorage.setItem(LEVEL_KEY, '1');
    syncFiltersToUrl();
    buildQueue();
  });
  document.addEventListener('keydown', event => {
    if (event.code === 'Space' && !['INPUT', 'SELECT', 'TEXTAREA', 'BUTTON'].includes(document.activeElement.tagName)) {
      event.preventDefault(); reveal();
    }
    if (revealed && ['1', '2', '3', '4'].includes(event.key)) grade({ 1: 'again', 2: 'hard', 3: 'good', 4: 'easy' }[event.key]);
  });

  fetch('/api/cards/')
    .then(response => { if (!response.ok) throw new Error('No se pudo cargar el mazo'); return response.json(); })
    .then(data => {
      allCards = data.cards;
      curriculum = data.curriculum;
      setFiltersFromUrl();
      syncFiltersToUrl();
      buildQueue();
    })
    .catch(error => { els.question.textContent = error.message; els.reveal.hidden = true; });
})();
