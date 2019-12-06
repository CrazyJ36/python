import PySimpleGUI as sg

# make items list in code
items_list = []
i = 0
while i < 9:
    if i == 0:
        i = i + 1
    else:
        num_text = 'text' + str(i)
        items_list.append([sg.Text(num_text, click_submits=True)])
        i = i + 1

# now that items are made with text, delete unused variable
del num_text

layout = [
    [sg.Column(layout=items_list, size=(300, 100), scrollable=True)],
    [sg.Text('click an item above, the chosen will show here', size=[20, 100], key='result')]
]

window = sg.Window('column test', layout, size=[400, 200])

while True:
    event, values = window.Read()

    if event == 'text1':
        print('text1 clicked')
        window['result'].update('text1 clicked')
    if event == 'text2':
        print('text2 clicked')
        window['result'].update('text2 clicked')
    if event == 'text3':
        print('text3 clicked')
        window['result'].update('text3 clicked')
    if event == 'text4':
        print('text4 clicked')
        window['result'].update('text4 clicked')
    if event == 'text5':
        print('text5 clicked')
        window['result'].update('text5 clicked')
    if event == 'text6':
        print('text6 clicked')
        window['result'].update('text6 clicked')
    if event == 'text7':
        print('text7 clicked')
        window['result'].update('text7 clicked')
    if event == 'text8':
        print('text8 clicked')
        window['result'].update('text8 clicked')

    if event is None:
        break

window.Close()
exit(0)
