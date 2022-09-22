import sys

N = int(input())
li = []
cnt = 1
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    li.append([a, b])
li.sort(key=lambda x: (x[1], x[0]))
n_s = 0
l_e = li[0][1]
for i in range(1, len(li)):
    if li[i][0] >= l_e:
        cnt += 1
        l_e = li[i][1]
print(cnt)