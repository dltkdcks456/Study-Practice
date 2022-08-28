def bfs(sti, stj, eni, enj):
    visited[sti][stj] = 1
    q = [[sti, stj]]
    while q:
        mvi, mvj = q.pop(0)
        if mvi == N and mvj == M:
            return visited[mvi][mvj]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nmi, nvj = mvi + di, mvj + dj
            if 0 <= nmi <= N and 0 <= nvj <= M and visited[nmi][nvj] == 0 and maze[nmi][nvj] == 1:
                q.append([nmi, nvj])
                visited[nmi][nvj] = visited[mvi][mvj] + 1

N, M = map(int, input().split())
maze = [[0] * (M + 1)] + [[0] + list(map(int, input())) for _ in range(N)]
visited = [[0] * (M + 1) for _ in range(N + 1)]
print(bfs(1, 1, N, M))