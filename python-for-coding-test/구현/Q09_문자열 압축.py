S = input()

res = []
for i in range(1, (len(S) // 2) + 1):
  num = 0
  temp = ''
  for j in range(0, len(S), i):
    if temp == S[j:j+i]:
      num += 1
    else:
      temp += S[j:j+1]

    print(S[j:j+i])
    # if temp == '':
    #   temp = S[:j]
    # elif temp == S[:j]

# 생각하기!