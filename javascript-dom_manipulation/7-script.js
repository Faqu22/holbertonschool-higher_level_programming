const movies = document.querySelector('#list_movies')
let Res = fetch('https://swapi-api.hbtn.io/api/films/?format=json')
Res.then((res) => res.json()).then((d) => {
    console.log(d)
    for (const movie in d.results) {
        var new_li = document.createElement('li')
        new_li.appendChild(document.createTextNode(d.results[movie].title))
        movies.appendChild(new_li)
    }
})
