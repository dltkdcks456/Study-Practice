import sys
cnt_num = [0] * 10

for i in sys.stdin.readline().rstrip():
    cnt_num[int(i)] += 1

print(''.join([str(j) * cnt_num[j] for j in range(9, -1, -1)]))