import sys

def check(x1, y1, x2, y2, x3, y3):
    vector1 = (x2 - x1, y2 - y1)
    vector2 = (x3 - x2, y3 - y2)
    z = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    return -1 if z < 0 else 1

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A = check(x1, y1, x2, y2, x3, y3)
B = check(x1, y1, x2, y2, x4, y4)
C = check(x3, y3, x4, y4, x1, y1)
D = check(x3, y3, x4, y4, x2, y2)
print(1 if A * B < 0 and C * D < 0 else 0)