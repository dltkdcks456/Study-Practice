import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
connect = [0] * (N + 1)
visited = [0] * (N + 1)
adjList = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjList[a].append(b)
    connect[b] += 1

q = deque()
for i in range(1, N + 1):
    if connect[i] == 0:
        q.append(i)
        visited[i] = 1

while q:
    v = q.popleft()
    print(v, end = ' ')
    for w in adjList[v]:
        connect[w] -= 1

    for j in range(1, N + 1):
        if visited[j] == 0 and connect[j] == 0:
            q.append(j)
            visited[j] = 1