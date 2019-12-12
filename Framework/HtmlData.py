
#Class for Data Analytic tool search, data, statistics text and dictionaries with information about the context

class SearchData():
    
  _localHtmlFiles=[]
  _localCssFiles=[]
  _localJsFiles=[]
  #All content of HTML,CC and JS
  _HtmlFiles=[]

  def createNewFileLocal(self,html,css,js):
    if html!="":
      self._localHtmlFiles.append(html)
    if css!="":
      self._localCssFiles.append(css)
    if js!="":
      self._localJsFiles.append(js)
    pass
  def readAllHtml(self,html):
      text=""
      with open(html,'r') as f:
        text= f.readlines()
      pass
      self._HtmlFiles.append(text)
      pass
  def loadHtml(self,indexHtml):
      print(self._HtmlFiles[indexHtml])
      return self._HtmlFiles[indexHtml]
      pass
  pass
