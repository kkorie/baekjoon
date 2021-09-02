N, M = map(int, input().split())
x, y, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

res = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

check = 0
while True:
  if data[x][y] == 0:
    data[x][y] = 2
    res += 1
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]
  if data[nx][ny] == 1 or data[nx][ny] == 2:
    check += 1
    if check == 4:
      check = 0
      nx = x - dx[d]
      ny = y - dy[d]
      if data[nx][ny] == 2:
        x, y = nx, ny
      else:
        break
    continue
  x, y = nx, ny
  check = 0
print(res)
print(data)

# 더 생각해보기!
# x, y가 변하거나(움직이면) check가 4인 경우 check를 다시 0으로 바꿔야 한다.