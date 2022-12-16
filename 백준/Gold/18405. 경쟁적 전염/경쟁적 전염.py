import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
S, X, Y = map(int, input().split())
q = []

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            q.append([arr[i][j], i, j])  # 바이러스 번호, 행, 열 위치 정보
            visited[i][j] = 1            # S초 후에 멈추기 위한 시간 진행
q.sort()
q = deque(q)
while q:
    virus, r, c = q.popleft()
    # 네 방향에 대한 탐색(바이러스 번호 순서대로)
    if r + 1 < N and arr[r + 1][c] == 0 and visited[r][c] <= S:
        arr[r + 1][c] = virus
        visited[r + 1][c] = visited[r][c] + 1
        q.append([virus, r + 1, c])
    if r - 1 >= 0 and arr[r - 1][c] == 0 and visited[r][c] <= S:
        arr[r - 1][c] = virus
        visited[r - 1][c] = visited[r][c] + 1
        q.append([virus, r - 1, c])
    if c + 1 < N and arr[r][c + 1] == 0 and visited[r][c] <= S:
        arr[r][c + 1] = virus
        visited[r][c + 1] = visited[r][c] + 1
        q.append([virus, r, c + 1])
    if c - 1 >= 0 and arr[r][c - 1] == 0 and visited[r][c] <= S:
        arr[r][c - 1] = virus
        visited[r][c - 1] = visited[r][c] + 1
        q.append([virus, r, c - 1])
print(arr[X - 1][Y - 1])