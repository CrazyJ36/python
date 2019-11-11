#!/usr/bin/env python
import PySimpleGUI as Gui

view = [
    # *IMPORTANT*:
    # for PySimpleGui, The elements in layouts are referenced by
    # their text. eg. for the layout here:
    # Gui.Text('Some words') will be referenced in the event 'Some Words'
    [Gui.Text('Some words')],
    [Gui.Button('The Button')]  # Use event 'The Button' later.
]

win = Gui.Window('Get Values', view)

while True:
    event, values = win.read()
    if event == 'The Button':  # The buttons title text is assigned to and used as event trigger.
        print('Button pressed.')
    elif event is None:
        break

win.close()
exit(0)
