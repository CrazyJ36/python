#!/usr/bin/env python3
import PySimpleGUIWeb as Gui

win = Gui.Window('Dbg', [[ ]])
while True:
  event, values = win.Read()
  show_debugger_window(0, 0)
  if event is None:
    break

win.close()
exit()
