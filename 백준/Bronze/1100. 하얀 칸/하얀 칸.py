import sys

board = []
cnt = 0
for j in range(8):
    if j % 2:
        board.extend(input()[::-1])
    else:
        board.extend(input())
for i in range(0, 64, 2):
    if board[i] == 'F':
        cnt += 1
print(cnt)