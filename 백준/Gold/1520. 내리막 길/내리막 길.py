import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(r, c):
    if visited[r][c] != -1:
        return visited[r][c]
    if r == M - 1 and c == N - 1:
        return 1
    a = s = d = f = 0
    if r + 1 < M and Map[r + 1][c] < Map[r][c]:
        a = dfs(r + 1, c)
    if r - 1 >= 0 and Map[r - 1][c] < Map[r][c]:
        s = dfs(r - 1, c)
    if c + 1 < N and Map[r][c + 1] < Map[r][c]:
        d = dfs(r, c + 1)
    if c - 1 >= 0 and Map[r][c - 1] < Map[r][c]:
        f = dfs(r, c - 1)
    visited[r][c] = a + s + d + f
    return a + s + d + f
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]
dfs(0, 0)
print(visited[0][0])