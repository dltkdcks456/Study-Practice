import sys
from collections import deque
input = sys.stdin.readline


def move():
    global ans
    while pos:
        r, c, w = pos.popleft()
        if w == 'F':
            if r + 1 < R and maze[r + 1][c] not in '#F':
                maze[r + 1][c] = 'F'
                pos.append([r + 1, c, 'F'])
            if c + 1 < C and maze[r][c + 1] not in '#F':
                maze[r][c + 1] = 'F'
                pos.append([r, c + 1, 'F'])
            if r - 1 >= 0 and maze[r - 1][c] not in '#F':
                maze[r - 1][c] = 'F'
                pos.append([r - 1, c, 'F'])
            if c - 1 >= 0 and maze[r][c - 1] not in '#F':
                maze[r][c - 1] = 'F'
                pos.append([r, c - 1, 'F'])
        else:
            if r == R - 1 or r == 0 or c == C - 1 or c == 0:
                ans = visited[r][c]
                break
            if r + 1 < R and maze[r + 1][c] not in '#F' and visited[r + 1][c] == 0:
                visited[r + 1][c] = visited[r][c] + 1
                pos.append([r + 1, c, 'J'])
            if c + 1 < C and maze[r][c + 1] not in '#F' and visited[r][c + 1] == 0:
                visited[r][c + 1] = visited[r][c] + 1
                pos.append([r, c + 1, 'J'])
            if r - 1 >= 0 and maze[r - 1][c] not in '#F' and visited[r - 1][c] == 0:
                visited[r - 1][c] = visited[r][c] + 1
                pos.append([r - 1, c, 'J'])
            if c - 1 >= 0 and maze[r][c - 1] not in '#F' and visited[r][c - 1] == 0:
                visited[r][c - 1] = visited[r][c] + 1
                pos.append([r, c - 1, 'J'])


R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
pos = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            pos.append([i, j, 'J'])
            visited[i][j] = 1
        elif maze[i][j] == 'F':
            pos.append([i, j, 'F'])
pos.sort(key=lambda x: x[2])
pos = deque(pos)
ans = 0
# print(pos)
move()
if ans:
    print(ans)
else:
    print('IMPOSSIBLE')
# print(maze)
# for l in visited:
#     print(l)