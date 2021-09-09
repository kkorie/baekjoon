N = int(input())
data = list(map(int, input().split()))

# data.sort(reverse=True)
# res = 0
# check = 0
# while check < N:
#   res += 1
#   max_value = data[check]
#   check += max_value
# print(res)

# 모든 모험가를 그룹으로 만들 필요X 정답
data.sort()
res = 0
check = 0
for i in data:
  check += 1
  if check >= data:
    res += 1
    check = 0

print(res)