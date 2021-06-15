import math
A, B, V = map(int, input().split())

x = (V-A)/(A-B)+1
print(math.ceil(x))