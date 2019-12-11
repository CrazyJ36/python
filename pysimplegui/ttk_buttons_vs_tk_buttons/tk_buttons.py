import PySimpleGUI as psg

layout = [
    [psg.Txt('tk_button')],
    [psg.Button('push')]
]

window = psg.Window('tk button', layout,
                    use_ttk_buttons=False, size=[300, 100])

while True:
    event, values = window.Read()
    if event == 'push':
        print('button pushed')
    if event is None:
        break

window.Close()
