import PySimpleGUI as psg

# For some reason, window.refresh didn't work at first.

layout = [
    [psg.Text('text one')],
    [psg.Button('press')],
    # Using A blank space to be filled later with window key update
    [psg.Text('', key='blank_space', size=[400, 20])],
]

window = psg.Window('title', layout, size=[400, 300])

extra = psg.Text('new text two')

while True:
    event, values = window.Read()
    if event == 'press':
        window['blank_space'].Update('new text two')
    if event is None:
        break
window.Close()
