import sys
from collections import deque
input = sys.stdin.readline

def move(r, c, d, cnt_move):
    while board[r + dr[d]][c + dc[d]] != '#' and board[r][c] != 'O':
        r, c = r + dr[d], c + dc[d]
        cnt_move += 1
    return r, c, cnt_move

def check(rR, cR, rB, cB, cnt):
    global ans
    if cnt == 11:
        return
    for D in range(4):
        nr_R, nc_R, cnt_R = move(rR, cR, D, 0)
        nr_B, nc_B, cnt_B = move(rB, cB, D, 0)

        if board[nr_B][nc_B] == 'O':
            continue
        elif board[nr_R][nc_R] == 'O':
            ans = cnt
            return
        if nr_R == nr_B and nc_R == nc_B:
            if cnt_R > cnt_B:
                nr_R, nc_R = nr_R - dr[D], nc_R - dc[D]
            elif cnt_R < cnt_B:
                nr_B, nc_B = nr_B - dr[D], nc_B - dc[D]
        if [nr_R, nc_R, nr_B, nc_B] not in visited:
            visited.append([nr_R, nc_R, nr_B, nc_B])
            q.append([nr_R, nc_R, nr_B, nc_B, cnt + 1])
    return


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
r_R, c_R, r_B, c_B = 0, 0, 0, 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            r_B, c_B = i, j
        elif board[i][j] == 'R':
            r_R, c_R = i, j

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
minV = 100000
ans = 0
visited = []
q = deque()
q.append([r_R, c_R, r_B, c_B, 1])
while q:
    x_R, y_R, x_B, y_B, Cnt = q.popleft()
    check(x_R, y_R, x_B, y_B, Cnt)

if ans > 0:
    print(1)
else:
    print(0)