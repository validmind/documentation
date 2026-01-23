// Makes .content-tile elements fully clickable by delegating clicks to the link inside
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.content-tile').forEach(function(tile) {
    tile.style.cursor = 'pointer';
    tile.addEventListener('click', function(e) {
      var link = tile.querySelector('a');
      if (link && !e.target.closest('a')) {
        link.click();
      }
    });
  });
});
