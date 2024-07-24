document.addEventListener('DOMContentLoaded', () => {
    function validateForm() {
      const username = document.getElementById('username').value;
      const nameFeedback = document.getElementById('nameFeedback');
      const namePattern = /^[A-Za-z]+( [A-Za-z]+)?$/;
  
      if (!namePattern.test(username)) {
        nameFeedback.style.display = 'block';
        return false;
      } else {
        nameFeedback.style.display = 'none';
        return true;
      }
    }
  
    document.querySelector('form').onsubmit = validateForm;
  });
  