#!/usr/bin/env python3
import curses
window = curses.initscr() # start an ncurses screen
window.border(0)  # makes a visible border like a window on screen
window.addstr(1,25,"Hi TJ")
window.refresh()
window.getch()
curses.endwin()
