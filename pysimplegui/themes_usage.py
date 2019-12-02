import PySimpleGUI as sg

# you can see list of themes in declaration,
# after 'def change_look_and_feel()' in a comment.
# themes are also defined in that file.
sg.change_look_and_feel('DarkAmber')

layout = [
    [sg.Text('DarkAmber')],
    [sg.Btn('close')]
]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()
    if event in (None, 'close'):  # check multiple parameters for event
        break

window.close()
