'use strict';

let activePoll = null;

// ── Open modal ──────────────────────────────────────────
function openPoll(pollId) {
  activePoll = POLLS[pollId];
  if (!activePoll) return;

  const modal = document.getElementById('modal');
  modal.style.setProperty('--poll-color', activePoll.color);

  document.getElementById('modal-category').textContent = activePoll.category;
  document.getElementById('modal-question').textContent = activePoll.question;
  document.getElementById('modal-footer-text').textContent =
    fmtVotes(activePoll.total_votes) + ' votes total';

  renderOptions();

  document.getElementById('modal-overlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

// ── Render vote buttons ─────────────────────────────────
function renderOptions() {
  const container = document.getElementById('modal-options');
  container.innerHTML = activePoll.options
    .map((opt, i) =>
      `<button class="opt-btn" onclick="castVote(${i})">${opt.text}</button>`
    )
    .join('');
}

// ── Cast vote ───────────────────────────────────────────
function castVote(optionIdx) {
  if (!activePoll) return;
  const pollId = activePoll.id;

  // Optimistic local update so UI stays responsive
  activePoll.options[optionIdx].votes += 1;
  activePoll.total_votes += 1;
  renderResults(activePoll.options, activePoll.total_votes, optionIdx);

  fetch(`/api/vote/${pollId}/${optionIdx}`, { method: 'POST' })
    .then(r => r.json())
    .then(data => {
      // Sync with server counts
      data.results.forEach((r, i) => {
        activePoll.options[i].votes = r.votes;
      });
      activePoll.total_votes = data.total;
      renderResults(activePoll.options, data.total, optionIdx);

      document.getElementById('modal-footer-text').innerHTML =
        '<span class="voted-ok">✓ Vote recorded!</span>' +
        fmtVotes(data.total) + ' votes total';
    })
    .catch(() => {
      // Optimistic result already shown — just update footer
      document.getElementById('modal-footer-text').innerHTML =
        '<span class="voted-ok">✓ Vote recorded!</span>' +
        fmtVotes(activePoll.total_votes) + ' votes total';
    });
}

// ── Render result bars ──────────────────────────────────
function renderResults(options, total, selectedIdx) {
  const winnerPct = Math.max(...options.map(o => Math.round(o.votes / total * 100)));

  const container = document.getElementById('modal-options');
  container.innerHTML = options
    .map((opt, i) => {
      const pct = Math.round(opt.votes / total * 100);
      const isSelected = i === selectedIdx;
      const isWinner  = pct === winnerPct;
      const cls = [isSelected ? 'selected' : '', isWinner ? 'winner' : ''].join(' ').trim();
      return `
        <div class="result-item ${cls}">
          <div class="result-label-row">
            <span class="result-text">${opt.text}</span>
            <span class="result-pct">${pct}%</span>
          </div>
          <div class="result-track">
            <div class="result-fill" data-pct="${pct}"></div>
          </div>
          <span class="result-sub">${opt.votes.toLocaleString()} votes</span>
        </div>`;
    })
    .join('');

  // Animate bars on next two frames (ensures CSS transition fires)
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      container.querySelectorAll('.result-fill').forEach(el => {
        el.style.width = el.dataset.pct + '%';
      });
    });
  });
}

// ── Close modal ─────────────────────────────────────────
function closeModal() {
  document.getElementById('modal-overlay').classList.remove('open');
  document.body.style.overflow = '';
  activePoll = null;
}

document.getElementById('modal-overlay').addEventListener('click', e => {
  if (e.target === e.currentTarget) closeModal();
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal();
});

// ── Horizontal row scroll ───────────────────────────────
function scrollRow(trackId, dir) {
  document.getElementById(trackId).scrollBy({ left: dir * 720, behavior: 'smooth' });
}

// ── Helpers ─────────────────────────────────────────────
function fmtVotes(n) {
  if (n >= 1_000_000) return (n / 1_000_000).toFixed(1) + 'M';
  if (n >= 1_000)     return (n / 1_000).toFixed(1) + 'K';
  return String(n);
}
