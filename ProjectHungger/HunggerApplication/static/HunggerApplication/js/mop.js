var mi = 0;
function carousel() {
    var i;
    var x = document.getElementsByClassName("fs");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
    }
    mi++;
    if (mi > x.length) {mi = 1}    
    x[mi-1].style.display = "block";  
    setTimeout(carousel, 1500);
}