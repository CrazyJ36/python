import PySimpleGUI as gui

layout = [ [gui.Text("Hello")], [gui.Text('World')] ]

window = gui.Window('title', layout)

# while loop that reads window events(clicks..), and values(input text..)
# Window doesn't show without read() being called.
while True:
  # Don't use try/except KeyboardInterrupt, ctrl-c does nothing when window open.
  event, values = window.read()
  if event:  # If no event left (as if user closed the window.)
    break
    print("Closed")
  
window.close()