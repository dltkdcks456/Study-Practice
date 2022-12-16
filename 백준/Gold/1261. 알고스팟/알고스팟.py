import sys
import heapq

def djikstra():
    q = []
    heapq.heappush(q, [0, 0, 0])
    while q:
        d, r, c = heapq.heappop(q)
        if visited[r][c] < d:
            continue
        if r + 1 < N and visited[r + 1][c] > visited[r][c] + area[r + 1][c]:
            visited[r + 1][c] = visited[r][c] + area[r + 1][c]
            heapq.heappush(q, [visited[r + 1][c], r + 1, c])
        if r - 1 >= 0 and visited[r - 1][c] > visited[r][c] + area[r - 1][c]:
            visited[r - 1][c] = visited[r][c] + area[r - 1][c]
            heapq.heappush(q, [visited[r - 1][c], r - 1, c])
        if c + 1 < M and visited[r][c + 1] > visited[r][c] + area[r][c + 1]:
            visited[r][c + 1] = visited[r][c] + area[r][c + 1]
            heapq.heappush(q, [visited[r][c + 1], r, c + 1])
        if c - 1 >= 0 and visited[r][c - 1] > visited[r][c] + area[r][c - 1]:
            visited[r][c - 1] = visited[r][c] + area[r][c - 1]
            heapq.heappush(q, [visited[r][c - 1], r, c - 1])


M, N = map(int, input().rstrip().split())
area = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
visited[0][0] = 0
# for j in area:
#     print(j)
# print(area)
djikstra()
# print(visited)
# for i in visited:
#     print(i)
print(visited[N - 1][M - 1])