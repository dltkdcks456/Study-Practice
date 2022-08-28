import sys

N, M = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
chosen = [-1] * M
visited = [0] * N
save = set()

def perm(n, M):
    if n == M:
        if tuple(chosen) not in save:
            save.add(tuple(chosen))
            print(' '.join(map(str, chosen)))
            return
        else:
            return
    for i in range(N):
        if visited[i] == 0:
            chosen[n] = num_list[i]
            visited[i] = 1
            perm(n + 1, M)
            chosen[n] = -1
            visited[i] = 0
perm(0, M)