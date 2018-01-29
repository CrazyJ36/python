import time
def doTime():
    print(time.asctime())
loop = True
while loop:
    doTime()
    time.sleep(5)
