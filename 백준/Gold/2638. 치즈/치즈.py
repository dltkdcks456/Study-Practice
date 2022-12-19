import sys
from collections import deque
input = sys.stdin.readline

def air(r_i, c_i):
    '''
    외부 공기와 접촉한 공기를 외부 공기화 시켜주는 함수(0 -> 2변경)
    '''
    q = deque()
    q.append([r_i, c_i])
    arr[r_i][c_i] = 2
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                q.append([nr, nc])

def check_cheese():
    '''
    모든 치즈를 순회하면서 다음에 녹게 될 치즈를 melten으로 넘겨주는 작업
    '''
    n = len(cheese) # 탐색할 횟수
    while n > 0:
        r, c = cheese.popleft()
        tmp = 0 # 외부 공기에 노출된 횟수
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 2:
                tmp += 1
                if tmp >= 2:
                    melten.append([r, c])
                    break
        else:
            cheese.append([r, c])
        n -= 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheese = deque()    # 총 치즈의 위치
melten = deque()    # 녹아 없어질 치즈

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheese.append([i, j])

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
air(0, 0) # 초기 상태에서 외부 공기 유입
ans = 0
while cheese:
    check_cheese()
    while melten:
        r, c = melten.popleft()
        if arr[r][c] == 1:
            air(r, c)
    ans += 1
print(ans)