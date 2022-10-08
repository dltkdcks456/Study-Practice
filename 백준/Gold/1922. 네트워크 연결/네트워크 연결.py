import sys
from collections import deque
input=sys.stdin.readline

def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def union_set(m, n):
    rep[find_set(n)] = find_set(m)

def kruskal(li):
    cost = 0
    for vertex in li:
        w, a, b = vertex
        if find_set(a) != find_set(b):
            cost += w
            union_set(a, b)
    return cost

N = int(input())
M = int(input())
data = []
rep = [i for i in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    data.append([w, a, b])
data.sort()
print(kruskal(data))

