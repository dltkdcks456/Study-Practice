import sys
input = sys.stdin.readline


N, M = map(int, input().split())
R = G = B = 0
for _ in range(N):
    x = input()
for _ in range(M):
    u, v, w = input().split()
    if w == 'R':
        R += 1
    elif w == 'G':
        G += 1
    else:
        B += 1
G = G % 2
minV = min(R, B)
R = R - minV
B = B - minV

if G == 0:
    if R == 0:
        print("jhnan917")
    else:
        print("jhnah917")
else:
    if R == 0:
        if B == 0:
            print("jhnah917")
        else:
            print("jhnan917")
    else:
        print("jhnah917")