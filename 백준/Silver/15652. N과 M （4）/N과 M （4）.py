n, m = map(int, input().split())
a = list(range(1, n + 1))
chosen = [-1] * m

def perm(n, m, j):
    if n == m:
        print(' '.join(map(str, chosen)))
        return
    for i in range(j, len(a)):
        chosen[n] = a[i]
        perm(n + 1, m, i)
perm(0, m, 0)