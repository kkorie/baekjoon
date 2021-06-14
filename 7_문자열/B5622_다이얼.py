number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

phone = input()
min_time = 0
for i in phone:
  for j in number:
    if i in j:
      min_time += 3 + number.index(j)
print(min_time)