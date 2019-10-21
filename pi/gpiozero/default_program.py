# 'default_program' means this my constantly running program
# that starts on boot. As an attempt to use attached hardware
# on Raspberry PI with purpose
# This is set to run on boot at:
# /etc/rc.local

import mylib
from time import sleep
from subprocess import run

def exitFunc():
  exit(0)

def flash():
  x = 0
  while x < 5:
    mylib.led2.on()
    sleep(0.1)
    mylib.led2.off()
    sleep(0.1)
    x = x + 1
  return

def rebootFunc():
  flash()
  flash()
  flash()
  run( ['sudo', 'reboot', 'now'] )
  return

#def testPrint():
#  run( ["printf" , "btn 2, printing\n"] )

# main loop
while True:
  if mylib.btn1.is_pressed:
    flash()
  #if mylib.btn2.is_pressed:
  #  testPrint()
  #if mylib.btn3.is_pressed:
  #if mylib.btn4.is_pressed:
  if mylib.btn6.is_pressed:
    exitFunc()
  if mylib.btn7.is_pressed:
    rebootFunc()
  sleep(0.2)
