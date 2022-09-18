import sys
A, B, C = map(int, sys.stdin.readline().split())
def dac(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = dac(a, b//2, c)
        if b % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c
print(dac(A, B, C))