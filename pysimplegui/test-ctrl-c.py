import PySimpleGUI as Gui
layout = [[Gui.Text('Try pressing ctrl-c', key='text')]]

# in Window definition, return_keyboard_events to get ctrl-c while window is in focus.
win = Gui.Window("Test CTRL-C", layout, return_keyboard_events=True, use_default_focus=False)

while True:
    try:
        event, values = win.read()
        if event == 'Control_L:17' and 'c':
            print("Ctrl-C pressed on GUI Window.")
            break
        elif event is None:
            break
    except KeyboardInterrupt:
        print("Ctrl-C pressed in terminal.")
        win.Element('text').set_focus(True)
        win.Close()
        exit(0)

win.Close()
exit(0)
