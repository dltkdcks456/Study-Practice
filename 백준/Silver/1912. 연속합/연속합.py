import sys
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dp = [-1001] * N

for n in range(N):
    if n == 0:
        dp[0] = li[0]
    else:
        dp_sum = li[n] + dp[n - 1]
        dp[n] = max(li[n], dp_sum)
print(max(dp))