import sys
K = int(sys.stdin.readline())
li = [0] * 100001
last = -1
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        last -= 1
    else:
        last += 1
        li[last] = n
print(sum(li[:last + 1]) if last != -1 else 0)