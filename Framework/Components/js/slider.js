/*////////////////////////////////
///// SLIDER ANIMATION //////////
////////////////////////////////*/

var query = document.querySelectorAll('[slider-py] > p > img');
var elementos = Array.from(query);
var tamanho = elementos.length;
var transicao = 500;
var intervalo = 4000;
var intervaloAtual = 4000;
var intervaloControle = 0;

function exibir(element, indice, array, exibir){

	if(intervaloControle == 0){
		setTimeout(() => $(elementos[indice]).show(transicao), transicao);
		setTimeout(() => $(elementos[indice]).fadeOut(transicao),intervalo);
		intervaloAtual = intervalo+transicao; 
		intervaloControle = 1;
	}else{
		setTimeout(() => $(elementos[indice]).fadeIn(transicao), intervaloAtual);
		intervaloAtual += (intervalo+transicao);
		setTimeout(() => $(elementos[indice]).fadeOut(transicao), intervaloAtual);
	}
	if(indice == (tamanho - 1)){
		setTimeout(startSlide, 0);
	}
	
}

function startSlide(){
	elementos.forEach(exibir);
}