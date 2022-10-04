import sys
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        v = q.popleft()
        for w in adjList[v]:
            if visited[w] == 0:
                visited[w] = 1
                par[w] = v
                q.append(w)

N = int(sys.stdin.readline())
adjList = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
par = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)
bfs(1)
for i in range(2, N + 1):
    print(par[i])