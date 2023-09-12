const toggle = document.querySelector('#toggle_header')
const header = document.querySelector('header')
toggle.addEventListener('click', (event) => {
    if (header.className === 'red') {
        header.classList.remove('red')
        header.classList.toggle('green')
    } else {
        header.classList.remove('green')
        header.classList.toggle('red')
    }
})
