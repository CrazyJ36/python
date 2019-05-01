import RPi.GPIO
print "Using python module RPi.GPIO, version: ", RPi.GPIO.VERSION
print "Your PI: ", RPi.GPIO.RPI_INFO, "Revision: ", RPi.GPIO.RPI_REVISION


RPi.GPIO.cleanup
exit()
