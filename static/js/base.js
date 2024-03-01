// Carousel interval timer

$('.carousel').carousel({
    interval: 4000
});

// Animations to the fontawesome icons when hover

$('.fa-trash-can').hover(function() {
    $(this).toggleClass('fa-shake');
});

$('.fa-spinner').hover(function() {
    $(this).toggleClass('fa-pulse');
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

/*
* To display which image has been selected before adding/updating product
*/

$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});