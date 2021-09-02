N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

res = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]

def bfs(x, y):
  
