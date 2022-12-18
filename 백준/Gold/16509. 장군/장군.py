import sys
from collections import deque
input = sys.stdin.readline

def catch(R, C):
    q = deque()
    q.append([R, C])
    while q:
        r, c = q.popleft()
        if r == R2 and c == C2:
            print(visited[r][c] - 1)
            return
        for d in range(8):
            flag = False
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                for ck_d in range(2):
                    cr = nr + ck_r[d][ck_d]
                    cc = nc + ck_c[d][ck_d]
                    if cr == R2 and cc == C2:
                        flag = True
                        break
                if flag:
                    continue
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append([nr, nc])

if __name__=='__main__':
    N, M = 10, 9  # N: 세로 길이, M: 가로 길이
    visited = [[0] * M for _ in range(N)]
    R1, C1 = map(int, input().split())
    R2, C2 = map(int, input().split())
    dr = [-3, -2, 2, 3, 3, 2, -2, -3]
    dc = [2, 3, 3, 2, -2, -3, -3, -2]
    ck_r = [[1, 2], [1, 2], [-1, -2], [-1, -2], [-1, -2], [-1, -2], [1, 2], [1, 2]]
    ck_c = [[-1, -2], [-1, -2], [-1, -2], [-1, -2], [1, 2], [1, 2], [1, 2], [1, 2]]
    visited[R1][C1] = 1
    catch(R1, C1)
    # for i in visited:
    #     print(i)