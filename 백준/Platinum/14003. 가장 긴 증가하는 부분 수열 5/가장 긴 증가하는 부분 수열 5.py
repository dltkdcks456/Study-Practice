import sys
from collections import deque
input = sys.stdin.readline

def serial(n):
    x = num[n]
    if x > stack[-1]:
        stack.append(x)
        dp[n] = len(stack) - 1
    else:
        start = 0
        end = len(stack) - 1
        while start <= end:
            mid = (start + end) // 2
            if stack[mid] > x:
                end = mid - 1
            elif stack[mid] < x:
                start = mid + 1
            else:
                break
        if stack[mid] == x:
            dp[n] = mid
            return
        elif stack[start] > x:
            stack[start] = x
            dp[n] = start


N = int(input())
num = list(map(int, input().split()))
dp = [0] * N
stack = []
for i in range(len(num)):
    if stack:
        serial(i)
    else:
        stack.append(num[i])
        dp[0] = 0
max_length = len(stack)
print(max_length)
max_length -= 1
# print(dp)
result = deque()
pos = 0
for k in range(len(dp) - 1, -1, -1):
    if dp[k] == max_length:
        pos = k
        result.append(num[k])
        max_length -= 1
        break

for j in range(pos - 1, -1, -1):
    if dp[j] == max_length:
        result.appendleft(num[j])
        max_length -= 1
        if max_length == -1:
            break
print(*result)