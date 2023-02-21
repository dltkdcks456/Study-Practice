'''
여러 섬들 중에서 거리가 가장 긴 값을 찾으면 된다.
브루트 포스 + 너비 우선 탐색 + 최댓값
'''
from collections import deque

def bfs(r, c):
    global ans_time
    q = deque()
    q.append([r, c])
    visited = [[-1] * M for _ in range(N)]
    visited[r][c] = 0
    while q:
        nr, nc = q.popleft()
        
        # 이동 시간이 최댓값을 가리킬 때 ans_time 변수값 수정
        if visited[nr][nc] > ans_time:
            ans_time = visited[nr][nc]
        
        # 총 4군데의 방향으로 탐색
        # 우
        if nc + 1 < M and land[nr][nc + 1] == 'L' and visited[nr][nc + 1] == -1:
            visited[nr][nc + 1] = visited[nr][nc] + 1
            q.append([nr, nc + 1])
        # 하
        if nr + 1 < N and land[nr + 1][nc] == 'L' and visited[nr + 1][nc] == -1:
            visited[nr + 1][nc] = visited[nr][nc] + 1
            q.append([nr + 1, nc])
        # 좌
        if nc - 1 >= 0 and land[nr][nc - 1] == 'L' and visited[nr][nc - 1] == -1:
            visited[nr][nc - 1] = visited[nr][nc] + 1
            q.append([nr, nc - 1])
        if nr - 1 >= 0 and land[nr - 1][nc] == 'L' and visited[nr - 1][nc] == -1:
            visited[nr - 1][nc] = visited[nr][nc] + 1
            q.append([nr - 1, nc])


if __name__ == '__main__':
    # 입력값 받기
    N, M = map(int, input().split())
    land = [list(input().strip()) for _ in range(N)]
    
    ans_time = 0
    
    # 육지에서만 BFS 탐색을 진행한다.
    for r in range(N):
        for c in range(M):
            if land[r][c] == 'L':
                bfs(r, c)
    
    print(ans_time)