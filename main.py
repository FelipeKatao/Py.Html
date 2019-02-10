import HTMLWrite as htwr
import CSSWrite as Csswr
#Algoritimo que cria um arquivo HTML automaticamente

html_write=htwr.ElementHtml()
CSS_write=Csswr.CriarCSS()
Num_div=0
idDiv=""
ConteudoDiv=""
Pergunta=""

Num_div=int(input("Quantas divs terá o seu HTML:"))
html_write.CriarHTML()

while(Num_div>=1):
  idDiv=input("Identificação da Div:")
  ConteudoDiv=input("Conteudo da Div:")
  html_write.CriarDiv(idDiv,ConteudoDiv)
  Pergunta=input("Deseja criar regras CSS? n ou s:")
  if(Pergunta=="s"):
    CSS_write.cor=input("Qual a cor:")
    CSS_write.height=input("Qual a largura:")
    CSS_write.width=input("Qual a Altura:")
    CSS_write.position=input("Qual a posição:")
    CSS_write.CorFont=input("Qual a cor fonte:")
    CSS_write.CriarRegra(idDiv,CSS_write.cor,CSS_write.height,CSS_write.width,CSS_write.position,CSS_write.CorFont)
    pass
  Num_div-=1
  pass
html_write.FecharHTML()