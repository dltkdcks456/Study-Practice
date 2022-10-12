import sys

def find_land(n):
    minV = 2 ** 20 + 1
    flag = True
    while n > 0:
        n = n // 2
        if land[n] == 1:
            flag = False
            if n < minV:
                minV = n
    if flag:
        return 0
    else:
        return minV

N, Q = map(int, sys.stdin.readline().split())
land = [0] * (N + 1)
for _ in range(Q):
    chick = int(sys.stdin.readline())
    if land[chick] == 1:
        ans = find_land(chick)
        if ans:
            print(ans)
        else:
            print(chick)
    else:
        land[chick] = 1
        print(find_land(chick))