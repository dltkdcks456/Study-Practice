N = int(input())
dp = [0] * 41
dp[1] = 1
dp[2] = 1
cnt = 0

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    cnt += 1

print(dp[i], cnt)
