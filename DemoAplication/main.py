from Framework import PyHtml
from Framework import CssTool

#code exemple:
contendArticle="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet"


<nav id='#'>
 <ul>
  <li>Item</li>

<nav id='#'>
 <ul>
  <li>Item</li>
  <li>Item</li>
  <li>Item</li>
 </ul>
</nav>

<nav id='#'>
 <ul>
  <li>Item</li>
  <li>Item</li>
  <li>Item</li>
 </ul>
</nav>

<nav id='#'>
 <ul>
  <li>Item</li>
  <li>Item</li>
  <li>Item</li>
 </ul>
</nav>

<nav id='#'>
 <ul>
  <li>Item</li>
  <li>Item</li>
  <li>Item</li>
 </ul>
</nav>
  <li>Item</li>
  <li>Item</li>
 </ul>
</nav>
html= PyHtml.HtmlPy()
css= PyHtml.CssPy()
resp=CssTool.Responsive()

html.CreateNewHtml("New App","app.html",1)
resp.importCssResponsive("app.html",5)

resp.containerBootstrap("app.html","<h1>Hello World</h1>\n\n",9)
resp.alertBootStrap("app.html","Create new app With Py.html\n",11)
resp.NavBootstrap("app.html",11)
resp.CardBodyBootstrap("app.html","Loren its App","Ago add in 3 years ago","\n"+contendArticle,21)


