import sys

def perm(n, m, j):
    if n == m:
        if tuple(chosen) in group:
            return
        else:
            group.add(tuple(chosen))
            print(' '.join(map(str,chosen)))
            return
    else:
        for i in range(j, len(li)):
            chosen[n] = li[i]
            perm(n + 1, m, i)

N, M = map(int, sys.stdin.readline().split())
li = sorted(list(map(int, sys.stdin.readline().split())))
group = set()
chosen = [-1] * M
perm(0, M, 0)

