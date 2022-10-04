import sys

def bfs():
    while shark_pos:
        r, c = shark_pos.pop(0)
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and land[nr][nc] == 0:
                land[nr][nc] = land[r][c] + 1
                shark_pos.append([nr, nc])


N, M = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
shark_pos = []
dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]
for rs in range(N):
    for cs in range(M):
        if land[rs][cs] == 1:
            shark_pos.append([rs, cs])
bfs()
maxV = max(map(max, land))
print(maxV - 1)