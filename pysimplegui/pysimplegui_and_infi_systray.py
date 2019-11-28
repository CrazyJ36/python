from infi.systray import SysTrayIcon
import PySimpleGUI as psg


def tray_menu1(systray):
    print('menu 1 clicked')


menu_options = (
    ("menu 1", None, tray_menu1),
)
systray = SysTrayIcon(
    None,
    "pysimplegui and infi.systray",
    menu_options,
)
systray.start()

psg_layout = [
    [psg.Text("Text")],
]
psg_window = psg.Window("psg and info.systray", psg_layout,
                        size=[300, 100],)

while True:
    event, values = psg_window.read()

    if event is None:
        systray.shutdown()
        break

psg_window.close()
exit(0)
