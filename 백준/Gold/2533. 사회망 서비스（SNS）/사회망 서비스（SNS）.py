import sys
input = sys.stdin.readline

N = int(input())
adjList = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

leaf_node = list()
for i in range(len(adjList)):
    if len(adjList[i]) == 1:
        leaf_node.append(i)

while leaf_node:
    v = leaf_node.pop()
    for k in adjList[v]:
        for l in adjList[k]:
            adjList[l].remove(k)
            if len(adjList[l]) == 1:
                leaf_node.append(l)
        visited[k] = 1
        adjList[k] = []

print(sum(visited))