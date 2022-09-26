import sys
from collections import deque

def bfs(n):
    global cnt
    q.append(n)
    while q:
        v = q.popleft()
        for w in path[v]:
            if visited[w] == 0:
                visited[w] = 1
                cnt += 1
                q.append(w)

node = int(input())
E = int(input())
path = [[] for _ in range(node + 1)]
visited = [0] * (node + 1)
for _ in range(E):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)
q = deque()
cnt = 0
bfs(1)
print(cnt - 1)