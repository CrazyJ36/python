import PySimpleGUIWeb as sg

layout = [
  [sg.Txt('Welcome')],  # A page header. pysimpleguiweb/remi expect this at top.
                       # If no header text was here, any text would be placed oddly.
  [sg.T('Text widget element instantiated with T() instead of Text().')]
]

window = sg.Window('Page Title',
  layout,
  web_port=8086,
  web_start_browser=False)

while True:
 # try:
    event, values = window.Read()
    if event is None:
      break
  #except KeyboardInterrupt:
   # break
window.Close()
exit(0)
