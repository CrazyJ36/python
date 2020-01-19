import PySimpleGUI as sg

children_layout = [
    [sg.Text('text1')],
    [sg.Text('text2')],
    [sg.Text('text3')],
    [sg.Text('text4')],
    [sg.Text('text5')],
    [sg.Text('text6')],
    [sg.Text('text7')],
    [sg.Text('text8')],
    [sg.Text('text9')],
    [sg.Text('text10')],
    [sg.Text('text11')],
    [sg.Text('text12')],
]

layout = [
    [sg.Column(layout=children_layout, size=(300, 100), scrollable=True)]
]

window = sg.Window('column test', layout, size=[400, 200])

while True:
    event, values = window.Read()
    if event is None:
        break

window.Close()
exit(0)
