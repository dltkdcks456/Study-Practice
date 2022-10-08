import sys
from collections import deque

def find_team(x):
    global ans
    circulation_start = 0
    stack = deque()
    visited = set()
    while True:
        if num[x] == -1:
            while stack:
                temp = stack.pop()
                num[temp] = -1
                ans += 1
            break
        if x in visited:
            circulation_start = x
            temp = stack.pop()
            while temp != circulation_start:
                num[temp] = temp
                temp = stack.pop()
            num[temp] = temp
            while stack:
                temp = stack.pop()
                num[temp] = -1
                ans += 1
            break
        else:
            stack.append(x)
            visited.add(x)
            x = num[x]




T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    num = [0] + list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(1, n + 1):
        if num[i] == i or num[i] == -1:
            continue
        find_team(i)
    print(ans)