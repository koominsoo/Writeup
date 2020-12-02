'use strict';
function btn2() {
    chrome.tabs.executeScript(null, {
        file : 'btn.js'
    }, function() {
        var htmlname = "olym1_1.html";
        if(htmlname == "olym1_1.html"){
            alert("Haha~ you stupid fool~xD");
        }
        location.href = htmlname;
    });
}

function readFlag() {
    var string = document.getElementById("flag_txt").innerHTML;
    
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", "../flag_file/flag3", false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                var replacedString = string.replace("", allText);
                document.getElementById("flag_txt").innerHTML = replacedString;
            }
        }
    }
    rawFile.send(null);
}

document.addEventListener('DOMContentLoaded', function () {
    readFlag();
});