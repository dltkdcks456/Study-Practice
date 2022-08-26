n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
chosen = [-1] * m

def perm(n, m):
    if n == m:
        print(' '.join(map(str, chosen)))
        return
    for i in range(len(a)):
        if a[i] in chosen:
            continue
        chosen[n] = a[i]
        perm(n + 1, m)
        chosen[n] = -1
perm(0, m)