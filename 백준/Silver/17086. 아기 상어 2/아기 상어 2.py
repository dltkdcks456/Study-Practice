import sys
from collections import deque
input = sys.stdin.readline

def shark_move():
    while q:
        shark_r, shark_c = q.popleft()
        if shark_r + 1 < N and visited[shark_r + 1][shark_c] == -1:
            visited[shark_r + 1][shark_c] = visited[shark_r][shark_c] + 1
            q.append([shark_r + 1, shark_c])
        if shark_r + 1 < N and shark_c + 1 < M and visited[shark_r + 1][shark_c + 1] == -1:
            visited[shark_r + 1][shark_c + 1] = visited[shark_r][shark_c] + 1
            q.append([shark_r + 1, shark_c + 1])
        if shark_r + 1 < N and shark_c - 1 >= 0 and visited[shark_r + 1][shark_c - 1] == -1:
            visited[shark_r + 1][shark_c - 1] = visited[shark_r][shark_c] + 1
            q.append([shark_r + 1, shark_c - 1])
        if shark_r - 1 >= 0 and visited[shark_r - 1][shark_c] == -1:
            visited[shark_r - 1][shark_c] = visited[shark_r][shark_c] + 1
            q.append([shark_r - 1, shark_c])
        if shark_r - 1 >= 0 and shark_c + 1 < M and visited[shark_r - 1][shark_c + 1] == -1:
            visited[shark_r - 1][shark_c + 1] = visited[shark_r][shark_c] + 1
            q.append([shark_r - 1, shark_c + 1])
        if shark_r - 1 >= 0 and shark_c - 1 >= 0 and visited[shark_r - 1][shark_c - 1] == -1:
            visited[shark_r - 1][shark_c - 1] = visited[shark_r][shark_c] + 1
            q.append([shark_r - 1, shark_c - 1])
        if shark_c + 1 < M and visited[shark_r][shark_c + 1] == -1:
            visited[shark_r][shark_c + 1] = visited[shark_r][shark_c] + 1
            q.append([shark_r, shark_c + 1])
        if shark_c - 1 >= 0 and visited[shark_r][shark_c - 1] == -1:
            visited[shark_r][shark_c - 1] = visited[shark_r][shark_c] + 1
            q.append([shark_r, shark_c - 1])


N, M = map(int, input().split()) # 세로의 길이 N, 가로 길이 M
ocean = [list(map(int, input().split())) for _ in range(N)] # 주어지는 입력값(아기 상어의 위치와 그 외의 공간)
visited = [[-1] * M for _ in range(N)]   # 상어의 이동 거리 기록


# 아기 상어 위치를 나타낸 덱(bfs로 접근 예정)
q = deque()

# 아기 상어 위치 추가
for i in range(N):
    for j in range(M):
        if ocean[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 0

shark_move()
print(max(map(max, visited)))