import sys

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
chosen = [-1] * M
saved = set()

def perm(n, m):
    if n == m:
        if tuple(chosen) not in saved:
            saved.add(tuple(chosen))
            print(' '.join(map(str, chosen)))
            return
        else:
            return
    else:
        for i in range(len(num)):
            chosen[n] = num[i]
            perm(n + 1, m)
            chosen[n] = -1
perm(0, M)
