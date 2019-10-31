#!/usr/bin/env python

import time


def doTime():
    print(time.asctime())


loop = True
while loop:
    doTime()
    time.sleep(1)  # sleep is from time module as well.
