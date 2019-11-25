import PySimpleGUI as Gui

window = Gui.Window('window', [


    # to use only title for event trigger, don't specify key.
    # use multiple element in same list to lay them out in one window row.
    [Gui.Btn('btn1_name'), Gui.Button('btn2_name', key='btn2_key')]

])

detected_event_str = 'last detected event:'
while True:
    event, values = window.Read()

    # these event show how you can use either text title or key
    if event == 'btn1_name':
        print(detected_event_str, event)

    elif event == 'btn2_key':
        print(detected_event_str, event)

    elif event is None:
        print(detected_event_str, event)
        break

window.Close()
exit(0)
