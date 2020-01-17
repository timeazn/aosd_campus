// JS for base.html

//navbar fade on scroll
$(window).scroll(function() {
  if($(this).scrollTop() > 100) {
    $('.navbar').removeClass('bg-transparent');
  } else {
    $('.navbar').addClass('bg-transparent');
  }
});
