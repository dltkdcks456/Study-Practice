import sys

def find_set(x):
    while home[x] != x:
        x = home[x]
    return x

def union_set(m, n):
    a = find_set(n)
    b = find_set(m)
    if a > b:
        home[a] = b
    else:
        home[b] = a

N, M = map(int, sys.stdin.readline().split())
cost = []
home = [i for i in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    cost.append([A, B, C])
cost.sort(key=lambda x:x[2])
sumV = 0
for a, b, c in cost:
    if find_set(a) != find_set(b):
        union_set(a, b)
        sumV += c
        max = c
print(sumV - max)