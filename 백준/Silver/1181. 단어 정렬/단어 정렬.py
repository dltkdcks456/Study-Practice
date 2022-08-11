import sys
from collections import deque

N = int(sys.stdin.readline())
text = deque([sys.stdin.readline().rstrip() for _ in range(N)])
len_text = sorted(set(deque([len(i) for i in text])))
ans = deque([])
for i in len_text:
    arr = deque([])
    for j in text:
        if len(j) == i and j not in arr:
            arr.append(j)
    arr = sorted(arr)
    for k in arr:
        ans.append(k)
print('\n'.join(ans))