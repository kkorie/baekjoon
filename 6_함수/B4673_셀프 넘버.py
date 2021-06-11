dn_set = set()
for n in range(1,10001):
  dn = n
  for i in str(n):
    dn += int(i)
  dn_set.add(dn)

self_num = set(range(1,10001)) - dn_set
self_num = list(sorted(self_num))

for num in self_num:
  print(num, end='\n')