'use strict';

$(document).ready(() => {
    let ingredients = 1, restrictions = 1;
    $("#add-ingredient").click(() => {
        if(ingredients < 10) {
            $("#ingredients").append('<input name="ingredients">');
            ingredients++;
        } else if(!$("#ing-warn").length) {
            $("#ingredients").append('<p id="ing-warn">too much data!</p>');
        }
    });
    $("#add-restriction").click(() => {
        if(restrictions < 10) {
            $("#restrictions").append('<input name="restrictions">');
            restrictions++;
        } else if(!$("#res-warn").length) {
            $("#restrictions").append('<p id="res-warn">too much data!</p>');
        }
    });
});