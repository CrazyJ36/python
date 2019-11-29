import PySimpleGUI as sg

children_layout = [
    [sg.Text('text1')],
    [sg.Text('text2')],
]

column = sg.Column(children_layout)

layout = [
    []
]

window = sg.Window('column test', layout, size=[400, 200])

while True:
    event, values = window.Read()
    if event is None:
        break

window.Close()
exit(0)