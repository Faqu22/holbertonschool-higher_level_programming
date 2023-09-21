$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    for (const movienum in data.results) {
        $("ul#list_movies").append($("<li></li>").text(data.results[movienum].title))
        }
});

