import sys

def check(x1, y1, x2, y2, x3, y3):
    global inline
    vector1 = (x2 - x1, y2 - y1)
    vector2 = (x3 - x2, y3 - y2)
    z = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    if z < 0:
        return -1
    elif z == 0:
        if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
            inline = 1
            return 0
        else:
            return 0
    else:
        return 1


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
inline = 0
A = check(x1, y1, x2, y2, x3, y3)
B = check(x1, y1, x2, y2, x4, y4)
C = check(x3, y3, x4, y4, x1, y1)
D = check(x3, y3, x4, y4, x2, y2)
ch1 = A * B
ch2 = C * D

if ch1 == 0 and ch2 == 0 and ((min(x3, x4) <= x1 <= max(x3, x4) or min(x3, x4) <= x2 <= max(x3, x4) or  min(x1, x2) <= x3 <= max(x1, x2) or min(x1, x2) <= x4 <= max(x1, x2)) and (min(y3, y4) <= y1 <= max(y3, y4) or min(y3, y4) <= y2 <= max(y3, y4) or  min(y1, y2) <= y3 <= max(y1, y2) or min(y1, y2) <= y4 <= max(y1, y2))):
    print(1)
elif ch1 == 0 or ch2 == 0:
    if inline:
        print(1)
    else:
        print(0)
elif ch1 < 0 and ch2 < 0:
    print(1)
else:
    print(0)