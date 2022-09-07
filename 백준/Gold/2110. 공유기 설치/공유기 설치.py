import sys
N, C = map(int, sys.stdin.readline().split())
num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()
diff = (num[-1] - num[0]) // (C - 1)
for k in range(diff, 0, -1):
    n = num[0]
    cnt = 1
    while n + k <= num[-1]:
        for j in range(1, len(num)):
            if num[j] >= n + k:
                n = num[j]
                cnt += 1
    if cnt >= C:
        print(k)
        break