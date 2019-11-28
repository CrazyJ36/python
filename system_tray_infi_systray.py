from infi.systray import SysTrayIcon


def menu_action1(systray):
    print("menu 1 clicked.")


def menu_action2(systray):
    print("menu 2 clicked")


def sub_action1(systray):
    print("sub 1 clicked")


def sub_action2(systray):
    print("sub 2 clicked")


def info_default_option(systray):
    print("CrazyJ36s' System Tray. Using infi.systray.")


def on_quit_callback(systray):
    print("quit clicked")


# Tuple of clickable menu items for system tray icon.
# All 'None' here are in place of icons for specific menu items.
menu_options = (
    ("menu option 1", "windows_icon.ico", menu_action1),
    ("menu option 2", None, menu_action2),
    ("sub-menu", None, (
        ('1', None, sub_action1),
        ('2', None, sub_action2),
        )
     ),
    ("about", None, info_default_option),
)

systray = SysTrayIcon(
    "windows_icon.ico",
    "system tray - infi.systray",
    menu_options,
    on_quit=on_quit_callback,
    default_menu_index=4,
)

# A default quit option is in the system tray icons' menu
systray.start()

# systray.shutdown() can close program from code.
