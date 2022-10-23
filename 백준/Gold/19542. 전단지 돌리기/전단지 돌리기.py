import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(n):
    global cnt
    if n != S and len(adjList[n]) == 1:
        return 0
    else:
        data = []
        for w in adjList[n]:
            if visited[w] == 0:
                visited[w]= 1
                distance = dfs(w) + 1
                data.append(distance)
        maxV = max(data)
        if len(data) >= 2:
            for j in data:
                if j > D and j != maxV:
                    cnt += j - D
            if maxV > D:
                cnt += (data.count(maxV) - 1) * (maxV - D)
        return maxV

N, S, D = map(int, input().split())
adjList = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
cnt = 0
visited[S] = 1
if N == 1:
    print(0)
else:
    root = dfs(S)
    if root > D:
        cnt += root - D
        print(cnt * 2)
    else:
        print(0)