from PySimpleGUI import Window, Image
from os import curdir

icon_str = str(curdir + '/explorer_icon64.png')

layout = [
    [Image(icon_str)],
]

window = Window('Image Test', layout)

while True:
    event, values = window.Read()
    if event is None:
        break
window.Close()
