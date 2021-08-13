const thumbnails = $(".card-deck");
let visibleThumbnails = 0;

function showThumbnailsUntil(index) {
  for (var i = visibleThumbnails; i <= index; i++) {
    if (i < thumbnails.length) {
      $(thumbnails[i]).addClass('visible');
      visibleThumbnails++;
    } else {
      break;
    }
  }
}

showThumbnailsUntil(5);


$(".loadMore").on("click", function() {
  showThumbnailsUntil(visibleThumbnails + 3)

  if (visibleThumbnails === thumbnails.length) {
    $(".loadMore").fadeOut(200); //this will hide
    //button when length is 0
  }
})

$('a.button-show').click(function() {
    $("#filterform").toggle(); // Show the search form.
});
