S = input()

# check = 1
# temp = int(S[0])
# for i in S[1:]:
#   i = int(i)
#   if i != temp:
#     check += 1
#     temp = i

# res = check // 2
# print(res)

# 다른 풀이
count0 = 0
count1 = 0

if S[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(S) - 1):
  if S[i] != S[i + 1]:
    if S[i + 1] == '1':
      count0 += 1
    else:
      count1 += 1

print(min(count0, count1))