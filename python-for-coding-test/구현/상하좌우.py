N = int(input())
A = input().split()

# x, y = 1, 1
# for i in A:
#   if i == 'L' and y > 1:
#     y -= 1
#   elif i == 'R' and y < N:
#     y += 1
#   elif i == 'U' and x > 1:
#     x -= 1
#   elif i == 'D' and x < N:
#     x += 1
# print(x, y)

# 다른 풀이 방법
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for i in A:
  for j in range(len(move_types)):
    if i == move_types[j]:
      nx = x + dx[j]
      ny = y + dy[j]
  if nx < 1 or nx > N or ny < 1 or ny > N:
    continue
  x, y = nx, ny
print(x, y)