import PySimpleGUI as Gui

layout = [
  [ Gui.Text('Clicking any element will show event and value') ],
  [ Gui.Text('Closing window will stop this.') ],
  [ Gui.Button('Button') ],  # returns A event 0
  [ Gui.Input() ],  # Only this (input-type element) would return A value.
  [ Gui.Exit() ]  # returns an event 0.
]

window = Gui.Window('Window Title', layout)

while True:
  # read() returns A tuple with an event and A dict of values.
  # when there's an event(button, a click, list items selected),
  # read() returns every time at that time(then loop start over).
  # 'event' returns None when window is closed.
  #
  # The 'values' is A dict of values of all input-style elements.
  # Dictionaries use keys for entries, and key is made from the
  # gui elements' text if key='' is not specified.
  # These keys are ints starting at zero.
  event, values = window.read()
  print(event, values)
  if event is None:
    break

window.close()
exit(0)
