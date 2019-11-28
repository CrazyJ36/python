#!/usr/bin/env python3

# TODO: check to see if led is on, if is, don't execute on().


print('Loading... Open pi address in browser with port \':8086\'')
import PySimpleGUIWeb as Gui

from gpiozero import LED
import PySimpleGUIWeb as Gui
print('Loading... Open pi address in browser with port \':8086\'')

led = LED(18)

layout = [
    [Gui.Text('Pi LED Controller')],
    [Gui.Button('On'), Gui.Button('Off')],
    [Gui.Button('Stop')]
    # if you get TypeError: list indices must.., you forgot commas
    # in this list.
]

# Here, set web_port=int, to force pi to use one http port everytime.
# and set web_start_browser=False so that local system browser doesn't
# steal connection(or set web_multiple_instance=True),
# then you can connect to pi from mobile phone.
win = Gui.Window('Pi Remote', layout, web_port=8086,
                 web_start_browser=False,)
# If you get runtime error about max(), you forgot Window(layout).

print('Ready.')
while True:
    try:
        event, values = win.Read()

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
            print('User closed browser page. Exiting...')
            break

    except KeyboardInterrupt:  # This works from server terminal
        print("\rCtrl-C pressed in server terminal.")
        break


win.Close()
print('Done.')
exit(0)
