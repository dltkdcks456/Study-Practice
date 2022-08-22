def check1(board):
    check = 0
    cnt_xl = 0
    cnt_xr = 0
    for r in range(5):
        cnt_c = 0
        if board[r][ : 5] == [0] * 5:
            check += 1
        if board[r][r] == 0:
            cnt_xl += 1
        if board[r][4 - r] == 0:
            cnt_xr += 1

        for c in range(5):
            if board[c][r] == 0:
                cnt_c += 1
        if cnt_c == 5:
            check += 1
    if cnt_xr == 5:
        check += 1
    if cnt_xl == 5:
        check += 1
    return check

board = [list(map(int, input().split())) for _ in range(5)]
choose = []
for _ in range(5):
    choose.extend(list(map(int, input().split())))

for i in range(len(choose)):
    for j in board:
        if choose[i] in j:
            idx = j.index(choose[i])
            j[idx] = 0
            break

    cnt_bingo = check1(board)
    if cnt_bingo >= 3:
        print(i + 1)
        break