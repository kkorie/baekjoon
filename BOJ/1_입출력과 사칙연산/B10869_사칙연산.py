def my_func(a, b):
  a, b = int(a), int(b)
  print(a+b)
  print(a-b)
  print(a*b)
  print(a//b)
  print(a%b)

a, b = input().split()
my_func(a, b)