document.addEventListener('DOMContentLoaded', function () {
    let Res = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    Res.then((res) => res.json()).then((d) => {
        document.querySelector('#hello').textContent = d.hello
    })
})
