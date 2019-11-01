#!/usr/bin/env python3

from tkinter import *
import time

window = Tk()
ntime = time.strftime("%I:%M")
text = Label(window, text=ntime)
text.pack()
window.mainloop()
