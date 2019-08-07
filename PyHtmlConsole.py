from Framework import PyHtml
from Framework import CssTool
import os
import ctypes, sys

#Command list
LISTCOMMAND= ["help","crete.html","exit"]

def main():
    CreateText("start")
    while(True):
        codInput=input(">")
        CommandList(codInput)
    pass

def CreateText(text):
    if text=="start":
        print("                    < Py.html >     \n")
         
        print("           Welcome to Py.html, framework to creation ")
        print("           of web designer front and or back end")
        print("         with suport react, create your site in fell times.\n")
        print("Its version: [V0.0.1] Beta \n")
        print(">Enter with command")
        pass
    pass

def CommandList(Command):
    validcomand=False
    for textList in LISTCOMMAND:
        if(textList==Command):
            ExecuteCommand(textList)
            validcomand=True
        pass
    if validcomand==False:
        print(">Invalid command or token ")
    pass

def ExecuteCommand(command):
    if command =="help":
        print("      VALID INPUTS FOR PY.HTML:   ")
        print("      create.html = Create one html file ")
        print("      create.css = = Create one Css file ")
        print("      exit = = Close the PY.html \n")

        pass
    if command =="exit":
        sys.exit()
    pass

if __name__ == '__main__':
    main()
    pass