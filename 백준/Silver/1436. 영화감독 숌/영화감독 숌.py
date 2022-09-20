import sys
from collections import deque

n = int(sys.stdin.readline())
a = '666'
li = [str(i) for i in range(10)]
result = deque()
def perm(n, m):
    if n == m:
        result.append(int(''.join(chosen)))
        return
    else:
        flag = True
        for j in range(len(li)):
            if chosen[n] == a:
                flag = False
                break
            else:
                chosen[n] = li[j]
            perm(n + 1, m)
        if not flag:
            perm(n + 1, m)

for k in range(5):
    chosen = [-1] * 5
    chosen[k] = a
    perm(0, 5)

print(sorted(set(result))[n - 1])


