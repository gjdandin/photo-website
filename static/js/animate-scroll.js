var vid = document.getElementById("intro");
vid.defaultMuted = true;

 $(function() {
    $('.scroll-down').click (function() {
      $('html, body').animate({scrollTop: $('#portfolio').offset().top }, 'slow');
      return false;
    });
  });