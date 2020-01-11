// JS for base.html

//scroll to top on logo click
function scrollToTop() {
     window.scrollTo(0, 0);
}

//navbar fade on scroll
$(window).scroll(function() {
  if($(this).scrollTop() > 100) {
    $('.navbar').removeClass('bg-transparent');
  } else {
    $('.navbar').addClass('bg-transparent');
  }
});
