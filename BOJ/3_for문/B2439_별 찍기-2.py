import sys

t = int(sys.stdin.readline())

for i in range(t):
  print(' '*(t-i-1) + '*'*(i+1))