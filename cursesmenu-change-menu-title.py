#!/usr/bin/env python3

from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
dtitle = "default title"
menu = CursesMenu(dtitle)
def myFunc():
    menu.title = "there's a new title"
# myFunc, the'()' were not allowed here, got TypeError str
function_item = FunctionItem("change title", myFunc)
menu.append_item(function_item)
menu.show()

