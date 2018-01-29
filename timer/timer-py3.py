def timer():
 import time
 if __name__ == '__main__':
  num=1
  while (num<=10):
   print(num)
   time.sleep(1)
   num = num + 1
   if num==5:
    print("half")
timer()
print("Reached 10 Seconds End")

