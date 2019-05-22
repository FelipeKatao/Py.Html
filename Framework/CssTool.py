from Framework import PyHtml
from io import StringIO

class Responsive():
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
    pass


