import PySimpleGUI as Gui

layout = [[Gui.Text('Try pressing ctrl-c')]]

# in Window definition, return_keyboard_events to get ctrl-c while window is in focus.
win = Gui.Window("Test CTRL-C",
                 layout,
                 return_keyboard_events=True)

while True:
    try:
        event, values = win.read()
        if event == 'Control_L:17' and 'c':  # ctrl-c in focused window
            print("Ctrl-C pressed on GUI Window.")
            break
        elif event is None:
            break
    except KeyboardInterrupt:  # must activate(click) window after ctrl-c in terminal :<(
        print('Ctrl-C pressed in terminal.')
        break

win.Close()
exit(0)
