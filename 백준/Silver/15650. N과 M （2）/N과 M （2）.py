N, M = map(int, input().split())
li = list(range(1, N + 1))

def perm(n, m, j):
    if n == m:
        print(*chosen)
        return
    else:
        for i in range(j, len(li)):
            chosen[n] = li[i]             
            perm(n + 1, m, i + 1)
  
chosen = [-1] * M
perm(0, M, 0)