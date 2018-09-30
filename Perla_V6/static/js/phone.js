
    
$("#mobile-number").intlTelInput({
  initialCountry: "fr",
  geoIpLookup: function(callback) {
    $.get('http://ipinfo.io', function() {}, "jsonp").always(function(resp) {
      var countryCode = (resp && resp.country) ? resp.country : "";
      callback(countryCode);
    });     
  },  
  preferredCountries: ['fr'],
  utilsScript: "https://www.besafty.com/besafty/static/js/utils.js" // just for formatting/placeholders etc
});







var telInpute = $("#mobile-number"),
  errorMsge = $("#error-msg"),
  validMsge = $("#valid-msg");


// initialise plugin
telInpute.intlTelInput({
  utilsScript: "js/error.js"
});

var reset = function() {
  telInpute.removeClass("error");
  errorMsge.addClass("hide");
  validMsge.addClass("hide");
   console.log('eeeee');
};

// on blur: validate
telInpute.blur(function() {

  reset();
  if ($.trim(telInpute.val())) {
    if (telInpute.intlTelInput("isValidNumber")) {
      validMsge.removeClass("hide");
       $('#verification').removeAttr('disabled');
    } else {
      telInpute.addClass("error");
      errorMsge.removeClass("hide");
      $('#verification').attr('disabled', "true");
    }
  }
});

// on keyup / change flag: reset
telInpute.on("keyup change", reset);


