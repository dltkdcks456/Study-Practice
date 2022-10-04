import sys

def perm(n, m):
    if n == m:
        print(*chosen)
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                chosen[n] = A[i]
                perm(n + 1, m)
                visited[i] = 0

N = int(input())
A = list(range(1, N + 1))
chosen = [0] * N
visited = [0] * N
perm(0, N)
