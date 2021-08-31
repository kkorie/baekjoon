import sys

N = int(sys.stdin.readline())
for _ in range(N):
  oxlist = sys.stdin.readline()
  cnts = []
  cnt = 0
  for ox in oxlist:
    if ox == "O":
      cnt += 1
      cnts.append(cnt)
    else:
      cnt = 0
  print(sum(cnts))