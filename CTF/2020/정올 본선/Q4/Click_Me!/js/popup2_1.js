'use strict';
document.addEventListener('DOMContentLoaded', function () {
    var url = location.href;
    var s = url.split("=");
    for(var i = 0; i < s[1]; i++){
        alert("oh...");
    }
    
    alert('think about it again');
    var num = parseInt(s[1]) + 1;
    var htmlname = "olym1.html";
    htmlname = htmlname + "?num=" + num;
    location.href = htmlname;
});