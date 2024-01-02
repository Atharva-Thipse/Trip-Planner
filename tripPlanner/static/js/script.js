document.addEventListener('DOMContentLoaded', function() {
  const body = document.body;
  const slides = document.querySelectorAll('.slide');

  setBgToBody();

  function setBgToBody() {
    if (slides.length > 0) {
      body.style.backgroundImage = slides[0].style.backgroundImage;
    }
  }
});
