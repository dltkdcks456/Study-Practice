import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().split()))
q = deque()
minV = N + 1
length = 0
for i in range(N):
    if len(q) < K and num[i] == 1:
        q.append(i)
        if len(q) == K:
            length = q[-1] - q[0] + 1
            if length < minV:
                minV = length
    elif len(q) == K and num[i] == 1:
        q.popleft()
        q.append(i)
        length = q[-1] - q[0] + 1
        if length < minV:
            minV = length
if minV != N + 1:
    print(minV)
else:
    print(-1)