import sys
input = sys.stdin.readline


N, M = map(int, input().split())
R = G = B = 0
for _ in range(N):
    a, b = map(int, input().split())
for _ in range(M):
    u, v, w = input().split()
    if w == 'R':
        R += 1
    elif w == 'G':
        G += 1
    else:
        B += 1

i = 1
while True:
    if G > 0:
        G -= 1
    elif i == 1 and R > 0:
        R -= 1
    elif i == 0 and B > 0:
        B -= 1
    elif i == 1 and R == 0:
        print("jhnan917")
        break
    elif i == 0 and B == 0:
        print("jhnah917")
        break

    if i == 1:
        i = 0
    else:
        i = 1