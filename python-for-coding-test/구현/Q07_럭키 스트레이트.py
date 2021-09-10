N = input()

mid = len(N) // 2
left = 0
right = 0

for i in N[:mid]:
  left += int(i)
for j in N[mid:]:
  right += int(j)

if left == right:
  print('LUCKY')
else:
  print('READY')