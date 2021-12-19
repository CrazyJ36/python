
#!/usr/bin/env python3

print("Loading")

from gpiozero import ButtonBoard, Button
from time import sleep

btns = ButtonBoard(btn1=22, btn2=24, btn3=25, btn4=5)

print("""
Press any button, will print list of all button device values.
Would show device_0=1 if not named in ButtonBoard declaration
""")
while True:
    try:
      btns.wait_for_press()
      print(btns.value)
      sleep(0.3)

    except KeyboardInterrupt:
      print("\rExiting... TODO: print only keyword name")
      btns.close() #  close each board button
      exit(0)

