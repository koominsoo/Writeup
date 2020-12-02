'use strict';
function btn1() {
    chrome.tabs.executeScript(null, {
        file : 'btn.js'
    }, function() {
        var url = location.href;
        var s = url.split("=");
        var num = 1;
        if (s[1] != null){
            num = s[1];
        }
        var htmlname = "olym1_1.html";
        if(htmlname == "olym1_1.html"){
            alert("Haha~ you stupid fool~xD");
        }
        htmlname = htmlname + "?num=" + num;
        location.href = htmlname;
    });
}

document.addEventListener('DOMContentLoaded', function () {
    var btns = document.querySelectorAll('button');
    for (var i = 0; i < btns.length; i++) {
        let btn = btns[i];
        if(btn.id == "btn1") {
            btn.addEventListener('click', btn1);
        }
    }
});