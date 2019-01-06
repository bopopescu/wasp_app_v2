  paypal.Button.render({
    env: 'sandbox', // Or 'production'
    // Set up the payment:
     style: {
            label: 'checkout',
            size:  'large',    // small | medium | large | responsive
            shape: 'pill',     // pill | rect
            color: 'blue'      // gold | blue | silver | black
        },
    // 1. Add a payment callback
    payment: function(data, actions) {
        //send id
        var the_id = document.getElementById("p_id").value;
        var value = document.getElementById("value_amount").value;
        console.log(the_id,value);
      // 2. Make a request to your server
      return actions.request.post('/payment',{
            prod_id: the_id,
            val: value
      })
        .then(function(res) {
          // 3. Return res.id from the response
          console.log(res);
          return res.payID;
        });
    },
    // Execute the payment:
    // 1. Add an onAuthorize callback
    onAuthorize: function(data, actions) {
      // 2. Make a request to your server
      return actions.request.post('/execute_payment', {
        paymentID: data.paymentID,
        payerID:   data.payerID
      })
        .then(function(res) {
        console.log(res.PID);
          // 3. Show the buyer a confirmation message.
         window.location.href="https://www.thewasp.co/"+res.PID;
        });
    }
  }, '#paypal-button');

$.ajax({
                            url:'/receipt',
                            data: JSON.stringify({'t_data': data.payment, 'p_data': data.user_info }),
                            type:'POST',
                            dataType: "json",
                            contentType: 'application/json;charset=UTF-8',
                            success: function(data){
                                window.location.href = data.redirect;
                            }
                        });