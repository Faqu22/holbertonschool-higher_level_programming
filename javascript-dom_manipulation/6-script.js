const char = document.querySelector('#character')
let Res = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
Res.then((res) => res.json()).then((d) => {
    char.textContent = d.name
})
