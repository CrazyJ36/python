# This checks git status in any platform on any local repo
import os
from tkinter import *

win = Tk()
win.pack_propagate(0)
win.geometry("600x500")
win.title(string="App")
repo = Entry(win, text="repo name")


if sys.platform == "win32" and os.scandir("C:\\Users\\Thomas"):
    devdir = "C:\\Users\\Thomas\\Development\\"""
elif sys.platform == "win32" and os.scandir("C:\\Users\\CrazyJ36"):
    devdir = "C:\\Users\\CrazyJ36\\Development\\"""
elif sys.platform == "linux":
    devdir = "/home/thomas/development/"
else:
    envwarn = Label(win, text="failed to get environment")
    envwarn.pack()
    exit(0)


def gitcmd():
    cmdstr = "cd " + devdir + repo.get() + " && git status"
    cmdlbl = Label(win, text="Using: " + cmdstr)
    cmdlbl.pack()
    outfileobj = os.popen(cmdstr)
    out = outfileobj.read()
    outfileobj.close()
    outtxt = Label(win, text=out)
    outtxt.pack()

if win.keys(win, ENTER)
btn = Button(win, text="Check Git Repo", command=lambda: gitcmd())
repo.pack()
btn.pack()

win.mainloop()

