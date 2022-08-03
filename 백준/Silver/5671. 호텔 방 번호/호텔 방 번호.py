import sys

c = 0
a = [0] * 5001
for i in range(5001):
    if len(str(i)) == len(set(str(i))):
        c += 1
    a[i] = c

for e in sys.stdin.readlines():
    n, m = map(int, e.split())
    print(a[m] - a[n - 1])