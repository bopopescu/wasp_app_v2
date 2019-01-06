function theload(){
    console.log(window.location.href);
    $.ajax({
        data: {
            link: window.location.href
        },
        url: '/facebook_token',
        type: "POST"
    })
}
$(document).ready(function(){
    $('#myportfolio').on('click',function(e){
    e.preventDefault();
     $.ajax({
        url: '/portfolio',
        type: 'POST',
        //cache: false,
        success: function(resp){
         $('#campaign').html(resp).fadeIn(500);
                }
            });
        });
    });

$(document).ready(function(){
    $(document).on('click','.view-btn',function(){
        var that = $(this);
        var id   = that.attr('id');
        window.open('/view_receipt/'+id,'_blank');
    })
});
