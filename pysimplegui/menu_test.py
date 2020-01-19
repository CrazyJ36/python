import PySimpleGUI as Gui

# list of lists with list in lists.
menu = [
    ['menu1', ['log', 'exit']],
    ['menu2', 'about']
]

# list of lists with functions in lists
layout = [
    [Gui.Menu(menu)],
    [Gui.Text("Menu Above.")]
]

window = Gui.Window('Menu Test', layout, size=[200, 100], resizable=True)

while True:
    event, values = window.Read()
    if event is None:
        break
    elif event == 'log':
        print('logged')
    elif event == 'exit':
        print('menu1 exit button clicked')
        break
    elif event == 'about':
        print('showing about dialog')
        Gui.Popup('Developer:\nCrazyJ36', button_type=0)

window.Close()
exit(0)
