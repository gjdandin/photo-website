jQuery(document).on('click','.load-more',function(e){
    e.preventDefault();
    jQuery.ajax({
        url:jQuery(this).attr('href')
    }).done(function(data){
        jQuery('.row>div').append(data);
    });
});