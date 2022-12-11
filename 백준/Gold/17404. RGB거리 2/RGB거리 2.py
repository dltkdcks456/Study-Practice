import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
minV = 1000001
dp = [[1000001] * 3 for _ in range(N)]
for cl in range(3):
    dp[0][cl], dp[0][cl - 1] = cost[0][cl], 1000001
    for idx in range(1, N):
        dp[idx][0] = cost[idx][0] + min(dp[idx - 1][1], dp[idx - 1][2])
        dp[idx][1] = cost[idx][1] + min(dp[idx - 1][0], dp[idx - 1][2])
        dp[idx][2] = cost[idx][2] + min(dp[idx - 1][0], dp[idx - 1][1])
    for ck in range(3):
        if ck != cl:
            minV = min(minV, dp[N - 1][ck])

print(minV)