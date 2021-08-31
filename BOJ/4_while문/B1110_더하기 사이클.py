import sys

n = int(sys.stdin.readline())
check = n
cycle = 0

while True:
  n_sum = check//10 + check%10
  n_new = (check%10)*10 + n_sum%10
  cycle += 1
  check = n_new
  if n==check:
    break
print(cycle)