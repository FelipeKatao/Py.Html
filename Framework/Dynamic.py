import sys

class Dynamic():
    def _createJsElements(self,local,element,lineIndex):
        text=""
        with open(local,'r') as f:
            text=f.readlines()
            pass
        with open(local,'w')as f:
            lineIndex-=1
            text[lineIndex]+=element
            for lines in text:
                f.write(lines)
            pass
        pass
    def AnimationOpacity(self,local,target,LineIndex):
        elementJs="opacityRepeat("+target+");"
        self._createJsElements(local,"",LineIndex)
        pass
    pass