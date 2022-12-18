import sys
import heapq
input = sys.stdin.readline

def djikstra():
    q = []
    heapq.heappush(q, [0, 0, 0])
    while q:
        sumV, r, c = heapq.heappop(q)
        if visited[r][c] < sumV:
            continue
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if room[nr][nc] == 1 and visited[nr][nc] > visited[r][c]: # 방문할 곳이 흰방일 경우
                    visited[nr][nc] = visited[r][c]
                    heapq.heappush(q, [visited[nr][nc], nr, nc])
                # 방문하고자 하는 장소가 검은 방일 경우
                elif room[nr][nc] == 0 and visited[nr][nc] > visited[r][c] + 1:
                    visited[nr][nc] = visited[r][c] + 1
                    heapq.heappush(q, [visited[nr][nc], nr, nc])


if __name__=="__main__":
    n = int(input())
    room = [list(map(int, input().rstrip())) for _ in range(n)]
    visited = [[102] * n for _ in range(n)]
    visited[0][0] = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    djikstra()
    # for i in visited:
    #     print(i)
    print(visited[n - 1][n - 1])