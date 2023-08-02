/* global $ */
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movieTitles = [];
    for (let i = 0; i < data.results.length; i++) {
      movieTitles.push(data.results[i].title);
    }
    $('UL#list_movies').html('<li>' + movieTitles.join('</li><li>') + '</li>');
  });
});
