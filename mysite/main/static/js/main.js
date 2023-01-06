$(function () {
    $(".alert").fadeOut(3000)
  });


  function setCurrentDateTime() {
    // Get the current date and time
    var currentDate = new Date();
  
    // Format the date and time as a string in the format "YYYY-MM-DDTHH:MM"
    var currentDateTimeString = currentDate.toISOString().substring(0, 16);
  
    // Set the value of the input element to the current date and time
    document.getElementById("due").value = currentDateTimeString;
  }

  window.addEventListener("load", function() {
    setCurrentDateTime();
  });