import sys
from collections import deque

def bfs(n, m):
    q = deque([[n, 0]])
    visited = [0] * (N + 1)
    while q:
        x, x_dist = q.popleft()
        if x == m:
            print(visited[x])
            break
        for y, dist in adjList[x]:
            if visited[y] == 0:
                visited[y] = visited[x] + dist
                q.append([y, dist])

N, M = map(int, sys.stdin.readline().split())
adjList = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    adjList[u].append([v, w])
    adjList[v].append([u, w])
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    bfs(s, e)