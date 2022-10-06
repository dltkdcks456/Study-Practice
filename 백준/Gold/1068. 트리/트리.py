import sys
from collections import deque

def node_erase(n):
    q = deque([n])
    visited[n] = 1
    while q:
        v = q.popleft()
        for w in adjList[v]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)

def leaf_node_cnt(m):
    global cnt
    p = deque([m])
    if visited[m] == 1:
        return
    else:
        visited[m] = 1
        while p:
            k = p.popleft()
            if adjList[k]:
                flag = True
                for l in adjList[k]:
                    if visited[l] == 0:
                        visited[l] = 1
                        flag = False
                        p.append(l)
                else:
                    if flag:
                        cnt += 1
            else:
                cnt += 1

N = int(sys.stdin.readline())
par = list(map(int, sys.stdin.readline().split()))
erase = int(sys.stdin.readline())
adjList = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
start_pos = []
for i in range(N):
    if par[i] >= 0:
        adjList[par[i]].append(i)
    elif par[i] == -1:
        start_pos.append(i)
cnt = 0
node_erase(erase)
for x in start_pos:
    leaf_node_cnt(x)

print(cnt)