#!/usr/bin/env python3
import curses
window = curses.initscr() # start an ncurses screen

curses.noecho()
curses.cbreak()
window.keypad(True)

window.border(0)  # makes a visible border like a window on screen
window.addstr(1, 1, "Hello!")
window.refresh()

loop = True
while loop:
  choice = window.getch()
  if choice == 113:
    loop = False
    curses.endwin()
