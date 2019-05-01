# Import RPi.GPIO code into this program. RPi.GPIO came installed by default
# with Raspbian Lite, and is faster than gpiozero in getting output to hardware,
# and is easy to code with. 
import RPi.GPIO as GPIO
from time import sleep # import time functions to put a timed wait on this process

# int number reference variable to be used as bcm pin number
# '27' is Pin according to GPIO and BCM. 'Position' 13 physically on board. File is named this way.
pin = 27

# GPIO is as imported above, a reference to RPi.GPIO
GPIO.setmode(GPIO.BCM) # set the GPIO module working mode to the Broadcom pin # system
GPIO.setup(pin, GPIO.OUT) # set operations for pin (27) to be output

GPIO.output(pin, GPIO.HIGH) # output power to pin as high(meaning full, or on)
sleep(1) # put this programs process to sleep for one second
GPIO.output(pin, GPIO.LOW) # output power to pin as low(off)

GPIO.cleanup()
exit() # exit after one flash of led as this was A test program.

