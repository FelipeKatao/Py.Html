var targetSelect="";
var speed=0;
var _posX=0;
var _posY=0

document.addEventListener('keydown',(event)=>{
    
    var keyName= event.key;
    

    if(keyName=="ArrowDown" || keyName=="s"){
        _movetargetLeft();
    }
    if(keyName=="ArrowLeft" || keyName=="d"){
        targetMove.style.left=+speed+"px";
        console.log("left");
    }
    if(keyName=="ArrowRight" || keyName=="a"){
        targetMove.style.right=+speed+"px";
        console.log("right");
    }
    if(keyName=="ArrowUp" || keyName=="w"){
        targetMove.style.top=+speed+"px";
        console.log("Up");
    }
});

function selectTarget(target,speedTarget,posX,PosY){
    targetSelect=target;
    speed=speedTarget;
    _posX=posX;
    _posY=PosY;
}
function _movetargeDown(){
    let targetMove= document.getElementById(targetSelect);
    _posY=_posY-speed;
    targetMove.style.top=_posY+"px";
}