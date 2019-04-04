from io import StringIO

#Create, edit and read Html files 
class HtmlPy():
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
      #<link href="css/style.css" rel="stylesheet" type="text/css" />
      text[line]="<link href='{Cssname}' rel='stylesheet' type='text/css' />\n".format(Cssname=CssName)
      for linha in text:
        f.write(linha)
      f.close()
                               
  pass

#Create, edit and read CSS files 
class CssPy():

  pass

#Class for search data in HTML files and create analitic data.
class SearchData():
  pass