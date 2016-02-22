
$('document').ready(function(){
    $(".slider").each(
        function() {
            $(this).slider({
              range: "max",
              min: 0,
              max: 100,
              value: 50,
              slide: function( event, ui ) {
                  $(this).closest('.slidercontainer').find('.number').val(ui.value);
              },
              create: function( event ) {
                  $(this).closest('.slidercontainer').find('.number').val(50);
              }
            });
    });

    $( ".info" ).mouseenter(function(){
        var text = $(this).find('.infotext');
        $(text).css('visibility','visible');

    });

    $( ".info" ).mouseleave(function() {
        $( ".infotext" ).each(function(){
            $(this).css('visibility','hidden');
        });
    });

    $( "option" ).mouseleave(function() {
        $( ".infotext" ).each(function(){
            $(this).css('visibility','hidden');
        });
    });

    $('.next').click(function() {
        $('.number').removeAttr('disabled');
    });

});