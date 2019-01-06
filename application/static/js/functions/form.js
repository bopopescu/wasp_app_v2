$(document).ready(function(){
    $('form#xs-login-form').on('submit',function(event){
        $.ajax({
            data: {
                email: $('#xs_user_login_name').val(),
                password: $('#xs_login_password').val()
            },
            type: "POST",
            url: "/login_user"
        })
        .done(function(data){
            if (data.error){
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            }else{
                $('#successAlert').text(data.name).show();
                $('#errorAlert').hide();
                window.location = '/login';
            }
        });
        event.preventDefault();
    });
});

$(document).ready(function(){
    $('form#xs-register-form').on('submit',function(event){
        $.ajax({
            data: {
                name: $('#xs_register_name').val(),
                email: $('#xs_register_email').val(),
                password: $('#xs_register_password').val(),
                confirm_password: $('#xs_register_repeat_pass').val(),
                dob: $('#dob').val(),
                country: $('#register_countries_states').find(":selected").text(),
                state: $('#register_state_selector').find(":selected").text(),
                phone: $('#register_phone_number').val()
            },
            type: 'POST',
            url: "/register"
        })
        .done(function(data){
            if (data.error){
                $('#errorRegisterAlert').text(data.error).show();
                $('#successRegisterAlert').hide();
            }else{
                $('#successRegisterAlert').text(data.name).show();
                $('#errorRegisterAlert').hide();
                window.location = '/verified_user';
            }
        });
        event.preventDefault();
    });
});

$(document).ready(function() {
  $("#xs_register_repeat_pass").keyup(validate);
});
$(document).ready(function() {
  $("#dob").keyup(checkdate);
});

$(document).ready(function(){
    $('form#subscribe-form').on('submit',function(event){
        $.ajax({
            data: {
                email: $('#the_email_sub').val()
            },
            type: "POST",
            url: "/subscribe"
        })
        .done(function(data){
                $('#successnewsletterAlert').text(data.success).show();
        });
        event.preventDefault();
    });
});
function checkdate(){
    var the_date = $("#dob").val().split('/');
    var year = the_date[2];
    var day = the_date[0];
    var month = the_date[1];
    var age = 18;
    var mydate = new Date();
    mydate.setFullYear(year, month-1, day);
    var currdate = new Date();
    currdate.setFullYear(currdate.getFullYear() - age);
    if ((currdate - mydate) < 0){
        alert("Sorry, only persons over the age of " + age + " may be registered with us");
        $("#age-status").text("Sorry you are below 18 years old.");
    }
    return true;
 }
function validate() {
  var password1 = $("#xs_register_password").val();
  var password2 = $("#xs_register_repeat_pass").val();

    if(password1 == password2) {
       $("#validate-status").text("valid");
    }
    else {
        $("#validate-status").text("Password don't match");
    }

}
$('.validate').mask("99/99/9999");
  $('.validate').change(function() {

    if ($(this).val().substring(0, 2) > 31 || $(this).val().substring(3, 5) == "00") {
      alert("Iregular Date Format");
      return false;
    }
    if ($(this).val().substring(3, 5) > 12 || $(this).val().substring(0, 2) == "00") {
      alert("Iregular Month Format");
      return false;
    }
  });

$(function () {
  $('[data-toggle="tooltip"]').tooltip({
    container : 'body'
  });
});

