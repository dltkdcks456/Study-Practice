import sys
input = sys.stdin.readline

def distance(x):
    if x > violin_max:
        return x - violin_max
    elif x < violin_min:
        return violin_min - x
    elif violin[x] == 1:
        return 0
    else:
        L = R = x
        d = 0
        while True:
            L = L - 1
            R = R + 1
            d += 1
            if violin[L] == 1 or violin[R] == 1:
                break
        return d


N, Q = map(int, input().split())
dummy = input()
violin = [0] * (N + 1)
check = False
violin_min = 100001
violin_max = 0
for _ in range(Q):
    c, v = map(int, input().split())
    if c == 1:
        check = True
        violin[v] = 1
        if v > violin_max:
            violin_max = v
        if v < violin_min:
            violin_min = v
    else:
        if check:
            print(distance(v))
        else:
            print(-1)