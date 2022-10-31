import sys
input = sys.stdin.readline

def longlong(sr, sc):
    for r in range(sr + 1):
        for c in range(sc + 1):
            if num[r][c] < num[sr][sc]:
                dp[sr][sc] = max(dp[sr][sc], dp[r][c] + 1)


N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
dp = [[1] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        longlong(i, j)

print(max(map(max, dp)))