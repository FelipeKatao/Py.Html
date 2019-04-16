from io import StringIO

#Create, edit and read Html files 
class HtmlPy(): 
  _menuHtmlConst="<nav id=""{Menuname}"">\n <ul>\n  <li>Item</li>\n  <li>Item</li>\n  <li>Item</li>\n </ul>\n</nav>\n"
  _formHtmlConst="<form action='{actForm1}'>\n   <label>Label</label>\n  <input id='{idName}' type='text' name='name'>\n  <input type='submit' value='save'>\n</form>"
  def CreateNewHtml(self,NameHtml,Local,PreCode):
    #Project\codReadme.md
    if PreCode == 1:
      with open(Local+"/"+NameHtml+".html", "w") as f:   
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
      with open(Local+"/"+NameHtml+".html","w") as f:
        f.write("<html></html>")
        f.close()  
  def LinkCss(self,CssName,HtmlPath):
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
    pass  
  def CreateFormHtml(self,local,idform,LineIndex,ActForm,IdnameInput)
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
  pass

#Create, edit and read CSS files 
class CssPy():
  def CreateCss(self,path,CssName):

    with open(path+"/"+CssName,"w") as f:
      f.write("/*Css Code write with: [Py.Html]*/")
      f.close()
      pass
    pass
  def CreateRuleId(self,NameCss,Local,Id,Rule):
    try:
      with open(Local+"/"+NameCss+".css", "a") as f: 
        f.write("\n")
        f.write("#"+Id+"{\n"+Rule+"\n" +"} \n")
        f.close()
        pass
      pass
    except:
      print("Error of local CSS file.")
      pass
    pass
  def CreateRuleClass(self,NameCss,Local,Class,Rule):
    try:
      with open(Local+"/"+NameCss+".css", "a") as f: 
        f.write("\n")
        f.write("."+Id+"{\n"+Rule+"\n" +"} \n")
        f.close()
        pass
      pass
    except:
      print("Error of local CSS file.")
      pass
    pass
  def CreateRuleClassRules(self,NameCss,Local,classCss,RuleA,Rule0,Rule1,Rule2):
    try:
      with open(Local+"/"+NameCss+".css", "a") as f: 
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
  def CreateRuleIdRules(self,NameCss,Local,Id,RuleA,Rule0,Rule1,Rule2):
    try:
      with open(Local+"/"+NameCss+".css", "a") as f: 
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
  def appendNewRule(self,CssPath,Id,RuleX1,RuleX2,RuleX3):
    line=0
    endline=0
    text=""
    with open(CssPath,"r")as f:
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
    with open(CssPath,"w")as f:
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
  pass

#Class for search data in HTML files and create analitic data.
class SearchData():
  pass