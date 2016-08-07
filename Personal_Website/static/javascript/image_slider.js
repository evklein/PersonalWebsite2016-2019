var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var images = document.getElementsByClassName("screenshot");
  var markers = document.getElementsByClassName("marker");

  if (n > images.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = images.length;
  }

  for (i = 0; i < images.length; i++) {
    images[i].style.display = "none";
        markers[i].src = "/static/images/ui/slider_marker_unselected.png";
  }

  images[slideIndex - 1].style.display = "block";
  markers[slideIndex -1 ].src = "/static/images/ui/slider_marker_selected.png";
}
