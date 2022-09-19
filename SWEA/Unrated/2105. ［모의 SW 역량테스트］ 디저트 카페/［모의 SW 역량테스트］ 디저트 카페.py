def dfs(r, c, sr, sc, d, last):
    global maxV
    if d == 3 and r == sr and c == sc:
        check = chosen[:last]
        if len(check) <= maxV:
            return
        else:
            for i in check:
                if check.count(i) >= 2:
                    return
            else:
                if len(check) > maxV:
                    maxV = len(check)
            return
    elif d == 3 and visited[r][c] == 1 or d == 4:
        return
    else:
        chosen[last] = data[r][c]
        visited[r][c] = 1
        r += dr[d]
        c += dc[d]
        if sr <= r < N and 0 <= c < N:
            dfs(r, c, sr, sc, d, last + 1)
            visited[r][c] = 0
            dfs(r, c, sr, sc, d + 1, last + 1)
            visited[r][c] = 0
        else:
            r -= dr[d]
            c -= dc[d]
            visited[r][c] = 0


T = int(input())
for test in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    chosen = [0] * (N * 2)
    maxV = -1
    for r in range(N - 2):
        for c in range(1, N - 1):
            dfs(r, c, r, c, 0, 0)

    print(f'#{test} {maxV}')