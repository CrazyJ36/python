import os

def showFsPath():
 ls = os.getcwd()
 print(ls)

def sPT():
 print("showing current directory")


sPT()
showFsPath()

os.chdir('/root')
showFsPath()
os.listDir()

os.chdir('/root/Development')
showFsPath()
os.listDir()
