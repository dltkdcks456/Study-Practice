N, K = map(int, input().split())
dp = [0] * 100002

for i in range(0, N):
    dp[i] = N - i

for j in range(N + 1, K + 2):
    if j % 2 == 0:
        dp[j] = min(dp[j - 1] + 1, dp[j // 2] + 1)
        dp[j - 1] = min(dp[j] + 1, dp[j - 1])
    else:
        dp[j] = dp[j - 1] + 1
        dp[j - 1] = min(dp[j] + 1, dp[j - 1])

print(dp[K])