#!/usr/bin/env python3
import PySimpleGUIWeb as psg

layout = [
    [psg.Text('Header')],
    [psg.Button('Press me')],
]
window = psg.Window('Title', layout,
                    web_start_browser=False,
                    web_port=8086)
while True:
    event, values = window.read()
    if event == 'Press me':
        psg.Popup('pressed')
    if event is None:
        break

window.close()

