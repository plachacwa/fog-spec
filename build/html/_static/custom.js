document.addEventListener('DOMContentLoaded', function() {
  document.body.addEventListener('click', function(event) {
    if (window.getSelection().toString().trim().length > 0) return;

    const assertion = event.target.closest('.spec-assertion');
    if (!assertion) return;

    const star = assertion.querySelector('.spec-id-toggle');
    const idNode = assertion.querySelector('.spec-id');

    if (!star || !idNode) return;
	
    if (star.classList.contains('spec-id-toggle-hidden')) {
      star.classList.remove('spec-id-toggle-hidden');
      idNode.classList.add('spec-id-hidden');
    } else {
      star.classList.add('spec-id-toggle-hidden');
      idNode.classList.remove('spec-id-hidden');
    }
  });
});