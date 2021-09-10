S = input()

S = sorted(S)
char = ''
num = 0
for i in S:
  if i.isdigit():
    num += int(i)
  else:
    char += i

if num != 0:
  res = char + str(num)
else:
  res = char

print(res)