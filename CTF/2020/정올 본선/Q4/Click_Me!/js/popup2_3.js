'use strict';
function btn2() {
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

function readFlag() {
    var string = document.getElementById("flag_txt").innerHTML;
    
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", "../flag_file/flag2", false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                //alert(allText);
                var replacedString = string.replace("", allText);
                document.getElementById("flag_txt").innerHTML = replacedString;
            }
        }
    }
    rawFile.send(null);
}

document.addEventListener('DOMContentLoaded', function () {
    readFlag();
    
    var btns = document.querySelectorAll('button');
    for (var i = 0; i < btns.length; i++) {
        let btn = btns[i];
        if(btn.id == "btn3") {
            btn.addEventListener('click', btn2);
        }
    }
});