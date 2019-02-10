
class CriarCSS():
  css=open("sytle.css","w+")
  cor=""
  CorFont=""
  height=""
  width=""
  position=""
  def CriarRegra(self,Id,Cor,height,width,position,CorFonte):
    self.css.write("#"+Id+"{ \n")
    self.css.write("background:"+self.cor+"; \n")
    self.css.write("height:"+self.height+"; \n")
    self.css.write("width:"+self.width+"; \n")
    self.css.write("color:"+self.CorFont+"; \n")
    self.css.write("position:"+self.position+";\n")
    self.css.write("}")
    pass
  def FecharCSS(self):
    self.css.close()
  pass