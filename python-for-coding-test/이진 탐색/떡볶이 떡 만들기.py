# N, M = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# def binary_search(array, target, start, end):
#   while start <= end:
#     mid = (start + end) // 2
#     if target == array[mid]:
#       return mid
#     elif target > array[mid]:
#       start = mid + 1
#     else:
#       end = mid - 1
#   return mid - 1

# H = data[-1]
# cutted = 0
# while cutted < M:
#   H -= 1
#   rest = binary_search(data, H, 0, N - 1)
#   cutted += len(data) - (rest + 1)
#   print(H, rest, cutted)
# print(H)

# 답
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

res = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  if total < m:
    end = mid - 1
  else:
    res = mid
    start = mid + 1
print(res)