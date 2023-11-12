
var colors = [];
var counter = 0;

function randon_number_generator(){
    var random_number = Math.round(Math.random()*3) + 1;
    return random_number;
}

function display_a_color(){
        var box_no = randon_number_generator();
        var highlighted_box = '.box'+ box_no;
        $(highlighted_box).addClass("highlight");
        setTimeout(function(){
            $(highlighted_box).removeClass("highlight")}, 1300)
        return box_no;
    }

function compare_arrays(array1, array2){
    var status = true;
    var i;
    if (array1.length = array2.length){
        for (i = 0; i< array1.length; i++){
            if (array1[i] != array2[i]){
                status = false;
            }
            else{
    
            }
        }
    }
    return status;
}
function run_game(){
    var click_no = 0;
    var clicked_list = []
    colors[counter] = display_a_color();
    $(document).click(function(event){
        event.stopImmediatePropagation();
        event.preventDefault();
        var clicked = event.target.innerHTML;
        clicked_list[click_no] = clicked;
        click_no += 1;
        console.log("clickedlist:" + clicked_list);    
        console.log("colorslist:" + colors);
    if (clicked_list.length == colors.length){
        if (compare_arrays(clicked_list, colors)){
            counter += 1;
            $("h1").text("score :" + counter);
            clicked_list = []
            click_no = 0;
            run_game();
        }
        else{
            $("h1").text("You got it wrong, try again");
            $("body").css("background-color", "red");
            setTimeout(function(){
                window.location.reload();
            }, 2000);
        }
    }
    else{

    }
    })

}

$(document).on("keydown" , run_game)
