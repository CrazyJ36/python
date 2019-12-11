import PySimpleGUI as psg

layout = [
    [psg.Txt('ttk_button')],
    [psg.Button('push')]
]

window = psg.Window('ttk button', layout,
                    use_ttk_buttons=True, size=[300, 100])

while True:
    event, values = window.Read()
    if event == 'push':
        print('button pushed')
    if event is None:
        break

window.Close()
