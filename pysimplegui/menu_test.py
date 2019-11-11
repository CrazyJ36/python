import PySimpleGUI as Gui

# list of lists with list in lists.
menu = [
    ['menu1', ['item1', 'item2']], 
    ['menu2', 'item1']
]

# list of lists with functions in lists
layout = [
    [Gui.Menu(menu)],
    [Gui.Text("Menu Above.")]
]

window = Gui.Window('Menu Test', layout, size=[200, 100])

while True:
    event, values = window.Read()
    if event is None:
        break

window.Close()
exit(0)
