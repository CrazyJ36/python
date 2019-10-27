import PySimpleGUI as Gui

# layout is type(class 'list') made up of lists
layout = [
    [Gui.Text('Text typed below will be shown here.', key='out')],
    [Gui.InputText('Type here... will clear once.', key='in', enable_events=True)],
    [Gui.Button('Button')]
]

window = Gui.Window('title', layout, size=[500, 100], return_keyboard_events=True)

is_input_clear = False
in_list = []

while True:
    event, values = window.Read()

    if event == 'Button':
        # update the "'text' of 'key' 'out'"
        # with window.read()s' returned 'values'
        # "'key' 'in'.
        window['out'].Update(values['in'])

        in_list.append(values['in'])

    elif event == 'in':
        #  do this only once, using counter, to clear input field.
        if not is_input_clear:
            window['in'].Update('')
            is_input_clear = True

    elif event is None:
        print('window closed')
        break

window.close()
print("\nItems entered are saved to:", str(type(in_list)), "in_list[]" + ":\n", in_list, "\n")
exit(0)
