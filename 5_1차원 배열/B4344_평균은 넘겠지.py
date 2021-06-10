import sys

C = int(sys.stdin.readline())

for _ in range(C):
  sc_list = list(map(int, sys.stdin.readline().split()))
  n = sc_list[0]
  score = sc_list[1:]
  sc_avg = sum(score)/n
  result_list = [x for x in score if x > sc_avg]
  print('{:.3f}%'.format(len(result_list)/n*100))