import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(n, p, q, x, y):
    if n <= 0:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = dfs(n//p - x, p, q, x, y) + dfs(n//q - y, p, q, x, y)
        return dfs(n//p - x, p, q, x, y) + dfs(n//q - y, p, q, x, y)

N, P, Q, X, Y = map(int, input().split())
memo = {0: 1}
print(dfs(N, P, Q, X, Y))