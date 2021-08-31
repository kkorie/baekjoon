N = int(input())

for _ in range(N):
  word = input()
  checked = []
  for w in word:
    if w not in checked:
      checked.append(w)
    else:
      if w == checked[-1]:
        continue
      else:
        N -= 1
        break

print(N)