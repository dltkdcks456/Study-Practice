import sys
sys.setrecursionlimit(10 ** 9)

def dfs(ch, par):
    if arr[ch] != par:
        s = 1
        for w in arr[ch]:
            if w != par:
                s += dfs(w, ch)
        memo[ch] = s
        return s
    else:
        return 1


N, R, Q = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    arr[U].append(V)
    arr[V].append(U)
memo = {i : 1 for i in range(N + 1)}
dfs(R, -1)
for _ in range(Q):
    X = int(sys.stdin.readline())
    print(memo[X])
