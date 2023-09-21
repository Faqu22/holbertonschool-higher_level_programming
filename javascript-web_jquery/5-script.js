$("div#add_item").click(function(){
    var new_li = $("<li></li>").text("Item")
    $("ul.my_list").append(new_li)
})
