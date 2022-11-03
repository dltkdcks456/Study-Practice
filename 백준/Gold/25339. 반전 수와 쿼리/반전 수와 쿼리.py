import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
ans = 0
for _ in range(Q):
    a, l, r = map(int, input().split())
    if a == 1:
        if ans == 1:
            ans = 0
        else:
            ans = 1
    else:
        diff = r - l + 1
        if diff == 2:
            if ans == 1:
                ans = 0
            else:
                ans = 1
        else:
            comb = diff * (diff - 1) // 2
            if comb % 2:
                if ans == 1:
                    ans = 0
                else:
                    ans = 1
    print(ans)