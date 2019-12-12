import PySimpleGUI as psg

layout = [
    [psg.Txt("text1")],
    [psg.Button("Move")],
]

window = psg.Window('window', layout, size=[100, 75])

while True:
    event, values = window.Read()
    if event is None:
        break
    elif event == "Move":
        window.move(100, 100)
window.Close()
