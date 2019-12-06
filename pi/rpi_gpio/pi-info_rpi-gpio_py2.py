#!/usr/bin/env python3
import RPi.GPIO

print("Using python module RPi.GPIO, version:\n", RPi.GPIO.VERSION, "\n")
print("Your PI:\n", RPi.GPIO.RPI_INFO, "Revision: ", RPi.GPIO.RPI_REVISION)

RPi.GPIO.cleanup
exit()
