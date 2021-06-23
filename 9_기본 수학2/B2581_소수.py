M = int(input())
N = int(input())

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

if len(num) > 0:
  print(sum(num), num[0], sep="\n")
else:
  print(-1)