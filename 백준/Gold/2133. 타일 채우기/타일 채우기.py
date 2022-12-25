import sys
input = sys.stdin.readline

'''
N이 홀수가 되는 경우네는 2가지 타일로 채울 수 없다.
타일의 모양으로 만들어지는 경우의 수를 확인하다보면 규칙을 발견할 수 있다.
'''

N = int(input()) # N: 타일의 가로 길이
dp = [0] * (N + 1)
if N % 2:
    print(0)
else:
    dp[2] = 3
    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(i - 4, 1, -2):
            dp[i] += dp[j] * 2
    
    print(dp[N])