from Framework import PyHtml
#Template for testes
#It's system work unique function with python tecnology
#Create HTML and CSS files with less lines in your Body.
#You no need create your web Project with hard dificult.
#Uses .CreateNewHtml() <--Where  create  one new HTML code.
#Its very easy and cool.
#Powered by Felipe Katao Tecnology.

#code exemple:
vr2= PyHtml.HtmlPy()
vr2.CreateNewHtml("about","Project",1)
vr2.CreateNewHtml("index","Project",1)
vr2.LinkCss(R"Project\style.css",R"Project\about.html")
vr2.LinkCss(R"Project\style.css",R"Project\index.html")
#Test
