h, m = map(int, input().split())

if m >= 45:
  print('{} {}'.format(h, m-45))
elif h == 0:
  print('{} {}'.format(23, (m-45)+60))
else:
  print('{} {}'.format(h-1, (m-45)+60))