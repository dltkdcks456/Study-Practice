import sys

def tetromino(r, c, depth, sumV, cnt):
    global maxV, max_value, sub_maxV
    if cnt == 1 and sumV + max_value * (3 - depth) <= maxV:
        return
    elif cnt == 0 and sumV + max_value * (3 - depth) <= sub_maxV:
        return
    if depth == 3:
        if cnt == 1:
            if sumV > maxV:
                maxV = sumV
            return
        else:
            if sumV > sub_maxV:
                sub_maxV = sumV
                for r1 in range(N):
                    for c1 in range(M):
                        if visited[r1][c1] == 0:
                            visited[r1][c1] = 1
                            tetromino(r1, c1, 0, data[r1][c1] + sumV, cnt + 1)
                            visited[r1][c1] = 0
            else:
                return
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if depth == 1:
                    visited[nr][nc] = 1
                    tetromino(r, c, depth + 1, sumV + data[nr][nc], cnt)
                    tetromino(nr, nc, depth + 1, sumV + data[nr][nc], cnt)
                    visited[nr][nc] = 0
                else:
                    visited[nr][nc] = 1
                    tetromino(nr, nc, depth + 1, sumV + data[nr][nc], cnt)
                    visited[nr][nc] = 0


N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_value = max(map(max, data))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
maxV = sub_maxV = 0
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        tetromino(r, c, 0, data[r][c], 0)
        visited[r][c] = 0
print(maxV)