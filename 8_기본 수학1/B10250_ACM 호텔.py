import sys
T = int(sys.stdin.readline())

for _ in range(T):
  H, W, N = map(int, sys.stdin.readline().split())
  if N < H:
    ans = N*100 + 1
  elif N%H == 0:
    ans = H*100 + (N//H)
  else:
    ans = (N%H)*100 + (N//H) + 1
  print(ans)

  # if N <= H:
  #   ans = N*100 + 1
  # elif N > H and N%H == 0:
  #   (N/H)*100 + (N/H)
  # else:
  #   ans = (N%H)*100 + (N//H) + 1
  # print(ans)