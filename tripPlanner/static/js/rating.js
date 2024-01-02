document.addEventListener('DOMContentLoaded', function() {
  console.log(document.getElementById('location').value);
  document.querySelector('button.submit').disabled = true; // disable button on load

  // Enable button 
  function enable_submit() {
    var button = document.querySelector('button.submit');
    if (button) {
      button.disabled = false;
      button.classList.add('not-disabled');
    }
  }
  
  // Disable button
  function disable_submit() {
    var button = document.querySelector('button.submit');
    if (button) {
      button.disabled = true;
      button.classList.remove('not-disabled');
    }
  }
  

  // Display feedback after rating
  document.querySelectorAll('.rating').forEach(function(rating) {
    rating.addEventListener('click', function() {
      var ratingValue = this.value;

      document.querySelector('.feedback').style.display = "block";

      feedback_validate(ratingValue);
    });
  });

  // Run enable button function based on input
  document.querySelector('.feedback textarea').addEventListener('keyup', function() {
    if (this.value.length > 3) {
      enable_submit();
    }
  });
});
