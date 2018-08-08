from tkinter import *

# Create Tk root(whole window) widget.
# One root per program, initialized before any widgets.
root = Tk()
# text Label as child view of root window
widget = Label(root, text="Window Text")
# Pack first widget. Sizing widget to fit into given text, and make it visible.
widget.pack()
# Window or widgets won't appear until to Tkinter loop is started.
root.mainloop()
# The loop stays running until the window is closed