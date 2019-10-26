import PySimpleGUI as Gui

layout = [
    [Gui.Button('Button')],

    # text can be cut off if size is not wide enough.
    [Gui.Text("Default Gui.Text(\'str\')", key='text_element_key', size=[350, 50])]
]

window = Gui.Window(
    'Title',
    layout,

    # increase window size for usability (width, height tuple)
    size=[400, 200]
)

while True:
    event, values = window.read()

    # sets new text in text field on button click
    if event == 'Button':
        window['text_element_key'].Update(
            "New string of text using:\nwindow[\'text_element_key\'].Update(\'new string\')."
        )

    if event is None:
        break

window.close()
exit(0)
