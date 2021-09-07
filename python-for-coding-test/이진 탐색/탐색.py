# 순차 탐색
# def sequential_search(n, target, array):
#   for i in range(n):
#     if array[i] == target:
#       return i+1

# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]
# array = input().split()
# print(sequential_search(n, target, array))

# 이진 탐색 : 반으로 쪼개면서 탐색하기
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
res = binary_search(array, target, 0, n-1)
print(res + 1)
