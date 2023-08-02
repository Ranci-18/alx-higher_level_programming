/* global $ */
$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    const newElm = $('<li>Item</li>');
    $('UL.my_list').append(newElm);
  });

  $('DIV#remove_item').click(function () {
    $('.my_list li:last-child').remove();
  });

  $('DIV#clear_list').click(function () {
    $('.my_list').empty();
  });
});
