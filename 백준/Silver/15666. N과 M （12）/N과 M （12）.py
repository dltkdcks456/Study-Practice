import sys
N, M = map(int, sys.stdin.readline().split())
li = sorted(list(map(int, sys.stdin.readline().split())))
chosen = [-1] * M
group = set()

def perm(n, m, j):
    if n == m:
        if tuple(chosen) not in group:
            group.add(tuple(chosen))
            print(*chosen)
            return
        else:
            return
    else:
        for i in range(j, N):
            chosen[n] = li[i]
            perm(n + 1, m, i)
perm(0, M, 0)