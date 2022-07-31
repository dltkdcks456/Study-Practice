T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if r1 == r2 and d == 0:
        print(-1)
    elif d > r1 + r2:
        print(0)
    elif d == r1 + r2:
        print(1)
    elif d == abs(r2 - r1):
        print(1)
    elif d < abs(r2 - r1):
        print(0)
    else:
        print(2)
