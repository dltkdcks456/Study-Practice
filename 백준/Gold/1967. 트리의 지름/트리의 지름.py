import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(a, sumV):
    for b in adjList[a]:
        if depth[b[0]] == -1:
            depth[b[0]] = sumV + b[1]
            dfs(b[0], sumV + b[1])

n = int(input())
adjList = [[] for _ in range(n + 1)]                # 인접 리스트 활용
depth = [-1] * (n + 1)                               # 깊이 저장 리스트
depth[1] = 0
for _ in range(n - 1):                              # 입력값 저장
    u, v, w = map(int, input().split())
    adjList[u].append([v, w])
    adjList[v].append([u, w])
dfs(1, 0)
first_maxV = max(depth)
new_start = depth.index(first_maxV)
depth = [-1] * (n + 1)                               # 깊이 저장 리스트
depth[new_start] = 0
dfs(new_start, 0)
print(max(depth))
