import random
while(1):
  a = random.randint(1,20)
  b = random.randint(1,10)
  print(a," X ",b," = ",end = " ")
  c = int(input())
  if a*b == c:
    print("OK")
  else:
    print("You are wrong!!")
