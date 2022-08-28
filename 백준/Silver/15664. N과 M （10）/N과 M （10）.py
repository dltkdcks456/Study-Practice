N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * N
chosen = [-1] * M
saved = []

def perm(n, m):
    if n == m:
        if sorted(chosen) not in saved:
            saved.append(chosen[:])
            print(' '.join(map(str, chosen)))
            return
        else:
            return
    else:
        for i in range(len(num)):
            if visited[i] == 0:
                chosen[n] = num[i]
                visited[i] = 1
                perm(n + 1, m)
                visited[i] = 0
                chosen[n] = -1
perm(0, M)
