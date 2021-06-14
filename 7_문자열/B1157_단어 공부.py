S = input().upper()

sdict = {}
for i in S:
  if i not in sdict:
    sdict[i] = 1
  else:
    sdict[i] += 1

sdict_max = 0
ans = ''
for k, v in sdict.items():
  if v > sdict_max:
    sdict_max = v
    ans = k
  elif v == sdict_max:
    ans = '?'

print(ans)