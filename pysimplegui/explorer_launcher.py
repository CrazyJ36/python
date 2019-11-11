#!/usr/bin/env python

import PySimpleGUI as sg
from subprocess import call
from os import curdir

layout = [
    [sg.Text("This starts Explorer")],
    [sg.Button("Go", key='btn')],
]

# Simple string icon definition. Only applies to window, taskbar stays default.
icon_data = str(curdir + '/windows_icon.ico')

# In window definition, the 'resizable=True' tag allows of course resizing,
# which is not doable by default, but also allows maximization of the window.
window = sg.Window("Explorer Launcher",
                   layout,
                   icon=icon_data,
                   size=(400, 200),
                   resizable=True,
                   )

while True:
    event, values = window.Read()
    if event == 'btn':
        call(['explorer'])
    elif event is None:
        break

window.close()
exit(0)
