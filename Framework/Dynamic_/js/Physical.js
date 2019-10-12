function gravity(target,force) {
    var elem = document.getElementById(target);   
    var pos = 0;
    var id = setInterval(frame,force);
    function frame() {
        pos++; 
        elem.style.top = pos + "px"; 
    }
  }