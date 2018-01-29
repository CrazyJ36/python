import curses
scr = curses.initscr()
scr.border(0)
scr.addstr(1,25,"Hi TJ")
scr.refresh()
scr.getch()
curses.endwin()
