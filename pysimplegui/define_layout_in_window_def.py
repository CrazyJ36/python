import PySimpleGUI as psg

# To define the layout inside the window definition for shorter code,
# you would use the same list-of-lists brackets as: '[[elements]]'
window = psg.Window('Title', [[psg.Text('String')]])

while True:
    event, values = window.Read()
    if event is None:
        break
window.Close()
