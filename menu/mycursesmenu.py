from cursesmenu import *
from cursesmenu.items import *

menu = CursesMenu("Do Stuff", "Useful")
menu_item = MenuItem("Menu Item")
function_item = FunctionItem("python function", "print", "1+2")
command_item = CommandItem("print hi", "ps")
selection_menu = SelectionMenu(["item1", "item2", "item3"])
submenu_item = SubmenuItem("Submenu item", selection_menu)
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)
menu.show()
menu.join()
