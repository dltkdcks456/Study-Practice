import sys
N, K = map(int, sys.stdin.readline().split())
coin = []
for _ in range(N):
    n = int(sys.stdin.readline())
    coin.append(n)

cnt = 0
for i in range(N - 1, -1, -1):
    if K - coin[i] >= 0:
        cnt += K // coin[i]
        K -= coin[i] * (K // coin[i])
print(cnt)