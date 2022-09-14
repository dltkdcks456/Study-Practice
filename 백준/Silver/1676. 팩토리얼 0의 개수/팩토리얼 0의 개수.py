dp = [0] * 501
dp[0] = dp[1] = 1
n = int(input())
for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]
cnt = 0
while dp[n] % 10 == 0:
    dp[n] = dp[n] // 10
    cnt += 1
print(cnt)