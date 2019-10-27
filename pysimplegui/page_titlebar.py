#!/usr/bin/env python3

import PySimpleGUIWeb as sg

layout = [
  [sg.Text('''
    Text.
    More Text(same function param).
    ''')
  ]
]

window = sg.Window(
  'Page Title',
  layout,
  web_start_browser=False,
  web_port=8086,
)

print("Ready")

while True:
  try:
    events = window.Read()

    if events is None:
      break
  except KeyboardInterrupt:
    break

window.Close()
exit(0)
