$(document).ready(function () {
    $("#to_poem").click(function () {
        var start = $("#head").val();
        var obj = document.getElementsByName("choices");
        var style;
        for(var i=0; i<obj.length; i ++){
            if(obj[i].checked){
                style = obj[i].value;
            }
        }
        window.location.href = '/poem?start='+start+'&style='+style;
    });
});