import PySimpleGUIWeb as sg

layout = [
  [sg.T('Text widget element instantiated with T() instead of Text().')]
]

window = sg.Window('Page Title',
  layout,
  web_port=8086,
  web_start_browser=False)

while True:
  evnt = window.Read()
  if event is None:
    break

window.Close()
exit(0)
