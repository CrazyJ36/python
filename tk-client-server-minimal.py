#!/usr/bin/env python3
from tkinter import Tk, Button, messagebox


def say_hi():

    print("They said hello!")
    messagebox.showinfo("title", "message")
    return 0


root = Tk()

hi = Button(text="hi", command=say_hi)  # say_hi no perenthesis
hi.pack(side="top")

quit_win = Button(text="quit", fg="red", command=root.destroy)
quit_win.pack(side="bottom")

root.mainloop()
