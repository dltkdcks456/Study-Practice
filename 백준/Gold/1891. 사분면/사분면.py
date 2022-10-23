import sys
input = sys.stdin.readline

def find_pos(li, r, c):
    idx = 0
    while idx < d:
        line = 2 ** (d - idx - 1)
        if num[idx] == 1:
            c += line
        elif num[idx] == 2:
            idx += 1
            continue
        elif num[idx] == 3:
            r += line
        elif num[idx] == 4:
            r += line
            c += line
        idx += 1
    return r, c

def find_num(d, xx, yy):
    idx_1 = d
    text = ''
    while idx_1 > 0:
        line = 2 ** (idx_1 - 1)
        if xx < line and yy < line:
            text += '2'
        elif xx >= line and yy < line:
            text += '3'
            xx -= line
        elif xx < line and yy >= line:
            text += '1'
            yy -= line
        elif xx >= line and yy >= line:
            text += '4'
            xx -= line
            yy -= line
        idx_1 -= 1
    return text

d, num = input().split()
d = int(d)
num = list(map(int, num))
x, y = map(int, input().split())
sx, sy = find_pos(num, 0, 0)
# print(sx, sy)
sx -= y
sy += x
# print(sx, sy)

if 0 <= sx < 2 ** d and 0 <= sy < 2 ** d:
    print(find_num(d, sx, sy))
else:
    print(-1)