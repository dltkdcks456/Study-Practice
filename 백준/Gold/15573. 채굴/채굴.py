import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
mineral = [list(map(int, input().split())) for _ in range(N)]
q = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
visited = [[0] * M for _ in range(N)]
for c in range(M):
    heapq.heappush(q, [mineral[0][c], 0, c])
    visited[0][c] = 1
for r in range(1, N):
    heapq.heappush(q, [mineral[r][0], r, 0])
    visited[r][0] = 1
    heapq.heappush(q, [mineral[r][M - 1], r, M - 1])
    visited[r][M - 1] = 1

cnt = D = 0

while cnt != K and q:
    s, rr, cc = heapq.heappop(q)
    mineral[rr][cc] = 0
    cnt += 1
    if s > D:
        D = s
    for d in range(4):
        nr = rr + dr[d]
        nc = cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            heapq.heappush(q, [mineral[nr][nc], nr, nc])
            visited[nr][nc] = 1
print(D)