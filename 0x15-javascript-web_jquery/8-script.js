$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const $listMovies = $('#list_movies');

    $.each(movies, function (index, movie) {
      $('<li>').text(movie.title).appendTo($listMovies);
    });
  });
});
