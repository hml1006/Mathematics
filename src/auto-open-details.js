(function () {
  function openDetailsForHash() {
    if (!window.location.hash) return;
    var id = decodeURIComponent(window.location.hash.slice(1));
    var target = document.getElementById(id);
    if (!target) return;
    var node = target.parentElement;
    while (node) {
      if (node.tagName && node.tagName.toLowerCase() === 'details') {
        node.open = true;
      }
      node = node.parentElement;
    }
  }

  window.addEventListener('DOMContentLoaded', openDetailsForHash);
  window.addEventListener('hashchange', openDetailsForHash);
  openDetailsForHash();
})();
