N, M, K, X = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]

distance = [0] * (N + 1)
visited = [False] * (N + 1)

# def resolve
