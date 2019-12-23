import PySimpleGUI as psg

layout = [
    [psg.Button("Move")],
]

window = psg.Window('window', layout, size=[75, 75])

while True:
    event, values = window.Read()
    if event is None:
        break
    elif event == "Move":
        window.move(100, 100)
window.Close()
