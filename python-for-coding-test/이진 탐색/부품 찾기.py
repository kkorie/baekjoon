# N = int(input())
# data = list(map(int, input().split()))
# M = int(input())
# order_data = list(map(int, input().split()))

# for order in order_data:
#   for i in range(N):
#     if data[i] == order:
#       print('yes', end=' ')
#       break
#     elif i == N-1 and data[i] != order:
#       print('no', end=' ')

# 이진 탐색
# N = int(input())
# data = sorted(list(map(int, input().split())), reverse=True)
# M = int(input())
# order_data = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#   while start <= end:
#     mid = (start + end) // 2
#     if array[mid] == target:
#       return mid
#     elif array[mid] < target:
#       end = mid - 1
#     else:
#       start = mid + 1
#   return None

# for i in order_data:
#   res = binary_search(data, i, 0, N - 1)
#   if res != None:
#     print('yes', end=' ')
#   else:
#     print('no', end=' ')

# 계수 정렬
# N = int(input())
# check = [0] * 1000001
# data = list(map(int, input().split()))
# M = int(input())
# order_data = list(map(int, input().split()))

# for i in data:
#   check[i] += 1

# for j in order_data:
#   if check[j] == 1:
#     print('yes', end=' ')
#   else:
#     print('no', end=' ')

# 집합
N = int(input())
data = set(map(int, input().split()))
M = int(input())
order_data = list(map(int, input().split()))

for i in order_data:
  if i in data:
    print('yes', end=' ')
  else:
    print('no', end=' ')