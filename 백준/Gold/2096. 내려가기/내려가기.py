import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, 0, 0] for _ in range(4)]
minV = 900001
maxV = 0
switch = 1
switch1 = 1
if N == 1:
    arr = list(map(int, input().split()))
    print(max(arr), min(arr))
else:
    for i in range(N):
        a, b, c = map(int, input().split())
        if i == 0:
            dp[0][0], dp[0][1], dp[0][2] = a, b, c
        else:
            if switch:
                dp[1][0] = a + min(dp[0][0], dp[0][1])
                dp[1][1] = b + min(dp[0][0], dp[0][1], dp[0][2])
                dp[1][2] = c + min(dp[0][1], dp[0][2])
                if i == N - 1:
                    minV = min(dp[1])
                switch = 0

            else:
                dp[0][0] = a + min(dp[1][0], dp[1][1])
                dp[0][1] = b + min(dp[1][0], dp[1][1], dp[1][2])
                dp[0][2] = c + min(dp[1][1], dp[1][2])
                if i == N - 1:
                    minV = min(dp[0])
                switch = 1

        if i == 0:
            dp[2][0], dp[2][1], dp[2][2] = a, b, c
        else:
            if switch1:
                dp[3][0] = a + max(dp[2][0], dp[2][1])
                dp[3][1] = b + max(dp[2][0], dp[2][1], dp[2][2])
                dp[3][2] = c + max(dp[2][1], dp[2][2])
                if i == N - 1:
                    maxV = max(dp[3])
                switch1 = 0

            else:
                dp[2][0] = a + max(dp[3][0], dp[3][1])
                dp[2][1] = b + max(dp[3][0], dp[3][1], dp[3][2])
                dp[2][2] = c + max(dp[3][1], dp[3][2])
                if i == N - 1:
                    maxV = max(dp[2])
                switch1 = 1
    print(maxV, minV)