import sys
input = sys.stdin.readline

'''
0~9까지의 숫자가 시작할 때 총 4가지의 상태로 하나의 숫자를 표시한다.
이때 0과 9를 모두 한 번씩 터치하고 나온 계단이어야만 정답에 포함될 수 있다.
인덱스별 의미:
0 -> 0, 9를 한 번 도 거치지 않고 만들어진 계단 수
1 -> 0을 한 번 거치고 나온 계단 수
2 -> 9를 한 번 거치고 나온 계단 수
3 -> 0과 9를 한 번씩 찍고 만들어진 계단 수(정답의 개수에 포함된다)
'''
N = int(input())
dp = [[[0] * 4] + [[1, 0, 0, 0 ] for _ in range(8)] + [[0, 0, 1, 0]] for _ in range(N)]
# 그 이후의 dp값 저장
for j in range(1, N):
    for k in range(10):
        # 0을 터치할 때 나타날 수 있는 경우의 수
        if k == 0:
            dp[j][k][0] = 0
            dp[j][k][1] = dp[j - 1][k + 1][0] + dp[j - 1][k + 1][1]
            dp[j][k][2] = 0
            dp[j][k][3] = dp[j - 1][k + 1][2] + dp[j - 1][k + 1][3]
        # 9를 터치할 때 나타날 수 있는 경우의 수
        elif k == 9:
            dp[j][k][0] = 0
            dp[j][k][1] = 0
            dp[j][k][2] = dp[j - 1][k - 1][0] + dp[j - 1][k - 1][2]
            dp[j][k][3] = dp[j - 1][k - 1][1] + dp[j - 1][k - 1][3]
        # 그 외의 경우의 수
        else:
            for l in range(4):
                dp[j][k][l] = dp[j - 1][k + 1][l] + dp[j - 1][k - 1][l]

sumV = 0
for x in range(10):
    sumV += dp[N - 1][x][3]
print(sumV % 1000000000)
