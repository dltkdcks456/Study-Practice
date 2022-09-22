import sys

def dfs(r, c, n, sumV):
    global maxV
    if maxV > sumV + (3 - n) * (total_max):
        return
    if n == 3:
        if sumV > maxV:
            maxV = sumV
        return
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dfs(nr, nc, n + 1, sumV + data[nr][nc])
                visited[nr][nc] = 0

def shape(n, m, j, sr, sc):
    global maxV
    if n == m:
        s = data[sr][sc]
        for dd in chosen:
            n_sr = sr + dr[dd]
            n_sc = sc + dc[dd]
            if 0 <= n_sr < N and 0 <= n_sc < M:
                s += data[n_sr][n_sc]
            else:
                return
        if maxV < s:
            maxV = s
        return
    else:
        for l in range(j, len(li)):
            if visited1[l] == 0:
                chosen[n] = li[l]
                visited1[l] = 1
                shape(n + 1, m, l + 1, sr, sc)
                visited1[l] = 0

N, M = map(int,sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
maxV = 0
total_max = max(map(max, data))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
chosen = [0] * 3
visited1 = [0] * 4
li = list(range(4))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, data[i][j])
        visited[i][j] = 0
        shape(0, 3, 0, i, j)

print(maxV)
