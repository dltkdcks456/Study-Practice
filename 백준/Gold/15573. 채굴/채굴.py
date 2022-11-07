import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
mineral = [list(map(int, input().split())) for _ in range(N)]
q = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
visited = set()
for c in range(M):
    heapq.heappush(q, [mineral[0][c], 0, c])
    visited.add((0, c))
for r in range(1, N):
    heapq.heappush(q, [mineral[r][0], r, 0])
    heapq.heappush(q, [mineral[r][M - 1], r, M - 1])
    visited.add((r, 0))
    visited.add((r, M - 1))

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
        if (nr, nc) not in visited and 0 <= nr < N and 0 <= nc < M:
            heapq.heappush(q, [mineral[nr][nc], nr, nc])
            visited.add((nr, nc))
print(D)
