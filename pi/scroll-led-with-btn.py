#!/usr/bin/env python3

print("Loading gpiozero..")

from gpiozero import Button, LEDBoard
from time import sleep

# LEDs' in indexed array with gpiozero's LEDBoard
leds = LEDBoard(24, 7, 6)

# if you get GPIOPinInUse error when using btns,leds in a loop,
# you may have to close, the reinitiate buttons after any button press,
# as the btn might still be used by led. place the button declarations
# in loop, then close after find-the-press loop done. This would be slow.
btn1 = Button(23)
btn2 = Button(8)

# instructions
print("""Press button 0(first soft one, left-to-right) to alternate through LEDs'.
Press button 7(right-most clicky), or Ctrl-C to exit.""")

# how led reacts to btn press
def led_flash(led_num):
  leds[led_num].on()
  sleep(0.3)
  leds[led_num].off()


def quit():
    print("\nExiting..")
    exit(0)


# a number representation on how many times btn1 has been pushed
# to loop with led_num
btn1_press_count = 0
# loop to constantly recognize any button press
while True:
  try:
    if btn1.is_pressed:
      # reset count to 0 to repeat count loop
      if btn1_press_count == 3:
        btn1_press_count = 0
        print(btn1_press_count, flush=True, end='')  # end=empty char, dont print newline
        led_flash(btn1_press_count)
        btn1_press_count = btn1_press_count + 1
      # the same, but not at the end of leds
      else:
        print(btn1_press_count, flush=True, end='')
        led_flash(btn1_press_count)
        btn1_press_count = btn1_press_count + 1
    if btn2.is_pressed:
      quit()


  except KeyboardInterrupt:
    quit()
