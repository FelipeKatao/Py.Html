#Classe para Criação do  HTML
class ElementHtml():

  HTML=open('index.html','w+')

  def CriarHTML(self):
    self.HTML.write("<html> \n")
    self.HTML.write("<head>\n")
    self.HTML.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"")
    self.HTML.write("</head>\n")
    self.HTML.write("<body>\n")
    pass
  def CriarDiv(self,identificar,conteudo):
    self.HTML.write("<div id=\""+identificar+"\">")
    self.HTML.write(conteudo+"</div>\n")
    pass
  def FecharHTML(self):
    self.HTML.write("</body>\n \n</html>")
    self.HTML.close()
    pass
  pass