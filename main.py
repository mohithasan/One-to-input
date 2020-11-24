import time

i = int(input("Input Your Number Here."))

num = 1

def timer(a):
  while num < a:
    print (num)
    num = num + 1
    time.sleep(0.5)

timer(i)
