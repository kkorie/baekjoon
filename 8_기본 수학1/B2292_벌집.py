N = int(input())

cnt = 1
temp = 1
if N == 1:
  print(cnt)
else:
  while temp < N:
    temp += 6*cnt
    cnt += 1
  print(cnt)