import sys
from collections import deque

def bfs():
    while q:
        rs, cs = q.popleft()
        for d in range(6):
            nr = rs + dr[d]
            nc = cs + dc[d]
            if 0 <= nr < total_H and 0 <= nc < M and tomato[nr][nc] == 0:
                tomato[nr][nc] = tomato[rs][cs] + 1
                q.append((nr, nc))

input = sys.stdin.readline
M, N, H = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N * H)]
q = deque()
for block in range(N * H, -1, -N):
    tomato.insert(block, [1] * M)
total_H = len(tomato)
for r in range(total_H):
    for c in range(M):
        if tomato[r][c] == 1 and r % (N + 1) != 0:
            q.append((r, c))
dr = [0, 1, 0, -1, N + 1, - N - 1]
dc = [1, 0, -1, 0, 0, 0]
bfs()
total_max = max(map(max, tomato))
total_min = min(map(min, tomato))
flag = True
for r1 in tomato:
    if 0 in r1:
        flag = False
if total_max == total_min == 1:
    print(0)
elif flag == False:
    print(-1)
elif flag == True:
    print(total_max - 1)