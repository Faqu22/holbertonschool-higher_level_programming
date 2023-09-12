const add = document.querySelector('#add_item')
add.addEventListener('click', (event) => {
    var new_li = document.createElement('li')
    new_li.appendChild(document.createTextNode('Item'))
    document.querySelector('.my_list').appendChild(new_li)
})
