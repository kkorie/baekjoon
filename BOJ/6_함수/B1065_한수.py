def result(n):
  cnt = 0
  for i in range(1, n+1):
    num_set = set()
    for x in range(int(len(str(i)))-1):
      num_set.add(int(str(i)[x])-int(str(i)[x+1]))
    if len(num_set)==0 or len(num_set)==1:
      cnt += 1
  print(cnt)

result(int(input()))