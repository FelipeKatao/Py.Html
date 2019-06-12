from io import StringIO
OUTPUT_CODEC= "utf-8"

class Responsive():
    def importCssMobile(self,local,lineIndex):
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w')as f:
            lineIndex-=1
            text[lineIndex]+="\n <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'> \n  <script src='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js'></script>\n"
            for lines in text:
                f.write(lines)
                pass
            pass    
        pass
    def importCssResponsive(self,local,LineIndex):
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w')as f:
            LineIndex-=1
            text[LineIndex]+="\n  <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>\n"     
            for lines in text:
                 f.write(lines)
                 pass  
    def alertBootStrap(self,local,Content,LineIndex):
        divAlert="\n     <div class='alert alert-primary' role='alert'>"+Content+"</div>\n"
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w') as f:
            LineIndex-=1
            text[LineIndex]=divAlert
            for line in text:
                f.write(line)
            pass
        pass
    def containerBootstrap(self,local,Content,LineIndex):
        divAlert="\n     <div class='container'>"+Content+"</div>\n"
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w') as f:
            LineIndex-=1
            text[LineIndex]=divAlert
            for line in text:
                f.write(line)
            pass
        pass
    def containerFluidBootstrap(self,local,Content,LineIndex):
        divAlert="\n     <div class='container-fluid'>"+Content+"</div>\n"
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w') as f:
            LineIndex-=1
            text[LineIndex]=divAlert
            for line in text:
                f.write(line)
            pass
        pass
    def NavBootstrap(self,local,LineIndex):
        divNav="\n <ul class='navbar navbar-expand-lg navbar-light bg-light'>\n     <li class='navbar-brand'>\n<a class='nav-link active' href='#'>Menu</a>\n</li>\n     <li class='navbar-brand'>\n<a class='nav-link active' href='#'>Menu</a>\n</li>\n </ul> "
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w') as f:
            LineIndex-=1
            text[LineIndex]=divNav
            for line in text:
                f.write(line)
            pass
        pass
    def spinnerBootstrap(self,local,LineIndex):
        divNav="\n  <div class='spinner-grow' role='status'>\n    <span class='sr-only'>Loading...</span>\n  </div>\n "
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w') as f:
            LineIndex-=1
            text[LineIndex]=divNav
            for line in text:
                f.write(line)
            pass
        pass
    def CardBootstrap(self,local,Size,Title,SubTitle,contentCard,LineIndex):
        divNav="\n  <div class='card' style='width: {size}rem;'>\n   <div class='card-body'>\n   <h5 class='card-title'>{title}</h5>\n   <h6 class='card-subtitle mb-2 text-muted'>{sub}</h6>\n     <p class='card-text'>{content}</p>\n   <a href='#' class='card-link'>link</a>\n  </div>\n   <div>".format(size=Size,title=Title,sub=SubTitle,content=contentCard)
        text=""
        with open(local,'r',encoding=OUTPUT_CODEC) as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w',encoding=OUTPUT_CODEC) as f:
            LineIndex-=1
            text[LineIndex]=divNav
            for line in text:
                f.write(line)
            pass
        pass
    def CardBodyBootstrap(self,local,Title,Footer,contentCard,LineIndex):
        divNav="\n   <div class='card text-center'>\n<div class='card-header'>{title}</div>\n  <div class='card-body'>\n   <p class='card-text'>\n{content}</p>\n  </div>\n  <div class='card-footer text-muted'>{sub}</div>\n   </div>   ".format(title=Title,sub=Footer,content=contentCard)
        text=""
        with open(local,'r',encoding=OUTPUT_CODEC) as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,'w',encoding=OUTPUT_CODEC) as f:
            LineIndex-=1
            text[LineIndex]=divNav
            for line in text:
                f.write(line)
            pass
        pass
    def CollectionMobile(self,local,title,element,lineIndex):

        """Create Collection Mobile
        Arguments:
            local {String} -- Select local to your Html code
            title {String]} -- Create Title to collection
            element {String} -- Create element to your collection
            lineIndex {Int} -- Select line to your Htmll, for insert its collection 
        """
        collectDiv="\n<ul class='collection with-header'>\n <li class='collection-header'><h4>{titleName}</h4></li>\n <li class='collection-item'><div>{contentName}<a href='#' class='secondary-content'><i class='material-icons'>send</i></a></div></li>\n".format(titleName=title,contentName=element)
        text=""
        with open(local,'r',encoding=OUTPUT_CODEC) as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,"w",encoding=OUTPUT_CODEC)as f:
            lineIndex-=1
            text[lineIndex]=collectDiv
            for lines in text:
                f.write(lines)
                pass
            pass 
    def CollectionLinksMobile(self,local,title,element,lineIndex):

        """Create Collection of links Mobile
        Arguments:
            local {String} -- Select local to your Html code
            title {String]} -- Create Title to collection
            element {String} -- Create element to your collection
            lineIndex {Int} -- Select line to your Htmll, for insert its collection 
        """
        collectDiv="\n<div class='collection'>\n<a href='#!' class='collection-item'>{contentName}</a>\n</div>\n ".format(titleName=title,contentName=element)
        text=""
        with open(local,'r',encoding=OUTPUT_CODEC) as f:
            text=f.readlines()
            f.close()
            pass
        with open(local,"w",encoding=OUTPUT_CODEC)as f:
            lineIndex-=1
            text[lineIndex]=collectDiv
            for lines in text:
                f.write(lines)
                pass
            pass 
    pass


