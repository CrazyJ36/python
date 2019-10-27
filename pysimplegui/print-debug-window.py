import PySimpleGUI as Gui

# Opens A dubug window to use(It's like the 'stdout' of PySimpleGUI)
# Using do_not_reroute_stdout=False will force regular python print() statements
# to be printed to this window.

# It's also called EasyPrint or eprint. or easy_print().

# Don't instantiate the Print() window as A variable. There is only one
# of these and the window generated by Print() is reused each time
# EasyPrint() is called

Gui.Print('This is A debug window. Output logs can be sent here.')


# need one main-looped window or the debug window will
# close after Print().
window = Gui.Window('window', [
    # use multiple element in same list to lay them out in one window row.
    [Gui.Btn('log'), Gui.Button('close logs', key='btn')]
    ])

while True:
    event, values = window.Read()

    if event == 'log':
        Gui.Print('log button pushed')

    elif event == 'btn':
        #  Gui.PrintClose() # DOESN'T WORK
        pass

    elif event is None:
        print('close button pushed.')
        break

window.Close()
exit(0)
