from Framework import HtmlData
from Framework import PyHtml
import os
import ctypes, sys

#Command list
LISTCOMMAND= ["help","create.html","exit","create.html.menu","set.path","link.css","create.element"]
#var envirioments 

#args for new imputs 
args0=""
argsX=""
argsY=""
LineIndex=""
#Create all constructors
dt=HtmlData.SearchData()
HTML=PyHtml.HtmlPy()

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
        print("create.html.menu = = Close the PY.html \n")
        pass

    if command =="exit":
        sys.exit()

    if command == "set.path":
        args0 = input("  >insert Html local File: ")
        argsX = input("  >Insert CSS local file: ")
        argsY = input("  >Insert Js local file: ")
        dt.createNewFileLocal(args0,argsX,argsY)
        print("         >The local files created: "+args0+"| |"+argsX+"| |"+argsY)
        pass

    if command == "create.html":
      args0 =input("   >Insert the name Html: ")
      argsX = input("   >Insert local Path:  ")
      argsY = input("  >Enter 0 or 1 (0: to create empety HTML and 1:to create with html template:  ")
      HTML.CreateNewHtml(args0,argsX,int(argsY))
      print("      >HTML create with  sucefull")
      pass

    if command == "create.html.menu":
        if(dt._localHtmlFiles!=""):
            argsX = input("   >Id of menu:  ")
            LineIndex = input("  >Line index to create menu: ") 
            HTML.CreateMenuHtml(dt._localHtmlFiles,argsX,int(LineIndex))
            print("      >Menu create with  sucefull")           
            pass
        else:
            args0 =input("   >Insert local Html: ")
            argsX = input("   >Id of menu:  ")
            LineIndex = input("  >Line index to create menu: ") 
            HTML.CreateMenuHtml(args0,argsX,int(LineIndex))
            print("      >Menu create with  sucefull")
            pass
        pass

    if command == "create.html.form":
        if(dt._localHtmlFiles!=""):
            args0= input("    >Insert the IdForm: ")
            argsX = input("   >Insert the index Line: ")
            argsY = input("   >Act form: ")
            argz =input("Id name Input form: ")
            HTML.CreateFormHtml(dt._localHtmlFiles,args0,int(argsX),argsY,argz)
            print("Forms create with susefull")
        else:
            argsE= input("    >Insert the local Html: ")
            args0= input("    >Insert the IdForm: ")
            argsX = input("   >Insert the index Line: ")
            argsY = input("   >Act form: ")
            argz =input("Id name Input form: ")
            HTML.CreateFormHtml(argsE,args0,int(argsX),argsY,argz)
            print("Forms create with susefull")
        pass
    if command == "link.css":
         if(dt._localHtmlFiles!=""):
            argsY = input("   >Insert the index Line: ")
            HTML.linkCssFile(dt._localHtmlFiles,dt._localCssFiles,int(argsY))
            print("Css Link anexed with susefull")             
            pass
         else:
            args0= input("    >Insert the Html Path: ")
            argsX = input("   >Insert the Css Path: ")
            argsY = input("   >Insert the index Line: ")
            HTML.linkCssFile(args0,argsX,int(argsY))
            print("Css Link anexed with susefull")
            pass
    if command == "create.element":
         if(dt._localHtmlFiles!=""):
            argsX = input("   >Insert the ID of element: ")
            argsY = input("   >Insert the type element (ex: <div>): ")
            argsE = input("   >Insert the index Line: ")
            value = input("   >Value of the element: ")
            HTML.createNewElement(dt._localHtmlFiles,argsX,argsY,int(argsE),value)
            print("Element create with susefull")             
            pass
         else:
            args0= input("    >Insert the Html Path: ")
            argsX = input("   >Insert the ID of element: ")
            argsY = input("   >Insert the type element (ex: <div>): ")
            argsE = input("   >Insert the index Line: ")
            value = input("   >Value of the element: ")
            HTML.createNewElement(args0,argsX,argsY,int(argsE),value)
            print("Element create with susefull") 
            pass        
    pass

if __name__ == '__main__':
    main()
    pass
