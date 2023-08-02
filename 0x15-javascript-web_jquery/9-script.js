/* global $ */
$(document).ready(function () {
  const api = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(api, function (data) {
  $('DIV#hello').text(data.hello);
  });
});
