N = int(input())
data = []
for _ in range(N):
  data.append(int(input()))

res = sorted(data, reverse=True)
for i in res:
  print(i, end=' ')