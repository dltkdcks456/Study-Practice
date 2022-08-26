import sys
from collections import deque

T = int(sys.stdin.readline())
stack = []
dices = deque()
maxV = 0
for _ in range(T):
    dices.append(list(map(int, sys.stdin.readline().split())))
for i in range(6):

    if i == 0:
        stack.append(dices[0][5])
        num = dices[0][5]
    elif i == 1 or i == 2:
        stack.append(dices[0][i + 2])
        num = dices[0][i + 2]
    elif i == 3 or i == 4:
        stack.append(dices[0][i - 2])
        num = dices[0][i - 2]
    elif i == 5:
        stack.append(dices[0][0])
        num = dices[0][0]
    stack.append(dices[0][i])
    num = dices[0][i]

    for j in range(1, T):
        idx = dices[j].index(num)
        if idx == 0:
            stack.append(dices[j][5])
            num = dices[j][5]
        elif idx == 1 or idx == 2:
            stack.append(dices[j][idx + 2])
            num = dices[j][idx + 2]
        elif idx == 3 or idx == 4:
            stack.append(dices[j][idx - 2])
            num = dices[j][idx - 2]
        elif idx == 5:
            stack.append(dices[j][0])
            num = dices[j][0]

    total = 0
    for k in range(len(stack) - 1):
        if stack[k] == 6 and stack[k + 1] != 5:
            total += 5
        elif stack[k] != 5 and stack[k + 1] == 6:
            total += 5
        elif stack[k] == 6 and stack[k + 1] == 5:
            total += 4
        elif stack[k] == 5 and stack[k + 1] == 6:
            total += 4
        else:
            total += 6
    if maxV < total:
        maxV = total
    stack = []
print(maxV)