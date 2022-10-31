import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
num = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)


maxV = max(dp)
idx = dp.index(maxV)
start_value = num[dp.index(maxV)]
result = deque([start_value])
start_idx = maxV - 1
for k in range(idx - 1, -1, -1):
    if num[k] < start_value and start_idx == dp[k]:
        result.appendleft(num[k])
        start_value = num[k]
        start_idx -= 1


print(maxV)
print(*result)