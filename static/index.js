'use strict';

$(document).ready(() => {
    let ingredients = 1, restrictions = 1;
    $("#add-ingredient").click(() => {
        if(ingredients < 20) {
            $("#ingredients").append('<input name="ingredients[]">');
            ingredients++;
        } else if(!$("#ing-warn").length) {
            $("#ingredients").append('<p id="ing-warn" class="text-sm text-danger xtra">Search limited to 20 ingredients</p>');
        }
    });
    $("#add-restriction").click(() => {
        if(restrictions < 10) {
            $("#restrictions").append('<input name="restrictions[]" class="xtra">');
            restrictions++;
        } else if(!$("#res-warn").length) {
            $("#restrictions").append('<p id="res-warn" class="text-sm text-danger text-right xtra">Search limited to 10 restrictions</p>');
        }
    });
    $("#clear-form").click(() => {
        $(".xtra").remove();
    })
});