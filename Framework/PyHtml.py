from io import StringIO

#Create, edit and read Html files 
class HtmlPy(): 

  _menuHtmlConst="<nav id=""{Menuname}"">\n <ul>\n  <li>Item</li>\n  <li>Item</li>\n  <li>Item</li>\n </ul>\n</nav>\n"
  _formHtmlConst="<form action='{actForm1}'>\n   <label>Label</label>\n  <input id='{idName}' type='text' name='name'>\n  <input type='submit' value='save'>\n</form>"
  _geneticElement="<{element} id={idElement}>{value}</{element}>"

  _LinkElement="<link href={locaLink} rel={typeLink} type={type} />"

  def CreateNewHtml(self,NameHtml,LocalFile,PreCode):
    #Project\codReadme.md
    if PreCode == 1:
      with open(LocalFile, "w") as f:   
        f.write("<!DOCTYPE html>")
        f.write("\n<html>")
        f.write("\n<head>  <title>{Html}</title>".format(Html=NameHtml))
        f.write("\n<meta charset='UTF-8'>") 
        f.write("\n<meta name="+"'viewport'"+ "content="+"'width=device-width, initial-scale=1.0'"+">")
        f.write("\n<link>     ")      
        f.write("\n </head>")
        f.write("\n   <body>")
        f.write("\n      </body>")
        f.write("\n        </html>")
        f.close() 
    else:
      with open(LocalFile,"w") as f:
        f.write("<html></html>")
        f.close()  
  def LinkCssStarter(self,CssName,HtmlPath):
    line=0
    text=""
    with open(HtmlPath,"r")as f:
      text=f.readlines()
      for linha in text:
        if "<link>" in linha:
          print(line)
          f.close()
          break
        line+=1
    with open(HtmlPath,"w")as f:
      text[line]="<link href='{Cssname}' rel='stylesheet' type='text/css' />\n".format(Cssname=CssName)
      for linha in text:
        f.write(linha)
      f.close()                             
  def CreateMenuHtml(self,local,idMenu,LineIndex):
    text=""
    with open(local,'r') as f:
      text=f.readlines()
      f.close()
      pass
    with open(local,'w')as f:
      LineIndex-=1
      text[LineIndex]+="\n"+self._menuHtmlConst.format(Menuname="'"+idMenu+"'")
      for lines in text:
        f.write(lines)
      pass
      f.close()
    pass  
  def CreateFormHtml(self,local,idform,LineIndex,ActForm,IdnameInput):
    text=""
    with open(local,'r') as f:
      text=f.readlines()
      f.close()
      pass
    with open(local,'w')as f:
      LineIndex-=1
      text[LineIndex]+="\n"+self._formHtmlConst.format(actForm1=ActForm,idName=IdnameInput)+"\n"
      for lines in text:
        f.write(lines)
      pass  
    pass
  def linkCssFile(self,local,CssPath,LineIndex):
    text=""
    with open(local,"r")as f:
      text=f.readlines()
      f.close()
      pass
    with open(local,"w")as f:
      LineIndex-=1
      text[LineIndex]+=self._LinkElement.format(locaLink=local,typeLink="stylesheet",type="text/css")+"\n"
      for lines in text:
        f.write(lines)
      pass
    pass
  def createNewElement(self,local,id,Element,Lineindex,Value):
    text=""
    with open(local,"r") as f:
      text=f.readlines()
      f.close()
      pass
    with open(local,"w") as f:
      Lineindex-=1
      text[Lineindex]+="\n"+self._geneticElement.format(element=Element,idElement=id,value=Value)+"\n"
      for lines in text:
        f.write(lines)
        pass
    pass
  def responsiveWindowMeta(self,local,escale,LineIndex):
    text=""
    with open(local,"r") as f:
      text=f.readlines()
      f.close()
    pass
    with open(local,"w")as f:
      LineIndex-=1
      text[LineIndex]+="\n"+"<meta name='Viewport' content='width=device-width, initial-scale={scale}'>\n".format(scale=escale)
      for lines in text:
        f.write(lines)
      f.close()
      pass
  def createAppSpaDefault(self,local,AppName,Content,LineIndex):
    text=""
    element="<div id='content'>    \n<main>    \n<div id='{name}' class='app default'>\n     <div>{content}</div>\n     </div>     \n    </main>\n</div>\n".format(name=AppName,content=Content)
    with open(local,"r") as f:
      text=f.readlines()
      f.close()
    pass
    with open(local,"w")as f:
      LineIndex-=1
      text[LineIndex]+=element
      for lines in text:
        f.write(lines)
      f.close()
      pass
  def createAppSpa(self,local,AppName,Content,LineIndex):
    text=""
    element="<div id='{name}' class='app'>\n     <div>{content}</div>\n     </div>\n".format(name=AppName,content=Content)
    with open(local,"r") as f:
      text=f.readlines()
      f.close()
    pass
    with open(local,"w")as f:
      LineIndex-=1
      text[LineIndex]+=element
      for lines in text:
        f.write(lines)
      f.close()
      pass

  pass

#Create, edit and read CSS files 
class CssPy():
  def CreateCss(self,pathCss,CssName):
    with open(pathCss,"w") as f:
      f.write("/*Css Code write with: [Py.Html]*/")
      f.close()
      pass
    pass
  def CreateRuleId(self,NameCss,LocalCss,Id,Rule):
    try:
      with open(LocalCss, "a") as f: 
        f.write("\n")
        f.write("#"+Id+"{\n"+Rule+"\n" +"} \n")
        f.close()
        pass
      pass
    except:
      print("Error of local CSS file.")
      pass
    pass
  def CreateRuleClass(self,NameCss,LocalCss,Class,Rule):
    try:
      with open(LocalCss, "a") as f: 
        f.write("\n")
        f.write("."+Id+"{\n"+Rule+"\n" +"} \n")
        f.close()
        pass
      pass
    except:
      print("Error of local CSS file.")
      pass
    pass
  def CreateMultipleRules(self,NameCss,LocalCss,classCss,RuleA,Rule0,Rule1,Rule2):
    try:
      with open(LocalCss, "a") as f: 
        f.write("\n")
        f.write("."+classCss+"{\n"+RuleA+"\n")
        f.write(Rule0+"\n"+Rule1+"\n"+Rule2+"\n")
        f.write("}\n")
        f.close()
        pass
      pass
    except:
      print("Error of local CSS file.")
      pass
    pass  
  def CreateRuleIdRules(self,NameCss,LocalCss,Id,RuleA,Rule0,Rule1,Rule2):
    try:
      with open(LocalCss, "a") as f: 
        f.write("\n")
        f.write("#"+Id+"{\n"+RuleA+"\n")
        f.write(Rule0+"\n"+Rule1+"\n"+Rule2+"\n")
        f.write("}\n")
        f.close()
        pass
      pass
    except:
      print("Error of local CSS file.")
      pass
    pass  
  def appendNewRule(self,LocalCss,Id,RuleX1,RuleX2,RuleX3):
    line=0
    endline=0
    text=""
    with open(LocalCss,"r")as f:
      text=f.readlines()
      for linha in text:
        print(linha)
        if "#"+Id+"{" == linha:
          print(line)
          for enline  in text:
            if "}" in enline:
              print(enline)
              break
            endline+=1
          f.close()
          break
        line+=1
      f.close()    
    pass
    with open(LocalCss,"w")as f:
      if(RuleX1!=""):
        text[endline-2]+=RuleX1+"\n"
      if(RuleX2!=""):
        text[endline-2]+=RuleX2+"\n"
      if(RuleX3!=""):
        text[endline-2]+=RuleX3+"\n"         
      for linha in text:
        f.write(linha)
      f.close()   
      pass
  def appendLinkSpaRule(self,HtmlPath,LineIndex):
    text=""
    rule= R"\n<link href='\Framework\cssComponents\Spa.css' rel='stylesheet' type='text/css' />\n"
    with open(HtmlPath,"r")as f:
      text=f.readlines()
      LineIndex-=1
      f.close()
    with open(HtmlPath,"w")as f:
      text[LineIndex]= rule
      for linha in text:
        f.write(linha)
      f.close()      
    pass
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
  def insertComponent(self,local,lineIndex,nameComponent):
    """Inserts components target to Html file.
    
    Arguments:
        local {string/Path} -- Select your  path of Html file
        lineIndex {int} -- Select line of your Html code, for Component.
        nameComponent {string} -- Select name valid names: nav , list , article
    """
    indexcount=0
    if(nameComponent=="nav"):
      with open(local,'r') as f:
        self.text= f.readlines()
      pass

      with open(R"Framework\Components\nav.html",'r') as c:
        self.comp=c.readlines()
        pass

      with open(local,'w') as w:
        for lines in self.text:
          w.write(lines)
          indexcount+=1
          if indexcount == lineIndex:
            print(self.comp)
            for linesx in self.comp:
              w.write(linesx)
            pass
        pass

    pass
  pass