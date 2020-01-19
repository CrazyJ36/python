import PySimpleGUI as psg

layout = [
    [],
]

window = psg.Window('', layout,)

while True:
    event, values = window.Read()

    if event is None:
        break

window.Close()
