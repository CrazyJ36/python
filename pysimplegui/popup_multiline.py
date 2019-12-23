#!/usr/bin/env python
import PySimpleGUI as sg

# This example would work great as A desktop
# double-click executable in windows. Just
# create shortcut(send-to Desktop) this file,
# and run it using pythonw.exe(no prompt) instead
# of python.exe(or open-with).
# Change default in files properties.

# Two arguments are two rows(Works as paragraphs with '\n').
# Should apply for other elements.
sg.Popup('One 1', 'Two\nTwo.One')

exit(0)
