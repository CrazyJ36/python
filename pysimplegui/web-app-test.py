import PySimpleGUIWeb as Gui

layout = [
  [Gui.Text('text')],
  [Gui.Button('button')]
]

win = Gui.Window('Title', layout)

while True:
  event, values = win.Read()
  if event is None:
    break
  elif event == 'button':
    print("user pressed button on web app")
win.Close()
exit(0)