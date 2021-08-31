M, N = map(int, input().split())

num = []
for i in range(M, N+1):
  temp = 0
  if i > 1:
    for j in range(2, i):
      if i%j == 0:
        temp += 1
        break
    if temp == 0:
      num.append(i)

for n in num:
  print(n)

# 시간 초과!