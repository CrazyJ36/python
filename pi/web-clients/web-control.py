import PySimpleGUIWeb as Gui
from gpiozero import LED

led = LED(18)

layout = [
  [ Gui.Text('Pi LED Controller') ],
  [ Gui.Button('On') , Gui.Button('Off') ]
]

# If you get runtime error about max(), you forgot Window(layout).
win = Gui.Window('Pi Remote', layout)

while True:
  event, values = win.Read()

  if event == 'On':
    led.on()
  elif event == 'Off':
    led.off()
  elif event is None:
    break

win.Close()
exit(0)
