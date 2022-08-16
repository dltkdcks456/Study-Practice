from collections import deque
n = deque(list(range(1, int(input()) + 1)))
while len(n) > 1:
    n.popleft()
    n.append(n.popleft())
print(n.pop())