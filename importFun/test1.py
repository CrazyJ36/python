def someFunc():
 print("other function from test1, someFunc")

def test1Func():
 print("test1 Function. Printing from test1")
 if __name__ == '__main__':
  test1Func()
  someFunc()
