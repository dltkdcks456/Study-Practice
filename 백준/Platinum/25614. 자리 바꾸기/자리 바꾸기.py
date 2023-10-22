N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
visited = [0 for i in range(N + 1)]
dp = [-1 for _ in range(N + 1)]

for i in range(1, N + 1):
    if visited[i] == 1:
        continue
    else:
        cycle = list()
        start = i
        while visited[start] != 1:
            cycle.append(arr[start])
            visited[start] = 1
            start = arr[start]
        size = len(cycle)
        if dp[size] != -1:
            offset = dp[size]
        else:
            offset = M % size
            dp[size] = offset
        for j in range(size):
            arr[cycle[j]] = cycle[(j + offset) % size]
print(*arr[1:])