import PySimpleGUI as Gui

menu = [
    ['Menu', ['Exit']]
]

layout = [
    [Gui.Menu(menu)],
    [Gui.Text('Use the top Menu, or Windows\' Close Button to Exit.')]
]

window = Gui.Window('Menu Exit', layout, keep_on_top=True)

while True:
    event, values = window.Read()
    if event == 'Exit':
        print('Menu Exit')
        break
    elif event is None:
        print('Close button Exit')
        break

window.Close()
exit(0)
