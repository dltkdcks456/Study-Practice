dp = [0] * 1001
dp[0] = dp[1] = 1
n, m = map(int, input().split())
for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]
print((dp[n]//dp[n-m]//dp[m]) % 10007)