import sys
N = sys.stdin.readline()
n = set(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
m = list(map(int, sys.stdin.readline().split()))
for i in m:
    if i in n:
        print(1)
    else:
        print(0)