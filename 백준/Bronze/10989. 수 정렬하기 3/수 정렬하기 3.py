import sys
n = int(sys.stdin.readline())
c = [0] * (10001)

for _ in range(n):
    text = int(sys.stdin.readline())
    c[text] = c[text] + 1

for idx, v in enumerate(c):
    for n in range(v):
        print(idx)