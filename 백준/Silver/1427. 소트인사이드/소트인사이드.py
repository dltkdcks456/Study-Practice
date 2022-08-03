import sys
N = sys.stdin.readline().rstrip()
cnt_num = [0] * 10

for i in N:
    cnt_num[int(i)] += 1

for j in range(len(cnt_num) - 1, -1, -1):
    print(str(j) * cnt_num[j], end='')