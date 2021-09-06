N = int(input())
data = []
for i in range(N):
  input_data = input().split()
  data.append((input_data[0], int(input_data[1])))
res = sorted(data, key=lambda data: data[1])
for i in res:
  print(i[0], end=' ')