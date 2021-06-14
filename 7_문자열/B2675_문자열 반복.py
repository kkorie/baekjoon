import sys

T = int(sys.stdin.readline())
for _ in range(T):
  R, S = sys.stdin.readline().split()
  P = ''
  for s in S:
    P += s*int(R)
  print(P)