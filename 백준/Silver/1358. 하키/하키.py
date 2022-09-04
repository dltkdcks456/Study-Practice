import sys
W, H, X, Y, P = map(int, sys.stdin.readline().split())
ans = 0
for _ in range(P):
    x, y = map(int, sys.stdin.readline().split())
    if X <= x <= X + W and Y <= y <= Y + H:
        ans += 1
    elif x < X and pow(x - X, 2) + pow(y - (Y + H / 2), 2) <= pow(H / 2, 2):
        ans += 1
    elif x > X + W and pow(x - (X + W), 2) + pow(y - (Y + H / 2), 2) <= pow(H / 2, 2):
        ans += 1
print(ans)