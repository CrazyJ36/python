#!/usr/bin/env python
import PySimpleGUI as sg

# Usage of Graph element.

layout = [
    [sg.Button('Move')],

    # Graph with 10x10 pixel points.
    [sg.Graph(canvas_size=(100, 100),  # screen size

              graph_bottom_left=(0, 0),  # base points
              graph_top_right=(100, 100),

              background_color='light grey',
              key='graph')],

]

# before adding additional graphics with graph,
# state 'finalize=True' in window.
window = sg.Window('Graph test', layout, size=[150, 150], finalize=True)

graph = window['graph']

# points mean the points based on graph canvas size as 'screen'
rectangle = graph.draw_rectangle(top_left=(1, 1), bottom_right=(5, 5))

while True:
    event, values = window.read()
    if event is None:
        break

    elif event == 'Move':
        # move to position on x,y of canvas size
        graph.RelocateFigure(rectangle, x=90, y=95)

window.close()
