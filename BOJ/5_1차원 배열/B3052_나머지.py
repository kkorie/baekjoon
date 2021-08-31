import sys

nums = []
b = 42
for _ in range(10):
  a = int(sys.stdin.readline())
  nums.append(a%b)

result = set(nums)
print(len(result))