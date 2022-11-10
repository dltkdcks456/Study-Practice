import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
li = dict()
for _ in range(N):
    x, y = map(int, input().split())
    if x in li:
        li[x].append(y)
    else:
        li[x] = [y]

new_li = []
for k, v in li.items():
    minV = min(v)
    maxV = max(v)
    new_li.append([k, minV, maxV])
new_li.sort()

idx = 1
q = deque([[new_li[0][0], new_li[0][1], 0], [new_li[0][0], new_li[0][2], 0]])

while idx < len(li):
    nx_1, ny_1, d1 = q.popleft()
    nx_2, ny_2, d2 = q.popleft()
    nx_3, ny_3, nx_4, ny_4 = new_li[idx][0], new_li[idx][1], new_li[idx][0], new_li[idx][2]
    d3 = max(d1 + ((nx_1 - nx_3) ** 2 + (ny_1 - ny_3) ** 2) ** 0.5, d2 + ((nx_2 - nx_3) ** 2 + (ny_2 - ny_3) ** 2) ** 0.5)
    d4 = max(d1 + ((nx_1 - nx_4) ** 2 + (ny_1 - ny_4) ** 2) ** 0.5, d2 + ((nx_2 - nx_4) ** 2 + (ny_2 - ny_4) ** 2) ** 0.5)
    q.append([nx_3, ny_3, d3])
    q.append([nx_4, ny_4, d4])
    idx += 1
print(max(q[0][2], q[1][2]))