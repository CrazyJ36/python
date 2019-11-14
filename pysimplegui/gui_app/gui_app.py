import PySimpleGUI as sg
from os import curdir

layout = [
    [sg.Text('Welcome')],
]

window = sg.Window('Title', layout, size=[300, 100])

while True:
    event, values = window.Read()
    if event is None:
        break

window.Close()
exit(0)
