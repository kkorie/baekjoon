# N = int(input())
# coins = list(map(int, input().split()))

# res = 0
# check = 0
# while True:
#   if check > 0:
#     break
#   res += 1
#   check = res
#   for coin in coins:
#     if check - coin == 0:
#       check = 0
#       break
#     elif check - coin > 0:
#       check -= coin

# print(res)

# 1 1 3 2 2 같은 경우 위의 코드X 정답
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
  if target < x:
    break
  target += x

print(target)