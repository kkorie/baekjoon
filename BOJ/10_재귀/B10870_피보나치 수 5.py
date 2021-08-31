n = int(input())

def p(n):
  ans = 0
  if n == 0:
    ans = 0
  elif n == 1:
    ans = 1
  else:
    ans = p(n-2) + p(n-1)
  return ans

print(p(n))