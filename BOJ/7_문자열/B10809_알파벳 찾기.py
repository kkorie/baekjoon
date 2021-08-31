import string
alphabet = string.ascii_lowercase

S = input()
ans = []
for i, v in enumerate(alphabet):
  if v in S:
    ans.append(S.find(v))
  else:
    ans.append(-1)
for a in ans:
  print(a, end=' ')