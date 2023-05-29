// Javascript to dsiplay a thank you message when form is submitted
document.getElementById("recipe-form").addEventListener("submit", function (e) {
    // Hide first view
    e.preventDefault();
    document.getElementById('recipe-form').style.display = 'none';

    // Show thank you message element
    document.getElementById('thank-you').style.display = 'contents';
    setTimeout(function() {
        e.target.submit(); // submit form after 5 seconds
      }, 5000);
});


