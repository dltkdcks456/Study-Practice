import sys
from collections import deque

# 트리로 구성되어 있으며, 두 노드가 선택되고 가장 가까운 공통 조상을 출력하는 문제
# 각각의 깊이를 구한 뒤, 동일 깊이에서 부터 하나씩 올라가면서 조상이 같은지 확인 진행(나동빈 유튜브 참고)

def depth_check(n):                         # 깊이 출력을 위한 함수(bfs), 자신의 부모 또한 저장
    q = deque([n])
    depth[n] = 1
    while q:
        v = q.popleft()
        for w in adjList[v]:
            if depth[w] == 0:
                depth[w] = depth[v] + 1
                q.append(w)
                par[w] = v                  # 부모 노드 저장

def find_ancestor(x, y):
    while depth[x] != depth[y]:             # 동일 높이로 맞추기
        if depth[x] > depth[y]:
            x = par[x]
        else:
            y = par[y]
    while x != y:                           # 부모를 거슬러가면서 같아질 경우 해당값 출력
        x = par[x]
        y = par[y]
    else:
        return x

N = int(sys.stdin.readline())
adjList = [[] for _ in range(N + 1)]        # 인접 행렬 정의
depth = [0] * (N + 1)                       # 각 노드의 깊이 정보
par = [0] * (N + 1)                         # 각 노드의 부모노드 저장
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)
depth_check(1)

# M개의 줄에 걸쳐서 두 노드가 주어진다.
M = int(sys.stdin.readline())
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(find_ancestor(s, e))