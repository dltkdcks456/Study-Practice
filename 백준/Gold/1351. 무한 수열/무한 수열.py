import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(n, p, q):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = dfs(n//p, p, q) + dfs(n//q, p, q)
        return dfs(n//p, p, q) + dfs(n//q, p, q)

N, P, Q = map(int, input().split())
memo = {0: 1}
print(dfs(N, P, Q))