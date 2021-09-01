N = int(input())

coins = [500, 100, 50, 10]
res = 0
# for coin in coins:
#   while N >= coin:
#     N -= coin
#     res += 1
# print(res)

# 나눠서 몫을 구하는 것이 더 효율적!
for coin in coins:
  res += N // coin
  N %= coin
print(res)