import PySimpleGUI as Gui

menu = [
    ['menu', ['exit']]
]

layout = [
    [Gui.Menu(menu)],
    [Gui.Text('Use the Windows Menu or Close Button to Exit.')]
]

window = Gui.Window('Menu Exit', layout, keep_on_top=True)

while True:
    event, values = window.Read()
    if event == 'exit':
        print('menu exit')
        break
    elif event is None:
        print('close button exit')
        break
    
window.Close()
exit(0)
