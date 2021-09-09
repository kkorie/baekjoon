S = input()
res = int(S[0])
for i in S[1:]:
  i = int(i)
  if i <= 1 or res <= 1:
    res += i
  else:
    res *= i

print(res)