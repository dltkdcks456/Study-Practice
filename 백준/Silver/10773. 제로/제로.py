from collections import deque

K = int(input())
dq = deque()
for _ in range(K):
    n = int(input())
    if n == 0:
        dq.pop()
    else:
        dq.append(n)
print(sum(dq))