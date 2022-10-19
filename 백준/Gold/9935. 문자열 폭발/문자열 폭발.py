import sys
input = sys.stdin.readline


text = list(input().rstrip())
bomb = list(input().rstrip())
N = len(text)
M = len(bomb)
stack = []

for i in range(N):
    stack.append(text[i])
    if len(stack) >= M and stack[-1] == bomb[-1]:
        if stack[-M:] == bomb:
            idx = 0
            while idx < M:
                stack.pop()
                idx += 1

if stack:
    print(''.join(stack))
else:
    print('FRULA')