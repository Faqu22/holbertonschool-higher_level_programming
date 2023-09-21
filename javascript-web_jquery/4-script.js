$("div#toggle_header").click(function(){
    if ($("header").attr("class") === "green") {
        console.log($("header").attr("class"), "Az")
        $("header").removeClass("green")
        $("header").addClass("red")
    }
    else if ($("header").attr("class") === "red") {
        $("header").removeClass("red")
        $("header").addClass("green")
    }
});
