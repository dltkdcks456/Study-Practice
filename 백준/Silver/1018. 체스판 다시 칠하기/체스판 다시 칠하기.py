import sys

def board_check(x, y, board):                           # 체스 보드의 변화값을 찾아주는 함수
    WB_board = BW_board = 0

    for i in range(8):                                  # 가로 위치
        for j in range(8):                              # 세로 위치
            check = board[x + i][y + j + (8 - 2 * j - 1) * (i % 2)]
            if j % 2 == 0:                              # WB 문양의 반복
                if check == 'B':
                    WB_board += 1
            else:
                if check == 'W':
                    WB_board += 1

            if j % 2 == 0:                              # BW 문양의 반복
                if check == 'W':
                    BW_board += 1
            else:
                if check == 'B':
                    BW_board += 1

    return min(WB_board, BW_board)

x, y = map(int, input().split())
board = [sys.stdin.readline().rstrip() for i in range(x)]
chg_list = []

for m in range(x - 7):
    for n in range(y - 7):
        chg = board_check(m, n, board)
        chg_list.append(chg)

print(min(chg_list))