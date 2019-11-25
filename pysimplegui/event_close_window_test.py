#!/usr/bin/env python
import PySimpleGUI as Gui


def print_to_console():
    print("Text printed to Console.")


layout = [
    [Gui.Text('''
Push windows close(x) to exit.

This tells the PySimpleGUI that no events 
are happening (None type of event exist).

We can then exit Python at that point.
''')],  
    
]

window = Gui.Window('title', layout)

while True:
    event, value = window.read()  # get any elements' events and values while reading the initiated window.

    if event is None:  # event(bool) is None when user clicks window close button(no events to receive).
        break          # If that happens, break the windows main loop, close window, and exit python below.

window.close()  # fully close window.
exit(0)  # exit python
