import sys
input = sys.stdin.readline

def gcb(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


N = int(input())
T = list(map(int, input().split()))
if N == 3:
    print(T[0])
else:
    temp = gcb(T[0], T[1])
    minV = T[0] * T[1] // temp
    for i in range(1, N - 2):
        temp = gcb(T[i], minV)
        minV = minV * T[i] // temp
    print(minV)