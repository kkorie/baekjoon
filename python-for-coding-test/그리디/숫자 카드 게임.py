N, M = map(int, input().split())
# data = []
# for _ in range(N):
#   data.append(list(map(int, input().split())))

# res = 0
# for i in data:
#   m = min(i)
#   if m > res:
#     res = m
# print(res)

# 행 순서대로 가장 작은 수를 찾고 다음 행과 비교하면 되기 때문에 데이터를 저장할 필요x, 큰 수를 찾을 때 max 사용 가능
res = 0
for _ in range(N):
  data = list(map(int, input().split()))
  min_value = min(data)
  res = max(res, min_value)
print(res)