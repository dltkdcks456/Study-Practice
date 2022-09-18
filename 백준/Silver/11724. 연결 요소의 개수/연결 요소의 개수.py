import sys
def bfs(n):
    visited[n] = 1
    q.append(n)
    while q:
        v = q.pop(0)
        for w in adjust[v]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)

N, M = map(int, sys.stdin.readline().split())
adjust = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjust[a].append(b)
    adjust[b].append(a)
q = []
cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)