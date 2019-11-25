import tkinter
from tkinter import messagebox

# Basic Frame
class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi = tkinter.Button(self) # Define A button
        self.hi["text"] = "Say Hello"
        self.hi["command"] = self.say_hi
        self.hi.pack(side="top")

        self.quit = tkinter.Button(self, text="QUIT", fg="red", command=root.destroy) # define button
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("They said hello!")
        messagebox.showinfo("Info","Hello!")

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
