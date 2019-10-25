print('Loading... Open pi address in browser with port \':8086\'')
import PySimpleGUIWeb as Gui
from gpiozero import LED
import sys

led = LED(18)

layout = [
  [Gui.Text('Pi LED Controller')],
  [Gui.Button('On'), Gui.Button('Off')],
  [Gui.Button('Stop')]
  # if you get TypeError: list indices must.., you forgot commas in this list.
]

# Here, set web_port=int, to force pi to use one port everytime. HELPS.
# and set web_start_browser=False so that local system browser doesn't
# steal connection, then you can connect to pi from mobile phone everytime.
win = Gui.Window('Pi Remote', layout, web_port=8086, web_start_browser=False,)
# If you get runtime error about max(), you forgot Window(layout).

print('Ready. Press stop in web app or press CTRL-C')
while True:
  event, values = win.Read()

  try:
    if event == 'On':
      led.on()
      print('LED On signal')
    elif event == 'Off':
      led.off()
      print('LED Off signal')
    elif event == 'Stop':
      print('Stop Button pushed. Exiting...')
      break
    elif event is None:  # browser page closed
      print('User closed browser page. I can probably stop this example. Exiting..')
      break

  except (KeyboardInterrupt, SystemExit):  # Multiple exceptions must be in perenthesis as to catch one thing
    win.CloseNonBlocking()
    break

win.Close()
print('done')
sys.exit(0)
