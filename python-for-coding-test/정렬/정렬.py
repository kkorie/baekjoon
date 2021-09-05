# 선택 정렬
# data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def selection(data):
  for i in range(len(data)):
    min_index = i
    for j in range(i+1, len(data)):
      if data[min_index] > data[j]:
        min_index = j
    data[i], data[min_index] = data[min_index], data[i]
  return data
# print(selection(data))

# 삽입 정렬
def insertion(data):
  for i in range(1, len(data)):
    for j in range(i, 0, -1):
      if data[j] < data[j-1]:
        data[j], data[j-1] = data[j-1], data[j]
      else:
        break
  return data
# print(insertion(data))

# 퀵 정렬
def quick(data):
  if len(data) <= 1:
    return data
  pivot = data[0]
  tail = data[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick(left_side) + [pivot] + quick(right_side)
# print(quick(data))

# 계수 정렬
data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
check = [0] * (max(data) + 1)

for i in data:
  check[i] += 1
for i in range(len(check)):
  for _ in range(check[i]):
    print(i, end=' ')