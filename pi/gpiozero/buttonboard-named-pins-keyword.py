#!/usr/bin/env python3

from gpiozero import ButtonBoard
import inspect
from time import sleep

# TheFunction(custom_name1=actual_arg, custom_name2=actual_arg)

btns=ButtonBoard(23, 27, 22)

btn_names = dict(btn1=btns[0], btn2=btns[1], btn3=btns[2])

btn_keys = list(btn_names)

print(btn_keys[0])

