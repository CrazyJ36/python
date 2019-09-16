from gpiozero import LED

led1 = LED(24)
led2 = LED(7)

x = 1
while(x < 5):
  led1.on()
  sleep(0.5)
  led1.off()
  led2.on()
  sleep(0.5)
  led2.off()
  x = x + 1

exit()
