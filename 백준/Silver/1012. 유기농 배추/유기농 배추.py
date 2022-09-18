import sys

def bfs(r, c):
    land[r][c] = 0
    q.append([r, c])
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and land[nr][nc] == 1:
                land[nr][nc] = 0
                q.append([nr, nc])


T = int(sys.stdin.readline())
for test in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    land = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, sys.stdin.readline().split())
        land[r][c] = 1
    cnt = 0
    q = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for r1 in range(N):
        for c1 in range(M):
            if land[r1][c1] == 1:
                cnt += 1
                bfs(r1, c1)
    print(cnt)