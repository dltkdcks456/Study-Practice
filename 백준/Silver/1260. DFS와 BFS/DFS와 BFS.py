def dfs(V):
    visited_dfs[V] = 1
    print(V, end = ' ')
    for w in node[V]:
        if visited_dfs[w] == 0:
            dfs(w)

def bfs(V):
    visited_bfs[V] = 1
    q = [V]
    print(V, end=' ')
    while q:
        v = q.pop(0)
        for w in node[v]:
            if visited_bfs[w] == 0:
                q.append(w)
                visited_bfs[w] = visited_bfs[v] + 1
                print(w, end = ' ')

N, M, V = map(int, input().split())
node = [[] for _ in range(N + 1)]
visited_bfs = [0 for _ in range(N + 1)]
visited_dfs = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(len(node)):
    node[j] = sorted(node[j])

dfs(V)
print()
bfs(V)

