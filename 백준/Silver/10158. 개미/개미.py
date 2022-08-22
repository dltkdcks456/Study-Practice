import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

x = p + t
y = q + t

x1 = x // w
y1 = y // h

if x1 % 2:
    ans_x = w - (x % w )
else:
    ans_x = x % w

if y1 % 2:
    ans_y = h - (y % h)
else:
    ans_y = y % h

print(ans_x, ans_y)