#!/usr/bin/env python
import PySimpleGUI as Gui

layout = [
    # Remember comma after each element. As this is one list.
    [Gui.Text('One Row with:'), Gui.Text('[..., ...]')],  # One one row. Remember comma.
	[Gui.Text('---------------')],  # Remember comma as this is one list.
    [Gui.Text('Two Rows with:')], [Gui.Text('[...], [...]')],  # Prints to two rows(different objects)
]

window = Gui.Window('Window Title', layout)

while True:
  event, value = window.read()
  
  if event is None:
    break

window.close()
exit(0)
