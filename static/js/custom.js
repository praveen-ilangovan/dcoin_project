$(function() {
  // For card rotation
     $('.btn-rotate').click(function(){
          $('.card-front').toggleClass(' rotate-card-front');
          $('.card-back').toggleClass(' rotate-card-back');
     });
  });