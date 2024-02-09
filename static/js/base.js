// Carousel interval timer

$('.carousel').carousel({
    interval: 4000
});

// Animations to the fontawesome icons when hover

$('.fa-trash-can').hover(function() {
    $(this).toggleClass('fa-shake');
});

// Hover animation only when the currentValue is less then 20

$('.increment-qty').hover(function() {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    if (currentValue < 20) {
        $(this).addClass('fa-beat');  
    }
}, function() {
    $(this).removeClass('fa-beat');
});

// Hover animation only when the currentValue is more then 1

$('.decrement-qty').hover(function() {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    if (currentValue > 1) {
        $(this).addClass('fa-beat');  
    }
}, function() {
    $(this).removeClass('fa-beat');
});