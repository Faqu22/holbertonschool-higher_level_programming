const update = document.querySelector('#update_header')
update.addEventListener('click', (event) => {
    document.querySelector('header').textContent = 'New Header!!!'
})
