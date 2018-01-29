n = ['a','b','c','d','e','f','g']
def intervalsMenu():
 print("--",rt,"---Intervals-----")
 print("1 Choose A Root note first")
 print("2 Minor Second")
 print("3 Major Second")
 print("-----Intervals-----")
 intCh = input("Choose root then find intervals")
 if intCh == "1":
  print(rt)

def swOrder():
 n1o = [1,2,3,4,5,6,0]
 n1 = [n[i] for i in n1o]
 print(n0)
 print(n1)

def intervalsPkRt():
 pkRoot = input("Choose root note: ")
 if pkRoot == "a":
  root = n[0]
 if pkRoot == "b":
  root = n[1]
 return root
rt = intervalsPkRt()

def nav():
 print("Welcome to the music reference app!\n")
 appFun = input("Type musical funtion for info.\neg. 'intervals', 'chords', 'scales': ")
 if appFun == "intervals":
  intervalsMenu()
 elif appFun == "chords":
  print("finish chords")
 elif appFun == "scales":
  print("finish scales, take from TinyScales App")
nav()
