let dictionary = [];

async function loadData() {
  const response = await fetch('data.json');
  dictionary = await response.json();
}

function renderResults(matches) {
  const results = document.getElementById('results');
  results.innerHTML = '';
  matches.forEach(item => {
    const div = document.createElement('div');
    div.innerHTML = `<strong>${item.headword}</strong>: ${item.definition}`;
    results.appendChild(div);
  });
}

function search() {
  const q = document.getElementById('search').value.trim().toLowerCase();
  if (!dictionary.length) return;
  if (!q) {
    document.getElementById('results').innerHTML = '';
    return;
  }
  const matches = dictionary.filter(item =>
    item.headword.toLowerCase().includes(q) ||
    item.definition.toLowerCase().includes(q)
  );
  renderResults(matches);
}

window.addEventListener('DOMContentLoaded', loadData);
