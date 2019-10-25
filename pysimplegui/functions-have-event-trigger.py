#!/usr/bin/env python
import PySimpleGUI as Gui
from time import sleep

view = [
  [Gui.Text('''
The function OK():
Makes and shows A Button(below) Object and has constant id of int: \'OK\'
The GUI OK() button can then be referenced in event loop with:
if event == 'OK':.
''')],
  [Gui.OK()]
]

win = Gui.Window('Simple Button', view)

while True:
  event, value = win.read()

  if event == 'OK':
    Gui.Popup('Detected Gui.OK() clicked with direct reference to int: \'OK\'')
    break
  elif event is None:
    break
  
win.close()
exit(0)
