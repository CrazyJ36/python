import PySimpleGUIWeb as Gui

layout = [
  [Gui.Input()],
  [Gui.Text('Type above, \'q\' to quit.', key='txt')]
]

win = Gui.Window("Title", layout,
 web_start_browser=0,  # False is 0
 use_default_focus=False,
 return_keyboard_events=True,  # 1 is True
 web_port=8086)

while True:
    values = win.Read()
    if values.key == 'q':
      break
    else:
      win.FindElement('txt').Update(values)

win.Close()
exit(0)
