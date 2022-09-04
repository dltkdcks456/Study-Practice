import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    ans = 0
    for _ in range(n):
        x, y, r = map(int, sys.stdin.readline().split())
        if pow(x1 - x, 2) + pow(y1 - y, 2) < pow(r, 2) and pow(x2 - x, 2) + pow(y2 - y, 2) > pow(r, 2):
            ans += 1
        if pow(x2 - x, 2) + pow(y2 - y, 2) < pow(r, 2) and pow(x1 - x, 2) + pow(y1 - y, 2) > pow(r, 2):
            ans += 1
    print(ans)