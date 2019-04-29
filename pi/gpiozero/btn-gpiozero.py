from gpiozero import Button
from gpiozero import LED
from signal import pause

btn = Button(22)
led = LED(27)

print "press the button, this will stay until button is pressed"
btn.wait_for_press()
print("btn pushed, exiting")
exit()
