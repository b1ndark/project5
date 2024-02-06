// Carousel interval timer

$('.carousel').carousel({
    interval: 4000
});

// Animations to the fontawesome icons when hover

$('.fa-trash-can').hover(function() {
    $(this).toggleClass('fa-shake');
});

$('.fa-minus, .fa-plus').hover(function() {
    $(this).toggleClass('fa-beat');
});