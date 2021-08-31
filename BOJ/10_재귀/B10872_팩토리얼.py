N = int(input())

def f(n):
  ans = 0
  for i in range(n+1):
    if i == 0:
      ans = 1
    elif i == 1 or i == 2:
      ans = i
    else:
      ans = i * f(n-1)
  return ans

print(f(N))