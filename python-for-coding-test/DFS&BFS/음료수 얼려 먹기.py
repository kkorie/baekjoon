N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y):
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  if data[x][y] == 0:
    data[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False
    

res = 0
for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      res += 1
print(res)