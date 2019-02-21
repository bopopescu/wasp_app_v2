$(document).ready(function(){
    $('#calculate').on('click',function(e){
    e.preventDefault();
    $.ajax({
        data:{
            parv:       $('#par').val(),
            timeperiod: $('#time_period').val(),
            ytm:        $('#ytm').val(),
            coupon:     $('#coupon').val(),
            freq:       $('#freq option:selected').val()
        },
        url: '/calculate_bond_price',
        type: 'POST',
        //cache: false,
        success: function(resp){
         $('#bondprice').text(resp.price).show();
                }
            });
          });
    })
$('#price').on('keyup',function(){
    var qty     = $('#qty').val()
    var price   = $('#price').val()
    var total   = qty * price
    var total_p = (total).toFixed(2);
    $('#totalpayment').html(numberWithCommas(total_p));
    $('#dispprice').html(numberWithCommas(price));
})

$('#qty').on('keyup',function(){
    var quantity         = $('#qty').val()
    var purchase_price   = $('#price').val()
    var total            = quantity * purchase_price
    var total_p          = (total).toFixed(2);

    $('#totalpayment').html(numberWithCommas(total_p));
    $('#dispqty').html(numberWithCommas(quantity));
})
$(document).ready(function(){
    $('#buyorsell').on('change',function(){
        var val = $(this).val();
        //var type_val = the_color.options[the_color.selectedIndex].value;
        if (val == 'sell'){
            $('#execution').html('SELL');
            document.getElementById('thecolor').style.backgroundColor='red';
            document.getElementById('executebtn').classList.remove('btn-outline-success');
            document.getElementById('executebtn').classList.add('btn-outline-danger');
        }else {
            $('#execution').html('BUY');
            document.getElementById('thecolor').style.backgroundColor='green';
            document.getElementById('executebtn').classList.remove('btn-outline-danger');
            document.getElementById('executebtn').classList.add('btn-outline-success');
        }
    })
})

function numberWithCommas(number) {
    var parts = number.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return parts.join(".");
}