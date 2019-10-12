function myMove(target) {
    var elem = document.getElementById(target);   
    var pos = 0;
    var id = setInterval(frame, 13);
    function frame() {
        pos++; 
        elem.style.top = pos + "px"; 
    }
  }