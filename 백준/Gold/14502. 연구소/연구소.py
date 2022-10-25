import sys
from collections import deque

def bfs():
    global maxV
    q = deque(pos)
    visited = [[0] * M for _ in range(N)]
    for start_virus in q:
        visited[start_virus[0]][start_virus[1]] = 1
    while q:
        rv, cv = q.popleft()
        for d in range(4):
            nr = rv + dr[d]
            nc = cv + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and Map[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append([nr, nc])
    ck = 0
    for i0 in range(N):
        for j0 in range(M):
            if visited[i0][j0] == 0 and Map[i0][j0] == 0:
                ck += 1
    if maxV < ck:
        maxV = ck
    return

def virus(r, c, cnt):
    if cnt == 3:
        bfs()
        return
    for ii in range(N):
        if ii < r:
            continue
        elif ii == r:
            for jj in range(M):
                if jj <= c:
                    continue
                else:
                    if Map[ii][jj] == 0:
                        Map[ii][jj] = 1
                        virus(ii, jj, cnt + 1)
                        Map[ii][jj] = 0
        else:
            for jj in range(M):
                if Map[ii][jj] == 0:
                    Map[ii][jj] = 1
                    virus(ii, jj, cnt + 1)
                    Map[ii][jj] = 0


N, M = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pos = []
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
maxV = 0
for rr in range(N):
    for cc in range(M):
       if Map[rr][cc] == 2:
           pos.append([rr, cc])


for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            Map[i][j] = 1
            virus(i, j, 1)
            Map[i][j] = 0
print(maxV)