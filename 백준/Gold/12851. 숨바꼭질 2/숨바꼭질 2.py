import sys
from collections import deque

def bfs(n):
    global cnt, time, minV
    q = deque([n])
    while q:
        v = q.popleft()
        if v == K:
            cnt += 1
            time = move[v]
            if time < minV:
                minV = time
        for w in (v - 1, v + 1, 2 * v):
            if 0 <= w <= max(N, K) * 2 and move[w] >= move[v] + 1 and move[v] + 1 <= minV:
                move[w] = move[v] + 1
                q.append(w)

N, K = map(int, input().split())
move = [100001] * (max(N, K) * 2 + 1)
move[N] = cnt = time = 0
minV = float('inf')
bfs(N)
print(time)
print(cnt)