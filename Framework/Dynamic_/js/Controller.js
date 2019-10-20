//Variaveis globais
var targetSelect="";
var speed=0;
var _posX=0;
var _posY=0

//Move the obj target with key//
document.addEventListener('keydown',(event)=>{    
    var keyName= event.key;
    if(keyName=="ArrowDown" || keyName=="s"){
        _movetargeDown();
    }
    if(keyName=="ArrowLeft" || keyName=="d"){
        _movetargeLeft();
    }
    if(keyName=="ArrowRight" || keyName=="a"){
        _movetargeRight()
    }
    if(keyName=="ArrowUp" || keyName=="w"){
        _movetargeUp();
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
    _posY=_posY+speed;
    targetMove.style.top=_posY+"px";
}
function _movetargeUp(){
    let targetMove= document.getElementById(targetSelect);
    _posY=_posY-speed;
    targetMove.style.top=_posY+"px";
}
function _movetargeLeft(){
    let targetMove= document.getElementById(targetSelect);
    _posX=_posX-speed;
    targetMove.style.left=_posX+"px";
}
function _movetargeRight(){
    let targetMove= document.getElementById(targetSelect);
    _posX=_posX+speed;
    targetMove.style.left=_posX+"px";
}