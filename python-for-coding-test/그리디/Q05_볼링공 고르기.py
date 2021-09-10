N, M = map(int, input().split())
data = list(map(int, input().split()))

res = 0
for i in range(N - 1):
  for j in range(i + 1, N):
    if data[i] != data[j]:
      res += 1

print(res)