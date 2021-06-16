import sys

T = int(sys.stdin.readline())
for _ in range(T):
  x, y = map(int, sys.stdin.readline().split())
  cnt = 0
  move = 1
  while x < y:
    cnt += 1
    x += move
    move += move
    # 추가 수정 필요

  print(cnt)