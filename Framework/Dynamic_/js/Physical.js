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
function detectColider(target,targetCol){
    target=document.getElementById(target);
    targetCol=document.getElementById(targetCol);

    let colider=[target.offsetLeft,target.offsetTop,target.offsetWidth,target.offsetHeight];
    let coliderTarget=[targetCol.offsetLeft,targetCol.offsetTop,targetCol.offsetWidth,targetCol.offsetHeight];
    let colidercheck= (coliderTarget[0]+coliderTarget[2]>=colider[0])&&(colider[0]+colider[2]>=coliderTarget[0]);
    let coliderchecktarget= (coliderTarget[1]+coliderTarget[3]>=colider[0])&&(colider[1]+colider[3]>=coliderTarget[1]);

    let id= setInterval(function frame(){   
        
         colider=[target.offsetLeft,target.offsetTop,target.offsetWidth,target.offsetHeight];
         coliderTarget=[targetCol.offsetLeft,targetCol.offsetTop,targetCol.offsetWidth,targetCol.offsetHeight];
         colidercheck= (coliderTarget[0]+coliderTarget[2]>=colider[0])&&(colider[0]+colider[2]>=coliderTarget[0]);
        // coliderchecktarget= (coliderTarget[1]+coliderTarget[3]>=colider[0])&&(colider[1]+colider[3]>=coliderTarget[1]);

        if((colidercheck && coliderchecktarget)){
            console.log("colidiu!");
        }
        else{
            console.log("procurando...")
        }
    },5);
}