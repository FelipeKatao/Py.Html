var intervalo = 4000;

function slide1(){
	document.getElementById("banner").src = "images/slide1.jpg";
	setTimeout("slide2()", intervalo);
}

function slide2(){
	document.getElementById("banner").src = "images/slide2.jpg";
	setTimeout("slide3()", intervalo);
}

function slide3(){
	document.getElementById("banner").src = "images/slide3.jpg";
	setTimeout("slide1()", intervalo);
}