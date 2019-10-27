#!/usr/bin/env python3

import PySimpleGUIWeb as sg

layout = [
  [sg.Text('''
    Get this text below header bar.
    ''')
  ]
]

window = sg.Window(
  'Page Title',
  layout,
  web_start_browser=True,
  web_port=8086,
)

print("Ready")

while True:
  try:
    event, values = window.Read()
    if event is None:
      break
  except KeyboardInterrupt:
    break

window.Close()
exit(0)
