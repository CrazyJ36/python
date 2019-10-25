import PySimpleGUIWeb as Gui
from time import sleep
view = [
  [Gui.Text("Hello")]
]
win = Gui.Window("Title", view)

while True:
    event, values = win.Read()
    if event == KeyboardInterrupt:
      win.Close()
      exit(0)