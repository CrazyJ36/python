import PySimpleGUI as Gui

Gui.TimerStart()

print('running A timed count to 100')

for i in range(101):
    print(i)

print('After loading python and A module, counting to 100 took:')

Gui.TimerStop()