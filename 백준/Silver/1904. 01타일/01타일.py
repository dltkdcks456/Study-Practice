N = int(input())
dp = [0, 1, 2]

if N <= 2:
    print(dp[N])
else:
    i = 3
    while i <= N:
        if i % 2:
            dp[1] = (dp[1] + dp[2]) % 15746
            i += 1
        else:
            dp[2] = (dp[1] + dp[2]) % 15746
            i += 1
    if N % 2:
        print(dp[1])
    else:
        print(dp[2])