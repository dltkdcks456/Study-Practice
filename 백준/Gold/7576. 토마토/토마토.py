import sys
from collections import deque


def bfs(li):
    while q:
        r1, c1 = q.popleft()
        for d in range(4):
            nr = r1 + dr[d]
            nc = c1 + dc[d]
            if 0 <= nr < N and 0 <= nc < M and tomato[nr][nc] == 0:
                q.append((nr, nc))
                tomato[nr][nc] = tomato[r1][c1] + 1

M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
flag = False
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            q.append((r, c))
        if tomato[r][c] == 0:
            flag = True
if flag:
    bfs(q)
    ans = 0
    for j in tomato:
        if 0 in j:
            ans = 0
            break
        else:
            if ans < max(j):
                ans = max(j)
    print(ans - 1)
else:
    print(0)