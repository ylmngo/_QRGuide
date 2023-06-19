document.addEventListener('DOMContentLoaded', function() {
    const contactButton = document.getElementById('contactButton');
    const contactInterface = document.getElementById('contactInterface');
  
    contactButton.addEventListener('click', function(event) {
      event.stopPropagation(); 
      const buttonRect = contactButton.getBoundingClientRect();
      const buttonTop = buttonRect.top;
      const buttonRight = buttonRect.right;
      contactInterface.classList.toggle('show');
  
      if (contactInterface.classList.contains('show')) {
        const desiredTop = buttonTop + buttonRect.height + 145;
        const desiredLeft = buttonRight - contactInterface.offsetWidth + ( 5* parseFloat(getComputedStyle(document.documentElement).fontSize));
        contactInterface.style.top = desiredTop + 'px';
        contactInterface.style.left = desiredLeft + 'px';
      }
    });
    document.addEventListener('click', function() {
      contactInterface.classList.remove('show');
    });
    const phonePatterns = [
      /^\d{10}$/,
      /^\+\d{12}$/,
      /^\d{3}-\d{3}-\d{4}$/,
      /^\(\d{3}\)\s?\d{3}-\d{4}$/,
      /^\d{4}\s\d{3}\s\d{4}$/
    ];
  
    const form = document.getElementById('myForm');
  
    form.addEventListener('submit', (event) => {
      event.preventDefault();
  
      const name = document.getElementById('name').value;
      const department = document.getElementById('department').value;
      const phone = document.getElementById('phone').value;
      const message = document.getElementById('message').value;
  
      let isValid = true;
      if (name.trim() === '') {
        displayWarning('name');
        isValid = false;
      }
      if (department.trim() === '') {
        displayWarning('department');
        isValid = false;
      }
      if (!validatePhone(phone)) {
        displayWarning('phone');
        isValid = false;
      }
      if (message.trim() === '') {
        displayWarning('message');
        isValid = false;
      }
  
      if (!isValid) {
        return;
      }
  
      if (isSubmissionExists(phone)) {
        const confirmation = confirm('A submission has already been made with this email address. Are you sure you want to submit another suggestion?');
        if (!confirmation) {
          return;
        }
      }
  
      saveSubmission(phone); 
  
      // alert(`Submitted Form Data:\nName: ${name}\nDepartment: ${department}\nPhone: ${phone}\nMessage: ${message}`);
  
      hideAllWarnings();
    });
  
    // form.addEventListener('click', (event) => {
    //   const target = event.target;
    //   if (target.id === 'email') {
    //     const email = target.value.trim();
    //     if (email !== '') {
    //       if (isSubmissionExists(email)) {
    //         const savedData = retrieveSavedData(email);
    //         if (savedData) {
    //           alert(`Saved Form Data:\nName: ${savedData.name}\nEmail: ${savedData.email}\nPhone: ${savedData.phone}\nMessage: ${savedData.message}`);
    //         }
    //       }
    //     }
    //   }
    // });
  
    function displayWarning(fieldId) {
      const inputField = document.getElementById(fieldId);
      inputField.classList.add('invalid');
      const warningSign = document.getElementById(`${fieldId}-warning`);
      warningSign.style.display = 'inline';
    }
  
    function hideWarning(fieldId) {
      const inputField = document.getElementById(fieldId);
      inputField.classList.remove('invalid');
      const warningSign = document.getElementById(`${fieldId}-warning`);
      warningSign.style.display = 'none';
    }
  
    function hideAllWarnings() {
      const inputFields = form.querySelectorAll('input, textarea');
      inputFields.forEach((field) => {
        const fieldId = field.id;
        hideWarning(fieldId);
      });
    }
  
    function validateEmail(email) {
      const emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      return emailPattern.test(email);
    }
  
    function validatePhone(phone) {
      for (const pattern of phonePatterns) {
        if (pattern.test(phone)) {
          return true;
        }
      }
      return false;
    }
  
    function isSubmissionExists(phone) {
      return false;
    }
  
    function saveSubmission(phone) {
    }
  
    function retrieveSavedData(phone) {
      return null;
    }
  
    hideAllWarnings();
  
  });
  window.onscroll = function () {
    scrollFunction();
  };
  
  function scrollFunction() {
    var goToTopButton = document.getElementById("goToTop");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      goToTopButton.style.display = "block";
    } else {
      goToTopButton.style.display = "none";
    }
  }
  
  function goToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
  
  ``