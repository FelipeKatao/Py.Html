//variaveis globais//
var colider=false;
function gravity(target,force) {
    let elem = document.getElementById(target);   
    let pos = 0;
    let id = setInterval(function frame(){
        if(colider==false){
            pos++;
            elem.style.top= pos+"px";            
        }
    },force);
  }
function returnColider(functionTarget){
    let colFunc=false;
    let id = setInterval(function frame(){
        if(colider==true && colFunc==false){
            functionTarget()
            colFunc=true;
        }
    },5)
}
function detectColider(target,targetCol){
   target=document.getElementById(target);
    targetCol=document.getElementById(targetCol);

    let top=0;
    let left=0;
    let BBoxA
    let BBoxB

    let id= setInterval(function frame(){   
        let rangeIntersect = function(min0, max0, min1, max1) {
            return Math.max(min0, max0) >= Math.min(min1, max1) && Math.min(min0, max0) <= Math.max(min1, max1)
        }

        let rectIntersect = function (r0, r1) {
            return rangeIntersect(r0.left, r0.right, r1.left, r1.right) && rangeIntersect(r0.top, r0.bottom, r1.top, r1.bottom)
        }
        BBoxA = target.getBoundingClientRect()
        BBoxB = targetCol.getBoundingClientRect()

        if(rectIntersect(BBoxA, BBoxB)){
           this.colider=true;
        }
        else{
            this.colider=false;
        }
    },5);
}