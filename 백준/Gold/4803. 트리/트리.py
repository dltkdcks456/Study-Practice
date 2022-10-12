import sys

def dfs(n, par):
    global flag
    for w in adjList[n]:
        if w != par:
            if visited[w] == 0:
                visited[w] = 1
                dfs(w, n)
            else:
                flag = False


test = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    adjList = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adjList[a].append(b)
        adjList[b].append(a)

    result = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            flag = True
            visited[i] = 1
            dfs(i, -1)
            if flag:
                result += 1

    if result == 0:
        print(f'Case {test}: No trees.')
    elif result == 1:
        print(f'Case {test}: There is one tree.')
    else:
        print(f'Case {test}: A forest of {result} trees.')
    test += 1