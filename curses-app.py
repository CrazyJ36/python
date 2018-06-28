#!/usr/bin/env python3
import curses

window = curses.initscr()
curses.noecho()
curses.cbreak()
window.keypad(True)
window.border(3)
help = "q: quit\n d: Show developer name"
window.addstr(1, 1, help)
window.refresh()

win1 = curses.newwin(5, 40, 7, 20)
win1.border(0)
win1.addstr(1, 1, "CrazyJ36")

loop = True
while loop:
  choice = window.getch()
  if choice == 113:
    loop = False
    curses.endwin()
  elif choice == 100:
    win1.refresh()
