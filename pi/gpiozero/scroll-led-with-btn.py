#!/usr/bin/env python3

print("Loading gpiozero..")

from gpiozero import Button, LEDBoard
from time import sleep

# LEDs' in indexed array with gpiozero's LEDBoard
leds = LEDBoard(15, 21, 19, 4)

# if you get GPIOPinInUse error when using btns,leds in a loop,
# you may have to close, the reinitiate buttons after any button press,
# as the btn might still be used by led. place the button declarations
# in loop, then close after find-the-press loop done. This would be slow.
btn1 = Button(14)
btn2 = Button(26)

# instructions
print("""Press right button to alternate through LEDs'.
Press left button to exit""")

# how led reacts to btn press
def led_flash(led_num):
  leds[led_num].on()
  sleep(0.3)
  leds[led_num].off()

# a number representation on how many times btn1 has been pushed
# to loop with led_num
btn1_press_count = 0

# loop to constantly recognize any button press
while True:

  if btn1.is_pressed:

    if btn1_press_count > 3:
      btn1_press_count = 0
      print(btn1_press_count, flush=True, end='') # end null, dont print newline
      led_flash(btn1_press_count)
      btn1_press_count = btn1_press_count + 1

    else:
      print(btn1_press_count, flush=True, end='')
      led_flash(btn1_press_count)
      btn1_press_count = btn1_press_count + 1

  if btn2.is_pressed:
    print("\nExiting..")
    exit(0)

