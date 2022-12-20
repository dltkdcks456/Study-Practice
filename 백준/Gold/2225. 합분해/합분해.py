import sys
# input = sys.stdin.readline
'''
개수가 0일 때 0을 만드는 경우의 수는 1개이다(dp[0][0])
dp[i][j]는 N이 i보다 작거나 같은 것들을 만들 수 있는 경우의 수들의 합이 와야한다.

N: 5, K: 2 일 경우
N\K   0  1  2
0    [1, 1, 1]
1    [0, 1, 2]
2    [0, 1, 3]
3    [0, 1, 4]
4    [0, 1, 5]
5    [0, 1, 6]
'''
N, K = map(int, input().split())
dp = [[1] * (K + 1)] + [[0] * (K + 1) for _ in range(N)]
for c in range(1, K + 1):
    for r in range(1, N + 1):
        dp[r][c] = dp[r][c - 1] + dp[r - 1][c]

# for i in dp:
#     print(i)
print(dp[N][K] % 1000000000)