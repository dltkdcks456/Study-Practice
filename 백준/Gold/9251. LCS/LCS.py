import sys
input = sys.stdin.readline


text1 = list(input().rstrip())
text2 = list(input().rstrip())

N1 = len(text1)
N2 = len(text2)

dp = [[0] * (N1 + 1) for _ in range(N2 + 1)]
for r in range(1, N2 + 1):
    for c in range(1, N1 + 1):
        if text1[c - 1] == text2[r - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

print(dp[N2][N1])