import sys
from collections import deque

def bfs(r, c, col):
    global cnt
    visited[r][c] = 1
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and color[nr][nc] == col:
                visited[nr][nc] = 1
                q.append((nr, nc))
    cnt += 1

def RG_bfs(r2, c2, col):
    global RG_cnt
    if col in 'RG':
        visited[r2][c2] = 1
        q.append((r2, c2))
        while q:
            r3, c3 = q.popleft()
            for d in range(4):
                nr = r3 + dr[d]
                nc = c3 + dc[d]
                if 0 <= nr < N and 0 <= nc < N and visited1[nr][nc] == 0 and color[nr][nc] in 'RG':
                    visited1[nr][nc] = 1
                    q.append((nr, nc))
        RG_cnt += 1
    else:
        visited[r2][c2] = 1
        q.append((r2, c2))
        while q:
            r3, c3 = q.popleft()
            for d in range(4):
                nr = r3 + dr[d]
                nc = c3 + dc[d]
                if 0 <= nr < N and 0 <= nc < N and visited1[nr][nc] == 0 and color[nr][nc] == 'B':
                    visited1[nr][nc] = 1
                    q.append((nr, nc))
        RG_cnt += 1

N = int(input())
color = [list(input()) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
q = deque()
cnt = RG_cnt = 0
visited = [[0] * N for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
for r1 in range(N):
    for c1 in range(N):
        if visited[r1][c1] == 0:
            bfs(r1, c1, color[r1][c1])
        if visited1[r1][c1] == 0:
            RG_bfs(r1, c1, color[r1][c1])
print(cnt, RG_cnt)