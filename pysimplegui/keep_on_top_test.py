import PySimpleGUI as psg

layout = [
    [psg.Text('This this window will stay focused above other OS windows.')]
]
window = psg.Window('Title', layout,
                    keep_on_top=True)
while True:
    event, values = window.Read()
    if event is None:
        break
window.Close()
