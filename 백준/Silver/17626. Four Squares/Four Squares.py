N = int(input())
dp = [0, 1] + [5] * (N - 1)
for i in range(2, N + 1):
    for j in range(1, i):
        if i >= j * j:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        else:
            break
print(dp[N])