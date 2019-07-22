from io import StringIO

#Create, edit and read Html files 
class HtmlPy(): 

  _menuHtmlConst="<nav id=""{Menuname}"">\n <ul>\n  <li>Item</li>\n  <li>Item</li>\n  <li>Item</li>\n </ul>\n</nav>\n"
  _formHtmlConst="<form action='{actForm1}'>\n   <label>Label</label>\n  <input id='{idName}' type='text' name='name'>\n  <input type='submit' value='save'>\n</form>"
  _geneticElement="<{element} id={idElement}>{value}</{element}>"

  _LinkElement="<link href={locaLink} rel={typeLink} type={type} />"
  _ScriptElement="<script src={localLink}></script>"

  def _BaseElement(self,local,componentTarget,lineIndex):
    text=""
    with open(componentTarget,'r') as f:
      text= f.readlines()
      pass
    with open(local,'w')as c:
      for lines in text:
        c.write(lines)
        pass
    pass
    
  def _createElements(self,local,element,lineIndexCr):
    text=""
    with open(local,'r') as f:
      text=f.readlines()
      f.close()
      pass
    with open(local,'w')as f:
      lineIndexCr-=1
      text[lineIndexCr]+=element
      for lines in text:
        f.write(lines)
      pass  
    pass

  def CreateNewHtml(self,NameHtml,LocalFile,PreCode):
    #Project\codReadme.md
    if PreCode == 1:
      self._BaseElement(LocalFile,"htmlBase.html",1)
    else:
      with open(LocalFile,"w") as f:
        f.write("<html>\n\n</html>")
        f.close()  

  def LinkCssStarter(self,CssName,HtmlPath,LineIndex):
    self._createElements(HtmlPath,"<link href='{Cssname}' rel='stylesheet' type='text/css' />\n".format(Cssname=CssName),LineIndex)
    pass         

  def CreateMenuHtml(self,local,idMenu,LineIndex):
    self._createElements(local,"\n"+self._menuHtmlConst.format(Menuname="'"+idMenu+"'"),LineIndex)
    pass  

  def CreateFormHtml(self,local,idform,LineIndex,ActForm,IdnameInput):
    self._createElements(local,"\n"+self._formHtmlConst.format(actForm1=ActForm,idName=IdnameInput)+"\n",LineIndex)
    pass

  def linkCssFile(self,local,CssPath,LineIndex):
    self._createElements(local,self._LinkElement.format(locaLink=local,typeLink="stylesheet",type="text/css")+"\n",LineIndex)
    pass

  def createNewElement(self,local,id,Element,Lineindex,Value):
    self._createElements(local,"\n"+self._geneticElement.format(element=Element,idElement=id,value=Value)+"\n",Lineindex)
    pass

  def responsiveWindowMeta(self,local,escale,LineIndex):
    self._createElements(local,"\n"+"<meta name='Viewport' content='width=device-width, initial-scale={scale}'>\n".format(scale=escale),LineIndex)
    pass

  def createAppSpa(self,local,AppName,Content,LineIndex):
    self._createElements(local,"<div id='{name}' class='app'>\n     <div>{content}</div>\n     </div>\n".format(name=AppName,content=Content),LineIndex)
    pass

  def LinkJsFile(self,local,jsPath,LineIndex):
    self._createElements(local,self._ScriptElement.format(locaLink=local)+"\n",LineIndex)
    pass

  def LinkJquery(self,local,LineIndex):
    self._createElements(local,self._ScriptElement.format(localLink="https://code.jquery.com/jquery-3.2.1.min.js")+"\n",LineIndex)
    pass

  pass

#Create, edit and read CSS files 
class CsPy():
  _elementgenericCss="\n#{idCss}"
  _elementgenericCssClass="\n.{idCss}"
  
  def _createElements(self,localCss,element,lineIndexCr):
    textCss=""
    with open(localCss,'r') as f:
      textCss=f.readlines()
      f.close()
      pass
    with open(localCss,'w')as f:
      lineIndexCr-=1
      textCss[lineIndexCr]+=element
      for lines in text:
        f.write(lines)
      pass  
    pass

  def CreateCss(self,pathCss,CssName):
    with open(pathCss,"w") as f:
      f.write("/*Css Code write with: [Py.Html]*/")
      f.close()
      pass
    pass

  def CreateRuleClass(self,NameCss,LocalCss,Class,Rule):
    self._createElements(LocalCss,self._elementgenericCssClass.format(idCss=Class)+"{\n\n}",0)
    pass 

  def CreateRuleIdRules(self,NameCss,LocalCss,rule,lineIndex):
    self._createElements(LocalCss,rule,lineIndex);
    pass

  def appendNewRule(self,LocalCss,Id,LineIndex):
    self._createElements(LocalCss,self._elementgenericCss.format(idCss=Id)+"{\n\n}",0)
    pass

  def appendLinkSpaRule(self,HtmlPath,LineIndex):
    self._createElements(HtmlPath,R"\n<link href='\Framework\cssComponents\Spa.css' rel='stylesheet' type='text/css' />\n",LineIndex)
  pass

#Class for search data in HTML files and create analitic data.
class SearchData():

  _localHtmlFiles=[]
  _localCssFiles=[]
  _localJsFiles=[]

  def createNewFileLocal(self,html,css,js):
    if html!="":
      self._localHtmlFiles.append(html)
    if css!="":
      self._localCssFiles.append(css)
    if js!="":
      self._localJsFiles.append(js)
    pass
  pass

class Component():

  text=""
  comp=""

  def _insertCodeCompReader(self,componentTarget,local,LineIndex):
    indexcount=0
    with open(local,'r') as f:
      self.text= f.readlines()
    pass
    with open(componentTarget,'r') as g:
      self.comp=g.readlines();
      pass
    with open(local,'w')as c:
      for lines in self.text:
        c.write(lines)
        indexcount+=1
        if indexcount == LineIndex:
          print(self.comp)
          for linesx in self.comp:
            c.write(linesx);
            pass
          pass
        pass
      pass
  def insertComponent(self,local,lineIndex,nameComponent):
     
    """Inserts components target to Html file.
    
    Arguments:
        local {string/Path} -- Select your  path of Html file
        lineIndex {int} -- Select line of your Html code, for Component.
        nameComponent {string} -- Select name valid names: nav , list , article
    """

    if(nameComponent == "article"):
      self._insertCodeCompReader("article.html",local,lineIndex)
      pass
    if(nameComponent == "nav"):
      self._insertCodeCompReader("ColocaOlinkAqui",local,lineIndex)
      pass
    if(nameComponent == "template-mobile"):
      self._insertCodeCompReader("ColocaOlinkAqui",local,lineIndex)      
      pass    
  pass
