from infi.systray import SysTrayIcon
import PySimpleGUI as psg


def tray_menu(systray):
    print('clicked')


menu_options = (
    ("menu", None, tray_menu),
)
systray = SysTrayIcon(
    None,
    "pysimplegui and infi.systray",
    menu_options,
)

psg_layout = [
    [psg.Text("Close this window, system tray icon will close.")],
]
psg_window = psg.Window("psg and systray", psg_layout,
                        size=[500, 100],)

systray.start()
while True:
    event, values = psg_window.read()

    if event is None:
        systray.shutdown()
        break

psg_window.close()
exit(0)
