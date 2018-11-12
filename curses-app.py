#!/usr/bin/env python3
import curses
import os

window = curses.initscr()
curses.noecho()
curses.cbreak()
window.keypad(True)

window.border(3)
window.addstr(1, 1, "q: quit\n d: Show developer name")
window.refresh()

while True:
	choice = window.getch()
	if choice == 113:
		curses.endwin()
		break
	elif choice == 100:
		win1 = curses.newwin(5, 40, 7, 20)
		win1.border(0)
		win1.addstr(1, 1, "CrazyJ36")
		win1.refresh()
		win1.getch()
		break

curses.endwin()
os.system("clear")
