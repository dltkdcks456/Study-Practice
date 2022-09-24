N = int(input())
data = [0]
for _ in range(N):
    data.append(int(input()))
dp = [0] * 301
dp[0] = data[0]
dp[1] = data[0] + data[1]
for i in range(2, len(data)):
    dp[i] = data[i] + max(data[i - 1] + dp[i - 3], dp[i - 2])
print(dp[N])