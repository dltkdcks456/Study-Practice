dp = [0, 1, 1, 1, 2, 2] + [0] * 95
def f(n):
    if dp[n]:
        return dp[n]
    else:
        dp[n] = f(n - 1) + f(n - 5)
        return dp[n]
T = int(input())
for _ in range(T):
    N = int(input())
    print(f(N))