import sys

N, K = map(int, sys.stdin.readline().split())
num_li = list(map(int, sys.stdin.readline().split()))

maxV = start = sum(num_li[:K])

for i in range(1, N - K + 1):
    start = start - num_li[i - 1] + num_li[i + K - 1]
    if start > maxV:
        maxV = start
print(maxV)