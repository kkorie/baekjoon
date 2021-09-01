N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

res = 0
res = (first * K + second) * (M // (K+1)) + (first * (M % (K+1)))
print(res)