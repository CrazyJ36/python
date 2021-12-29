#!/usr/bin/env python

from gpiozero import ButtonBoard
from time import sleep

# theFunction(custom_name1=actual_arg, custom_name2=actual_arg)

btns = ButtonBoard(17, 25, 24, 16)

btn_names = dict(btn1=btns[0], btn2=btns[1], btn3=btns[2], btn4=btns[3])

print(list(btn_names))
