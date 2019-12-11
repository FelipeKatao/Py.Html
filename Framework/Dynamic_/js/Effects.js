function fadeObj(target){
    document.getElementById(target).classList.toggle('fadein');
  }
function hiddenObj(target){
  //Fazer sumir algum objeto em teal via CSS//
  document.getElementById(target).classList.remove('visi-element');
  document.getElementById(target).classList.add('hid-element');
}
function visibleObj(target){
  document.getElementById(target).classList.remove('hid-element');
  document.getElementById(target).classList.add('visi-element');
}
function animationColorRed(target){
  document.getElementById(target).classList.add('redOrangeChangeColor');
}
function opacityRepeat(target){
  document.getElementById(target).classList.add('alphaRepeat');
}
function opacityAnim(target){
  document.getElementById(target).classList.add('animAlpha');
}
function nextScene(targetScene,gotoScene){
  //Thing it: when your implemnt all scenes all stay hidden some frist scene is visible//
  document.getElementById(targetScene).style.visibility="hidden"
  document.getElementById(gotoScene).style.visibility="visible"
}
function hiddenAllScenes(){
  let diScenes=document.getElementsByClassName('sceneBox')
  for(let i=0;i<diScenes.length;i++){
    diScenes[i].style.visibility="hidden"
  }
}