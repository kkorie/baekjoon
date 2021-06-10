N = int(input())

result = []
score = list(map(int, input().split()))
M = max(score)
for i in score:
  result.append(i/M*100)
print(sum(result)/len(result))