# This checks git status in any platform on any local repo
import os
from tkinter import *

win = Tk()
win.pack_propagate(0)
win.title(string="Git Status")
win.geometry("400x300")
repo = Entry(win)

# easier than below, use os.environ['HOME'] + regex for development dir name
if sys.platform == "win32" and os.environ['USERNAME'] == "Thomas":
    devdir = "C:\\Users\\Thomas\\Development\\"
elif sys.platform == "win32" and os.environ['USERNAME'] == "CrazyJ36":
    devdir = "C:\\Users\\CrazyJ36\\Development\\"
elif sys.platform == "win32" and os.environ['USERNAME'] == "thomas":
    devdir = "C:\\Users\\thomas\\Development\\"
elif sys.platform == "linux":
    devdir = "/home/thomas/development/"
else:
    envwarn = Label(win, text="failed to get environment")
    envwarn.pack()

def gitcmd():
    cmdstr = "cd " + devdir + repo.get() + " && git status"
    cmdfileobj = os.popen(cmdstr)
    out = cmdfileobj.read()
    cmdfileobj.close()
    outtxt = Label(win, text=out)
    outtxt.pack()


btn = Button(win, text="Check Git Repo", command=lambda: gitcmd())
repo.pack()
btn.pack()
win.mainloop()
