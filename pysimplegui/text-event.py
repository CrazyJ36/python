import PySimpleGUI as sg

layout = [
    # can't get clicks(if event == 'text_id'
    # on text without enable_events, therefor not values either.
    # also don't use click_submits, deprecated.
    [sg.Text('click me', key='text_id', enable_events=True)]
]

window = sg.Window('Title', layout)

while True:
    event, values = window.Read()

    if event == 'text_id':
        # 'con' + 'cat', no space.
        print('\ntext clicked!\n' + 'event=', event)
        # trying to get values from text_id raised keyerror
    if event is None:
        print('close clicked')
        break

print('done.')
window.Close()
exit(0)
