$(function() {
  'use strict';

  var body = $('body');

  function goToNextInput(e) {
    var key = e.which,
      t = $(e.target),
      sib = t.next('input');

    if (key != 9 && (key < 48 || key > 57)) {
      e.preventDefault();
      return false;
    }

    if (key === 9) {
      return true;
    }

    if (!sib || !sib.length) {
      sib = body.find('input').eq(0);
    }
    sib.select().focus();
  }

  function onKeyDown(e) {
    var key = e.which;

    if (key === 9 || (key >= 48 && key <= 57)) {
      return true;
    }

    e.preventDefault();
    return false;
  }

  function onFocus(e) {
    $(e.target).select();
  }
  body.on('keyup', 'input', goToNextInput);
  body.on('keydown', 'input', onKeyDown);
  body.on('click', 'input', onFocus);
})

$(document).ready(function(){
    $('form#form_verified').on('submit',function(event){
        $.ajax({
            data:{
                 c1: $('#1').val(),
                 c2: $('#2').val(),
                 c3: $('#3').val(),
                 c4: $('#4').val(),
                 c5: $('#5').val(),
                 c6: $('#6').val()
            },
             type: "POST",
             url: "/confirm_user"
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