import sys

N, K = map(int, input().split())
dp = [0] * (200001)
for i in range(N):
    dp[i] = N - i
for j in range(N + 1, K * 2 + 1):
    if j % 2:
        dp[j] = min(dp[j - 1] + 1, dp[(j + 1)//2] + 1)
    else:
        dp[j] = min(dp[j - 1] + 1, dp[j//2])
print(dp[K])