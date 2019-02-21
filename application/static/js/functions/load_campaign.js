$(document).ready(function(){
    $(document).on('click','.view-more',function(){
        var that = $(this);
        var id   = that.attr('id');
        console.log(id);
        window.location.href='/campaign_page/'+id;
    })
});
