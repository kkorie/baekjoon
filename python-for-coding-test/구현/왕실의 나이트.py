start = input()
x = ord(start[0]) - 96
y = start[1]

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
res = 0

for i in range(len(dx)):
  nx = x + dx[i]
  ny = int(y) + dy[i]
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  else:
    res += 1
print(res)