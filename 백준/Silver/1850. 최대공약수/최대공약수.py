import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N, M = map(int, input().split())
print('1' * gcd(N, M))