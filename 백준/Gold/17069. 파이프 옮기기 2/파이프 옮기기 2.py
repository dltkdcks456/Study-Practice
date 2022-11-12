import sys
input = sys.stdin.readline


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# 1: 가로, 2: 대각선, 3: 세로
dr = [0, 1, 1]
dc = [1, 1, 0]
for i in range(1, N):
    if home[0][i] == 0:
        visited[0][i][0] = 1
    else:
        break
for r in range(1, N):
    for c in range(2, N):
        if home[r][c] == 1:
            continue
        else:
            if home[r - 1][c - 1] == 0 and home[r][c - 1] == 0 and home[r - 1][c] == 0:
                visited[r][c][1] = sum(visited[r - 1][c - 1])
            if home[r][c - 1] == 0:
                visited[r][c][0] = visited[r][c - 1][0] + visited[r][c - 1][1]
            if home[r - 1][c] == 0:
                visited[r][c][2] = visited[r - 1][c][1] + visited[r - 1][c][2]

print(sum(visited[N - 1][N - 1]))