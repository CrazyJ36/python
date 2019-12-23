#!/usr/bin/env python
import PySimpleGUI as Gui

layout = [
    # This is one list. Remember comma after each element.
    # One row.
    [Gui.Text('One Row with:'), Gui.Text('[..., ...],')],
    [Gui.Text('---------------')],
    # Prints to two rows(different objects)
    [Gui.Text('Two Rows with:')], [Gui.Text('[...], [...],')],
]

window = Gui.Window('Window Title', layout)

while True:
    event, value = window.read()

    if event is None:
        break

window.close()
exit(0)
