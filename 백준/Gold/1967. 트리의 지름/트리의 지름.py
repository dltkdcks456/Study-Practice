import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def dfs(a, deep, sumV):                           # 깊이에 대한 정보
    weight[a] = sumV
    for b in adjList[a]:
        if depth[b[0]] == 0:
            depth[b[0]] = deep + 1
            dfs(b[0], deep + 1, sumV + b[1])

def lca(x, y):                              # 가장 가까운 공통 조상
    while depth[x] != depth[y]:
        if depth[x] > depth[y]:
            x = par[x]
        else:
            y = par[y]

    while x != y:
        x = par[x]
        y = par[y]
    return x


n = int(input())
adjList = [[] for _ in range(n + 1)]                # 인접 리스트 활용
depth = [0] * (n + 1)                               # 깊이 저장 리스트
depth[1] = 1
par = [0] * (n + 1)
weight = {i:0 for i in range(1, n + 1)}             # 추후 가중치의 합을 저장할 공간
for _ in range(n - 1):                              # 입력값 저장
    u, v, w = map(int, input().split())
    adjList[u].append([v, w])
    adjList[v].append([u, w])
    par[v] = u

leaf_node = []
for i in range(len(adjList)):                       # 리프노드 찾기
    if len(adjList[i]) == 1:                        # 리프노드에서 리프노드로 가는 경우가 가장 길다
        leaf_node.append(i)                         # 연결된 간선 정보가 하나인 경우가 리프 노드
dfs(1, 1, 0)
maxV = 0
for m in range(len(leaf_node) - 1):
    for n in range(m + 1, len(leaf_node)):
        ancestor = lca(leaf_node[n], leaf_node[m])
        total_sum = weight[leaf_node[n]] + weight[leaf_node[m]] - 2 * weight[ancestor]
        if total_sum > maxV:
            maxV = total_sum
print(maxV)
