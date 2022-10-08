import sys
input=sys.stdin.readline

def prim1(r, V):
    MST = [0] * (V + 1)
    key = [float('inf')] * (V + 1)
    key[r] = 0
    for _ in range(V - 1):
        u = 0
        minV = float('inf')
        for i in range(1, V + 1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1
        for j in range(1, V + 1):
            if MST[j] == 0 and 0 < arr[u][j]:
                key[j] = min(arr[u][j], key[j])
    return sum(key[1:])

N = int(input())
M = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    if a != b:
        arr[a][b] = w
        arr[b][a] = w

print(prim1(1, N))

