/* 
* Sorting function to filter products by price, rating and name 
*/

$('#sort-selector').change(function() {
    var selector = $(this)
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort =  selectedVal.split("_")[0]
        var direction =  selectedVal.split("_")[1]

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})

/*
* To display which image has been selected before adding/updating product
*/

$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

/*
* To Increment and Decrement quantities, range from 1 to 20
*/

function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 19;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// To Check and enabling/disabling all inputs when page is loaded
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++) {
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}


// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// To increment the quantity
$('.increment-qty').click(function(e) {
    e.preventDefault();
    var closestInput =$(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// To decrement the quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var closestInput =$(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

/*
* To update product quantities and remove products
*/

$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})