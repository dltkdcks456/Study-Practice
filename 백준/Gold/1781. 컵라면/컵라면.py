import sys
import heapq

N = int(sys.stdin.readline())
cup = [0] * (N + 1)
last_idx = [i for i in range(N + 1)]
q = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(q, [-b, a])
sumV = 0
while q:
    c = heapq.heappop(q)
    for ck in range(last_idx[c[1]], 0, -1):
        if cup[ck] == 0:
            cup[ck] = 1
            sumV += -c[0]
            last_idx[c[1]] = ck - 1
            break
print(sumV)