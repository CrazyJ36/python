import PySimpleGUI as psg

# some tk colors
tk_colors = ('snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
             'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
             'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
             'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
             'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
             )

# with colors defined, make list of psg.Txt fields, each using tk_color in loop
layout = []
i = 0
while i < len(tk_colors):
    layout.append([psg.Txt(str(tk_colors[i]), background_color=tk_colors[i])])
    i = i + 1

window = psg.Window('Tk Colors', layout)

while True:
    event, values = window.Read()
    if event is None:
        break

window.close()
exit(0)
