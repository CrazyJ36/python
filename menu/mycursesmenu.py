from cursesmenu import *
from cursesmenu.items import *

title = 'Title'
menu = CursesMenu(title)

function_item = FunctionItem("python method",
 input, ["type input"])


command_item = CommandItem("console command", "touch file.txt")

menu.append_item(function_item)
menu.append_item(command_item)
menu.show()
