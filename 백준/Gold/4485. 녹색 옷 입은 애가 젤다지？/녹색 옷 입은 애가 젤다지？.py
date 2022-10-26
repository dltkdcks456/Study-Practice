import sys
import heapq

def djikstra(r, c):
    q = []
    distance[r][c] = cave[r][c]
    heapq.heappush(q, [distance[r][c], r, c])
    while q:
        dis, rr, cc = heapq.heappop(q)
        for d in range(4):
            nr = rr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                next_move = dis + cave[nr][nc]
                if distance[nr][nc] <= next_move:
                    continue
                distance[nr][nc] = next_move
                heapq.heappush(q, [distance[nr][nc], nr, nc])

test = 1
while True:
    N = int(sys.stdin.readline())
    if not N:
        break
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    distance = [[125 * 125 * 9] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    djikstra(0, 0)
    print(f'Problem {test}: {distance[N - 1][N - 1]}')
    test += 1