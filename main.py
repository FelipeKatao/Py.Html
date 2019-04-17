from Framework import PyHtml
#Template for testes
#It's system work unique function with python tecnology
#Create HTML and CSS files with less lines in your Body.
#You no need create your web Project with hard dificult.
#Uses .CreateNewHtml() <--Where  create  one new HTML code.
#Its very easy and cool.
#Powered by Felipe Katao Tecnology.

#code exemple:

#Class for create
html= PyHtml.HtmlPy()
css= PyHtml.CssPy()
#start code
html.CreateNewHtml("index","Example",1)
css.CreateCss("Example","style.css")
html.LinkCss("style.css","Example")
html.CreateMenuHtml(R"Example\index.html","menu",7)
css.CreateRuleIdRules("style","Example","menu ul li","background-color:red;","float:left;","padding:10px;","")
#Test

