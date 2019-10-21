
#Class for Data Analytic tool search, data, statistics text and dictionaries with information about the context

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
