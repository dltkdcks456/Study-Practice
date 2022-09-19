import sys
M, N = map(int, sys.stdin.readline().split())
num = [1] * (N + 1)
num[0] = num[1] = 0
for i in range(2, N + 1):
    if num[i] == 1:
        if i >= M:
            print(i)
        for j in range(2, (N // i) + 1):
            num[i * j] = 0