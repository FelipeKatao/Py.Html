var targetSelect="";
var speed=0;

document.addEventListener('keydown',(event)=>{
    const keyName= event.key;
    let targetMove= document.getElementById(targetSelect);

    if(keyName=="ArrowDown" || keyName=="s"){
        targetMove.style.down=speed+"px";
        console.log("down"+speed);

    }
    if(keyName=="ArrowLeft" || keyName=="d"){
        targetMove.style.left=speed+"px";
        console.log("left");
    }
    if(keyName=="ArrowRight" || keyName=="a"){
        targetMove.style.right=speed+"px";
        console.log("right");
    }
    if(keyName=="ArrowUp" || keyName=="w"){
        targetMove.style.top=speed+"px";
        console.log("Up");
    }
})

function selectTarget(target,speedTarget){
    targetSelect=target;
    speed=speedTarget;
}