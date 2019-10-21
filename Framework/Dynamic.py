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
    def CreateScriptArea(self,local,element,LineIndex):
        elementJs="\n <script src='Framework\Dynamic_\js\Physical.js'></script> \n<script src='Framework\Dynamic_\js\Effects.js'></script> \n<script src='Framework\Dynamic_\js\Controller.js'></script>\n<script>\n\n<\script>"
        self._createJsElements(local,"",LineIndex)        
        pass
    def AnimationOpacity(self,local,target,LineIndex):
        elementJs="\n opacityRepeat("+target+");"
        self._createJsElements(local,"",LineIndex)
        pass
    def AnimationChangeColorRed(self,local,target,LineIndex):
        elementJs="\n animationColorRed("+target+");"
        self._createJsElements(local,"",LineIndex)        
        pass
    def AnimationFadeObj(self,local,target,LineIndex):
        elementJs="\n fadeObj("+target+");"
        self._createJsElements(local,"",LineIndex)   
        pass
    pass