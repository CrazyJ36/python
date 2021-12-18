#!/usr/bin/env python3
import mylib
from time import sleep

# import mylib (line 2), assign A variable from that file to use here
led2 = mylib.led2

led2.on()
sleep(1)
led2.off()
led2.close()
del led2
exit(0)
