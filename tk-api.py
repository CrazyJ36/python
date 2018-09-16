from tkinter import *
import os
win = Tk()
btn1 = Button(win, command="os.system('cmd.exe')")
btn1.pack()
win.mainloop()

