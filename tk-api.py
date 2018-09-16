import os
from tkinter import *

win = Tk()
win.pack_propagate(0)
win.title(string="App")


def taskmgr():
    os.system("Taskmgr.exe")


btn = Button(win, text="taskmgr", command=lambda: taskmgr())
btn.pack()
win.mainloop()

