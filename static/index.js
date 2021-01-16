'use strict';

$(document).ready(() => {
    $("#add").click(() => {
        $("#ingredients").append('<input name="ingredients"><br>');
    });
});