import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
K = int(input())
board = [[1] * (N + 2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N + 2)] # 방벽을 둘러싸기
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 2

L = int(input())
move_data = []

for _ in range(L):
    a, b = input().split()
    move_data.append([int(a), b]) # L이면 왼쪽으로 90도 R이면 오른쪽으로 90도

dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
dc = [1, 0, -1, 0]
d = 0               # 초기 방향
snake_pos = deque([[1, 1]])  # 뱀의 위치 기록
board[1][1] = 1
X = 0
r = c = 1       # 뱀의 초기 위치
for i in move_data:
    flag = True # 뱀의 종료를 알릴 신호
    time, direction = i
    while X < time:
        X += 1
        r = r + dr[d]
        c = c + dc[d]
        if board[r][c] == 1:
            flag = False
            break
        else:
            if board[r][c] == 2:
                snake_pos.append([r, c])
                board[r][c] = 1
            else:
                snake_pos.append([r, c])
                board[r][c] = 1
                er, ec = snake_pos.popleft()
                board[er][ec] = 0
    if direction == 'L':
        d -= 1
        if d == -1:
            d = 3
    else:
        d += 1
        if d == 4:
            d = 0
    if not flag:
        break

if flag:
    while True:
        X += 1
        r = r + dr[d]
        c = c + dc[d]
        if board[r][c] == 1:
            break
        else:
            snake_pos.append([r, c])
            board[r][c] = 1
            er, ec = snake_pos.popleft()
            board[er][ec] = 0
print(X)