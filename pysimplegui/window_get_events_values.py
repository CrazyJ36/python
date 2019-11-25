import PySimpleGUI as Gui

layout = [
  [Gui.Text('Clicking buttons returns button name event.')],
  [Gui.Button('button',)],  # returns event 'button', values None

  [Gui.Text('Changing text in input causes event when window(return_keyboard_events=True)')],

  # Use Window(return_keyboard_events=True) normally for Input().
  # Input(key='input_id') to return input_id reference in values(key:value) on event.
  # Returns char entered as event, and as value in values{dict} dict object
  [Gui.Input(key='input_id')]
]

# Using return_keyboard_events=True causes the window.read() to return events
# even when text is simply entered into input(). No other events required.
window = Gui.Window('Get events and values',
                    layout,
                    return_keyboard_events=True,
                    )

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
  print("\nEvents: ", event, "\nValues: ", values)
  if event is None:
    break

window.close()
exit(0)
